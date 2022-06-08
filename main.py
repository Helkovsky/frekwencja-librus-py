from py_librus_api import Librus

librus = Librus()

# Login i hasło do librusa synergii
librus.login("LOGIN", "HASŁO")


class Lekcja:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.semestr1ob = 0
        self.semestr1nb = 0
        self.semestr2ob = 0
        self.semestr2nb = 0

    def add(self, semestr, ob):
        if semestr == 1:
            if ob:
                self.semestr1ob = self.semestr1ob + 1
            else:
                self.semestr1nb = self.semestr1nb + 1
        else:
            if ob:
                self.semestr2ob = self.semestr2ob + 1
            else:
                self.semestr2nb = self.semestr2nb + 1

    def get(self):
        print("=======================")
        print(f"Lekcja: {self.nazwa}")
        if not self.semestr1nb + self.semestr1ob == 0:
            print(
                f"Semestr 1: Ob {self.semestr1ob} Nb {self.semestr1nb} {round(self.semestr1ob / (self.semestr1nb + self.semestr1ob) * 100, 1)}%")
        if not self.semestr2nb + self.semestr2ob == 0:
            print(
                f"Semestr 2: Ob {self.semestr2ob} Nb {self.semestr2nb} {round(self.semestr2ob / (self.semestr2nb + self.semestr2ob) * 100, 1)}%")


if librus.logged_in:
    frekwencjaAll = librus.get_attendances()
    frekwencja = []

    for record in frekwencjaAll:
        przedmiot = record["Lesson"]["Subject"]
        semestr = record["Semester"]
        ob = record["Type"]["IsPresenceKind"]

        if not any(x.nazwa == przedmiot for x in frekwencja):
            lekcja = Lekcja(przedmiot)
            frekwencja.append(lekcja)

        for lekcja in frekwencja:
            if lekcja.nazwa == przedmiot:
                lekcja.add(semestr, ob)

    for lekcja in frekwencja:
        lekcja.get()
