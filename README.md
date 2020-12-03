# Ohjelmistotekniikka, harjoitustyö

## Release

[Viikon 5 release](https://github.com/tuukkalai/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/tuukkalai/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/tuukkalai/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)


## Tehtävät

### [Viikko 1](https://github.com/tuukkalai/ot-harjoitustyo/blob/main/laskarit/viikko1/)

- [gitlog.txt](https://github.com/tuukkalai/ot-harjoitustyo/blob/main/laskarit/viikko1/gitlog.txt)
- [komentorivi.txt](https://github.com/tuukkalai/ot-harjoitustyo/blob/main/laskarit/viikko1/komentorivi.txt)

### [Viikko 2](https://github.com/tuukkalai/ot-harjoitustyo/blob/main/laskarit/viikko2/)

- [Unicafe Maksukortin testit](https://github.com/tuukkalai/ot-harjoitustyo/blob/main/laskarit/viikko2/Unicafe/src/test/java/com/mycompany/unicafe/MaksukorttiTest.java)
- [Unicafe Kassapäätteen testit](https://github.com/tuukkalai/ot-harjoitustyo/blob/main/laskarit/viikko2/Unicafe/src/test/java/com/mycompany/unicafe/KassapaateTest.java)

<img src="https://raw.githubusercontent.com/tuukkalai/ot-harjoitustyo/main/laskarit/viikko2/jacoco_testiraportti.png" width="750">

## Sovelluksen komennot

### Testaus

Testit voidaan ajaa komennolla

```sh
mvn test
```

### Sovelluksen suoritus

Sovelluksen voi suorittaa komennolla

```sh
mvn compile exec:java -Dexec.mainClass=matopeli.Main
```

Jar-tiedoston saa luotua komennolla

```sh
mvn package
```

Generoitu jar-tiedosto löytyy target -hakemiston alta.

### Checkstyle

Checkstyle saadaan ajettua komennolla

```sh
mvn jxr:jxr checkstyle:checkstyle
```

Checkstylen muodostama tiedosto löytyy hakemistosta target/site/checkstyle.html
