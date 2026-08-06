# Portinel: Gelişmiş Ağ Tarayıcı ve Log Yöneticisi

Portinel, siber güvenlik uzmanları ve savunma (Blue Team) analistleri için tasarlanmış, çoklu iş parçacığı (multi-threading) destekli bir port tarama ve servis keşif (banner grabbing) aracıdır. 

Araç, makine öğrenmesi tabanlı saldırı tespit sistemleri (IDS) için ağın normal durum (baseline) haritasını çıkarmak amacıyla tarama sonuçlarını doğrudan yapısal bir ilişkisel veri tabanına (MySQL/MariaDB) entegre eder.

## 🚀 Özellikler

*   **Yüksek Hız:** `concurrent.futures` kütüphanesi ile eşzamanlı (multi-threaded) tarama yeteneği.
*   **Servis Keşfi (Banner Grabbing):** Sadece portların durumunu değil, arkada koşan servisin başlık bilgisini (banner) de yakalar.
*   **İzole Raporlama:** Taramaları bağımsız olarak JSON formatında dışa aktarma.
*   **Veri Tabanı Otomasyonu:** JSON loglarını okuyup, gerekli tabloları otomatik oluşturarak MySQL'e "Batch Insert" yöntemiyle yazar.

## 🛠️ Kurulum

Sistem gereksinimlerini kurmak için:

```bash
# Gerekli kütüphaneyi kurun
pip install mysql-connector-python
