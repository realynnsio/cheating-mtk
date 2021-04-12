# Setting up a few stuff at the beginning
derajat = int(input("Derajat polinom adalah: "))
n = derajat + 1
koefisien = []
akar_rasional = []

# To check if the number is an integer or a float
def is_number_int(y):
    try:
        a = int(y)
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

# Precaution if koefisien[0] = 0
if koefisien[0] == 0:
    akar_rasional.append(0)
    koefisien.pop(0)
    n = n - 1

# Nyari faktor a[0]
limit_a0 = abs(koefisien[0]) + 1
factors_akhir = []

for x in range (1, limit_a0):
    y = abs(koefisien[0])/x
    y_int = y.is_integer()
    if y_int == True:
        factors_akhir.append(int(y))

# Nyari faktor a[n]
limit_an = abs(koefisien[n-1]) + 1
factors_awal = []

for x in range (1, limit_an):
    y = abs(koefisien[n-1])/x
    y_int = y.is_integer()
    if y_int == True:
        factors_awal.append(int(y))

# Semua kemungkinan k
nilai_k = []

for i in range(len(factors_akhir)):
    for x in range(len(factors_awal)):
        z = factors_akhir[i] / factors_awal[x]
        nilai_k.append(abs(z))
        nilai_k.append(-abs(z))

# Mencari akar rasional dari list nilai_k
for i in range(len(nilai_k)):
    sum = 0
    for x in range(n):
        z = koefisien[x] * pow(nilai_k[i], x)
        sum = float(sum) + float(z)
    if int(sum) == 0:
        akar_rasional.append(nilai_k[i])
    elif (ValueError, TypeError):
        pass
    else:
        pass

akar_rasional = set(akar_rasional)

# Printing the results
print("Akar rasionalnya adalah...")
print(*akar_rasional, sep=", ")


# This is hot garbage but at least it works
