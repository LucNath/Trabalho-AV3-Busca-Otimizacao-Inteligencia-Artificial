import numpy as np
import matplotlib.pyplot as plt
import random
import math
import time

# =========================================================
# PARTE 2.1: 8 RAINHAS (SIMULATED ANNEALING)
# =========================================================

class RainhasSA:
    def __init__(self, temp_inicial=10.0, alpha=0.95, max_iter=2000):
        self.temp_inicial = temp_inicial
        self.alpha = alpha
        self.max_iter = max_iter

    def fitness(self, tabuleiro):
        # Maximizar: 28 - conflitos [cite: 162]
        n = len(tabuleiro)
        conflitos = 0
        for i in range(n):
            for j in range(i + 1, n):
                if tabuleiro[i] == tabuleiro[j]:
                    conflitos += 1
                elif abs(tabuleiro[i] - tabuleiro[j]) == abs(i - j):
                    conflitos += 1
        return 28 - conflitos

    def gerar_vizinho(self, tabuleiro):
        novo = list(tabuleiro)
        col = random.randint(0, 7)
        linha_atual = novo[col]
        nova_linha = random.randint(0, 7)
        while nova_linha == linha_atual:
            nova_linha = random.randint(0, 7)
        novo[col] = nova_linha
        return novo

    def run(self):
        atual = [random.randint(0, 7) for _ in range(8)]
        atual_fit = self.fitness(atual)
        melhor = list(atual)
        melhor_fit = atual_fit
        temp = self.temp_inicial
        
        for _ in range(self.max_iter):
            if melhor_fit == 28: return melhor, melhor_fit

            vizinho = self.gerar_vizinho(atual)
            vizinho_fit = self.fitness(vizinho)
            delta = vizinho_fit - atual_fit
            
            aceitar = False
            if delta > 0:
                aceitar = True
            else:
                try: prob = math.exp(delta / temp)
                except OverflowError: prob = 0
                if random.random() < prob: aceitar = True
            
            if aceitar:
                atual = vizinho
                atual_fit = vizinho_fit
                if atual_fit > melhor_fit:
                    melhor = list(atual)
                    melhor_fit = atual_fit
            
            temp *= self.alpha # Decaimento [cite: 184]
            if temp < 0.001: temp = 0.001
            
        return melhor, melhor_fit

def resolver_rainhas():
    print("\n=== PARTE 2.1: 8 RAINHAS (ENCONTRAR 92 SOLUÇÕES) ===")
    solucoes_unicas = set()
    tentativas = 0
    inicio = time.time()
    
    # Loop até encontrar as 92 soluções distintas [cite: 187]
    while len(solucoes_unicas) < 92:
        tentativas += 1
        sa = RainhasSA()
        sol, fit = sa.run()
        
        if fit == 28:
            sol_tuple = tuple(sol)
            if sol_tuple not in solucoes_unicas:
                solucoes_unicas.add(sol_tuple)
                if len(solucoes_unicas) % 10 == 0:
                    print(f"Encontradas: {len(solucoes_unicas)}/92...")
    
    print(f"Sucesso! 92 soluções encontradas em {tentativas} tentativas.")

# =========================================================
# PARTE 2.2: CAIXEIRO VIAJANTE (GENETIC ALGORITHM)
# =========================================================

class GeneticAlgorithmTSP:
    def __init__(self, coordenadas, pop_size=100, max_gen=500, prob_mut=0.01):
        self.coords = coordenadas
        self.num_cidades = len(coordenadas)
        self.pop_size = pop_size
        self.max_gen = max_gen
        self.prob_mut = prob_mut
        
        # Pré-cálculo da matriz de distâncias
        self.dist_matrix = np.zeros((self.num_cidades, self.num_cidades))
        for i in range(self.num_cidades):
            self.dist_matrix[i] = np.linalg.norm(self.coords - self.coords[i], axis=1)

        # População inicial aleatória [cite: 214]
        self.populacao = np.array([np.random.permutation(self.num_cidades) for _ in range(pop_size)])

    def fitness(self, rota):
        # Custo total da rota
        d = 0
        for i in range(self.num_cidades - 1):
            d += self.dist_matrix[rota[i], rota[i+1]]
        d += self.dist_matrix[rota[-1], rota[0]] # Retorno à origem
        return d, 1.0 / (d + 1e-6)

    def selection(self, fitness_vals):
        # Método do Torneio [cite: 234]
        pais = []
        for _ in range(self.pop_size):
            indices = np.random.randint(0, self.pop_size, 3)
            best_idx = indices[np.argmax(fitness_vals[indices])]
            pais.append(self.populacao[best_idx])
        return np.array(pais)

    def crossover_ordered(self, p1, p2):
        # Recombinação de dois pontos/ordem [cite: 236]
        size = self.num_cidades
        start, end = sorted(random.sample(range(size), 2))
        
        filho = -1 * np.ones(size, dtype=int)
        filho[start:end] = p1[start:end]
        
        pos = end
        if pos >= size: pos = 0
        for gene in np.roll(p2, -end):
            if gene not in filho:
                filho[pos] = gene
                pos += 1
                if pos >= size: pos = 0
        return filho

    def mutation(self, individuo):
        # Troca de genes (Swap) [cite: 241]
        if random.random() < self.prob_mut:
            i, j = random.sample(range(self.num_cidades), 2)
            individuo[i], individuo[j] = individuo[j], individuo[i]
        return individuo

    def run(self):
        melhor_rota = None
        melhor_dist = float('inf')
        
        for g in range(self.max_gen):
            fitness_vals = []
            dists = []
            for ind in self.populacao:
                d, f = self.fitness(ind)
                dists.append(d)
                fitness_vals.append(f)
            
            fitness_vals = np.array(fitness_vals)
            
            idx_best = np.argmin(dists)
            if dists[idx_best] < melhor_dist:
                melhor_dist = dists[idx_best]
                melhor_rota = self.populacao[idx_best].copy()
            
            # Evolução
            pais = self.selection(fitness_vals)
            nova_pop = []
            for i in range(0, self.pop_size, 2):
                p1, p2 = pais[i], pais[i+1] if i+1 < self.pop_size else pais[0]
                f1 = self.crossover_ordered(p1, p2)
                f2 = self.crossover_ordered(p2, p1)
                nova_pop.append(self.mutation(f1))
                nova_pop.append(self.mutation(f2))
            self.populacao = np.array(nova_pop)
            
        return melhor_rota, melhor_dist

def plotar_rota_3d(coords, rota, dist):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    
    idx_rota = np.append(rota, rota[0])
    x, y, z = coords[idx_rota, 0], coords[idx_rota, 1], coords[idx_rota, 2]
    
    ax.plot(x, y, z, '-o', color='b', alpha=0.6)
    ax.scatter(x[0], y[0], z[0], color='r', s=50, label='Origem')
    
    ax.set_title(f"Rota TSP (Distância: {dist:.2f})")
    plt.legend()
    plt.show()

def resolver_tsp(csv_path='CaixeiroGruposGA (1).csv'):
    print("\n=== PARTE 2.2: CAIXEIRO VIAJANTE (GENETIC ALGORITHM) ===")
    
    # Carregar dados
    try:
        dados = np.loadtxt(csv_path, delimiter=',', skiprows=1)
        coords = dados[:, -3:] if dados.shape[1] >= 3 else dados
    except:
        print("Arquivo CSV não encontrado. Gerando dados aleatórios.")
        coords = np.random.uniform(-50, 50, (30, 3))

    # Executa o GA uma vez para gerar o gráfico
    ga = GeneticAlgorithmTSP(coords, pop_size=100, max_gen=500, prob_mut=0.01)
    rota, dist = ga.run()
    
    print(f"Melhor distância encontrada: {dist:.4f}")
    print("Gerando gráfico 3D...")
    plotar_rota_3d(coords, rota, dist)