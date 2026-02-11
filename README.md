# 🧬 Trabalho AV3 - Busca e Otimização com Meta-heurísticas

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Completo-success.svg)

Implementação de algoritmos de busca e otimização utilizando meta-heurísticas aplicadas a problemas de otimização discreta e contínua, com foco no **Problema do Caixeiro Viajante (TSP - Traveling Salesman Problem)**.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina de **Inteligência Artificial Computacional** e implementa diversos algoritmos de meta-heurísticas para resolver problemas clássicos de otimização, incluindo:

- **Otimização Discreta**: Problema do Caixeiro Viajante (TSP)
- **Otimização Contínua**: Funções matemáticas complexas

## 🎯 Funcionalidades

### Algoritmos Implementados

#### Otimização Discreta
- ✅ **Algoritmo Genético (GA)** para TSP
- ✅ Operadores de crossover e mutação especializados
- ✅ Seleção por torneio e elitismo
- ✅ Visualização de rotas e convergência

#### Otimização Contínua
- ✅ **Simulated Annealing**
- ✅ **Hill Climbing**
- ✅ **Algoritmos Genéticos**
- ✅ Otimização de funções multi-dimensionais
- ✅ Visualização em 2D e 3D

### Recursos Adicionais
- 📊 Plotagem de gráficos 2D e 3D
- 📈 Análise de convergência
- 🔢 Controle de número de iterações/rodadas
- 💾 Importação de dados via CSV

## 🗂️ Estrutura do Projeto

```
Trabalho-AV3-Busca-Otimizacao-Meta-heuristica/
│
├── biblioteca_continuo.py      # Funções de otimização contínua
├── biblioteca_discreto.py      # Funções de otimização discreta (TSP)
├── main.py                     # Script principal de execução
├── CaixeiroGruposGA.csv       # Dataset com coordenadas das cidades
├── README.md                   # Documentação do projeto
└── .gitignore                  # Arquivos ignorados pelo Git
```

## 🚀 Como Executar

### Pré-requisitos

```bash
Python 3.13 ou superior
pip (gerenciador de pacotes Python)
```

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/LucNath/Trabalho-AV3-Busca-Otimizacao-Inteligencia-Artificial.git
cd Trabalho-AV3-Busca-Otimizacao-Inteligencia-Artificial
```

2. Instale as dependências:
```bash
pip install numpy matplotlib pandas
```

### Executando o Projeto

```bash
python main.py
```

## 📊 Exemplos de Uso

### Problema do Caixeiro Viajante

O algoritmo genético resolve o TSP encontrando a rota mais curta que visita todas as cidades exatamente uma vez e retorna à cidade inicial.

**Entrada**: Arquivo CSV com coordenadas das cidades
**Saída**: 
- Melhor rota encontrada
- Distância total percorrida
- Gráfico da evolução da fitness
- Visualização da rota

### Otimização de Funções Contínuas

Implementações de meta-heurísticas para encontrar mínimos/máximos globais de funções matemáticas complexas.

**Algoritmos disponíveis**:
- Simulated Annealing
- Hill Climbing
- Algoritmos Genéticos

## 🧮 Algoritmos e Técnicas

### Algoritmo Genético (GA)
- **Representação**: Permutação de cidades (para TSP)
- **Seleção**: Torneio
- **Crossover**: Order Crossover (OX) / Partially Mapped Crossover (PMX)
- **Mutação**: Swap / Inversão
- **Elitismo**: Preservação dos melhores indivíduos

### Simulated Annealing
- **Estratégia de resfriamento**: Geométrico
- **Temperatura inicial**: Configurável
- **Critério de aceitação**: Metropolis

### Métricas de Avaliação
- Convergência ao longo das gerações
- Melhor solução encontrada
- Tempo de execução
- Diversidade populacional

## 🛠️ Tecnologias Utilizadas

- **Python 3.13** - Linguagem principal
- **NumPy** - Operações numéricas e vetoriais
- **Matplotlib** - Visualização de dados e gráficos
- **Pandas** - Manipulação de dados (CSV)

## 📈 Resultados

O projeto demonstra a eficácia das meta-heurísticas em problemas de otimização:

- ✅ Convergência eficiente para soluções de qualidade
- ✅ Capacidade de escapar de ótimos locais
- ✅ Balanceamento entre exploração e explotação
- ✅ Visualização clara da evolução das soluções

## 👨‍💻 Autor

**Lucas Nathan**
- GitHub: [@LucNath](https://github.com/LucNath)

## 📝 Licença

Este projeto é de código aberto e está disponível para fins educacionais.

## 🙏 Agradecimentos

- Professor André - Disciplina de Inteligência Artificial Computacional
- UNIFOR - Universidade de Fortaleza

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
