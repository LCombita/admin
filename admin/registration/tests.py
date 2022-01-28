from genericpath import exists
from django.test import TestCase
from .models import User, Grantor, DataGrantor


class GrantorTestCase(TestCase):
    """Verificar si al crear un Otorgante desde el proxy model Grantor,
    crea automaticamente el DataGrantor con la señál create_data_otorgante.
    Y al crear un usuario el DataGrantor no se crea"""
    def setUp(self):
        Grantor.objects.create_user('test', 'test@test.com', 'test1234')
        #User.objects.create_user('test', 'test@test.com', 'test1234')
    
    def test_datagrantor_of_grantor(self):
        exists = DataGrantor.objects.filter(user__username='test').exists()
        self.assertEqual(exists, True)
        #self.assertEqual(exists, False)

