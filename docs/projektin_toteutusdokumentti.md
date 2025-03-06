Toteutusdokumentti

Ohjelman avulla voidaan pakata tekstitiedosto pienempään muotoon käyttäen kahta klassista datanpakkausalgoritmia: 
Huffmanin koodausta ja LZ-78. Ohjelmassa on myös ominaisuus, jonka avulla käyttäjä voi "pakata" itse kirjoittamaansa 
tekstiä, kuten sanaa tai fraasia. Tämä ominaisuus ei varsinaisesti pakkaa tietoa, vaan näyttää käyttäjälle, miltä 
kirjoitetun tekstin pakkauskoodi näyttää riippuen valitusta algoritmista. Huffmanin koodauksessa käyttäjä pystyy myös 
näkemään Huffman-puun, joka auttaa havainnollistamaan, miten koodaus toimii. Tämä ominaisuus on erityisen hyödyllinen 
algoritmien toiminnan ymmärtämisessä.

Algoritmien rakenne ja aikavaativuudet

Huffmanin koodaus

Huffmanin koodaus on tehokas tapa pakata dataa, ja se perustuu merkkien esiintymistiheyteen. Algoritmi luo jokaiselle 
merkille muuttuvan pituisen binäärikoodin siten, että usein esiintyvät merkit saavat lyhyemmät koodit ja harvemmin 
esiintyvät merkit pidemmät. Tämä vähentää datan kokonaistilaa.

Algoritmin vaiheet:

Frekvenssisanakirjan luonti: Lasketaan kunkin merkin esiintymiskerrat. Aikavaativuus: O(n), missä n on merkkien määrä 
syötteessä.
Prioriteettijonon (min-heap) luonti frekvenssien perusteella: Aikavaativuus: O(k log k), missä k on erilaisten merkkien 
määrä.
Huffman-puun rakentaminen: Yhdistetään pienimmän frekvenssin omaavat solmut, kunnes puu on valmis. Aikavaativuus: O(k log 
k).
Koodien muodostus: Kuljetaan puuta ja luodaan kullekin merkille binäärikoodi. Aikavaativuus: O(k).
Datan koodaus: Korvataan jokainen merkki sen binäärikoodilla. Aikavaativuus: O(n).
Datan purku: Luetaan binäärikoodia ja kuljetaan Huffman-puuta. Aikavaativuus: O(m), missä m on binäärikoodin pituus.
Kokonaisaikavaativuus: O(n + k log k), koska puun rakentaminen ja koodaus dominoivat prosessia. Tämä tekee Huffmanin 
koodauksesta erityisen tehokkaan, kun datassa on paljon toistoa.

LZ78

LZ78 on menetelmä, joka pakkaa tietoa rakentamalla sanakirjan dynaamisesti tekstin lukemisen yhteydessä. Algoritmin 
rakenne on seuraava:

Luodaan tyhjä sanakirja ja alustetaan muuttujat.
Käydään syöte läpi merkki kerrallaan.
Jos nykyinen merkkijono on jo sanakirjassa, jatketaan merkkijonon kasvattamista.
Jos merkkijono ei ole sanakirjassa, lisätään (index, merkki) -pari pakattuun tietoon ja tallennetaan uusi merkkijono 
sanakirjaan.
Lopuksi mahdollinen jäljelle jäänyt merkkijono lisätään pakattuun tietoon.
Purkamisvaiheessa:

Luodaan tyhjä sanakirja.
Käydään pakattu data läpi (index, merkki) -pareittain.
Rakennetaan alkuperäinen merkkijono hyödyntämällä sanakirjaa.
Aikavaativuus: O(n), missä n on syötteen pituus, sillä jokainen merkki käsitellään kerran.

Tiedoston tallennus ja lataus

Pakkauksen yhteydessä lasketaan optimaalinen bittimäärä indeksille ja merkille.
Data tallennetaan binääritiedostoon käyttäen bitarray-kirjastoa.
Latausvaiheessa tiedosto luetaan bittijonona ja puretaan alkuperäiseen muotoonsa.
Aikavaativuus tallennuksessa ja latauksessa riippuu tiedon määrästä ja käytettävästä bittimäärästä, mutta käytännössä ne 
toimivat tehokkaasti O(n) ajassa.

Yhteenveto

Huffmanin koodaus ja LZ78 ovat kaksi yleisesti käytettyä tiedonpakkausalgoritmia, joilla on erilaisia vahvuuksia ja 
heikkouksia. Huffmanin koodaus perustuu merkkien toistuvuuteen: mitä useammin tietty merkki esiintyy tiedostossa, sitä 
tehokkaammin se pakataan. Tämä tekee Huffmanin koodauksesta erityisen tehokkaan tiedostoissa, joissa on suuria määriä 
toistuvaa dataa. LZ78 puolestaan luo dynaamisesti sanakirjan koodatessaan dataa, mikä mahdollistaa nopean pakkauksen ja 
purkamisen. Se tunnistaa toistuvia merkkijonoja tekstissä, mikä tekee siitä erityisen nopean, mutta tämä nopeus saattaa 
heikentää sen pakkaustehokkuutta verrattuna Huffmanin koodaukseen. Molemmat algoritmit tarjoavat siis erilaisia 
ratkaisuja tiedonpakkaukseen riippuen käyttötarkoituksesta ja datan luonteesta.
