import decimal
from decimal import Decimal as D


def main():
    menu()


def menu():
    print("Main Menu")
    print()
    choice = input("""
                        A: Basic Conversions
                        B: Exit
                        Please enter:  """)
    if choice.lower() == "a":
        conversions()
    elif choice.lower() == "b":
        quit()


def conversions():
    choice = input("""
                        A: Grams to Moles
                        B: Moles to Grams
                        C: Atoms to Moles
                        D: Back
                        Please enter:  """)
    if choice.lower() == "a":
        g2m()
    elif choice.lower() == "b":
        m2g()
    elif choice.lower() == "c":
        a2m()
    elif choice.lower() == "d":
        menu()


def g2m():
    x = D(input("grams of species?"))
    y = D(input("molecular weight?"))
    z = float(x / y)
    print(z)
    conversions()


def m2g():
    x = D(input("moles of species?"))
    y = D(input("molecular weight?"))
    z = float(x * y)
    print(z)
    conversions()


def a2m():
    a = D(input("Number of Atoms?"))
    p = D(a) * D(6.022 * 10**23)
    print('{:10.2E}'.format(p))
    conversions()


main()
