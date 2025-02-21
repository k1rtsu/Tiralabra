Testaus

Toimivuustestaus

Projektia testataan yksikkö- ja end-to-end-testeillä. Yksikkötesteissä keskitytään tarkistamaan kaikki pienetkin 
apufunktiot, joita löytyy erityisesti Huffmanin koodista. End-to-end-testit puolestaan varmistavat, että algoritmit 
toimivat kokonaisuutena oikeilla tiedostoilla ja syötteillä.

Testidataksi on pyritty kokoamaan mahdollisimman erityylisiä ja eri pituisia tekstejä. Testaus suoritetaan kahdeksalla 
(tällä hetkellä seitsemällä) erilaisella tiedostolla. Testitiedostot ovat:

suurin_satunnainen.txt – satunnaisesti generoitu teksti (10 MB)

hw.txt – klassinen "Hello World" -fraasi

kalevala.txt – Kalevalan runoja vanhalla suomen kielellä

karri_koira.txt – Karri Koiran "Sydämmet"-kappaleen lyriikat

loremipsum.txt – noin 1 MB kokoinen Lorem Ipsum -teksti

rc.txt – "Life and Adventures of Robinson Crusoe" -kirjan viisi ensimmäistä lukua englanniksi

redundancy_zero.txt – lyhyt teksti, jossa ei ole toistoa

empty.txt – tyhjä tekstitiedosto

Testikattavuus

Testikattavuuden voi tarkistaa komennolla:

poetry run coverage html

Kompressiotestit

Kompressiotesteissä käydään läpi compressing_test_data/-kansion tiedostot yksi kerrallaan. Jokainen tiedosto pakataan ja 
puretaan, minkä jälkeen tarkistetaan, että tiedoston sisältö on identtinen alkuperäisen kanssa. Testissä myös vertaillaan 
pakatun tiedoston kokoa alkuperäiseen nähden.

Testit voi ajaa algoritmista riippuen seuraavilla komennoilla:

Huffman-koodaus:

poetry run python3 src/compressing_testing_huffman.py

LZ78-algoritmi:

poetry run python3 src/compressing_testing_lz78.py

Tehokkuustestaus

TODO


