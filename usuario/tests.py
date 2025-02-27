from django.test import TestCase
from .models import Usuario

class UsuarioTestModel(TestCase):
    def test_criar_usuario(self):
        usuario = Usuario.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='123123',
            nome='Test User'
        )

        self.assertEqual(usuario.email, 'test@example.com')

        self.assertEqual(usuario.username, 'testuser')

        self.assertEqual(usuario.nome, 'Test User')

        self.assertTrue(usuario.check_password('123123'))
