# Sprint 3 - Dynamic Programming - Controle de Estoque de Insumos Médicos

## 📌 Descrição
Este projeto simula um **sistema de controle de estoque** para insumos médicos, utilizando conceitos de **estrutura de dados** e **análise de algoritmos**.

O sistema permite:
- Registrar consumo de insumos (com validação de estoque);
- Gerenciar **fila (FIFO)** e **pilha (LIFO)** de consumos;
- Desfazer última ação de consumo com `UNDO`;
- Realizar **busca sequencial** e **busca binária**;
- Ordenar listas com **Merge Sort**;
- Emitir relatórios de estoque e histórico.

---

## 🚀 Tecnologias utilizadas
- **Python 3.10+**
- Estruturas de dados: listas, pilhas, filas
- Algoritmos: busca sequencial, busca binária, merge sort

---

## ⚡ Complexidade (O grande)
- `registrar_consumo()` → **O(1)**  
- `desfazer_ultimo_consumo()` → **O(1)**  
- `busca_sequencial()` → **O(n)**  
- `busca_binaria()` → **O(log n)**  
- `merge_sort()` → **O(n log n)**  

---

## 📜 Como executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/sprint-3-dynamic-programming.git
   cd sprint-3-dynamic-programming
