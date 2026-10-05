try:
    num1 = int(input("coloque o primeiro número: "))
    num2 = int(input("coloque o segundo número: "))  
    divisao = num1 / num2
    print(f"A divisão de {num1} por {num2} é: {divisao}")

except ValueError:
    print("Erro, insira apenas números.")
except ZeroDivisionError:
    print("Erro, não é possível dividir por zero.")