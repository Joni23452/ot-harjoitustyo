# Changelog

## Viikko 3

- Lisätty Item-luokka, joka sisältää tiedot tavarasta.
- Lisätty ItemsDatabase-luokka, joka pitää kirjaa olemassa olevista tavaroista.
- Lisätty Inventory-luokka, joka pitää kirjaa pelaajan omistamista tavaroista.
- Lisätty ItemService-luokka, joka hoitaa sovelluslogiikan.
- Lisätty tekstikäyttöliittymä. Pelaaja voi saada yhdenlaista tavaraa ja näkee omistamansa tavarat.
- Testattu, että Item-luokan olio palauttaa nimensä.

## Viikko 4

- Lisätty RandomService-luokka joka vastaa logiikasta ja satunnaisuudesta tavaroiden muuntamisessa toiseksi.
    - Lasketaan olemassa olevien tavaroiden arvojen etäisyydet muunnettavan tavaran arvoon ja käytetään näiden käänteislukuja painoina arvottaessa uutta tavaraa.
- Lisätty CONVERT-komento jolla pelaaja voi muuntaa tavaran toiseksi.
    - Muunto perustuu tavaran arvoon. Takaisin saa todennäköisesti lähes samanarvoisen tavaran mutta on mahdollista saada minkäarvoinen tavara tahansa.
- Muutettu GET-komennolla tavaran saamista niin että pelaaja saa satunnaisen tavaran jonka arvo on todennäköisesti lähellä nollaa.
- Pelissä on nyt 4 eriarvoista tavaraa.
- Käyttöliittymää hieman kehitetty.

## Viikko 5

- Pelaajan tavaraluettelo tallennetaan nyt tiedostoon. Tallentamisesta ja tavaraluettelon ylläpitämisestä vastaa InventoryRepository-luokka.
- Peliin lisätään tavarat nyt tiedostosta. Tiedoston lukemisesta ja tietojen hausta vastaa ItemRepository-luokka.
- Pelaaja nyt näkee tavaroidensa arvon ja yhteisarvon sekä näkee enemmän tietoja saadessaan ja muuntaessaan tavaraa.
- Testattu convert-toimintoa

## Viikko 6

- Muutettu CONVERT komentoa niin että suuren arvoeron tavara on nyt entistä harvinaisempaa saada.
- Lisätty ITEMS-komento jolla pelaaja näkee kohtaamansa tavarat sekä montako pelin tavaroista on löydetty.
- Testattu että muuntaminen onnistuneena muuttaa pelaajan tavaraluettelon sisältöä ja epäonnistuneena tavaraluettelo pysyy entisellään.
