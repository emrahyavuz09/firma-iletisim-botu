# 🏢 Firma İletişim Bilgileri Toplayıcı (Selenium Bot)

Bu proje, bir listedeki firmaların web sitelerini otomatik olarak ziyaret eden, iletişim sayfalarına giden ve buradaki **telefon numarası** ile **e-posta** adreslerini ayıklayıp Excel'e kaydeden bir Python botudur.

## 🚀 Özellikler
* **Tarayıcı Otomasyonu:** Selenium kullanarak gerçek bir kullanıcı gibi Chrome üzerinden işlem yapar.
* **Akıllı Navigasyon:** Web sitesine girdiğinde otomatik olarak "İletişim", "Contact" veya "Bize Ulaşın" sayfalarını bulur.
* **Regex Desteği:** Karmaşık metinler içinden Türkiye formatındaki telefonları ve kurumsal e-postaları ayıklar.
* **Excel Çıktısı:** Toplanan verileri temiz bir tablo halinde Masaüstüne kaydeder.

## 🛠 Kurulum
Projeyi çalıştırmak için bilgisayarınızda Python yüklü olmalıdır. Ardından gerekli kütüphaneleri yükleyin:

```bash
pip install selenium webdriver-manager pandas openpyxl



🚀 Kullanım Talimatları

Kodun kendi listenizle çalışması için şu adımları izleyin:

Dosyayı Düzenleyin: firma_bulucu.py dosyasını bir metin düzenleyici (VS Code, TextEdit vb.) ile açın.

Listeyi Güncelleyin: Kodun içindeki --- FİRMA LİSTESİ --- bölümünü bulun. Buradaki tırnak işaretleri arasına kendi firma isimlerinizi ekleyin veya mevcut olanları düzenleyin.

Çalıştırın: Terminali açın, dosyanın bulunduğu klasöre gidin ve şu komutu yazarak botu başlatın:

Bash
python3 firma_bulucu.py
Sonuç: İşlem bittiğinde masaüstünüzde verilerin bulunduğu bir Excel dosyası oluşacaktır.

