# Variáveis para armazenar os valores
numero1 = 10
numero2 = 20
numero3 = 30
numero4 = 40

frase = "eu amo azul"
palavra = "azul"

# Cálculo da média aritmética
media = (numero1 + numero2 + numero3 + numero4) / 4

# Cálculo do quadrado de um número (usando o número3 como exemplo)
quadrado_numero3 = numero3 ** 2

# Cálculo do dobro de um número (usando o número4 como exemplo)
dobro_numero4 = 2 * numero4

# Contagem de letras na palavra
quantidade_letras_palavra = len(palavra)

# Contagem de espaços em branco na frase
quantidade_espacos_frase = frase.count(" ")

# Verificação se o primeiro número é maior que o segundo
primeiro_maior_que_segundo = numero1 > numero2

# Encontrar o maior número
maior_numero = max(numero1, numero2, numero3, numero4)

# Impressão dos resultados
print(f"Média aritmética: {media:.2f}")
print(f"Quadrado do número 3: {quadrado_numero3}")
print(f"Dobro do número 4: {dobro_numero4}")
print(f"Quantidade de letras na palavra: {quantidade_letras_palavra}")
print(f"Quantidade de espaços em branco na frase: {quantidade_espacos_frase}")
print(f"O primeiro número é maior que o segundo? {primeiro_maior_que_segundo}")
print(f"O maior número é: {maior_numero}")
