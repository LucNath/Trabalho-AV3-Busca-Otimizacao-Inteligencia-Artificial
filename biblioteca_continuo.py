import numpy as np

# =========================================================
# FUNÇÕES OBJETIVO (f1 a f6)
# =========================================================

def f1(x): 
    return x[0]**2 + x[1]**2

def f2(x):
    term1 = np.exp(-(x[0]**2 + x[1]**2))
    term2 = 2 * np.exp(-((x[0]-1.7)**2 + (x[1]-1.7)**2))
    return term1 + term2

def f3(x):
    term1 = -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x[0]**2 + x[1]**2)))
    term2 = -np.exp(0.5 * (np.cos(2*np.pi*x[0]) + np.cos(2*np.pi*x[1])))
    return term1 + term2 + 20 + np.e

def f4(x):
    term1 = x[0]**2 - 10 * np.cos(2*np.pi*x[0]) + 10
    term2 = x[1]**2 - 10 * np.cos(2*np.pi*x[1]) + 10
    return term1 + term2

def f5(x):
    term1 = (x[0] * np.cos(x[0])) / 20.0
    term2 = 2 * np.exp(-(x[0]**2 + (x[1]-1)**2))
    term3 = 0.01 * x[0] * x[1]
    return term1 + term2 + term3

def f6(x):
    return x[0] * np.sin(4*np.pi*x[0]) - x[1] * np.sin(4*np.pi*x[1] + np.pi) + 1

PROBLEMAS = {
    "f1": {"func": f1, "bounds": [(-100, 100), (-100, 100)], "tipo": "min"},
    "f2": {"func": f2, "bounds": [(-2, 4), (-2, 5)], "tipo": "max"},
    "f3": {"func": f3, "bounds": [(-8, 8), (-8, 8)], "tipo": "min"},
    "f4": {"func": f4, "bounds": [(-5.12, 5.12), (-5.12, 5.12)], "tipo": "min"},
    "f5": {"func": f5, "bounds": [(-10, 10), (-10, 10)], "tipo": "max"},
    "f6": {"func": f6, "bounds": [(-1, 3), (-1, 3)], "tipo": "max"},
}

# =========================================================
# ALGORITMOS DE BUSCA
# =========================================================

def verifica_limites(x, bounds):
    x_clippado = []
    for i in range(len(x)):
        x_clippado.append(np.clip(x[i], bounds[i][0], bounds[i][1]))
    return np.array(x_clippado)

def melhor_que(cand, atual, tipo):
    return cand < atual if tipo == "min" else cand > atual

# Hill Climbing
def hill_climbing(func, bounds, tipo, max_iter=1000, eps=0.1):
    # Início no limite inferior (Requisito PDF Pag 2) [cite: 37]
    x_atual = np.array([bounds[0][0], bounds[1][0]]) 
    val_atual = func(x_atual)
    sem_melhora = 0
    
    for _ in range(max_iter):
        vizinho = x_atual + np.random.uniform(-eps, eps, size=2)
        vizinho = verifica_limites(vizinho, bounds)
        val_vizinho = func(vizinho)

        if melhor_que(val_vizinho, val_atual, tipo):
            x_atual = vizinho
            val_atual = val_vizinho
            sem_melhora = 0
        else:
            sem_melhora += 1
        if sem_melhora >= 50: break # Parada antecipada [cite: 43]
    return x_atual, val_atual

# Local Random Search (LRS)
def local_random_search(func, bounds, tipo, max_iter=1000, sigma=0.5):
    # Início aleatório
    x_atual = np.array([np.random.uniform(b[0], b[1]) for b in bounds])
    val_atual = func(x_atual)
    sem_melhora = 0

    for _ in range(max_iter):
        # Perturbação gaussiana (Normal) [cite: 40]
        vizinho = x_atual + np.random.normal(0, sigma, size=2)
        vizinho = verifica_limites(vizinho, bounds)
        val_vizinho = func(vizinho)

        if melhor_que(val_vizinho, val_atual, tipo):
            x_atual = vizinho
            val_atual = val_vizinho
            sem_melhora = 0
        else:
            sem_melhora += 1
        if sem_melhora >= 50: break
    return x_atual, val_atual

# Global Random Search (GRS)
def global_random_search(func, bounds, tipo, max_iter=1000):
    x_atual = np.array([np.random.uniform(b[0], b[1]) for b in bounds])
    val_atual = func(x_atual)
    sem_melhora = 0

    for _ in range(max_iter):
        # Novo candidato totalmente aleatório [cite: 41]
        cand = np.array([np.random.uniform(b[0], b[1]) for b in bounds])
        val_cand = func(cand)

        if melhor_que(val_cand, val_atual, tipo):
            x_atual = cand
            val_atual = val_cand
            sem_melhora = 0
        else:
            sem_melhora += 1
        if sem_melhora >= 50: break
    return x_atual, val_atual

# =========================================================
# FUNÇÃO PRINCIPAL DA PARTE 1
# =========================================================

def resolver_parte_1():
    print("\n=== PARTE 1: FUNÇÕES CONTÍNUAS (100 RODADAS) ===")
    R = 100 # Quantidade de rodadas exigida 
    
    print(f"{'Função':<6} | {'Algoritmo':<5} | {'Melhor Global':<15} | {'Média Final':<15}")
    print("-" * 55)

    for nome, dados in PROBLEMAS.items():
        func = dados["func"]
        bounds = dados["bounds"]
        tipo = dados["tipo"]
        
        # Ajuste dinâmico de parâmetros (Heurística)
        tam_dominio = bounds[0][1] - bounds[0][0]
        eps = tam_dominio * 0.05
        sigma = tam_dominio * 0.1

        resultados = {"HC": [], "LRS": [], "GRS": []}
        
        # Executa R vezes
        for _ in range(R):
            resultados["HC"].append(hill_climbing(func, bounds, tipo, eps=eps)[1])
            resultados["LRS"].append(local_random_search(func, bounds, tipo, sigma=sigma)[1])
            resultados["GRS"].append(global_random_search(func, bounds, tipo)[1])

        for alg, vals in resultados.items():
            melhor = min(vals) if tipo == "min" else max(vals)
            media = np.mean(vals)
            print(f"{nome:<6} | {alg:<5} | {melhor:.4e}     | {media:.4e}")