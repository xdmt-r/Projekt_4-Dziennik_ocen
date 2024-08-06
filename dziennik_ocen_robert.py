# DZIENNIK OCEN
child1 = {
    1: dict(Matematyka=[1, 2, 3, 4, 5]),
    2: dict(Polski=[1, 2, 3, 4, 5]),
    3: dict(Przyrka=[5, 4, 3, 2, 1]),
    4: dict(Fizyka=[5, 4, 3, 2, 1])
}
child2 = {
    1: dict(Matematyka=[1, 1, 3, 4, 1]),
    2: dict(Polski=[2, 2, 3, 1, 2]),
    3: dict(Przyrka=[1, 2, 3, 2, 1]),
    4: dict(Fizyka=[3, 2, 2, 2, 1])
}
child3 = {
    1: dict(Matematyka=[3, 2, 3, 4, 2]),
    2: dict(Polski=[2, 3, 3, 4, 1]),
    3: dict(Przyrka=[2, 2, 3, 2, 2]),
    4: dict(Fizyka=[1, 1, 1, 2, 1])
}
child4 = {
    1: dict(Matematyka=[5, 3, 2, 4, 2]),
    2: dict(Polski=[2, 4, 3, 4, 3]),
    3: dict(Przyrka=[4, 4, 3, 3, 2]),
    4: dict(Fizyka=[5, 4, 3, 5, 2])
}
child5 = {
    1: dict(Matematyka=[1, 1, 1, 1, 1]),
    2: dict(Polski=[2, 2, 2, 2, 2]),
    3: dict(Przyrka=[3, 3, 3, 3, 3]),
    4: dict(Fizyka=[4, 4, 4, 4, 4])
}
child6 = {
    1: dict(Matematyka=[5, 5, 5, 5, 5]),
    2: dict(Polski=[4, 4, 4, 4, 4]),
    3: dict(Przyrka=[3, 3, 3, 3, 3]),
    4: dict(Fizyka=[2, 2, 1, 2, 1])
}
child7 = {
    1: dict(Matematyka=[]),
    2: dict(Polski=[]),
    3: dict(Przyrka=[]),
    4: dict(Fizyka=[])
}
child8 = {
    1: dict(Matematyka=[]),
    2: dict(Polski=[]),
    3: dict(Przyrka=[]),
    4: dict(Fizyka=[])
}

lista_obecnosci = {
    1: child1,
    2: child2,
    3: child3,
    4: child4,
    5: child5,
    6: child6,
    7: child7,
    8: child8
}

students = {
    1: dict(child1="Adam Adam"),
    2: dict(child2="Beata Beata"),
    3: dict(child3="Celina"),
    4: dict(child4="Darek Darek"),
    5: dict(child5="Edek"),
    6: dict(child6="Filip Filip"),
    7: dict(child7="grażyna Grażyna"),
    8: dict(child8="janusz janusz")
}

# pokazuje imię i nazwisko oraz numer w dzienniku ucznia.
def info_oceny(numer):
    if numer in students:
        obj = students[numer]
        print("Numer w dzienniku: ", numer)
        for child, name in obj.items():
            print("Imię i nazwisko:", name)
# pokazuje oceny z danego przedmiotu lub wyświetla wszystkie oceny.
# zastanawiam się czy nie poprzenosić "print" niżej, żeby wypluwało wszystko "na raz"
def przedmioty(numer):
    if numer in lista_obecnosci:
        lista = lista_obecnosci[numer]
        przedmiot = int(input("Wprowadź numer przedmiotu: "
        "1 - Matematyka, 2 - Polski, 3 - Przyrka, 4 - Fizyka lub wpisz '5'"
                              " by zobaczyć wszystkie oceny."))
        if 0 < przedmiot <= 4:
            print(f"Oceny: {przedmiot}: {lista[przedmiot]}")
        elif przedmiot == 5:
            for i, przedmiot in lista.items():
                if przedmiot:
                    print(f"{i}: {przedmiot}")
        elif przedmiot < 0:
            print("Nieprawidłowy numer przedmiotu.")
        else:
            print("Nieprawidłowy numer przedmiotu.")
    else:
        print("Brak takiego numer w dzienniku.")


# DO ZROBIENIA
# ew. poprzenosić "print" tak aby wypluwało wszystkie info. na raz. ???
# dodać dla przećwiczenia linijki poprawiające: imię i nazwisko
# def avg(przedmiot):

def wpisz_oceny(numer):
    question = "t"
    while question != "n":

        numer = int(input("Podaj swój numer w dzienniku: "))
        if numer in range(1, 7):
            info_oceny(numer)
            przedmioty(numer)
            # avg(przedmiot)
        elif numer == 7 or numer == 8:
            wpisz_oceny(numer)
            # avg(przedmiot)
        else:
            print("Niepoprawny numer, jest tylko 8 osób w dzienniku.")

        question = input("jeszcze raz t/n?")

wpisz_oceny(7)