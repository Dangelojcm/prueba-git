texto = "Estoy aprendiendo Git y GitHub"
vocales = "aeiouAEIOU"
contador = sum(1 for letra in texto if letra in vocales)
print(f"Número de vocales: {contador}")