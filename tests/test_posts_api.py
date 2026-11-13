"""Testes automatizados da API pública JSONPlaceholder (/posts).

Usa somente a biblioteca padrão do Python. Para rodar:
    python -m unittest discover -s tests -v
"""

import json
import unittest
import urllib.error
import urllib.request

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 10


def requisicao(metodo, caminho, corpo=None):
    """Faz uma requisição HTTP e devolve (status, json_ou_None)."""
    dados = None
    cabecalhos = {"Accept": "application/json"}
    if corpo is not None:
        dados = json.dumps(corpo).encode("utf-8")
        cabecalhos["Content-Type"] = "application/json; charset=UTF-8"

    req = urllib.request.Request(
        BASE_URL + caminho, data=dados, headers=cabecalhos, method=metodo
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            conteudo = resp.read().decode("utf-8")
            return resp.status, json.loads(conteudo) if conteudo else None
    except urllib.error.HTTPError as erro:
        erro.close()
        return erro.code, None


CAMPOS_POST = {"id", "title", "body", "userId"}


class TestListarPosts(unittest.TestCase):
    def test_retorna_status_200(self):
        status, _ = requisicao("GET", "/posts")
        self.assertEqual(status, 200)

    def test_retorna_lista_com_100_posts(self):
        _, posts = requisicao("GET", "/posts")
        self.assertIsInstance(posts, list)
        self.assertEqual(len(posts), 100)

    def test_cada_post_tem_os_campos_esperados(self):
        _, posts = requisicao("GET", "/posts")
        for post in posts:
            with self.subTest(post_id=post.get("id")):
                self.assertTrue(CAMPOS_POST.issubset(post.keys()))
                self.assertIsInstance(post["id"], int)
                self.assertIsInstance(post["userId"], int)
                self.assertIsInstance(post["title"], str)


class TestBuscarPost(unittest.TestCase):
    def test_busca_post_existente(self):
        status, post = requisicao("GET", "/posts/1")
        self.assertEqual(status, 200)
        self.assertEqual(post["id"], 1)

    def test_post_inexistente_retorna_404(self):
        status, _ = requisicao("GET", "/posts/9999")
        self.assertEqual(status, 404)


class TestCriarPost(unittest.TestCase):
    def test_criar_post_retorna_201_com_id(self):
        novo = {"title": "Teste de QA", "body": "Corpo do teste", "userId": 1}
        status, criado = requisicao("POST", "/posts", novo)
        self.assertEqual(status, 201)
        self.assertIn("id", criado)
        self.assertEqual(criado["title"], novo["title"])
        self.assertEqual(criado["body"], novo["body"])
        self.assertEqual(criado["userId"], novo["userId"])


class TestAtualizarPost(unittest.TestCase):
    def test_atualizar_post_existente(self):
        alteracao = {"id": 1, "title": "Titulo alterado", "body": "Novo corpo", "userId": 1}
        status, atualizado = requisicao("PUT", "/posts/1", alteracao)
        self.assertEqual(status, 200)
        self.assertEqual(atualizado["title"], "Titulo alterado")


class TestRemoverPost(unittest.TestCase):
    def test_remover_post_existente(self):
        status, _ = requisicao("DELETE", "/posts/1")
        self.assertEqual(status, 200)


if __name__ == "__main__":
    unittest.main()
