import sys
from itertools import chain, combinations
from typing import Generator, Iterable, Self

import aoc


# Common
class Actor():
    def __init__(self: Self, name: str, hit_points: int, damage: int, armor: int):
        self.name = name
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor

class Item():
    def __init__(self: Self, name: str, cost: int, damage: int, armor: int):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

class Shop():
    def __init__(self: Self, weapons: list[Item], armors: list[Item], rings: list[Item]):
        self.weapons = weapons
        self.armors = armors
        self.rings = rings

def parse_data(data: str) -> Actor:
    lines = data.splitlines()
    hit_points = int(lines[0].split(': ')[1])
    damage = int(lines[1].split(': ')[1])
    armor = int(lines[2].split(': ')[1])
    return Actor('Boss', hit_points, damage, armor)

def build_shop() -> Shop:
    weapons = [
        Item('Dagger', 8, 4, 0),
        Item('Shortsword', 10, 5, 0),
        Item('Warhammer', 25, 6, 0),
        Item('Longsword', 40, 7, 0),
        Item('Greatsxe', 74, 8, 0)
    ]
    armors = [
        Item('Leather', 13, 0, 1),
        Item('Chainmail', 31, 0, 2),
        Item('Splintmail', 53, 0, 3),
        Item('Bandedmail', 75, 0, 4),
        Item('Platemail', 102, 0, 5)
    ]
    rings = [
        Item('Damage +1', 25, 1, 0),
        Item('Damage +2', 50, 2, 0),
        Item('Damage +3', 100, 3, 0),
        Item('Defense +1', 20, 0, 1),
        Item('Defense +2', 40, 0, 2),
        Item('Defense +3', 80, 0, 3)
    ]
    return Shop(weapons, armors, rings)

def item_combos(shop: Shop, weapons_range: range, armors_range: range, rings_range: range) -> Generator[Iterable[Item]]:
    for weapon_count in weapons_range:
        for armor_count in armors_range:
            for ring_count in rings_range:
                for weapons in combinations(shop.weapons, weapon_count):
                    for armors in combinations(shop.armors, armor_count):
                        for rings in combinations(shop.rings, ring_count):
                            yield chain(weapons, armors, rings)

def build_player(player_name: str, shopping_list: Iterable[Item]) -> tuple[int, Actor]:
    damage = armor = cost = 0
    for item in shopping_list:
        damage += item.damage
        armor += item.armor
        cost += item.cost
    player = Actor(player_name, 100, damage, armor)
    return cost, player

def play_game(left: Actor, right: Actor) -> str:
    players: list[Actor] = [
        Actor(left.name, left.hit_points, left.damage, left.armor),
        Actor(right.name, right.hit_points, right.damage, right.armor)
    ]

    attacking = 0
    defending = 1

    while True:
        damage_done = max(players[attacking].damage - players[defending].armor, 1)
        players[defending].hit_points -= damage_done
        if players[defending].hit_points <= 0:
            return players[attacking].name
        
        attacking = 1 - attacking
        defending = 1 - defending

# Part 1
def p1(data: str) -> int:
    boss = parse_data(data)
    shop = build_shop()

    cheapest_succesful_loadout = sys.maxsize
    player_name = 'Player'

    for shopping_list in item_combos(shop, range(1, 2), range(2), range(3)):
        cost, player = build_player(player_name, shopping_list)
        if cost < cheapest_succesful_loadout:
            winner = play_game(player, boss)
            if winner == player_name:
                cheapest_succesful_loadout = cost
    
    return cheapest_succesful_loadout

# Part 2
def p2(data: str) -> int:
    boss = parse_data(data)
    shop = build_shop()

    highest_cost_fail = 0
    player_name = 'Player'

    for shopping_list in item_combos(shop, range(1, 2), range(2), range(3)):
        cost, player = build_player(player_name, shopping_list)
        if cost > highest_cost_fail:
            winner = play_game(player, boss)
            if winner != player_name:
                highest_cost_fail = cost
    
    return highest_cost_fail

# Main
if __name__ == '__main__':
    data = aoc.d21_data()
    print(p1(data))
    print(p2(data))
