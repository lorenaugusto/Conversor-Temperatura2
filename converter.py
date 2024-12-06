print("Conversor de Temperaturas")
tipo = input("Digite 'C' para Celsius ou 'F' para Fahrenheit: ").upper()
valor = float(input("Digite o valor da temperatura: "))

if tipo == 'C':
    fahrenheit = (valor * 9/5) + 32
    print(f"{valor}°C é igual a {fahrenheit:.2f}°F")
elif tipo == 'F':
    celsius = (valor - 32) * 5/9
    print(f"{valor}°F é igual a {celsius:.2f}°C")
else:
    print("Opção inválida.")
