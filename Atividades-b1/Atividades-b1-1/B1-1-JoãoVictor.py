"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
"                  FATEC São Caetano do Sul                 "
"                       Atividade B1-1                      "
"                João Victor Pitareli stoffel               "
"                Objetivo: Catalogo de Filmes               "
"                Data: 24.02.2026                           "
"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="

catalogo = {}
def adicionar_filme(id_filme, titulo, diretor):
    if id_filme in catalogo:
        print("Este ID já existe!")
    else:
        catalogo[id_filme] = {"titulo": titulo, "diretor": diretor}

def buscar_filme(id_filme):
    return catalogo.get(id_filme, "Este filme não foi encontrado")

def remover_filme(id_filme):
    catalogo.pop(id_filme, None)
    print ("Este filme foi removido!")

def listar_todos():
    if not catalogo:
        print("\nO catálogo está vazio.")
    else:
        print("\nCatálogo de Filmes:")
        for id_f, dados in catalogo.items():
            print(f"ID: {id_f} | Título: {dados['titulo']} | Diretor: {dados['diretor']}")

adicionar_filme("1", "O poderoso chefão", "Francis Ford Coppola")
adicionar_filme("2", "O Grande Hotel Budapeste", "Wes Anderson")
adicionar_filme("3", "Coringa", "Todd Phillips")
adicionar_filme("4", "O Senhor dos Anéis: A Sociedade do Anel", "Peter Jackson")
adicionar_filme("5", "Gladiador", "Ridley Scott")
