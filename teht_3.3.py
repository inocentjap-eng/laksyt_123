sukupuolen = input("Anna sukupuolen: ")
arvo = int(input("Anna arvo: "))

if sukupuolen == "nainen":
    if arvo < 117:
        print(f"hemoglobiiniarvo {arvo} g/l on alhainen")

    elif arvo <= 175:
        print(f"hemoglobiiniarvo {arvo} g/l on normaali")
    else:
        print(f"hemoglobiiniarvo {arvo} g/l on korkea")

if  sukupuolen == "mies":
    if arvo < 134:
        print(f"hemoglobiiniarvo {arvo} g/l on alhainen")

    elif arvo <= 195:
        print(f"hemoglobiiniarvo {arvo} g/l on normaali")

    else:
        print(f"hemoglobiiniarvo {arvo} g/l korkea")
