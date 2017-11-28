from app import app
import unittest


class Test(unittest.TestCase):
    
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

    def test_url(self):
        # envia uma requisicao GET para a URL
        result = self.app.get('/') 

        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(result.status_code, 200) 

    def test_content(self):
        # envia uma requisicao GET para a URL
        result = self.app.get('/') 

        # verifica o retorno do conteudo da pagina
        self.assertEqual(result.data.decode(), "TESTE")


if __name__ == "__main__":
    unittest.main()