# test_main.py
#Feito por Daniel dos Santos Gama - RU: 4121047
import unittest
from main import Produto, Cliente


class TestProduto(unittest.TestCase):
    """Teste para a classe Produto."""

    def test_criar_produto(self):
        produto = Produto("001", "Pneu XYZ", 50, 200.0)
        self.assertEqual(produto.codigo, "001")
        self.assertEqual(produto.marca, "Pneu XYZ")
        self.assertEqual(produto.quantidade_estoque, 50)
        self.assertEqual(produto.valor_unitario, 200.0)

    def test_registrar_entrada(self):
        produto = Produto("002", "Óleo", 20, 50.0)
        produto.registrar_entrada(30)
        self.assertEqual(produto.quantidade_estoque, 50)

    def test_registrar_saida(self):
        produto = Produto("003", "Filtro", 10, 100.0)
        produto.registrar_saida(5)
        self.assertEqual(produto.quantidade_estoque, 5)

    def test_saida_insuficiente(self):
        produto = Produto("004", "Bateria", 5, 500.0)
        with self.assertRaises(ValueError):
            produto.registrar_saida(10)


class TestCliente(unittest.TestCase):
    """Teste para a classe Cliente."""

    def test_criar_cliente(self):
        cliente = Cliente("Carlos Silva", "12345678900", "carlos@email.com")
        self.assertEqual(cliente.nome, "Carlos Silva")
        self.assertEqual(cliente.cpf, "12345678900")
        self.assertEqual(cliente.email, "carlos@email.com")
        self.assertEqual(len(cliente.historico_compras), 0)

    def test_registrar_compra(self):
        cliente = Cliente("Ana Souza", "98765432100", "ana@email.com")
        cliente.registrar_compra("Pneu XYZ", 2, 400.0)
        self.assertEqual(len(cliente.historico_compras), 1)
        self.assertEqual(cliente.historico_compras[0]["produto"], "Pneu XYZ")
        self.assertEqual(cliente.historico_compras[0]["quantidade"], 2)
        self.assertEqual(cliente.historico_compras[0]["valor_total"], 400.0)


if __name__ == "__main__":
    unittest.main()
