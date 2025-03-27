


x = input("Gebe die Zahl ein, von der du den Kehrwert bilden möchtest: ")
if x.isdigit():
    x = int(x)
    if x == 0:
        print("Division durch 0 ist nicht möglich!")
        pass
    if type(x) != int:
        print("Bitte geben nur Zahlen eingeben!")

    else:
        print("Der Kehrwert von ", x, " ist ", 1 / x)
else:
    print("Bitte geben nur Zahlen eingeben!")
    pass

x = input("Gebe die Zahl ein, von der du den Kehrwert bilden möchtest: ")
x = int(x)
print("Der Kehrwert von ",x, " ist " ,1/x)



