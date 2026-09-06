vuodenajat = (
    "talvi", "talvi", "kevät", "kevät",
    "kevät", "kesä", "kesä", "kesä",
    "syksy", "syksy", "syksy", "talvi"
)

kuukausi = int(input("Anna kuukauden numero (1-12): "))
vuodenaika = vuodenajat[kuukausi - 1]

print(f"{kuukausi}. kuukausi kuuluu vuodenaikaan {vuodenaika}.")