max_food = 1200
max_wood = 800
max_gold = 600
best_power = 0
best_combo = (0, 0, 0)

for swordsmen in range(0, 21):       # 60 * 20 = 1200 (límite de comida)
    for bowmen in range(0, 16):      # 80 * 15 = 1200
        for horsemen in range(0, 9): 
            food = swordsmen * 60 + bowmen * 80 + horsemen * 140
            wood = swordsmen * 20 + bowmen * 10
            gold = bowmen * 40 + horsemen * 100

            if food <= max_food and wood <= max_wood and gold <= max_gold:
                power = swordsmen * 70 + bowmen * 95 + horsemen * 230

                if power > best_power:
                    best_power = power
                    best_combo = (swordsmen, bowmen, horsemen)

print('================= Solución =================')
print(f'Poder óptimo = {best_power} 💪power')
print('Ejército:')
print(f' - 🗡️Swordsmen = {best_combo[0]}')
print(f' - 🏹Bowmen = {best_combo[1]}')
print(f' - 🐎Horsemen = {best_combo[2]}')