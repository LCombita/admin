from django.test import TestCase
from registration.models import User
from project.models import Cliente, Proyecto
from deed.models import Reparto
from stage.models import Etapa, RepartoEtapa

class RepartoEtapasTestCase(TestCase):

    def setUp(self):    
        us = User.objects.create_user('test', 'test@test.com', 'test1234')
        cl = Cliente.objects.create(nombre_cliente='generico')
        pr = Proyecto.objects.create(cliente=cl, nombre_proyecto='generico')
        Etapa.objects.create(tipo_etapa='REC', nombre_etapa='ELABORACION')
        Etapa.objects.create(tipo_etapa='REC', nombre_etapa='REVISION VIRTUAL')
        Reparto.objects.create(protocolista=us, proyecto=pr, fecha_reparto='2022-02-11', fecha_escritura='2022-02-12', escritura=111)

    def agregar_etapas_a_reparto(self):
        r = Reparto.objects.get(fecha_reparto='2022-02-11')
        print('reparto desde el test created: ', r.id,' hoja ruta: ', r.hoja_ruta)
        eta = Etapa.objects.filter()
        for et in eta:
            print('etapas desde el test created: ', et.nombre_etapa)
        for e in eta:
            RepartoEtapa.objects.create(reparto=r, etapa=e, fecha_inicio='2022-03-16')
        ret = RepartoEtapa.objects.filter()
        for reta in ret:
            print('RepartoEtapa desde el test created: ', 'reparto: ', reta.reparto, ', etapa: ', reta.etapa.nombre_etapa, ', fecha: ', reta.fecha_inicio)
