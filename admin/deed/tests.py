from django.test import TestCase
from .models import User, Reparto, Proyecto, Cliente
from django.utils.timezone import now

class FechaRepartoTestCase(TestCase):

    def setUp(self):
        us = User.objects.create_user('test', 'test@test.com', 'test1234')
        cl = Cliente.objects.create(nombre_cliente='generico')
        pr = Proyecto.objects.create(cliente=cl, nombre_proyecto='generico')
        Reparto.objects.create(protocolista=us, proyecto=pr, fecha_reparto='2022-02-11')

    def test_fecha_reparto(self):
        r = Reparto.objects.get(fecha_reparto='2022-02-11')
        h = now()
        print('hoy: ', h, ', fecha reparto: ', r.fecha_reparto, ',  creado: ', r.creado )

