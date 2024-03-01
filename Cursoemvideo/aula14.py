# Sabendo o LIMITE tanto faz usar o for ou while!!
# Não sabendo o limite é melhor usar só o while!
'''for c in range(1, 5):
    n = int(input("Digite um valor: "))
print("FIM")'''

'''r = "SIM"
while r == "SIM":
    n = int(input("Digite um valor: ")) # <- Isso eu chamo de condição de parada!!
    r = str(input("Quer continuar: [S/N] ")).upper()
print("FIM")'''

n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digito {} números pares e {} números impares.".format(par, impar))
