def gallonat_litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat

while True:
    gallonat = float(input("Anna bensiinin määrä gallonina: "))

    if gallonat < 0:
        break

    litrat = gallonat_litroiksi(gallonat)
    print(f"{gallonat} gallona on {litrat:.3f} litraa")