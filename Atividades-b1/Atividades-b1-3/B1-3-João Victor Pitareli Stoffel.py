"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
"                  FATEC São Caetano do Sul                 "
"                       Atividade B1-3                      "
"                João Victor Pitareli stoffel               "
"                Objetivo: Calculadora RPN                  "
"                Data: 24.03.2026                           "
"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="



x = y = z = t = 0
string_x = string_y = string_z = string_t = ""

notacao = "7 5 3 / 2 + - 4 *"
entradas = notacao.split(' ')

pilha = 0

for entrada in entradas:
    if entrada in ['+', '-', '*', '/']:
        if pilha < 2:
            raise ValueError("Esta faltando numeros")
        if entrada == '+':
            x = y + x
        elif entrada == '-':
            x = y - x
        elif entrada == '*':
            x = y * x
        elif entrada == '/':
            x = y / x

        string_x = f"({string_y} {entrada} {string_x})"

        y = z
        z = t
        string_y = string_z
        string_z = string_t
        string_t = ""
        pilha -= 1
    else:
        try:
            valor = int(entrada)
        except ValueError:
            raise ValueError(f"A entrada é inválida: {entrada}")
        t = z
        z = y
        y = x
        x = valor
        string_t = string_z
        string_z = string_y
        string_y = string_x
        string_x = entrada
        pilha += 1
    print(f"Pilha: T={t}, Z={z}, Y={y}, X={x}")

print(f"Expressão em notação algébrica: {string_x}")
print(f"O resultado é: {x}")
