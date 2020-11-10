package com.mycompany.unicafe;

import static org.hamcrest.core.Is.is;
import static org.hamcrest.core.IsNull.notNullValue;
import static org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;

public class MaksukorttiTest {

    Maksukortti kortti;

    @Before
    public void setUp() {
        kortti = new Maksukortti(1000);
    }

    @Test
    public void luotuKorttiOlemassa() {
        assertThat(kortti, notNullValue());
    }

    @Test
    public void kortinSaldoAlussaOikein() {
        assertThat(kortti.toString(), is("saldo: 10.0"));
    }

    @Test
    public void rahanLataaminenKasvattaaSaldoaOikein() {
        kortti.lataaRahaa(1500);
        assertThat(kortti.toString(), is("saldo: 25.0"));
    }
    
    @Test
    public void negatiivinenLatausEiMuutaSaldoa() {
        kortti.lataaRahaa(-400);
        assertThat(kortti.toString(), is("saldo: 10.0"));
    }

    @Test
    public void saldoVaheneeOikeinJosRahaaOnTarpeeksi() {
        kortti.otaRahaa(600);
        assertThat(kortti.toString(), is("saldo: 4.0"));
    }

    @Test
    public void saldoEiMuutuJosRahaaEiOleTarpeeksi() {
        kortti.otaRahaa(700);
        kortti.otaRahaa(400);
        assertThat(kortti.toString(), is("saldo: 3.0"));
    }
    
    @Test
    public void negatiivinenOttoEiMuutaSaldoa() {
        boolean otto = kortti.otaRahaa(-50);
        assertThat(otto, is(false));
        assertThat(kortti.toString(), is("saldo: 10.0"));
    }
    
    @Test
    public void korttiPalauttaaTrueJosRahatRiittivat() {
        boolean otto = kortti.otaRahaa(1000);
        assertThat(otto, is(true));
    }
    
    @Test
    public void korttiPalauttaaFalseJosRahatEivatRiita() {
        boolean otto = kortti.otaRahaa(1000000);
        assertThat(otto, is(false));
    }
    
    @Test
    public void saldoMetodiPalauttaaSaldonOikein() {
        kortti.otaRahaa(100);
        assertThat(kortti.saldo(), is(900));
    }
}
