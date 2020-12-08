# Ohjelmistotekniikka, harjoitustyö

## Release

[Viikon 5 release](https://github.com/tuukkalai/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

[Vaatimusmäärittely](https://github.com/tuukkalai/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/tuukkalai/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)

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
