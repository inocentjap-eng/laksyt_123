import random

num1 = random.randint(0,9)
num2 = random.randint(0,9)
num3 = random.randint(0,9)

kolmenumeroisen_koodin = f"{num1}{num2}{num3}"

num4 = random.randint(1,6)
num5 = random.randint(1,6)
num6 = random.randint(1,6)
num7 = random.randint(1,6)

nelinumeroisen_koodin = f"{num4}{num5}{num6}{num7}"

print(f"kolmenumeroisen koodi: {kolmenumeroisen_koodin}")
print(f"nelinumeroisen koodi: {nelinumeroisen_koodin}")