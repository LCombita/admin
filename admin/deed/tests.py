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
        h = None
        print('hoy: ', h, ', fecha reparto: ', r.fecha_reparto, ',  creado: ', r.creado )
        #print ('año: ', h.strftime('%Y')+'-'+'12324')
        if h:
            a = h.strftime('%Y')
            ae = a + '-' + '4564'
            print (ae)
        else:
            print('nada')


class ActualizarRepartoTestCase(TestCase):

    def setUp(self):    
        us = User.objects.create_user('test', 'test@test.com', 'test1234')
        cl = Cliente.objects.create(nombre_cliente='generico')
        pr = Proyecto.objects.create(cliente=cl, nombre_proyecto='generico')
        Reparto.objects.create(protocolista=us, proyecto=pr, fecha_reparto='2022-02-11', fecha_escritura='2022-02-12', escritura=111)

    def test_hoja_ruta_anio_escritura(self):
        r = Reparto.objects.get(fecha_reparto='2022-02-11')
        print('reparto desde el test created: ', r.id,'escritura: ', r.escritura, 'hoja ruta: ', r.hoja_ruta)
        Reparto.objects.filter(id=1).update(escritura=555)
        rr = Reparto.objects.get(fecha_reparto='2022-02-11')
        print('reparto desde el test update: ', rr.escritura, 'anio escritura: ', rr.anio_escritura)
