import json
import mysql.connector
from mysql.connector import Error

# KULLANIM: Kodu çalıştırmadan önce kendi veri tabanı bilgilerinizi giriniz.
DB_CONFIG = {
    'host': 'localhost',
    'user': 'KULLANICI_ADINIZ_BURAYA',
    'password': 'SIFRENIZ_BURAYA',
    'database': 'security_logs'
}

def create_database_and_table(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS security_logs")
    cursor.execute("USE security_logs")
    
    table_query = """
    CREATE TABLE IF NOT EXISTS port_scans (
        id INT AUTO_INCREMENT PRIMARY KEY,
        target_ip VARCHAR(50) NOT NULL,
        scan_time DATETIME NOT NULL,
        port INT NOT NULL,
        status VARCHAR(20) NOT NULL,
        banner TEXT
    )
    """
    cursor.execute(table_query)

def load_json_to_db(json_file_path):
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
        target_ip = data.get("target")
        scan_time = data.get("scan_time")
        results = data.get("results", [])

        if not results:
            print("[-] JSON dosyasında kaydedilecek açık port bulunamadı.")
            return

        conn = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        cursor = conn.cursor()

        create_database_and_table(cursor)

        insert_query = """
        INSERT INTO port_scans (target_ip, scan_time, port, status, banner)
        VALUES (%s, %s, %s, %s, %s)
        """
        
        records_to_insert = []
        for item in results:
            records_to_insert.append((
                target_ip,
                scan_time,
                item["port"],
                item["status"],
                item["banner"]
            ))
            
        cursor.executemany(insert_query, records_to_insert)
        conn.commit()
        
        print(f"[+] Başarılı! {cursor.rowcount} adet açık port kaydı veri tabanına işlendi.")

    except Error as e:
        print(f"[-] Veri tabanı hatası: {e}")
    except FileNotFoundError:
        print(f"[-] Hata: '{json_file_path}' dosyası bulunamadı.")
    except Exception as e:
        print(f"[-] Beklenmeyen bir hata oluştu: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    load_json_to_db("scan_results.json")
