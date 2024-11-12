def obebBulma(num1, num2):
    obeb = 0
    if num2 > num1:
        x = num1
    else:
        x = num2
    while x > 0:
        if num1 % x == 0 and num2 % x == 0:
            obeb = x
            break
        x -= 1
    return obeb

def okekBulma(num1, num2):
    okek = 0
    if num1 < num2:
        x = num2
    else:
        x = num1
    while x <= num1 * num2:
        if x % num1 == 0 and x % num2 == 0:
            okek = x
            break
        x += 1
    return okek

num1 = int(input("Birinci sayıyı girin: "))
num2 = int(input("İkinci sayıyı girin: "))

obeb = obebBulma(num1, num2)
okek = okekBulma(num1, num2)

print("OBEB:", obeb)
print("OKEK:", okek)
