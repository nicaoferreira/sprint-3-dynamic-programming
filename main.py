# Sprint 3 - Dynamic Programming

# Participantes:

# Dayana Ticona Quispe - RM 558023
# Luiz Felipe Motta da Silva - RM 559126
# Nicolas Lorenzo Ferreira da Silva - RM 557962
# Pedro Henrique Faim dos Santos - RM 557440
# Victoria Moura Miyamoto - RM 555474

import bisect

estoque = {
    "seringas": 50,
    "luvas": 100,
    "mascaras": 200
}

fila_consumo = []

historico = []

def registrar_consumo(insumo, quantidade):
    """
    Registra consumo no estoque, adiciona na fila e no histórico (pilha).
    Complexidade: O(1)
    """
    if insumo in estoque and estoque[insumo] >= quantidade:
        estoque[insumo] -= quantidade
        fila_consumo.append((insumo, quantidade))  # FIFO
        historico.append((insumo, quantidade))     # LIFO
        print(f"Consumo registrado: {quantidade} {insumo}")
    else:
        print("Insumo insuficiente ou inexistente.")

def desfazer_ultimo_consumo():
    """
    Desfaz última ação de consumo usando pilha (LIFO).
    Complexidade: O(1)
    """
    if historico:
        insumo, quantidade = historico.pop()
        estoque[insumo] += quantidade
        print(f"Último consumo desfeito: {quantidade} {insumo} devolvidos ao estoque.")
    else:
        print("Nenhuma ação para desfazer.")

def busca_sequencial(lista, item):
    """
    Busca sequencial em uma lista.
    Complexidade: O(n)
    """
    for i, elemento in enumerate(lista):
        if elemento == item:
            return i
    return -1

def busca_binaria(lista, item):
    """
    Busca binária em lista ORDENADA.
    Complexidade: O(log n)
    """
    index = bisect.bisect_left(lista, item)
    if index < len(lista) and lista[index] == item:
        return index
    return -1

def merge_sort(lista):
    """
    Ordenação Merge Sort.
    Complexidade: O(n log n)
    """
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def relatorio():
    print("\n📦 Estoque atual:")
    for item, qtd in estoque.items():
        print(f"- {item}: {qtd}")

    print("\n📜 Fila de consumo (FIFO):")
    for c in fila_consumo:
        print(f"- {c[1]} {c[0]}")

    print("\n⏪ Histórico de consumo (Pilha/LIFO):")
    for c in reversed(historico):
        print(f"- {c[1]} {c[0]}")

if __name__ == "__main__":
    registrar_consumo("seringas", 10)
    registrar_consumo("luvas", 20)
    relatorio()

    desfazer_ultimo_consumo()
    relatorio()

    lista = [5, 2, 9, 1, 7]
    print("\nLista original:", lista)
    print("Merge Sort:", merge_sort(lista))
    print("Busca sequencial (7):", busca_sequencial(lista, 7))
    print("Busca binária (em lista ordenada) (7):", busca_binaria(sorted(lista), 7))
