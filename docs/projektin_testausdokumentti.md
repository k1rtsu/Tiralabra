# Testaus

## Toimivuustestaus

Projektia testataan yksikkö- ja end-to-end-testeillä. Yksikkötesteissä keskitytään tarkistamaan kaikki pienetkin apufunktiot, joita löytyy erityisesti Huffmanin koodista. End-to-end-testit puolestaan varmistavat, että algoritmit toimivat kokonaisuutena oikeilla tiedostoilla ja syötteillä.

Testidataksi on pyritty kokoamaan mahdollisimman erityylisiä ja eri pituisia tekstejä. Testaus suoritetaan kahdeksalla (tällä hetkellä seitsemällä) erilaisella tiedostolla. Testitiedostot ovat:

- **suurin_satunnainen.txt** – satunnaisesti generoitu teksti (10 MB)
- **hw.txt** – klassinen "Hello World" -fraasi
- **kalevala.txt** – Kalevalan runoja vanhalla suomen kielellä
- **karri_koira.txt** – Karri Koiran "Sydämmet"-kappaleen lyriikat
- **loremipsum.txt** – noin 1 MB kokoinen Lorem Ipsum -teksti
- **rc.txt** – "Life and Adventures of Robinson Crusoe" -kirjan viisi ensimmäistä lukua englanniksi
- **redundancy_zero.txt** – lyhyt teksti, jossa ei ole toistoa
- **empty.txt** – tyhjä tekstitiedosto

## Testikattavuus

Testikattavuuden voi tarkistaa komennolla:

```sh
poetry run coverage html
```
<img width="667" alt="Näyttökuva 2025-2-21 kello 19 22 13" src="https://github.com/user-attachments/assets/f288457d-6a51-4ce0-bf8e-65417499ceb7" />

## Kompressiotestit

Kompressiotesteissä käydään läpi `compressing_test_data/`-kansion tiedostot yksi kerrallaan. Jokainen tiedosto pakataan ja puretaan, minkä jälkeen tarkistetaan, että tiedoston sisältö on identtinen alkuperäisen kanssa. Testissä myös vertaillaan pakatun tiedoston kokoa alkuperäiseen nähden.

Testit voi ajaa algoritmista riippuen seuraavilla komennoilla:

### Huffman-koodaus:
```sh
poetry run python3 src/compressing_testing_huffman.py
```

<img width="838" alt="Näyttökuva 2025-2-21 kello 20 47 10" src="https://github.com/user-attachments/assets/c92fd6f7-2b2a-4a08-9c51-b1574836ff2a" />



### LZ78-algoritmi:
```sh
poetry run python3 src/compressing_testing_lz78.py
```

<img width="791" alt="Näyttökuva 2025-2-21 kello 20 46 40" src="https://github.com/user-attachments/assets/92c3b275-6b1f-447a-9cf3-5e7342c69836" />

## Tehokkuustestaus

Tehokkuustestaus suoritetaan samalla datalla kuin kompressointitestaus. Tehokkuustestit mittaavat molempien algoritmien suoritusaikaa eri vaiheissa: koodauksessa, datan lataamisessa bittitiedostoon, datan haussa bittitiedostosta ja dekoodauksessa. Lisäksi testit tarkistavat, että dekoodattu syöte vastaa alkuperäistä dataa. 

Tehokkuustestin tulokset voi nähdä suorittamalla seuraavan komennon projektin juurikansiosta: 
```sh
poetry run python3 src/performance_testing.py 
```
