import re
from collections import deque, namedtuple

import aoc

# Common
Ingredient = namedtuple('Ingredient', 'name, capacity, durability, flavor, texture, calories')

def parse_data(data: str) -> list[Ingredient]:
    result = list()
    for line in data.splitlines():
        name, capacity, durability, flavor, texture, calories = re.match(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line).group(1, 2, 3, 4, 5, 6)
        result.append(Ingredient(name, int(capacity), int(durability), int(flavor), int(texture), int(calories)))
    return result

def calculate_score(ingredients: list[Ingredient], usedIngredients: list[int]) -> int:
    num_used = len(usedIngredients)
    capacity = max(sum(ingredients[n].capacity * usedIngredients[n] for n in range(num_used)), 0)
    durability = max(sum(ingredients[n].durability * usedIngredients[n] for n in range(num_used)), 0)
    flavor = max(sum(ingredients[n].flavor * usedIngredients[n] for n in range(num_used)), 0)
    texture = max(sum(ingredients[n].texture * usedIngredients[n] for n in range(num_used)), 0)
    return capacity * durability * flavor * texture

# Part 1
def optimise_score(ingredients: list[Ingredient], usedIngredients: list[int], number_to_add: int) -> list[int]:
    best_usage = usedIngredients
    for _ in range(number_to_add):
        max_score = 0
        for trial_pos in range(len(usedIngredients)):
            trial_usage = list(best_usage)
            trial_usage[trial_pos] += 1
            score = calculate_score(ingredients, trial_usage)
            if score > max_score:
                max_score = score
                best_trial = trial_usage
        best_usage = best_trial
    return best_usage

def p1(data: str) -> int:
    ingredients = parse_data(data)
    usedIngedients = [1] * len(ingredients)
    best_usage = optimise_score(ingredients, usedIngedients, 100-sum(usedIngedients))
    result = calculate_score(ingredients, best_usage)
    return result

# Part 2
def calculate_calories(ingredients: list[Ingredient], usedIngredients: list[int]) -> int:
    num_used = len(usedIngredients)
    calories = sum(ingredients[n].calories * usedIngredients[n] for n in range(num_used))
    return calories

def optimise_score_for_calories(ingredients: list[Ingredient], target_num_ingredients: int, target_calories: int) -> list[int]:
    q = deque()
    num_ingredient_types = len(ingredients)
    best_score = 0
    q.append(list())
    while q:
        usage: list[int] = q.popleft()
        calories_used = calculate_calories(ingredients, usage)
        num_ingredients_used = sum(usage)
        if len(usage) == num_ingredient_types:
            # all types of ingredient have been used, check score
            if num_ingredients_used == target_num_ingredients and calories_used == target_calories:
                score = calculate_score(ingredients, usage)
                if score > best_score:
                    best_score = score
                    best_usage = list(usage)
        else:
            next_ingredient = len(usage)
            next_ingredient_calories = ingredients[next_ingredient].calories
            calories_remaining = target_calories - calories_used
            max_num_next_ingredient = min(calories_remaining // next_ingredient_calories, target_num_ingredients - num_ingredients_used)
            if next_ingredient == len(ingredients) - 1:
                # last ingredient, so there's only one amount we could use
                q.append(usage + [max_num_next_ingredient])
            else:
                for num_of_next_ingredient in range(1, max_num_next_ingredient+1):
                    q.append(usage + [num_of_next_ingredient])
    return best_usage

def p2(data: str) -> int:
    ingredients = parse_data(data)
    best_usage = optimise_score_for_calories(ingredients, 100, 500)
    result = calculate_score(ingredients, best_usage)
    return result

# Main
if __name__ == '__main__':
    data = aoc.d15_data()
    print(p1(data))
    print(p2(data))
