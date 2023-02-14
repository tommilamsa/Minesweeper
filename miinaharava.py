import haravasto
import random
import datetime
import math

tila = {
    "leveys": 0,
    "korkeus": 0,
    "kentta": [],
    "jaljella": [],
    "avatut": [],
    "miinat": 0,
    "aika": None,
    "vuorot": 0,
    "loppu": False,
    "tilastot": []
}

def miinoita(pelikentta, vapaat, miinat):
    """
    Asettaa kentälle N kpl miinoja satunnaisiin paikkoihin.
    
    :param list pelikentta: listarakenne, joka kuvaa pelikenttää
    :param list vapaat: monikkoja sisältävä lista, jotka sisältävät vapaana olevien ruutujen koordinaattipareja
    :param int miinat: asetettavien miinojen lukumäärä
    """
    
    for i in range(miinat):
        ruutu = random.choice(vapaat)
        x, y = ruutu
        pelikentta[y][x] = "x"
        vapaat.remove(ruutu)

def laske_miinat(rakenne):
    """
    Laskee annetussa kentässä jokaisen ruudun ympärillä olevat miinat.
    
    :param list rakenne: listarakenne, joka kuvaa pelikenttää
    """
    
    for i in range(len(rakenne)):
        for j in range(len(rakenne[i])):
            
            luku = 0
            
            if rakenne[i][j] == 'x':
                continue
            if i > 0 and rakenne[i-1][j] == 'x':
                luku += 1
            if i < len(rakenne) - 1 and rakenne[i+1][j] == 'x':
                luku += 1
            if j > 0 and rakenne[i][j-1] == 'x':
                luku += 1
            if j < len(rakenne[i]) - 1 and rakenne[i][j+1] == 'x':
                luku += 1
            if i > 0 and j > 0 and rakenne[i-1][j-1] == 'x':
                luku += 1
            if i > 0 and j < len(rakenne[i]) - 1 and rakenne[i-1][j+1] == 'x':
                luku += 1
            if i < len(rakenne) - 1 and j > 0 and rakenne[i+1][j-1] == 'x':
                luku += 1
            if i < len(rakenne) - 1 and j < len(rakenne[i]) - 1 and rakenne[i+1][j+1] == 'x':
                luku += 1
            
            teksti = str(luku)
            rakenne[i][j] = teksti

def tulvataytto(kentta, avatut, jaljella, aloitus_x, aloitus_y):
    """
    Merkitsee kentällä olevat numerolla 0 merkityt alueet avatuksi siten, että
    avaaminen aloitetaan annetusta x, y -pisteestä.
    
    :param list kentta: listarakenne, joka kuvastaa pelikenttää
    :param list avatut: listarakenne, joka kertoo mitkä pelikentän ruudut on avattu
    :param list jaljella: listarakenne, joka kertoo mitkä ruudut pelikentällä ovat vielä avaamattomia
    :param int aloitus_x: tulvatäytön aloituspisteen x-koordinaatti
    :param int aloitus_y: tulvatäytön aloituspisteen y-koordinaatti
    """
    
    tuntemattomat = [(aloitus_x, aloitus_y)]
    tutkitut = []
    while tuntemattomat:
        x, y = tuntemattomat.pop()
        if (x, y) in tutkitut:
            continue
        else:
            tutkitut.append((x, y))
            avatut[y][x] = "a"
            ruutu = (x, y)
            if ruutu in jaljella:
                jaljella.remove(ruutu)
            
            if y > 0 and kentta[y-1][x] != "x":
                if kentta[y-1][x] == "0":
                    tuntemattomat.insert(0, (x, y-1))
                else:
                    avatut[y-1][x] = "a"
                    ruutu = (x, y-1)
                    if ruutu in jaljella:
                        jaljella.remove(ruutu)
            if y < len(kentta) - 1 and kentta[y+1][x] != "x":
                if kentta[y+1][x] == "0":
                    tuntemattomat.insert(0, (x, y+1))
                else:
                    avatut[y+1][x] = "a"
                    ruutu = (x, y+1)
                    if ruutu in jaljella:
                        jaljella.remove(ruutu)
            if x > 0 and kentta[y][x-1] != "x":
                if kentta[y][x-1] == "0":
                    tuntemattomat.insert(0, (x-1, y))
                else:
                    avatut[y][x-1] = "a"
                    ruutu = (x-1, y)
                    if ruutu in jaljella:
                        jaljella.remove(ruutu)
            if x < len(kentta[y]) - 1 and kentta[y][x+1] != "x":
                if kentta[y][x+1] == "0":
                    tuntemattomat.insert(0, (x+1, y))
                else:
                    avatut[y][x+1] = "a"
                    ruutu = (x+1, y)
                    if ruutu in jaljella:
                        jaljella.remove(ruutu)
            if y > 0 and x > 0 and kentta[y-1][x-1] != "x":
                if kentta[y-1][x-1] == "0":
                    tuntemattomat.insert(0, (x-1, y-1))
                else:
                    avatut[y-1][x-1] = "a"
                    ruutu = (x-1, y-1)
                    if ruutu in jaljella:
                        jaljella.remove(ruutu)
            if y > 0 and x < len(kentta[y]) - 1 and kentta[y-1][x+1] != "x":
                if kentta[y-1][x+1] == "0":
                    tuntemattomat.insert(0, (x+1, y-1))
                else:
                    avatut[y-1][x+1] = "a"
                    ruutu = (x+1, y-1)
                    if ruutu in jaljella:
                        jaljella.remove(ruutu)
            if y < len(kentta) - 1 and x > 0 and kentta[y+1][x-1] != "x":
                if kentta[y+1][x-1] == "0":
                    tuntemattomat.insert(0, (x-1, y+1))
                else:
                    avatut[y+1][x-1] = "a"
                    ruutu = (x-1, y+1)
                    if ruutu in jaljella:
                        jaljella.remove(ruutu)
            if y < len(kentta) - 1 and x < len(kentta[y]) - 1 and kentta[y+1][x+1] != "x":
                if kentta[y+1][x+1] == "0":
                    tuntemattomat.insert(0, (x+1, y+1))
                else:
                    avatut[y+1][x+1] = "a"
                    ruutu = (x+1, y+1)
                    if ruutu in jaljella:
                        jaljella.remove(ruutu)
    
def piirra_kentta():
    """
    Käsittelijäfunktio, joka piirtää kaksiulotteisena listana kuvatun miinakentän
    ruudut näkyviin peli-ikkunaan. Funktiota kutsutaan aina kun pelimoottori pyytää
    ruudun näkymän päivitystä.
    """
    
    piirrettava = tila["kentta"]
    avatut = tila["avatut"]
    onko_loppu = tila["loppu"]
    haravasto.tyhjaa_ikkuna()
    haravasto.aloita_ruutujen_piirto()
    
    if not onko_loppu:
        for y in range(len(piirrettava)):
            for x in range(len(piirrettava[y])):
                if piirrettava[y][x] == "x" and avatut[y][x] == "a":
                    haravasto.lisaa_piirrettava_ruutu("x", x * 40, y * 40)
                elif piirrettava[y][x] == "1" and avatut[y][x] == "a":
                    haravasto.lisaa_piirrettava_ruutu("1", x * 40, y * 40)
                elif piirrettava[y][x] == "2" and avatut[y][x] == "a":
                    haravasto.lisaa_piirrettava_ruutu("2", x * 40, y * 40)
                elif piirrettava[y][x] == "3" and avatut[y][x] == "a":
                    haravasto.lisaa_piirrettava_ruutu("3", x * 40, y * 40)
                elif piirrettava[y][x] == "4" and avatut[y][x] == "a":
                    haravasto.lisaa_piirrettava_ruutu("4", x * 40, y * 40)
                elif piirrettava[y][x] == "5" and avatut[y][x] == "a":
                    haravasto.lisaa_piirrettava_ruutu("5", x * 40, y * 40)
                elif piirrettava[y][x] == "6" and avatut[y][x] == "a":
                    haravasto.lisaa_piirrettava_ruutu("6", x * 40, y * 40)
                elif piirrettava[y][x] == "7" and avatut[y][x] == "a":
                    haravasto.lisaa_piirrettava_ruutu("7", x * 40, y * 40)
                elif piirrettava[y][x] == "8" and avatut[y][x] == "a":
                    haravasto.lisaa_piirrettava_ruutu("8", x * 40, y * 40)
                elif piirrettava[y][x] == "0" and avatut[y][x] == "a":
                    haravasto.lisaa_piirrettava_ruutu("0", x * 40, y * 40)
                else:
                    haravasto.lisaa_piirrettava_ruutu(" ", x * 40, y * 40)
    else:
        for y in range(len(piirrettava)):
            for x in range(len(piirrettava[y])):
                if piirrettava[y][x] == "x":
                    haravasto.lisaa_piirrettava_ruutu("x", x * 40, y * 40)
                elif piirrettava[y][x] == "1":
                    haravasto.lisaa_piirrettava_ruutu("1", x * 40, y * 40)
                elif piirrettava[y][x] == "2":
                    haravasto.lisaa_piirrettava_ruutu("2", x * 40, y * 40)
                elif piirrettava[y][x] == "3":
                    haravasto.lisaa_piirrettava_ruutu("3", x * 40, y * 40)
                elif piirrettava[y][x] == "4":
                    haravasto.lisaa_piirrettava_ruutu("4", x * 40, y * 40)
                elif piirrettava[y][x] == "5":
                    haravasto.lisaa_piirrettava_ruutu("5", x * 40, y * 40)
                elif piirrettava[y][x] == "6":
                    haravasto.lisaa_piirrettava_ruutu("6", x * 40, y * 40)
                elif piirrettava[y][x] == "7":
                    haravasto.lisaa_piirrettava_ruutu("7", x * 40, y * 40)
                elif piirrettava[y][x] == "8":
                    haravasto.lisaa_piirrettava_ruutu("8", x * 40, y * 40)
                elif piirrettava[y][x] == "0":
                    haravasto.lisaa_piirrettava_ruutu("0", x * 40, y * 40)
                else:
                    haravasto.lisaa_piirrettava_ruutu(" ", x * 40, y * 40)
    
    haravasto.piirra_ruudut()
    
def hiiri_kasittelija(x, y, nappi, muokkausnappaimet):
    """
    Käsittelijäfunktio, jota kutsutaan aina kun käyttäjä klikkaa sovellusikkunaa hiirellä.
    
    :param int x: klikatun kohdan x-koordinaatti
    :param int y: klikatun kohdan y-koordinaatti
    :param nappi: hiiren painike, jolla kohtaa klikattiin
    :param muokkausnappaimet: muokkausnäppäimet joita painettiin klikkauksen aikana
    """
    
    onko_loppu = tila["loppu"]
    
    try:
        if not onko_loppu:
            if nappi == haravasto.HIIRI_VASEN:
                x_koor = int(x / 40)
                y_koor = int(y / 40)
                kentta = tila["kentta"]
                avatut = tila["avatut"]
                jaljella = tila["jaljella"]
                
                if kentta[y_koor][x_koor] == "x" and avatut[y_koor][x_koor] == " ":
                    tila["vuorot"] += 1
                    tila["loppu"] = True
                    lopetus(False)
                elif kentta[y_koor][x_koor] == "0" and avatut[y_koor][x_koor] == " ":
                    tila["vuorot"] += 1
                    tulvataytto(kentta, avatut, jaljella, x_koor, y_koor)
                elif avatut[y_koor][x_koor] == " ":
                    tila["vuorot"] += 1
                    avatut[y_koor][x_koor] = "a"
                    jaljella.remove((x_koor, y_koor))
                    
                if not jaljella:
                    tila["loppu"] = True
                    lopetus(True)
        else:
            if nappi == haravasto.HIIRI_VASEN:
                haravasto.lopeta()
    except IndexError:
        print("Klikattu kohta on pelikentän ulkopuolella!")
        
def lopetus(lopputulos):
    """
    Funktio, jota kutsutaan kun peli päättyy. Ilmoittaa pelaajalle pelin lopputuloksesta sekä luo tilaston kyseisestä pelistä tallennettavaksi.
    
    :param bool lopputulos: pelin lopputulos (arvo True vastaa voittoa, arvo False vastaa häviötä)
    """
    aloitus_aika = tila["aika"]
    lopetus_aika = datetime.datetime.now()
    minuutit = round((lopetus_aika - aloitus_aika).total_seconds() / 60)
    vuorot = tila["vuorot"]
    leveys = tila["leveys"]
    korkeus = tila["korkeus"]
    miinat = tila["miinat"]
    tilastot = tila["tilastot"]
    
    if lopputulos:
        print()
        print("Voitit pelin! Pelin kesto: {} minuuttia, {} vuoroa".format(minuutit, vuorot))
        print("Tallennetaan pelin tulos tilastoihin...\n")
        tilasto = {
            "ajankohta": aloitus_aika.strftime("%d.%m.%Y %H:%M:%S"),
            "minuutit": minuutit,
            "vuorot": vuorot,
            "tulos": "Voitto",
            "leveys": leveys,
            "korkeus": korkeus,
            "miinat": miinat
        }
        tilastot.append(tilasto)
        tallenna_tilastot(tilastot, "tilastot.txt")
    else:
        print()
        print("Hävisit pelin! Pelin kesto: {} minuuttia, {} vuoroa".format(minuutit, vuorot))
        print("Tallennetaan pelin tulos tilastoihin...\n")
        tilasto = {
            "ajankohta": aloitus_aika.strftime("%d.%m.%Y %H:%M:%S"),
            "minuutit": minuutit,
            "vuorot": vuorot,
            "tulos": "Häviö",
            "leveys": leveys,
            "korkeus": korkeus,
            "miinat": miinat
        }
        tilastot.append(tilasto)
        tallenna_tilastot(tilastot, "tilastot.txt")

def tallenna_tilastot(tilastot, tiedosto):
    """
    Tallentaa tilastot annettuun tiedostoon.
    
    :param list tilastot: lista, joka sisältää pelattujen pelien tilastot
    :param str tiedosto: tiedoston nimi, johon tilastot tallennetaan
    """
    try:
        with open(tiedosto, "w") as kohde:
            for tilasto in tilastot:
                kohde.write("{ajankohta}, {minuutit}, {vuorot}, {tulos}, {leveys}, {korkeus}, {miinat}\n".format(
                    ajankohta=tilasto["ajankohta"],
                    minuutit=tilasto["minuutit"],
                    vuorot=tilasto["vuorot"],
                    tulos=tilasto["tulos"],
                    leveys=tilasto["leveys"],
                    korkeus=tilasto["korkeus"],
                    miinat=tilasto["miinat"]
                ))
    except IOError:
        print("Kohdetiedostoa ei voitu avata. Tallennus epäonnistui")

def lataa_tilastot(tiedosto):
    """
    Lataa pelattujen pelien tilastot annetusta tiedostosta.
    
    :param str tiedosto: tiedoston nimi, josta tilastot ladataan
    """
    tilastot = []
    try:
        with open(tiedosto) as lahde:
            for rivi in lahde.readlines():
                lue_tilasto(rivi, tilastot)
    except IOError:
        print("Tilastoja ei löytynyt. Pelaa peli aloittaaksesi tilastojen luonnin.")
    
    return tilastot

def lue_tilasto(rivi, tilastot):
    """
    Lukee tilastot annetulta tiedoston riviltä ja tallentaa ne listaan.
    
    :param str rivi: tiedoston rivi, josta tilasto luetaan
    :param list tilastot: lista tilastoista, johon riviltä luettu tilasto lisätään
    """
    try:
        ajankohta, minuutit, vuorot, tulos, leveys, korkeus, miinat = rivi.split(",")
        tilasto = {
            "ajankohta": ajankohta.strip(),
            "minuutit": int(minuutit),
            "vuorot": int(vuorot),
            "tulos": tulos.strip(),
            "leveys": int(leveys),
            "korkeus": int(korkeus),
            "miinat": int(miinat)
        }
        tilastot.append(tilasto)
    except ValueError:
        print("Riviä ei saatu luettua: {}".format(rivi))

def tulosta_tilastot(tilastot):
    """
    Tulostaa pelattujen pelien tilastot.
    
    :param list tilastot: lista pelattujen pelien tilastoista
    """
    print()
    tulostus_lkm = math.ceil(len(tilastot) / 10)
    for i in range(tulostus_lkm):
        alku = i * 10
        loppu = (i + 1) * 10
        muotoile_sivu(tilastot[alku:loppu], i)
        if i < tulostus_lkm - 1:
            input("   -- paina enter jatkaaksesi tulostusta --")
    print()

def muotoile_sivu(rivit, sivu):
    """
    Muotoilee tulostettavan tilaston halutunlaisiksi.
    
    :param list rivit: lista riveistä jotka tulostetaan kyseiselle sivulle
    :param int sivu: sivu, jolle annetut rivit tulostetaan
    """
    for i, tilasto in enumerate(rivit, sivu * 10 + 1):
        print("{:2}. {ajankohta} - {minuutit} minuuttia, {vuorot} vuoroa, lopputulos: {tulos}, kentän koko: {leveys}x{korkeus}, miinoja: {miinat}".format(
            i,
            ajankohta=tilasto["ajankohta"],
            minuutit=tilasto["minuutit"],
            vuorot=tilasto["vuorot"],
            tulos=tilasto["tulos"],
            leveys=tilasto["leveys"],
            korkeus=tilasto["korkeus"],
            miinat=tilasto["miinat"]
        ))

def kysy_luku(kysymys):
    """
    Kysyy käyttäjältä kokonaisluvun ja varmistaa, että syöte on haluttua muotoa
    
    :param str kysymys: kysymys, joka käyttäjältä kysytään syötteen yhteydessä
    """
    while True:
        try:
            luku = int(input(kysymys))
        except ValueError:
            print("Syötteen täytyy olla kokonaisluku!")
        else:
            break
    return luku

def main():
    """
    Lataa pelin grafiikat, luo peli-ikkunan ja asettaa siihen käsittelijäfunktiot. Tallentaa myös pelin aloitusajan.
    """
    
    haravasto.lataa_kuvat("spritet")
    haravasto.luo_ikkuna(len(tila["kentta"][0]) * 40, len(tila["kentta"]) * 40)
    haravasto.aseta_piirto_kasittelija(piirra_kentta)
    haravasto.aseta_hiiri_kasittelija(hiiri_kasittelija)
    tila["aika"] = datetime.datetime.now()
    haravasto.aloita()

if __name__ == "__main__":
    while True:
        kentta = []
        jaljella = []
        avatut = []
        tila["loppu"] = False
        tila["vuorot"] = 0
        
        print("Tervetuloa Miinaharava-peliin!\n")
        tilastot = lataa_tilastot("tilastot.txt")
        if tilastot:
            tila["tilastot"] = tilastot
        print("Vaihtoehdot:")
        print("(A)loita uusi peli")
        print("(T)utki tilastoja")
        print("(L)opeta peli")
        valinta = input("Valintasi: ").strip().lower()
        
        if valinta == 'a':
            leveys = kysy_luku("Anna pelikentän leveys: ")
            korkeus = kysy_luku("Anna pelikentän korkeus: ")
            miinat = kysy_luku("Anna asetettavien miinojen lukumäärä: ")
            
            
            if miinat > leveys * korkeus:
                print("Miinojen lukumäärä ei voi olla suurempi kuin pelikentän koko!")
            else:
                for rivi in range(korkeus):
                    kentta.append([])
                    for sarake in range(leveys):
                        kentta[-1].append(" ")
                tila["kentta"] = kentta
                
                for rivi in range(korkeus):
                    avatut.append([])
                    for sarake in range(leveys):
                        avatut[-1].append(" ")
                tila["avatut"] = avatut
                
                for x in range(leveys):
                    for y in range(korkeus):
                        jaljella.append((x, y))
                tila["jaljella"] = jaljella
                
                tila["leveys"] = leveys
                tila["korkeus"] = korkeus
                tila["miinat"] = miinat
                
                miinoita(tila["kentta"], tila["jaljella"], tila["miinat"])
                laske_miinat(tila["kentta"])
                main()
        elif valinta == 't':
            if tilastot:
                tulosta_tilastot(tilastot)
            else:
                print("Tilastoja ei löytynyt. Pelaa peli aloittaksesi tilastojen luonnin.\n")
        elif valinta == 'l':
            break
        else:
            print("Virheellinen vaihtoehto!")