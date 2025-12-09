import biblioteca_continuo
import biblioteca_discreto
import numpy as np

def main():
    print(">>> INICIANDO TRABALHO COMPLETO <<<\n")
    
    # --- 1. Executa Funções Contínuas (f1-f6) com 100 rodadas ---
    # Isso satisfaz os requisitos 
    biblioteca_continuo.resolver_parte_1()
    
    print("\n" + "="*60)
    
    # --- 2. Executa Rainhas (Até achar 92 soluções) ---
    # Isso satisfaz os requisitos 
    biblioteca_discreto.resolver_rainhas()
    
    print("\n" + "="*60)
    
    # --- 3. Executa Caixeiro Viajante (TSP) ---
    # Isso satisfaz os requisitos [cite: 231, 243]
    # Certifique-se que o arquivo 'CaixeiroGruposGA (1).csv' está na pasta
    biblioteca_discreto.resolver_tsp('trabalho busca otimizada/av3_ia/CaixeiroGruposGA.csv')

    print("\n>>> EXECUÇÃO FINALIZADA <<<")

if __name__ == "__main__":
    main()