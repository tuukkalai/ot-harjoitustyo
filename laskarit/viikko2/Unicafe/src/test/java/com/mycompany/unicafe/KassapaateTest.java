/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.unicafe;

import static org.hamcrest.core.Is.is;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author tuukkala
 */
public class KassapaateTest {

    Kassapaate kassa;
    
    @Before
    public void setUp(){
        this.kassa = new Kassapaate();
    }
    
//    luodun kassapäätteen rahamäärä ja myytyjen lounaiden määrä on oikea (rahaa 1000, lounaita myyty 0)
    @Test
    public void kassanRahamaaraAlussaOikea() {
        assertThat(kassa.kassassaRahaa(), is(100000));
    }
    
    @Test
    public void kassanMyytyjenEdullistenLounaidenMaaraAlussaOikea() {
        assertThat(kassa.edullisiaLounaitaMyyty(), is(0));
    }

    @Test
    public void kassanMyytyjenMaukkaidenLounaidenMaaraAlussaOikea() {
        assertThat(kassa.maukkaitaLounaitaMyyty(), is(0));
    }    
    
//    käteisosto toimii sekä edullisten että maukkaiden lounaiden osalta
//    jos maksu riittävä: kassassa oleva rahamäärä kasvaa lounaan hinnalla ja vaihtorahan suuruus on oikea
    @Test
    public void edullinenLounasOstoKateinen() {
        int vaihtoraha = kassa.syoEdullisesti(500);
        assertThat(vaihtoraha, is(260));
        assertThat(kassa.edullisiaLounaitaMyyty(), is(1));
        assertThat(kassa.kassassaRahaa(), is(100240));
    }
    
    @Test
    public void edullinenLounasOstoLiianVahanRahaa() {
        int vaihtoraha = kassa.syoEdullisesti(200);
        assertThat(vaihtoraha, is(200));
        assertThat(kassa.edullisiaLounaitaMyyty(), is(0));
        assertThat(kassa.kassassaRahaa(), is(100000));
    }
    
    
    @Test
    public void edullinenLounasOstoKortti() {
        Maksukortti kortti = new Maksukortti(1000);
        boolean maksu = kassa.syoEdullisesti(kortti);
        assertThat(maksu, is(true));
        assertThat(kassa.edullisiaLounaitaMyyty(), is(1));
        // Korttiosto ei lisää rahaa (käteistä) kassaan
        assertThat(kassa.kassassaRahaa(), is(100000));
    }
    
    @Test
    public void edullinenLounasOstoKorttiLiianVahanRahaa() {
        Maksukortti kortti = new Maksukortti(238);
        boolean maksu = kassa.syoEdullisesti(kortti);
        assertThat(maksu, is(false));
        assertThat(kassa.edullisiaLounaitaMyyty(), is(0));
        assertThat(kassa.kassassaRahaa(), is(100000));
    }
//    jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
//    jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu, kaikki rahat palautetaan vaihtorahana ja myytyjen lounaiden määrässä ei muutosta
//    seuraavissa testeissä tarvitaan myös Maksukorttia jonka oletetaan toimivan oikein
//    korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
//    jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan true
//    jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
//    jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu, myytyjen lounaiden määrä muuttumaton ja palautetaan false
//    kassassa oleva rahamäärä ei muutu kortilla ostettaessa
//    kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla

}
