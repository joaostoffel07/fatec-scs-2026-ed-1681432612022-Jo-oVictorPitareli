class No:
    def __init__(self, valor):
        self.valor = valor
        self.esq = self.dir = None


class ArvoreBST:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        self.raiz = self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if not no:
            return No(valor)

        if valor < no.valor:
            no.esq = self._inserir(no.esq, valor)
        else:
            no.dir = self._inserir(no.dir, valor)

        return no

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, no, valor):
        if not no or no.valor == valor:
            return no
        return self._buscar(no.esq, valor) if valor < no.valor else self._buscar(no.dir, valor)

    def imprimir_nos_internos(self):
        print("Nós Internos:")
        self._internos(self.raiz)
        print()

    def _internos(self, no):
        if no:
            if no.esq or no.dir:
                print(no.valor, end=" ")
            self._internos(no.esq)
            self._internos(no.dir)

    def imprimir_folhas(self):
        print("Folhas:")
        self._folhas(self.raiz)
        print()

    def _folhas(self, no):
        if no:
            if not no.esq and not no.dir:
                print(no.valor, end=" ")
            self._folhas(no.esq)
            self._folhas(no.dir)

    def imprimir_niveis(self):
        fila = [self.raiz]
        nivel = 0

        while fila:
            print(f"Nível {nivel}: ", end="")
            for _ in range(len(fila)):
                atual = fila.pop(0)
                print(atual.valor, end=" ")

                if atual.esq:
                    fila.append(atual.esq)
                if atual.dir:
                    fila.append(atual.dir)

            print()
            nivel += 1

    def calcular_altura(self, no):
        if not no:
            return -1
        return 1 + max(self.calcular_altura(no.esq), self.calcular_altura(no.dir))

    def calcular_profundidade(self, valor):
        atual = self.raiz
        profundidade = 0

        while atual:
            if atual.valor == valor:
                return profundidade

            atual = atual.esq if valor < atual.valor else atual.dir
            profundidade += 1

        return -1

    def imprimir_ancestrais(self, valor):
        ancestrais = []
        atual = self.raiz

        while atual and atual.valor != valor:
            ancestrais.append(atual.valor)
            atual = atual.esq if valor < atual.valor else atual.dir

        print("Ancestrais:", ancestrais)

    def imprimir_descendentes(self, valor):
        print("Descendentes:", end=" ")
        self._descendentes(self.buscar(valor))
        print()

    def _descendentes(self, no):
        if no:
            if no.esq:
                print(no.esq.valor, end=" ")
                self._descendentes(no.esq)

            if no.dir:
                print(no.dir.valor, end=" ")
                self._descendentes(no.dir)

    def grau_no(self, valor):
        no = self.buscar(valor)
        if not no:
            return -1
        return int(no.esq is not None) + int(no.dir is not None)

    def analisar_arvore(self, valor_busca):
        print("===== DIAGNÓSTICO GERAL =====")
        print("Raiz:", self.raiz.valor)

        self.imprimir_nos_internos()
        self.imprimir_folhas()
        self.imprimir_niveis()

        print("\n===== DIAGNÓSTICO DO NÓ =====")
        print("Valor pesquisado:", valor_busca)
        print("Grau:", self.grau_no(valor_busca))

        self.imprimir_ancestrais(valor_busca)
        self.imprimir_descendentes(valor_busca)

        no = self.buscar(valor_busca)
        print("Altura:", self.calcular_altura(no))
        print("Profundidade:", self.calcular_profundidade(valor_busca))