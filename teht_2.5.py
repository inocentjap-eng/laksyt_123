leiviska = float(input("Anna leiviskat: "))
naula = float(input("Anna naula: "))
luoti = float(input("Anna luodit: "))

# 1 leiviska on 20 naulaa
# 1 naula on 32 luotia
# 1 luoti on 13,3 grammaa
# 1 naula = 32 luoti -> 1 naula = 32 × 13.3 g
# 1 leiviska = 20 naula = 20 × 32 luoti -> 1 leiviska = 20 × 32 × 13.3 g

grammaa_leiviska = 20 * 32 * 13.3
grammaa_naula = 32 * 13.3
grammaa_luoti = 13.3

summa_grammaa_leiviska = leiviska * grammaa_leiviska
summa_grammaa_naula = naula * grammaa_naula
summa_grammaa_luoti = luoti * grammaa_luoti

summa_grammaa = summa_grammaa_leiviska + summa_grammaa_naula + summa_grammaa_luoti

kg = int(summa_grammaa // 1000)
g = summa_grammaa % 1000

print(f"Massa nykymittojen mukaan:\n{kg} kilogrammaa ja {g:.2f} grammaa.")