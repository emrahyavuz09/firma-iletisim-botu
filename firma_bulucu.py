import re
import time
import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# --- AYIKLAMA DESENLERİ ---
EMAIL_RE = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
PHONE_RE = r'(?:\+90|0)[ ]?[\(]?[2-8][0-9]{2}[\)]?[ ]?[0-9]{3}[ ]?[0-9]{2}[ ]?[0-9]{2}|444[ ]?[0-9]{3}[ ]?[0-9]?'

def tarayiciyi_hazirla():
    chrome_options = Options()
    # Pencereyi görmek için headless mod kapalı
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # macOS için bazen gerekli olan kullanıcı kimliği
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def bilgileri_ayikla(metin):
    mailler = list(set(re.findall(EMAIL_RE, metin)))
    mailler = [m for m in mailler if not m.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    teller = list(set(re.findall(PHONE_RE, metin)))
    return ", ".join(mailler), ", ".join(teller)

def yandex_tara(firmalar):
    driver = tarayiciyi_hazirla()
    sonuclar = []

    print(f"🚀 {len(firmalar)} firma için Yandex otomasyonu başlıyor...")

    for firma in firmalar:
        print(f"🔎 Yandex'de Aranan: {firma}")
        try:
            # Yandex Türkiye'ye git
            driver.get("https://www.yandex.com.tr")
            time.sleep(2)
            
            # Yandex arama kutusunun adı genellikle 'text'tir
            search_box = driver.find_element(By.NAME, "text")
            search_box.clear()
            search_box.send_keys(f"{firma} iletişim telefon eposta")
            search_box.send_keys(Keys.RETURN)
            
            # Sonuçların yüklenmesi için bekle
            time.sleep(4) 
            
            # Sayfadaki tüm görünür metni al
            sayfa_metni = driver.find_element(By.TAG_NAME, "body").text
            mail, tel = bilgileri_ayikla(sayfa_metni)
            
            sonuclar.append({
                "Firma Adı": firma,
                "Telefon": tel if tel else "Bulunamadı",
                "E-posta": mail if mail else "Bulunamadı",
                "Yandex Linki": driver.current_url
            })
            
            print(f"   ✅ Bitti: {tel if tel else 'Bilgi yok'}")
            
        except Exception as e:
            print(f"⚠️ {firma} taranırken bir sorun oluştu.")
            sonuclar.append({"Firma Adı": firma, "Telefon": "Hata", "E-posta": "Hata"})
        
        # Yandex'in bizi engellememesi için her aramada kısa bir mola
        time.sleep(3)

    driver.quit()
    return sonuclar

# --- FİRMA LİSTESİ ---
liste = [
    "Firma yaz", "Firma Yaz 2",
    "Firma Yaz 3", "Firma Yaz 4 bu şekilde çoğaltabilirsiniz.",
    
]

# --- ÇALIŞTIR ---
veriler = yandex_tara(liste)

# Excel'e aktar
df = pd.DataFrame(veriler)
desktop = os.path.expanduser("~/Desktop/Firma_Yandex_Sonuc.xlsx")
df.to_excel(desktop, index=False)

print(f"\n✅ İŞLEM TAMAMLANDI! Dosya Masaüstünde: {desktop}")