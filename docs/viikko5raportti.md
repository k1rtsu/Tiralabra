Viikko 5

Tällä viikolla olen hieman laajentanut projektin toiminnallisuutta – nyt algoritmit voivat käsitellä myös tiedostojen 
pakkaamista. Tämän seurauksena laajensin myös testejä. Projekti testataan suurilla, pienillä, tyhjillä ja täysin 
toistumattomilla teksteillä. Testin aluksi tiedosto pakataan koodimuotoon, jonka jälkeen se dekoodataan takaisin 
alkuperäiseen muotoonsa ja verrataan keskenään.

Testien laajentamisen seurauksena jouduin myös hieman muokkaamaan Huffmanin koodausta, koska törmäsin ongelmaan tyhjien 
syötteiden käsittelyssä. Tämä korjaantui kuitenkin yhdellä koodirivillä. Lopulta algoritmit läpäisivät kaikki testit 
onnistuneesti, ja itse asiassa yllätyin niiden tehokkuudesta.

Ensi viikolla aion käyttää näppäimistöä pääasiassa tekstin, en koodin kirjoittamiseen. Suunnitelmissa on 
testausdokumentin ja käyttöohjeen kirjoittaminen sekä toteutusdokumentin aloittaminen. Lisäksi aion panostaa koodin 
dokumentaatioon, sillä se on tällä hetkellä hyvin puutteellinen. Vaikka suurimman osan ajasta käytän dokumentointiin, 
haluaisin myös koodata jonkin verran ja ainakin korjata vertaispalautteessa esiin tulleet puutteet ja korjausehdotukset. 
Jos aikaa jää, haluaisin lisätä vielä pari testitiedostoa, joissa käytettäisiin esimerkiksi muunnoskielellä kirjoitettuja 
tekstejä tai erikoismerkkejä sisältäviä tiedostoja.

Minulla on myös yksi kysymys:
En oikein keksi muita tapoja testata algoritmejani kuin yksikkötestit ja "päästä päähän" -testit tiedostoilla. 
Riittävätkö nämä testit vitosen arvosanaan, vai tulisiko projektiani testata vielä jollakin muulla tavalla? Jos kyllä, 
voisitko ehdottaa sopivan testausmenetelmän?

| Tehtävä           | Tunnit |
|-------------------|--------|
| Koodaus          | 5h     |
| Vertaisarviointi | 2h     |
| Dokumentaatio    | 1h     |
| **Yhteensä**     | **8h** |
