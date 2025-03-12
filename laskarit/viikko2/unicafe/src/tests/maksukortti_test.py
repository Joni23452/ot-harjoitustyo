import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(50)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.5)

    def test_rahan_ottaminen_vähentää_saldoa_oikein(self):
        self.maksukortti.ota_rahaa(50)

        self.assertEqual(self.maksukortti.saldo_euroina(), 9.5)

    def test_liian_rahan_ottaminen_ei_vähennä_saldoa(self):
        self.maksukortti.ota_rahaa(1050)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_ota_rahaa_palauttaa_true_kun_otto_onnistuu(self):
        result = self.maksukortti.ota_rahaa(50)

        self.assertTrue(result)
    
    def test_ota_rahaa_palauttaa_false_kun_otto_epäonnistuu(self):
        result = self.maksukortti.ota_rahaa(1050)

        self.assertFalse(result)

    def test_kortti_palauttaa_rahan_määrän(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")