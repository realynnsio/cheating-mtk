# Copying my code from the last one to make things easier lol
derajat = int(input("Derajat polinom adalah: "))
n = derajat + 1
koefisien = []

# To check if the number is an integer or a float
def is_number_int(y):
    try:
        y = int(y)
        return True
    except (TypeError, ValueError):
        return False

# Just to elaborate
print("Masukan koefisiennya satu2 dari belakang!")

# Picking up the koefisiens
for i in range(n):
    x = (input())

    if is_number_int(x) == True:
        x = int(x)
    else:
        x = float(x)

    koefisien.append(x)

# Avoiding error in banyak turunan input
def banyak_turunan():
    a = input("Masukkan banyak turunan: ")

    if is_number_int(a) == True:
        return int(a)
    else:
        print("insert a valid number!\n")
        banyak_turunan()

# Getting banyaknya turunan
n_turunan = banyak_turunan()

# Proses penurunan
for i in range(n_turunan):
    for x in range(n):
        koefisien[x] = koefisien[x] * x
    koefisien.pop(0)
    n = n - 1

# Printing out what we have lol
for y in range(n):
    if koefisien[y] != 0:
        print(str(koefisien[y]) + "x^" + str(y))
    else:
        pass

# This is also hot garbage
