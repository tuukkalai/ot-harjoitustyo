import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), 'saldo: 10.0')

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), 'saldo: 20.0')

    # def test_negatiivinen_lataus_ei_vahenna_saldoa(self):
    #    self.maksukortti.lataa_rahaa(-500)
    #    self.assertEqual(str(self.maksukortti), 'saldo: 10.0')

    def test_saldo_vahenee_oikein_jos_rahaa_on(self):
        self.maksukortti.ota_rahaa(100)
        self.assertEqual(str(self.maksukortti), 'saldo: 9.0')

    def test_saldo_ei_vahene_jos_rahaa_on_liian_vahan(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(str(self.maksukortti), 'saldo: 10.0')

    def test_ota_rahaa_palauttaa_true_jos_rahaa_on_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)

    def test_ota_rahaa_palauttaa_false_jos_rahaa_ei_ole_tarpeeksi(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)
