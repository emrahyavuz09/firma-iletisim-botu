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


💻 Nasıl Çalışır?
firma_bulucu.py dosyasını çalıştırın.

Bot, Yandex üzerinden firma isimlerini aratır.

Bulduğu ilk resmi web sitesine giriş yapar.

Sitenin iletişim bölümüne giderek bilgileri kopyalar.

İşlem bittiğinde Firma_Site_Detayli.xlsx dosyası oluşturulur.
