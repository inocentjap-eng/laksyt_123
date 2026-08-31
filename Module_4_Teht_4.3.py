pienin = None
suurin = None

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")

    if syote == "":
        break

    luku = float(syote)

    if pienin is None or luku < pienin:
        pienin = luku

    if suurin is None or luku > suurin:
        suurin = luku

if pienin is not None:
    print(f"Pienin luku: {pienin}")
    print(f"Suurin luku: {suurin}")