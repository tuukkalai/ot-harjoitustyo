import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
	def setUp(self):
		self.kassa = Kassapaate()
		self.kortti = Maksukortti(1000)

	def test_alustettaessa_oikea_maara_rahaa(self):
		self.assertEqual(self.kassa.kassassa_rahaa, 100000)

	def test_alustettaessa_oikea_maara_myytyja_edullisia_lounaita(self):
		self.assertEqual(self.kassa.edulliset, 0)

	def test_alustettaessa_oikea_maara_myytyja_maukkaita_lounaita(self):
		self.assertEqual(self.kassa.maukkaat, 0)

	# Käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta
    # Jos maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla ja vaihtorahan suuruus on oikea
	def test_kateisosto_edullinen_palauttaa_oikein(self):
		self.assertEqual(self.kassa.syo_edullisesti_kateisella(500), 260)
	
	def test_kateisosto_edullinen_kassassa_rahaa_oikein(self):
		self.kassa.syo_edullisesti_kateisella(500)
		self.assertEqual(self.kassa.kassassa_rahaa, 100240)

	def test_kateisosto_maukkaat_palauttaa_oikein(self):
		self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)
	
	def test_kateisosto_maukkaat_kassassa_rahaa_oikein(self):
		self.kassa.syo_maukkaasti_kateisella(500)
		self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    # Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
	def test_kateisosto_edullinen_kassassa_lounaat_oikein(self):
		self.kassa.syo_edullisesti_kateisella(500)
		self.assertEqual(self.kassa.edulliset, 1)

	def test_kateisosto_maukkaat_kassassa_lounaat_oikein(self):
		self.kassa.syo_maukkaasti_kateisella(500)
		self.assertEqual(self.kassa.maukkaat, 1)

    # Jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu, kaikki rahat palautetaan vaihtorahana ja myytyjen lounaiden määrässä ei muutosta
	def test_kateisosto_edullinen_kassa_palauttaa_oikein_liian_pienelle_summalle(self):
		self.assertEqual(self.kassa.syo_edullisesti_kateisella(200), 200)

	def test_kateisosto_edullinen_kassan_rahat_ei_muutu(self):
		self.kassa.syo_edullisesti_kateisella(200)
		self.assertEqual(self.kassa.kassassa_rahaa, 100000)

	def test_kateisosto_edullinen_kassa_ei_lisaa_myytyja_lounaita_liian_pienelle_summalle(self):
		self.kassa.syo_edullisesti_kateisella(200)
		self.assertEqual(self.kassa.edulliset, 0)

	def test_kateisosto_maukkaat_kassa_palauttaa_oikein_liian_pienelle_summalle(self):
		self.assertEqual(self.kassa.syo_maukkaasti_kateisella(300), 300)

	def test_kateisosto_maukkaat_kassan_rahat_ei_muutu(self):
		self.kassa.syo_maukkaasti_kateisella(300)
		self.assertEqual(self.kassa.kassassa_rahaa, 100000)

	def test_kateisosto_maukkaat_kassa_ei_lisaa_myytyja_lounaita_liian_pienelle_summalle(self):
		self.kassa.syo_maukkaasti_kateisella(300)
		self.assertEqual(self.kassa.maukkaat, 0)

	# Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
    # Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan True
	def test_korttiosto_edullinen_veloittaa_kortilta_oikein(self):
		self.kassa.syo_edullisesti_kortilla(self.kortti)
		self.assertEqual(str(self.kortti), 'saldo: 7.6')

	def test_korttiosto_edullinen_palauttaa_true(self):
		self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)

	def test_korttiosto_maukkaat_veloittaa_kortilta_oikein(self):
		self.kassa.syo_maukkaasti_kortilla(self.kortti)
		self.assertEqual(str(self.kortti), 'saldo: 6.0')

	def test_korttiosto_maukkaat_palauttaa_true(self):
		self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)

    # Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
	def test_korttiosto_edullinen_myytyjen_lounaiden_maara_kasvaa(self):
		self.kassa.syo_edullisesti_kortilla(self.kortti)
		self.assertEqual(self.kassa.edulliset, 1)

	def test_korttiosto_maukkaat_myytyjen_lounaiden_maara_kasvaa(self):
		self.kassa.syo_maukkaasti_kortilla(self.kortti)
		self.assertEqual(self.kassa.maukkaat, 1)

    # Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan False
	def test_korttiosto_edullinen_ei_veloita_kortilta_jos_rahaa_liian_vahan(self):
		koyha = Maksukortti(100)
		self.kassa.syo_edullisesti_kortilla(koyha)
		self.assertEqual(str(koyha), 'saldo: 1.0')

	def test_korttiosto_edullinen_palauttaa_false(self):
		koyha = Maksukortti(100)
		self.assertEqual(self.kassa.syo_edullisesti_kortilla(koyha), False)

	def test_korttiosto_edullinen_ei_kasvata_myytyjen_lounaiden_maaraa_jos_rahaa_liian_vahan(self):
		koyha = Maksukortti(100)
		self.kassa.syo_edullisesti_kortilla(koyha)
		self.assertEqual(self.kassa.edulliset, 0)

	def test_korttiosto_maukkaat_ei_veloita_kortilta_jos_rahaa_liian_vahan(self):
		koyha = Maksukortti(100)
		self.kassa.syo_maukkaasti_kortilla(koyha)
		self.assertEqual(str(koyha), 'saldo: 1.0')

	def test_korttiosto_maukkaat_palauttaa_false(self):
		koyha = Maksukortti(100)
		self.assertEqual(self.kassa.syo_maukkaasti_kortilla(koyha), False)

	def test_korttiosto_maukkaat_ei_kasvata_myytyjen_lounaiden_maaraa_jos_rahaa_liian_vahan(self):
		koyha = Maksukortti(100)
		self.kassa.syo_maukkaasti_kortilla(koyha)
		self.assertEqual(self.kassa.maukkaat, 0)

    # Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
	def test_korttiosto_edullinen_ei_kasvata_kassan_rahamaaraa(self):
		self.kassa.syo_edullisesti_kortilla(self.kortti)
		self.assertEqual(self.kassa.kassassa_rahaa, 100000)

	def test_korttiosto_maukkaat_ei_kasvata_kassan_rahamaaraa(self):
		self.kassa.syo_maukkaasti_kortilla(self.kortti)
		self.assertEqual(self.kassa.kassassa_rahaa, 100000)

	# Kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
	def test_kortin_lataus_kasvattaa_kassaa(self):
		self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
		self.assertEqual(self.kassa.kassassa_rahaa, 101000)

	def test_kortin_negatiivinen_lataus_ei_kasvata_kassaa(self):
		self.kassa.lataa_rahaa_kortille(self.kortti, -500)
		self.assertEqual(self.kassa.kassassa_rahaa, 100000)

	# Kortin toiminta parempi testata ainoastaan maksukortti_test.py:ssä ?
	def test_kortin_lataus_kasvattaa_kortin_saldoa(self):
		self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
		self.assertEqual(str(self.kortti), 'saldo: 20.0')

	def test_kortin_negatiivinen_lataus_ei_kasvata_kortin_saldoa(self):
		self.kassa.lataa_rahaa_kortille(self.kortti, -500)
		self.assertEqual(str(self.kortti), 'saldo: 10.0')
