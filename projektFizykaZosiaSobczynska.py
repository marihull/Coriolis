import numpy as np
import matplotlib.pyplot as plt


def pobierzLiczbe(prompt, warunek=lambda x: True, komunikatBledu="Błędna wartość. Spróbuj ponownie."):
    while True:
        try:
            wartosc = float(input(prompt))
            if warunek(wartosc):
                return wartosc
            else:
                print(komunikatBledu)
        except ValueError:
            print("Nieprawidłowy format. Podaj liczbę.")


def wybierzCialo():
    cialaNiebieskie = {
        "Merkury": (3.7, 1.240),
        "Wenus": (8.87, 1.811),
        "Ziemia": (9.81, 7.2921159e-5),
        "Mars": (3.71, 7.088e-5),
        "Jowisz": (24.79, 1.76e-4),
        "Saturn": (10.44, 1.64e-4),
        "Uran": (8.69, 1.29e-4),
        "Neptun": (11.15, 1.08e-4),
        "Ganimedes": (1.428, 1.02e-5),
        "Tytan": (1.352, 4.56e-6),
        "Księżyc": (1.62, 2.66e-6),
        "Tryton": (0.779, 2.29e-5)
    }
    while True:
        print("Dostępne planety i księżyce:")
        for cialo in cialaNiebieskie.keys():
            print(f"- {cialo}")
        wybor = input("Wybierz ciało niebieskie: ")
        if wybor in cialaNiebieskie:
            return wybor, cialaNiebieskie[wybor]
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


def obliczPrzesuniecie(H, g, omega, phi):
    phiRad = np.radians(phi)
    return (2 / 3) * omega * np.sqrt((2 * H ** 3) / g) * np.cos(phiRad)


def obliczWysokosc(deltaX, g, omega, phi):
    phiRad = np.radians(phi)
    licznik = (deltaX ** 2) * 9 * g
    mianownik = 8 * (omega ** 2) * (np.cos(phiRad) ** 2)
    return (licznik / mianownik) ** (1 / 3)


def main():
    print("Program obliczający przesunięcie spowodowane siłą Coriolisa.")

    # Pobieranie danych wejściowych
    nazwaCiala, (g, omega) = wybierzCialo()

    H = pobierzLiczbe("Podaj wysokość puszczenia ciała (w metrach): ",
                      warunek=lambda x: x > 0,
                      komunikatBledu="Wysokość musi być dodatnia.")
    phi = pobierzLiczbe("Podaj szerokość geograficzną (w stopniach, od 0 do 90): ",
                        warunek=lambda x: 0 <= x <= 90,
                        komunikatBledu="Szerokość geograficzna musi być w zakresie od 0 do 90 stopni.")

    # Obliczenie przesunięcia Delta x
    deltaX = obliczPrzesuniecie(H, g, omega, phi)
    print(f"\nPrzesunięcie \u0394x: {deltaX:.4f} metra\n")

    # Wykres przesunięcia w funkcji szerokości geograficznej
    szerokosci = np.linspace(0, 90, 500)
    przesuniecia = [obliczPrzesuniecie(H, g, omega, p) for p in szerokosci]

    plt.figure(figsize=(10, 6))
    plt.plot(szerokosci, przesuniecia, label=f"{nazwaCiala}", color='blue')
    plt.xlabel("Szerokość geograficzna (stopnie)")
    plt.ylabel("Przesunięcie \u0394x (metry)")
    plt.title(f"Przesunięcie Coriolisa w funkcji szerokości geograficznej dla {nazwaCiala}")
    plt.grid(True)
    plt.legend()
    plt.show()

    # Obliczenie wymaganej wysokości dla podanego przesunięcia
    deltaXInput = pobierzLiczbe("Podaj wartość przesunięcia \u0394x (w metrach): ",
                                warunek=lambda x: x >= 0,
                                komunikatBledu="Przesunięcie musi być nieujemne.")

    wymaganaWysokosc = obliczWysokosc(deltaXInput, g, omega, phi)
    print(f"\nWymagana wysokość H dla przesunięcia \u0394x = {deltaXInput:.4f} m: {wymaganaWysokosc:.4f} metra\n")


if __name__ == "__main__":
    main()