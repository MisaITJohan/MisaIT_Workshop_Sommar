# Övning 07-02: Skriv en modul med funktioner för kattläten
# och anropa den modulens funktioner från det här programmets main-funktion.

from UppgifterFrånPythonGrundkurs.Lektion07.exempelpaket.animals import bark, bark_loudly


def main():
    bark()
    bark_loudly()


main()
