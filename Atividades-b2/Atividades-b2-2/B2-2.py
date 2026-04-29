""""------------------------------------------ *
        Fatec São Caetano do Sul
            Atividade B2 - 2

RA : 1681432612022
Objetivo: Atividade passada em aula
data: 28 / 04 / 2026
*------------------------------------------ * """

fila_aluno = []
fila_admin = []
fila_reorganizada = []
role = 0


class Pedido:
    def __init__(self, role, nome, paginas):
        self.role = role
        self.nome = nome
        self.paginas = paginas

    def __str__(self):
        tipo = "Admin" if self.role == 1 else "Aluno"
        return f"[{tipo}] Arquivo: {self.nome} | Páginas: {self.paginas}"


while True:
    try:
        opt = int(input("""
0 - definir função
1 - fazer pedido
2 - mostrar filas
3 - organizar fila
4 - processar pedido
> """))
    except ValueError:
        print("Digite um número válido.")
        continue

    if opt == 0:
        if role == 1:
            print("Você já é administrador.")
        else:
            senha = input("Digite a senha: ")
            if senha == "123":
                role = 1
                print("Agora você é administrador.")
            else:
                print("Senha incorreta.")

    elif opt == 1:
        if fila_reorganizada:
            print("Não dá pra adicionar pedidos depois de organizar a fila.")
            continue

        nome = input("Nome do arquivo: ")
        try:
            paginas = int(input("Número de páginas: "))
        except ValueError:
            print("Número inválido.")
            continue

        pedido = Pedido(role, nome, paginas)

        if role == 1:
            fila_admin.append(pedido)
        else:
            fila_aluno.append(pedido)

        print("Pedido adicionado.")

    elif opt == 2:
        print("\n--- Fila Aluno ---")
        for item in fila_aluno:
            print(item)

        print("\n--- Fila Admin ---")
        for item in fila_admin:
            print(item)

        print("\n--- Fila Reorganizada ---")
        for item in fila_reorganizada:
            print(item)

    elif opt == 3:
        if not fila_admin and not fila_aluno:
            print("Não há pedidos para organizar.")
        else:
            fila_reorganizada = fila_admin + fila_aluno
            fila_admin.clear()
            fila_aluno.clear()
            print("Fila reorganizada com sucesso.")

    elif opt == 4:
        if not fila_reorganizada:
            print("A fila ainda não foi organizada.")
        else:
            atual = fila_reorganizada.pop(0)
            print("\nProcessando pedido:")
            print(atual)

    else:
        print("Opção inválida.")