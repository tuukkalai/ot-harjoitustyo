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
    public void edullinenLounasOstoKateinenLiianVahanRahaa() {
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
        assertThat(kortti.saldo(), is(760));
        assertThat(kassa.edullisiaLounaitaMyyty(), is(1));
        assertThat(kassa.kassassaRahaa(), is(100000));
    }
    
    @Test
    public void edullinenLounasOstoKorttiLiianVahanRahaa() {
        Maksukortti kortti = new Maksukortti(238);
        boolean maksu = kassa.syoEdullisesti(kortti);
        assertThat(maksu, is(false));
        assertThat(kortti.saldo(), is(238));
        assertThat(kassa.edullisiaLounaitaMyyty(), is(0));
        assertThat(kassa.kassassaRahaa(), is(100000));
    }
    
    @Test
    public void edullinenLounasOstoKateinenTasaraha() {
        int vaihtoraha = kassa.syoEdullisesti(240);
        assertThat(vaihtoraha, is(0));
        assertThat(kassa.edullisiaLounaitaMyyty(), is(1));
        assertThat(kassa.kassassaRahaa(), is(100240));
    }    
    
    @Test
    public void edullinenLounasOstoKorttiTasaraha() {
        Maksukortti kortti = new Maksukortti(240);
        boolean maksu = kassa.syoEdullisesti(kortti);
        assertThat(maksu, is(true));
        assertThat(kortti.saldo(), is(0));
        assertThat(kassa.edullisiaLounaitaMyyty(), is(1));
        assertThat(kassa.kassassaRahaa(), is(100000));
    }
        
    @Test
    public void maukasLounasOstoKateinen() {
        int vaihtoraha = kassa.syoMaukkaasti(500);
        assertThat(vaihtoraha, is(100));
        assertThat(kassa.maukkaitaLounaitaMyyty(), is(1));
        assertThat(kassa.kassassaRahaa(), is(100400));
    }
    
    @Test
    public void maukasLounasOstoKateinenLiianVahanRahaa() {
        int vaihtoraha = kassa.syoMaukkaasti(300);
        assertThat(vaihtoraha, is(300));
        assertThat(kassa.maukkaitaLounaitaMyyty(), is(0));
        assertThat(kassa.kassassaRahaa(), is(100000));
    }    
    
    @Test
    public void maukasLounasOstoKortti() {
        Maksukortti kortti = new Maksukortti(1000);
        boolean maksu = kassa.syoMaukkaasti(kortti);
        assertThat(maksu, is(true));
        assertThat(kortti.saldo(), is(600));
        assertThat(kassa.maukkaitaLounaitaMyyty(), is(1));
        assertThat(kassa.kassassaRahaa(), is(100000));
    }
    
    @Test
    public void maukasLounasOstoKorttiLiianVahanRahaa() {
        Maksukortti kortti = new Maksukortti(238);
        boolean maksu = kassa.syoMaukkaasti(kortti);
        assertThat(maksu, is(false));
        assertThat(kortti.saldo(), is(238));
        assertThat(kassa.maukkaitaLounaitaMyyty(), is(0));
        assertThat(kassa.kassassaRahaa(), is(100000));
    }
    
    @Test
    public void maukasLounasOstoKateinenTasaraha() {
        int vaihtoraha = kassa.syoMaukkaasti(400);
        assertThat(vaihtoraha, is(0));
        assertThat(kassa.maukkaitaLounaitaMyyty(), is(1));
        assertThat(kassa.kassassaRahaa(), is(100400));
    }    
    
    @Test
    public void maukasLounasOstoKorttiTasaraha() {
        Maksukortti kortti = new Maksukortti(400);
        boolean maksu = kassa.syoMaukkaasti(kortti);
        assertThat(maksu, is(true));
        assertThat(kortti.saldo(), is(0));
        assertThat(kassa.maukkaitaLounaitaMyyty(), is(1));
        assertThat(kassa.kassassaRahaa(), is(100000));
    }
    
//    kortille rahaa ladattaessa kortin saldo muuttuu ja kassassa oleva rahamäärä kasvaa ladatulla summalla
    @Test
    public void lataaRahaaKortille() {
        Maksukortti kortti = new Maksukortti(200);
        kassa.lataaRahaaKortille(kortti, 600);
        assertThat(kortti.saldo(), is(800));
        assertThat(kassa.kassassaRahaa(), is(100600));
    }
    
    @Test
    public void lataaNegatiivinenMaaraRahaaKortille() {
        Maksukortti kortti = new Maksukortti(200);
        kassa.lataaRahaaKortille(kortti, -200);
        assertThat(kortti.saldo(), is(200));
        assertThat(kassa.kassassaRahaa(), is(100000));
    }
}
