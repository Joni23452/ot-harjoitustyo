import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)
    
    def test_luotu_kassapaate_nolla_myyty(self):
        self.assertEqual(self.kassapaate.edulliset + self.kassapaate.maukkaat, 0)
    
    def test_kateisosto_edullisilla_nostaa_myytyjä(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    
    def test_kateisosto_edullisilla_nostaa_kassan_rahaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002.4)
    
    def test_kateisosto_edullisilla_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(vaihtoraha, 0)
    
    def test_kateisosto_edullisilla_raha_ei_riitä_kassan_rahat_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_kateisosto_edullisilla_raha_ei_riita_ei_myydä(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kateisosto_edullisilla_rahat_ei_riitä_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)


    def test_kateisosto_maukkailla_nostaa_myytyjä(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_kateisosto_maukkailla_nostaa_kassan_rahaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1004)
    
    def test_kateisosto_maukkaasti_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(vaihtoraha, 0)
    
    def test_kateisosto_maukkaasti_raha_ei_riitä_kassan_rahat_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_kateisosto_maukkaasti_raha_ei_riita_ei_myydä(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_maukkaasti_rahat_ei_riitä_vaihtoraha_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihtoraha, 200)

    def test_korttiosto_edullisesti_rahat_riittää(self):
        maksukortti = Maksukortti(1000)
        ostos = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(maksukortti.saldo_euroina(), 7.6)
        self.assertTrue(ostos)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)

    def test_korttiosto_edullisesti_rahat_ei_riittää(self):
        maksukortti = Maksukortti(100)
        ostos = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(maksukortti.saldo_euroina(), 1)
        self.assertFalse(ostos)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)

    def test_korttiosto_maukkaasti_rahat_riittää(self):
        maksukortti = Maksukortti(1000)
        ostos = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(maksukortti.saldo_euroina(), 6)
        self.assertTrue(ostos)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)

    def test_korttiosto_maukkaasti_rahat_ei_riittää(self):
        maksukortti = Maksukortti(100)
        ostos = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(maksukortti.saldo_euroina(), 1)
        self.assertFalse(ostos)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)

    def test_kortille_rahaa_ladattaessa_kortin_raha_kasvaa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 10)
        self.assertEqual(maksukortti.saldo_euroina(), 10.1)

    def test_kortille_rahaa_ladattaessa_kassan_raha_kasvaa(self):
        maksukortti = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 10)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.1)