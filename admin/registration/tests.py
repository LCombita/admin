from genericpath import exists
from django.test import TestCase
from .models import User, Grantor, DataGrantor
from django.contrib.auth.models import  Group


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


class GroupTestCase(TestCase):
    """Verificar el registro de un grupo nuevo, al registrar un usuario
    y  asignarlo al al usuario creado"""

    def setUp(self):
        Group.objects.create(name='notario')
        Grantor.objects.create_user('test', 'test@test.com', 'test1234')
    
    def test_create_group(self):
        exists = Group.objects.filter(name='notario').exists()
        notario = Group.objects.get(name='notario')
        user = Grantor.objects.get(username='test')
        user.groups.add(notario)
        print("test: grupo ", notario, " usuario ", user)
        ingroup = user.groups.filter(name=notario)
        print("test: en grupo notario? ", ingroup)
        self.assertEqual(exists, True)
