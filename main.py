# main.py
#Feito por Daniel dos Santos Gama - RU: 4121047

class Produto:

    def __init__(self, codigo, marca, quantidade_estoque, valor_unitario):
        self.codigo = codigo
        self.marca = marca
        self.quantidade_estoque = quantidade_estoque
        self.valor_unitario = valor_unitario

    def registrar_entrada(self, quantidade):
        if quantidade < 0:
            raise ValueError("A quantidade de entrada não pode ser negativa.")
        self.quantidade_estoque += quantidade

    def registrar_saida(self, quantidade):
        if quantidade > self.quantidade_estoque:
            raise ValueError("Estoque insuficiente.")
        self.quantidade_estoque -= quantidade

    def __str__(self):
        return (
            f"Produto {self.marca} (Código: {self.codigo})\n"
            f"Quantidade em Estoque: {self.quantidade_estoque}\n"
            f"Preço Unitário: R$ {self.valor_unitario:.2f}\n"
        )


class Cliente:
    """Classe para gerenciar dados de clientes."""

    def __init__(self, nome, cpf, email):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.historico_compras = []

    def registrar_compra(self, produto, quantidade, valor_total):
        compra = {
            "produto": produto,
            "quantidade": quantidade,
            "valor_total": valor_total,
        }
        self.historico_compras.append(compra)

    def __str__(self):
        historico = "\n".join(
            [
                f"- {compra['produto']} | Quantidade: {compra['quantidade']} | Valor: R$ {compra['valor_total']:.2f}"
                for compra in self.historico_compras
            ]
        )
        return (
            f"Cliente: {self.nome} (CPF: {self.cpf})\n"
            f"E-mail: {self.email}\n"
            f"Compras:\n{historico if historico else 'Nenhuma compra registrada.'}\n"
        )


# Demonstração no terminal
if __name__ == "__main__":
    # Cadastro de produtos
    produto1 = Produto("001", "Pneu XYZ", 100, 300.0)
    produto2 = Produto("002", "Óleo Lubrificante", 200, 50.0)

    # Exibindo informações dos produtos
    print("Produtos cadastrados:")
    print(produto1)
    print(produto2)

    # Cadastro de clientes
    cliente1 = Cliente("Carlos Silva", "12345678900", "carlos@email.com")
    cliente2 = Cliente("Ana Souza", "98765432100", "ana@email.com")

    # Registrar compras para os clientes
    cliente1.registrar_compra(produto1.marca, 4, 1200.0)
    cliente1.registrar_compra(produto2.marca, 2, 100.0)

    cliente2.registrar_compra(produto2.marca, 10, 500.0)

    # Exibindo informações dos clientes
    print("\nClientes cadastrados e suas compras:")
    print(cliente1)
    print(cliente2)
