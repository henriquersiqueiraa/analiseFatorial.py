n = int(input("Digite um número inteiro\n"))

while n >= 0:
    fatorial = 1
    while n > 1:
        fatorial = fatorial * n
        n -= 1
    print(fatorial)
    
    n = int(input("Digite um número inteiro\n"))