def karsi_parittomat(luvut):
    parilliset = [luku for luku in luvut if luku % 2 == 0]
    return parilliset

alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

karsittu_lista = karsi_parittomat(alkuperainen_lista)

print("Alkuperäinen lista:", alkuperainen_lista)
print("Karsittu lista:", karsittu_lista)