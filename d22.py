import sys
from collections import namedtuple
from typing import Self

import aoc


# Common
class Fighter():
    def __init__(self: Self, name: str, hit_points: int, mana_points: int, damage: int, armor: int, mana_spent: int = 0):
        self.name = name
        self.hit_points = hit_points
        self.mana_points = mana_points
        self.damage = damage
        self.armor = armor
        self.mana_spent = mana_spent
    
    def __repr__(self):
        return f'{self.name}: HP={self.hit_points} MP={self.mana_points},{self.mana_spent} D={self.damage} A={self.armor}'
    
    def copy(self: Self):
        return Fighter(self.name, self.hit_points, self.mana_points, self.damage, self.armor, self.mana_spent)

def parse_data(data: str) -> Fighter:
    lines = data.splitlines()
    hit_points = int(lines[0].split(': ')[1])
    damage = int(lines[1].split(': ')[1])
    
    return Fighter('Boss', hit_points, 0, damage, 0)

Spell = namedtuple('Spell', 'name, cost, apply')

def apply_magic_missile(player: Fighter, boss: Fighter, effects: dict[str,int]) -> None:
    boss.hit_points -= 4

def apply_drain(player: Fighter, boss: Fighter, effects: dict[str,int]) -> None:
    boss.hit_points -= 2
    player.hit_points += 2

def apply_shield(player: Fighter, boss: Fighter, effects: dict[str,int]) -> None:
    effects |= {'Shield': 6}

def apply_poison(player: Fighter, boss: Fighter, effects: dict[str,int]) -> None:
    effects |= {'Poison': 6}

def apply_recharge(player: Fighter, boss: Fighter, effects: dict[str,int]) -> None:
    effects |= {'Recharge': 5}

def apply_effects(player: Fighter, boss: Fighter, effects: dict[str, int]) -> dict[str, int]:
    if 'Shield' in effects:
        player.armor = 7
    else:
        player.armor = 0
    if 'Poison' in effects:
        boss.hit_points -= 3
    if 'Recharge' in effects:
        player.mana_points += 101
    for effect in effects:
        effects[effect] -= 1
    return {k: v for k,v in effects.items() if v > 0}

spell_book: list[Spell] = [
        Spell('Magic Missile', 53, apply_magic_missile),
        Spell('Drain', 73, apply_drain),
        Spell('Shield', 113, apply_shield),
        Spell('Poison', 173, apply_poison),
        Spell('Recharge', 229, apply_recharge)
    ]

def play_game(part: int, prev_player: Fighter, prev_boss: Fighter, prev_effects: dict[str, int], least_mana_to_win: int = sys.maxsize) -> int:   
    # Select a spell. Can't afford any -> player loses
    available_spells = [spell for spell in spell_book if spell.cost <= prev_player.mana_points and spell.name not in prev_effects]
    if len(available_spells) == 0:
        return least_mana_to_win
    for spell in available_spells:
        player = prev_player.copy()
        boss = prev_boss.copy()
        effects = prev_effects.copy()
        player.mana_points -= spell.cost
        player.mana_spent += spell.cost
        if player.mana_spent >= least_mana_to_win: continue
        
        # Cast the spell
        spell.apply(player, boss, effects)
        
        # Check end condition (boss loss)
        if boss.hit_points <= 0:
            least_mana_to_win = min(least_mana_to_win, player.mana_spent)
            continue
        
        # Apply effects
        effects = apply_effects(player, boss, effects)
        
        # Check end condition (boss loss)
        if boss.hit_points <= 0:
            least_mana_to_win = min(least_mana_to_win, player.mana_spent)
            continue
        
        # Boss Acts
        damage_done = max(boss.damage - player.armor, 1)
        player.hit_points -= damage_done
        
        # Check end condition (player loss)
        if player.hit_points <= 0:
            continue
        
        # Apply effects
        effects = apply_effects(player, boss, effects)
        if part == 2:
            player.hit_points -= 1
        
        # Check end condition (boss loss)
        if boss.hit_points <= 0:
            least_mana_to_win = min(least_mana_to_win, player.mana_spent)
            continue
        
        least_mana_to_win = min(least_mana_to_win, play_game(part, player, boss, effects, least_mana_to_win))
    
    return least_mana_to_win

# Part 1
def p1(data: str) -> int:
    boss = parse_data(data)
    
    player = Fighter('Player', 50, 500, 0, 0)
    least_mana_to_win = play_game(1, player, boss, dict())
    return least_mana_to_win

# Part 2
def p2(data: str) -> int:
    boss = parse_data(data)
    
    player = Fighter('Player', 49, 500, 0, 0)
    least_mana_to_win = play_game(2, player, boss, dict())
    return least_mana_to_win

# Main
if __name__ == '__main__':
    data = aoc.d22_data()
    print(p1(data))
    print(p2(data))
