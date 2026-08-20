# Portinel: Advanced Network Scanner & Log Manager

*Read this in [Turkish](#türkçe)*

Portinel is a multi-threaded port scanning and service discovery (banner grabbing) tool designed for cybersecurity professionals and Blue Team analysts. 
The tool integrates scan results directly into a structured relational database (MySQL/MariaDB) to map the network's baseline for machine learning-based Intrusion Detection Systems (IDS).

## 🚀 Features

* **High Speed:** Concurrent scanning capabilities utilizing the `concurrent.futures` library.
* **Banner Grabbing:** Captures not only the port status but also the service header information running in the background.
* **Isolated Reporting:** Exports scans independently in JSON format.
* **Database Automation:** Reads JSON logs, automatically creates necessary tables, and writes to the database using the "Batch Insert" method.

## 🛠️ Installation

To install the system requirements:

```bash
pip install mysql-connector-python
```

## 💻 Usage

**1. Scanning the Network and Saving as JSON:**
Use the `prt_scan.py` file to scan ports on a specific IP address.

```bash
python prt_scan.py -t 192.168.1.1 -s 1 -e 1024 -o scan_results.json
```

**2. Logging Results to the Database:**
Update the database credentials (username, password, etc.) in the `db_logger.py` file according to your environment. Then, run the script to import the JSON data into MySQL/MariaDB.

```bash
python db_logger.py
```

---

# Türkçe

Portinel, siber güvenlik uzmanları ve savunma (Blue Team) analistleri için tasarlanmış, çoklu iş parçacığı (multi-threading) destekli bir port tarama ve servis keşif (banner grabbing) aracıdır. 
Araç, makine öğrenmesi tabanlı saldırı tespit sistemleri (IDS) için ağın normal durum (baseline) haritasını çıkarmak amacıyla tarama sonuçlarını doğrudan yapısal bir ilişkisel veri tabanına (MySQL/MariaDB) entegre eder.

## 🚀 Özellikler

* **Yüksek Hız:** `concurrent.futures` kütüphanesi ile eşzamanlı (multi-threaded) tarama yeteneği.
* **Servis Keşfi (Banner Grabbing):** Sadece portların durumunu değil, arkada koşan servisin başlık bilgisini (banner) de yakalar.
* **İzole Raporlama:** Taramaları bağımsız olarak JSON formatında dışa aktarma.
* **Veri Tabanı Otomasyonu:** JSON loglarını okuyup, gerekli tabloları otomatik oluşturarak veri tabanına "Batch Insert" yöntemiyle yazar.

## 🛠️ Kurulum

Sistem gereksinimlerini kurmak için:

```bash
pip install mysql-connector-python
```

## 💻 Kullanım

**1. Ağı Tarama ve JSON Olarak Kaydetme:**
Belirli bir IP adresindeki portları taramak için `prt_scan.py` dosyasını kullanın.

```bash
python prt_scan.py -t 192.168.1.1 -s 1 -e 1024 -o scan_results.json
```

**2. Sonuçları Veri Tabanına Yazma:**
`db_logger.py` dosyasındaki veri tabanı bilgilerinizi (kullanıcı adı, şifre vb.) kendi ortamınıza göre güncelleyin. Ardından scripti çalıştırarak JSON verilerini MySQL/MariaDB'ye aktarın.

```bash
python db_logger.py
```
