'''
Created on May 12, 2016

@author: carlos
'''
from Billetera import *
import unittest

class PruebasBilletera(unittest.TestCase):  
    def testClaseDueno(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
    
    def testClaseBilletera(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        
    def testRecargar(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134902)
        bill = BilleteraElectronica('255', Angel, 2201)
        bill.recargar(1500, '2201')
        self.assertEqual(1500, bill.saldo)
        
    def testSaldo(self):
        Angel = dueno('Angel', 'Martiñez Gonzalez', 21134
        bill = BilleteraElectronica('255', Angel, 2201)
        self.assertEqual(0, bill.saldo())
    
        