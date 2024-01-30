import requests
from bs4 import BeautifulSoup
import pandas as pd

def veri_topla_ve_kaydet(url, dosya_adı):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    urunler = []

    # Sitenin HTML yapısına göre gerekli etiketleri belirleyin
    for urun_etiketi in soup.find_all('div', class_='urun-etiketi'):
        try:
            aa = urun_etiketi.find('h1').text.strip()
        except AttributeError:
            aa = ""

        try:
            bb = urun_etiketi.find('h2').text.strip()
        except AttributeError:
            bb = ""

        try:
            cc = urun_etiketi.find('p').text.strip()
        except AttributeError:
            cc = ""

        try:
            dd = urun_etiketi.find('p1').text.strip()
        except AttributeError:
            dd = ""

        try:
            aciklama = urun_etiketi.find('p2').text.strip()
        except AttributeError:
            aciklama = ""

        print(aa, bb, cc, dd, aciklama)

        urunler.append({'UrunAdi': aa, 'UrunKodu': bb, 'Fiyat': cc, 'StokDurumu': dd, 'Aciklama': aciklama})

    df = pd.DataFrame(urunler)
    df.to_csv(dosya_adı, index=False)
    print(f"Veriler {dosya_adı} adlı dosyaya kaydedildi.")

if __name__ == "__main__":
    siteler = [
        "https://www.ozdisan.com/",
            "https://www.megasan.com/"
            "http://www.gamateknik.com/",
            "http://www.testone.com.tr/",
            "http://www.tdsmuhendislik.com/",
            "http://www.tekniktest.com/"
            "http://www.brotechelectronics.com/"
            "https://www.olcualetlerisepeti.com/"
            "https://www.kartalotomasyon.com.tr/"
            "https://partnerelectronic.com/"
            "https://www.kamitekno.com/"
            "https://unitekelektrik.com/"
            "http://www.elektronikekipman.com/"
            "https://www.elektronomi.com/"
            "http://www.antistatikmarket.com/"
            "http://www.hatfon.com/"
            "http://eginelektronik.com/"
            "https://www.entegreci.com/"
            "http://www.dorukanstore.com/"
            "https://www.direnc.net/"
            "http://www.robitshop.com/"
            "https://www.robotistan.com/"
            "https://www.bluemavi.com/"
            "https://www.marketdijital.com/"
            "https://www.robotsepeti.com/"
            "https://www.hobidevre.com/"
            "https://www.f1depo.com/"
            "https://www.e-komponent.com/"
            "https://karakoyelektronik.com/"
            "https://www.motorobit.com/"
            "https://www.robolinkmarket.com/"
            "https://www.prosmt-market.com/"
            "https://www.ersinelektronik.com/"
            "https://shop.nifbilisim.com/"
            "https://www.elektrovadi.com/"
            "https://www.robo90.com/"
            "https://www.modulelektronik.com/"
            "https://www.guneselektronik.com.tr/"
            "http://www.ersasatis.com/"
            "https://www.assemshop.com/"
            "https://www.c3teknolojimarket.com/"
            "https://zengerelektronik.com.tr/"
            "https://www.onemobileteknik.com"
            "https://www.avrasya1453.com"
            "https://www.ertelgsm.com/"
            "https://kizilelmateknik.com/"
            "https://el-kom.com.tr/"
            "http://ekatrafo.com/"
            "https://www.temametal.com.tr/"
            "https://www.ferritnuve.com/"
            "https://cagtrafo.com/"
            "https://www.demsay.com/tr/"
            "http://www.ekom-ltd.com/"
            "https://www.odesan.com/"
            "https://www.elektrikmarket.com.tr/"
            "https://iletimelektrik.com.tr/"
            "https://www.aksamotorfan.com"
            "https://www.bilgisayartoptancisi.com/"
            "https://www.altinkaya.com.tr/"
            "https://www.etkenelektronik.com.tr/"
            "http://www.emkatr.com/"
            "https://www.ttaf.com.tr/"
            "https://www.megaradar.com.tr/"
            "https://www.saralelektrik.com/"
            "https://bhmelektroniksatis.com/"
            "https://www.proteldepo.com/"
            "https://www.interkom.co/"
            "https://openzeka.com/"
            "https://www.empastore.com/"
            "https://deneyapkart.org/"
            "https://market.samm.com/"   
            "https://www.emayteknik.com"
            "https://www.ertelgsm.com"  
    ]

    for site in siteler:
        dosya_adi = f"{site.split('//')[1].split('.')[0]}_verileri.csv"
        veri_topla_ve_kaydet(site, dosya_adi)
