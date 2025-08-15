# Solution 1 - Advent of Code 2015, Day 21
from itertools import combinations as combos


INPUT_FILE = "input.txt"
with open(INPUT_FILE, "r") as f:
  lines = [line.strip() for line in f.readlines()]


def main():


  def fight(boss_hp, boss_dmg, boss_armor,
            player_hp, player_dmg, player_armor):
    player_atk = max(player_dmg - boss_armor, 1)
    boss_atk = max(boss_dmg - player_armor, 1)

    while True:
      boss_hp -= player_atk
      if boss_hp <= 0:
        return True
      else:
        player_hp -= boss_atk
        if player_hp <= 0:
          return False


  boss_hp = int(lines[0].split()[-1])
  boss_dmg = int(lines[1].split()[-1])
  boss_armor = int(lines[2].split()[-1])

  player_hp = 100

  with open("shop.txt", "r") as f:
    shop_lines = [line.strip() for line in f.readlines()]

  weapons = {}
  armor = {}
  rings = {}

  # weapon info
  for line in shop_lines[1:6]:
    items = line.split()
    name = items[0]
    # cost, dmg, armor
    weapons[name] = [int(n) for n in items[1:]]

  # armor info
  for line in shop_lines[8:13]:
    items = line.split()
    name = items[0]
    # cost, dmg, armor
    armor[name] = [int(n) for n in items[1:]]

  # ring info
  for line in shop_lines[15:]:
    items = line.split()
    # rings have multi-word names e.g. "Defense +3"
    name = " ".join(items[0:2])
    # cost, dmg, armor
    rings[name] = [int(n) for n in items[2:]]


  ring_combos = list(combos(rings.keys(), 2))
  for ring in rings.keys():
    ring_combos.append([ring])

  all_equipment = weapons.copy()
  all_equipment.update(armor)
  all_equipment.update(rings)


  equipment_loadouts = []

  # weapon only
  for weapon in weapons.keys():
    e = [weapon]
    equipment_loadouts.append(e)

    # weapon + 1 ring, weapon + 2 rings
    for ring_combo in ring_combos:
      e = [weapon]
      for r in ring_combo:
        e.append(r)
      equipment_loadouts.append(e)

    # weapon + armor
    for armor_name in armor.keys():
      e = [weapon, armor_name]
      equipment_loadouts.append(e)

      # weapon + armor + 1 ring, weapon + armor + 2 rings
      for ring_combo in ring_combos:
#        equipment_loadouts.append([weapon, armor_name, ring_combo])
        e = [weapon, armor_name]
        for r in ring_combo:
          e.append(r)
        equipment_loadouts.append(e)


  loadout_stats = []

  for e in equipment_loadouts:
    t_cost, t_damage, t_armor = 0, 0, 0
    for item in e:
      cost, damage, armor = all_equipment[item]
      t_cost += cost
      t_damage += damage
      t_armor += armor
    stats = [t_cost, t_damage, t_armor]
    loadout_stats.append(stats)


  gold_spent_to_win = 0

  for stats in loadout_stats:
    cost, player_dmg, player_armor = stats
    if fight(boss_hp, boss_dmg, boss_armor,
             player_hp, player_dmg, player_armor):
      if gold_spent_to_win == 0:
        gold_spent_to_win = cost
      else:
        gold_spent_to_win = min(gold_spent_to_win, cost)


  print(gold_spent_to_win)


if __name__ == "__main__":
  main()
