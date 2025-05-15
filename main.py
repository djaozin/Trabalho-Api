class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

    def __str__(self):
        return f"{self.nome} | R$ {self.valor:.2f}"

class LojaGeek:
    def __init__(self):
        self.produtos = []

    def menu(self):
        print("\n--- LOJA GEEK FAKE API ---")
        print("1 - Cadastrar item")
        print("2 - Deletar item")
        print("3 - Mostrar itens")
        print("4 - Mostrar valor total da compra")
        print("5 - Sair")

    def cadastrar_item(self):
        nome = input("Digite o nome do item: ")
        try:
            valor = float(input("Digite o valor do item (R$): "))
            produto = Produto(nome, valor)
            self.produtos.append(produto)
            print(f"{nome} foi adicionado com sucesso.")
        except ValueError:
            print("Valor inválido.")

    def deletar_item(self):
        self.mostrar_itens()
        nome = input("Digite o nome do item que deseja deletar: ")
        produto_encontrado = next((produto for produto in self.produtos if produto.nome == nome), None)

        if produto_encontrado:
            self.produtos.remove(produto_encontrado)
            print(f"{nome} foi removido com sucesso.")
        else:
            print("Item não encontrado.")

    def mostrar_itens(self):
        if not self.produtos:
            print("Nenhum item cadastrado.")
        else:
            print("\nItens cadastrados:")
            for produto in self.produtos:
                print(produto)

    def mostrar_total(self):
        total = sum(produto.valor for produto in self.produtos)
        print(f"Valor total da compra: R$ {total:.2f}")

# Instanciando a classe LojaGeek e rodando o loop principal
loja = LojaGeek()

while True:
    loja.menu()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        loja.cadastrar_item()
    elif opcao == "2":
        loja.deletar_item()
    elif opcao == "3":
        loja.mostrar_itens()
    elif opcao == "4":
        loja.mostrar_total()
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")
