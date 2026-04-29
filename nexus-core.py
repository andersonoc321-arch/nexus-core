import time
import os

def main():
    print("------------------------------------------")
    print("   NEXUS OMNI-CORE V10.4 - ONLINE         ")
    print("   STATUS: CONECTADO AO TERMUX            ")
    print("------------------------------------------")
    
    ciclo = 0
    while True:
        ciclo += 1
        print(f"[LOG] Ciclo de Evolução {ciclo} ativo...")
        # Aqui o Nexus gravará os novos conhecimentos
        with open("status.txt", "w") as f:
            f.write(f"NEXUS V10.4 Ativo. Ultimo Ciclo: {ciclo}")
        
        time.sleep(60) # Pulsa a cada 1 minuto

if __name__ == "__main__":
    main()
