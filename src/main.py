from lib.iris import iris
from lib.digits import digits
from lib.linnerud import linnerud
from lib.wine import wine
from lib.breast_cancer import breast_cancer

while (True) :

    print("Data mana yang ingin anda visualisasikan convex hull-nya ?")
    print("1. Iris")
    print("2. Breast_Cancer")
    print("3. Digits")
    print("4. Linnerud")
    print("5. Wine")
    print("6. Exit")
    print()

    choice = int(input("Pilihan anda >> "))

    if choice == 1:
        iris()
    elif choice == 2:
        breast_cancer()
    elif choice == 3:
        digits()
    elif choice == 4:
        linnerud()
    elif choice == 5:
        wine()
    elif choice == 6:
        break