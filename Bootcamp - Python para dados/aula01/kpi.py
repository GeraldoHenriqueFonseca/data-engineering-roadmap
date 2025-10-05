# 1) Solicita ao usuário que digite seu nome
nome = input("Digite seu nome: ")
# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salario = float(input("Digite o valor do seu salário: "))
# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
bonus = float(input("Digite o valor do bônus recebido: "))
# 4) Calcule o valor do bônus final
BONUS = 1000
bonus_final = BONUS + (salario * bonus)
# 5) Imprima cálculo do KPI para o usuário
kpi = salario + bonus_final

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Olá {nome}, seu salário é R$ {salario:.2f} e seu bônus final é R$ {bonus_final:.2f}.")
# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

# 1 Não há verificação de entrada para garantir que o salário e o bônus sejam números válidos.
# 2 Não há verificação para garantir que o salário e o bônus sejam positivos.
# 3 O cálculo do bônus final pode resultar em um valor inesperado se o fator bônus digitado for incorreto, deveria ser algo constante como o valor 1000 somado.
# 4 Não há tratamento de exceções para entradas inválidas, o que pode causar falhas no programa.
# 5 A mensagem final não formata os valores monetários, o que pode dificultar a leitura.