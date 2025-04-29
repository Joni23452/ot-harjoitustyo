# Arkkitehtuurikuvaus

## Ohjelman rakenne
Ui-hakemiston käyttöliittymä pyytää tietoa sekä lähettää suorituspyyntöjä Services-hakemiston ItemService-luokalle. Services-hakemiston luokat suorittavat pyyntöihin liittyvän sovelluslogiikan ja lähettävät Repositories-hakemiston luokille pyyntöjä tarvittavista haettavista tiedoista sekä tallennettavista tiedoista. Services-hakemiston luokat sitten palauttavat Ui-hakemiston luokille pyydetyt tiedot päivitykset.

## Sovelluslogiikasta
ItemService vastaanottaa pyyntöjä tavaran saamisesta ja muuntamisesta sekä tietojen hakemisesta. Tavaran saamiseen ja muuntamiseen avustaa RandomService ja tietojen hakemiseen Repositories.

# Luokkakaavio
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

# Sekvenssikaavio tavaran muuntamisesta
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