import socket
import argparse
import concurrent.futures
import json
from datetime import datetime

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1.0)
            result = s.connect_ex((ip, port))
            
            if result == 0:
                banner = "Servis bilgisi alınamadı"
                try:
                    s.sendall(b"HELLO\r\n")
                    banner = s.recv(1024).decode('utf-8', errors='ignore').strip()
                except socket.timeout:
                    pass
                except Exception:
                    pass
                
                print(f"[+] Port {port} AÇIK | Servis: {banner[:50]}")
                return {"port": port, "status": "open", "banner": banner}
    except Exception:
        pass
    return None

def main():
    parser = argparse.ArgumentParser(description="Gelişmiş Ağ Port Tarayıcı ve Servis Keşfedici")
    parser.add_argument("-t", "--target", help="Hedef IP adresi", required=True)
    parser.add_argument("-s", "--start", type=int, default=1, help="Başlangıç Portu (Varsayılan: 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="Bitiş Portu (Varsayılan: 1024)")
    parser.add_argument("-o", "--output", help="Sonuçları JSON olarak kaydet", default="scan_results.json")
    
    args = parser.parse_args()
    
    print(f"[*] {args.target} üzerinde tarama başlatılıyor... ({args.start}-{args.end})")
    start_time = datetime.now()
    
    open_ports = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(scan_port, args.target, port): port for port in range(args.start, args.end + 1)}
        
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(result)
                
    end_time = datetime.now()
    print(f"\n[*] Tarama tamamlandı. Geçen süre: {end_time - start_time}")
    
    if open_ports:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump({"target": args.target, "scan_time": str(start_time), "results": open_ports}, f, indent=4)
        print(f"[*] Sonuçlar '{args.output}' dosyasına kaydedildi.")
    else:
        print("[-] Açık port bulunamadı.")

if __name__ == "__main__":
    main()
