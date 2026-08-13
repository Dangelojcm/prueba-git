def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Números primos del 1 al 30:")
for num in range(1, 31):
    if es_primo(num):
        print(num)

def saludo():
    return "Hola"