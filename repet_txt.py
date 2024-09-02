# Solicita uma string ao usuário
texto = input("Digite uma string: ")

# Solicita um número inteiro ao usuário
numero = int(input("Digite um número inteiro: "))

# Retorna a string repetida o número de vezes informado com espaço entre elas
resultado = (texto + " ") * numero

# Remove o espaço extra no final (opcional)
resultado = resultado.strip()

# Exibe o resultado
print("Resultado:", resultado)