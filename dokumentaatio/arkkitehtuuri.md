# Arkkitehtuurikuvaus

## Ohjelman rakenne
Ohjelman rakenne koostuu kolmesta tasosta jotka sijaitsevat omissa hakemistoissaan:
- Käyttöliittymä (ui-hakemisto)
- Sovelluslogiikka (services-hakemisto)
- Tietojen tallennus ja haku (repositories-hakemisto)

### Käyttöliittymä
Käyttöliittymä toteuttaa ohjelman käyttöliittymän ja aina tarvittaessa pyytää tietoa sekä lähettää suorituspyyntöjä sovelluslogiikan ItemService-luokalle.  

### Sovelluslogiikka
ItemService-luokka vastaanottaa pyyntöjä sovelluslogiikan suorittamisesta sekä tavaroita ja tavaraluetteloa koskevien tietojen hausta. ItemService kommunikoi muiden sovelluslogiikan luokkien kanssa suorittaakseen pyyntöihin liittyvän sovelluslogiikan ja aina tarvittaessa tietojen hakuun ja tallennukseen lähetetään pyyntöjä repositories-hakemiston luokille. ItemService-luokka lopulta palauttaa käyttöliittymälle käyttöliittymän tarvitsemat pyyntöön liittyvät tiedot.

### Tietojen tallennus ja haku
Repositories-hakemiston luokat vastaavat suorituksen aikaisesta tietojen tallennuksesta ja hausta sekä päivittävät pysyväistallennuksen tiedostoja. Lisäksi ne ylläpitävät entities-hakemiston olioita jotta tietojen hakuun ei aina tarvitse avata tiedostoja. Vain repositories-hakemiston luokat ovat tietoisia olioiden toteutuksesta. Tavaraluettelossa tavaroihin viitataan niitä kuvaavilla luvuilla ja tavaroista saa tietoa vastaavalla luvulla pyytämällä ItemRepository-luokalta.

# Luokkakaavio ohjelman luokista

```mermaid
 classDiagram
    ItemService "1" -- "1" ItemRepository
    ItemService "1" -- "1" InventoryRepository
    ItemRepository "1" -- "1" ItemDatabase
    ItemDatabase "1" -- "*" Item
    ItemService "1" -- "1" RandomService
    RandomService "1" .. "1" ItemRepository
    class Item{
        name
        value
    }
    class ItemRepository{
        get_item_name(item_id)
        get_item_value(item_id)
    }
    class RandomService{
        convert(value)
    }
    class InventoryRepository{
        add_item(item_id)
        remove_item(item_id)
        get_content()
        has_item(item_id)
    }
```

# Sekvenssikaavio tavaran muuntamisen toteutuksesta
```mermaid
sequenceDiagram
    actor player
    participant Ui
    participant ItemService
    participant RandomService
    Participant InventoryRepository
    Participant ItemRepository
    player ->> Ui: "CONVERT"
    Ui ->> player: Item name?
    player ->> Ui: "Banana"
    Ui ->> ItemService: convert_item("Banana")
    ItemService ->> ItemRepository: item_with_name_exists("Banana")
    ItemRepository ->> ItemService: True
    ItemService ->> ItemRepository: get_item_id_by_name("Banana")
    ItemRepository ->> ItemService: 1
    ItemService ->> InventoryRepository: has_item(1)
    InventoryRepository ->> ItemService: True
    ItemService ->> ItemRepository: get_item_value(1)
    ItemRepository ->> ItemService: 5
    ItemService ->> RandomService: convert(5)
    RandomService ->> ItemService: 3
    ItemService ->> InventoryRepository: remove_item(1)
    ItemService ->> InventoryRepository: add_item(3)
    ItemService ->> ItemRepository: get_item_name(3)
    ItemRepository ->> ItemService: "Mug"
    ItemService ->> ItemRepository: get_item_value(3)
    ItemRepository ->> ItemService: 15
    ItemService ->> Ui: [True, "Mug", 15-5=10]
    Ui ->> player: Converted Banana to Mug, value gain/loss: 10

```