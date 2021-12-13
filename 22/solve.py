import heapq


with open('input') as infile:
    lines = infile.readlines()
    boss_hp = int(lines[0].strip().split()[-1])
    boss_damage = int(lines[1].strip().split()[-1])

def fight(state, wither=False):
    mana_spent, my_current_hp, my_mana, boss_current_hp, shield_remaining, poison_remaining, recharge_remaining, my_turn = state
    # do pre turn things
    my_armor = 0
    if wither:
        my_current_hp -= 1
    if my_current_hp <= 0:
        yield (mana_spent, my_current_hp, my_mana, boss_current_hp, shield_remaining, poison_remaining, recharge_remaining, my_turn)
        return

    if shield_remaining > 0:
        my_armor = 7
        shield_remaining -= 1
    if poison_remaining > 0:
        boss_current_hp -= 3
        poison_remaining -= 1
    if recharge_remaining > 0:
        my_mana += 101
        recharge_remaining -= 1
    if boss_current_hp <= 0:
        yield (mana_spent, my_current_hp, my_mana, boss_current_hp, shield_remaining, poison_remaining, recharge_remaining, my_turn)
        return

    if my_turn:
        my_turn = not my_turn
        if my_mana >= 53:
            yield (mana_spent + 53, my_current_hp, my_mana - 53, boss_current_hp - 4, shield_remaining, poison_remaining, recharge_remaining, my_turn)
        if my_mana >= 73:
            yield (mana_spent + 73, my_current_hp + 2, my_mana - 73, boss_current_hp - 2, shield_remaining, poison_remaining, recharge_remaining, my_turn)
        if my_mana >= 113 and shield_remaining <= 0:
            yield (mana_spent + 113, my_current_hp, my_mana - 113, boss_current_hp, 6, poison_remaining, recharge_remaining, my_turn)
        if my_mana >= 173 and poison_remaining <= 0:
            yield (mana_spent + 173, my_current_hp, my_mana - 173, boss_current_hp, shield_remaining, 6, recharge_remaining, my_turn)
        if my_mana >= 229 and recharge_remaining <= 0:
            yield (mana_spent + 229, my_current_hp, my_mana - 229, boss_current_hp, shield_remaining, poison_remaining, 5, my_turn)
    else:
        my_turn = not my_turn
        yield (mana_spent, my_current_hp -  max(1, boss_damage - my_armor), my_mana, boss_current_hp, shield_remaining, poison_remaining, recharge_remaining, my_turn)

def solve(wither):
    explore_heap = []
    initial_state = (0, 50, 500, boss_hp, 0, 0, 0, True)
    heapq.heappush(explore_heap, initial_state)
    while True:
        mana_spent, my_current_hp, my_mana, boss_current_hp, shield_remaining, poison_remaining, recharge_remaining, my_turn = explore = heapq.heappop(explore_heap)
        if my_current_hp <= 0:
            continue
        if boss_current_hp <= 0:
            print(explore)
            return mana_spent
        for newstate in fight(explore, wither=wither):
            heapq.heappush(explore_heap, newstate)

print(solve(False))
print(solve(True))
