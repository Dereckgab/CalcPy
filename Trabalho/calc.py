def Somar(a, b):
    return a + b

def Subtrair(a, b):
    return a - b

def Multplicar(a, b):
    return a * b

def Dividir(a, b):
    if b == 0:
        return "Erro divisao por 0"
    return a / b

def calculadora():
    print("Calculadora em py")
    print("Selecione a operação")
    print("1 Soma")
    print("2 Subtrair")
    print("3 Mutiplicar")
    print("4 Dividir")

    escolha = input("Digite o número da operação desejada (1/2/3/4):")

    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segunndo numero: "))

    if escolha == '1':
        print("Resultado:", Somar(num1, num2))
    elif escolha == '2':
        print("Resultado:", Subtrair(num1, num2))
    elif escolha == '3':
        print("Resultado:", Multplicar(num1, num2))
    elif escolha == '4':
        print("Resultado:", Dividir(num1, num2))
    else:
        print("Opção inválida. Por favor, escolha uma operação válida.")

calculadora()

# --- EXPLICAÇÃO DAS FUNÇÕES ---

# somar(a, b):
# Esta função recebe dois parâmetros (a e b) e retorna a soma deles.
# É usada quando o usuário escolhe a opção 1 (adição).

# subtrair(a, b):
# Esta função recebe dois parâmetros (a e b) e retorna a subtração (a - b).
# É usada quando o usuário escolhe a opção 2 (subtração).

# multiplicar(a, b):
# Esta função recebe dois parâmetros (a e b) e retorna a multiplicação entre eles.
# É usada quando o usuário escolhe a opção 3 (multiplicação).

# dividir(a, b):
# Esta função realiza a divisão de 'a' por 'b', mas antes verifica se 'b' é igual a zero.
# Se for zero, retorna uma mensagem de erro, pois dividir por zero não é permitido.
# Caso contrário, retorna o resultado da divisão.

# calculadora():
# Esta é a função principal do programa. Ela:
# - Mostra as opções de operações para o usuário.
# - Recebe a escolha da operação via input.
# - Recebe dois números que o usuário deseja calcular.
# - Com base na escolha, chama uma das quatro funções (somar, subtrair, multiplicar, dividir).
# - Exibe o resultado final.
# - Se o usuário digitar uma opção inválida, exibe uma mensagem de erro.

# No final do código, a função calculadora() é chamada para iniciar o programa.
