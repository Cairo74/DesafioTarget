def exercicio2():
    numero = int(input("Informe um número: "))

    if pertence_a_fibonacci(numero):
        print(f"{numero} pertence à sequência de Fibonacci.")
    else:
        print(f"{numero} NÃO pertence à sequência de Fibonacci.")

def pertence_a_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n or n == 0

exercicio2()