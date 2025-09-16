# Challenge Dynamic Programming

# Participantes:
# Dayana Ticona Quispe - RM 558023
# Luiz Felipe Motta da Silva - RM 559126
# Nicolas Lorenzo Ferreira da Silva - RM 557962
# Pedro Henrique Faim dos Santos - RM 557440
# Victoria Moura Miyamoto - RM 555474



from collections import deque

# ===============================
# Simulação de Dados de Consumo
# ===============================
consumos = [
    {"insumo": "Reagente A", "quantidade": 10, "validade": "2025-10-10"},
    {"insumo": "Reagente B", "quantidade": 5, "validade": "2025-09-20"},
    {"insumo": "Reagente C", "quantidade": 8, "validade": "2025-09-25"},
    {"insumo": "Reagente D", "quantidade": 12, "validade": "2025-11-01"},
    {"insumo": "Reagente E", "quantidade": 3, "validade": "2025-09-18"},
]

# ===============================
# FILA (FIFO) – Registro de consumo
# ===============================
def fila_consumo(consumos):
    fila = deque()
    for c in consumos:
        fila.append(c)
    return fila

# ===============================
# PILHA (LIFO) – Consultas inversas
# ===============================
def pilha_consumo(consumos):
    pilha = []
    for c in consumos:
        pilha.append(c)
    return pilha

# ===============================
# BUSCA SEQUENCIAL
# ===============================
def busca_sequencial(consumos, nome_insumo):
    for c in consumos:
        if c["insumo"] == nome_insumo:
            return c
    return None

# ===============================
# BUSCA BINÁRIA
# (precisa da lista ordenada pelo nome do insumo)
# ===============================
def busca_binaria(consumos, nome_insumo):
    consumos_ordenados = sorted(consumos, key=lambda x: x["insumo"])
    esquerda, direita = 0, len(consumos_ordenados) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if consumos_ordenados[meio]["insumo"] == nome_insumo:
            return consumos_ordenados[meio]
        elif consumos_ordenados[meio]["insumo"] < nome_insumo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None

# ===============================
# MERGE SORT
# ===============================
def merge_sort(lista, chave):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)

    return merge(esquerda, direita, chave)

def merge(esquerda, direita, chave):
    resultado = []
    i, j = 0, 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i][chave] <= direita[j][chave]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

# ===============================
# QUICK SORT
# ===============================
def quick_sort(lista, chave):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [x for x in lista[1:] if x[chave] <= pivo[chave]]
    maiores = [x for x in lista[1:] if x[chave] > pivo[chave]]
    return quick_sort(menores, chave) + [pivo] + quick_sort(maiores, chave)

# ===============================
# TESTES / DEMONSTRAÇÃO
# ===============================
if __name__ == "__main__":
    print("=== FILA (ordem cronológica) ===")
    fila = fila_consumo(consumos)
    for c in fila:
        print(c)

    print("\n=== PILHA (últimos consumos) ===")
    pilha = pilha_consumo(consumos)
    while pilha:
        print(pilha.pop())

    print("\n=== BUSCA SEQUENCIAL por 'Reagente C' ===")
    print(busca_sequencial(consumos, "Reagente C"))

    print("\n=== BUSCA BINÁRIA por 'Reagente D' ===")
    print(busca_binaria(consumos, "Reagente D"))

    print("\n=== MERGE SORT por quantidade ===")
    ordenado_merge = merge_sort(consumos, "quantidade")
    for c in ordenado_merge:
        print(c)

    print("\n=== QUICK SORT por validade ===")
    ordenado_quick = quick_sort(consumos, "validade")
    for c in ordenado_quick:
        print(c)