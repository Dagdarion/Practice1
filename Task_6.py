value = 1000
resultat = 1

while value > 0:
    if (value % 10) != 0:
        resultat *= value % 10
    value //= 10

print("Произведение:", resultat)
