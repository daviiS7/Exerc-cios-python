s = 0
n = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n
print('A soma entre todos os números é igual a {}'.format(s))
