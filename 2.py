def verificador_fib(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return True
    else:
        return False
6

input_numero = int(input("Digite um numero para saber se ele está na sequência de Fibonacci: "))

if verificador_fib(input_numero):
    print(f"{input_numero} está na sequência de Fibonacci.")
else:
    print(f"{input_numero} não está na sequência de Fibonacci.")
