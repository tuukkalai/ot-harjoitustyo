/**
 *
 * @author tuukkala
 */

//import org.junit.After;
//import org.junit.AfterClass;
import org.junit.Before;
//import org.junit.BeforeClass;
import static org.junit.Assert.*;
import org.junit.Test;

public class MaksukorttiTest {
    
    Maksukortti kortti;
    
    @Before
    public void setUp(){
        kortti = new Maksukortti(10);
    }
    
    @Test
    public void konstruktoriAsettaaSaldonOikein(){
        assertEquals("Kortilla on rahaa 10.0 euroa", kortti.toString());
    }
    
    @Test
    public void syoEdullisestiVahentaaSaldoaOikein(){
        kortti.syoEdullisesti();
        assertEquals("Kortilla on rahaa 7.5 euroa", kortti.toString());
    }
    
    @Test
    public void syoMaukkaastiVahentaaSaldoaOikein(){
        kortti.syoMaukkaasti();
        assertEquals("Kortilla on rahaa 6.0 euroa", kortti.toString());
    }
    
    @Test
    public void syoEdullisestiEiVieSaldoaNegatiiviseksi(){
        kortti.syoMaukkaasti();
        kortti.syoMaukkaasti();
        kortti.syoEdullisesti();
        assertEquals("Kortilla on rahaa 2.0 euroa", kortti.toString());
    }
    
    @Test
    public void syoMaukkaastiEiVieSaldoaNegatiiviseksi(){
        kortti.syoEdullisesti();
        kortti.syoMaukkaasti();
        kortti.syoMaukkaasti();
        assertEquals("Kortilla on rahaa 3.5 euroa", kortti.toString());
    }
    
    @Test
    public void kortilleVoiLadataRahaa(){
        kortti.lataaRahaa(25);
        assertEquals("Kortilla on rahaa 35.0 euroa", kortti.toString());
    }
    
    @Test
    public void kortinSaldoEiYlitaKortinMaksimiarvoa(){
        kortti.lataaRahaa(200);
        assertEquals("Kortilla on rahaa 150.0 euroa", kortti.toString());
    }
    
    @Test
    public void negatiivisenArvonLataaminenKortilleEiMuutaSaldoa(){
        kortti.lataaRahaa(-5);
        assertEquals("Kortilla on rahaa 10.0 euroa", kortti.toString());
    }
    
    @Test
    public void tasarahallaSaaSyodaEdullisesti(){
        kortti.syoEdullisesti();
        kortti.syoEdullisesti();
        kortti.syoEdullisesti();
        kortti.syoEdullisesti();
        assertEquals("Kortilla on rahaa 0.0 euroa", kortti.toString());
    }
    
    @Test
    public void tasarahallaSaaSyodaMaukkaasti(){
        kortti.lataaRahaa(2);
        kortti.syoMaukkaasti();
        kortti.syoMaukkaasti();
        kortti.syoMaukkaasti();        
        assertEquals("Kortilla on rahaa 0.0 euroa", kortti.toString());
    }
}