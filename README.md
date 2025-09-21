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

## 🧩 Uso das Estruturas no Contexto do Problema

- **Fila (FIFO)**: Usada para registrar os consumos diários em ordem cronológica, representando a sequência real de utilização dos insumos nas unidades de diagnóstico. Assim, o gestor pode consultar o histórico de forma linear.

- **Pilha (LIFO)**: Usada para simular consultas em ordem inversa (últimos consumos primeiro) e também para implementar a funcionalidade **UNDO**, permitindo desfazer o último consumo registrado.

- **Busca Sequencial**: Aplicada quando o estoque ou o histórico de consumo está em uma lista não ordenada. Permite localizar insumos de forma simples, ainda que custosa para grandes volumes.

- **Busca Binária**: Utilizada em listas ordenadas de insumos, garantindo maior eficiência na localização de itens específicos em comparação à busca sequencial.

- **Merge Sort**: Usado para organizar insumos por quantidade consumida. Essa ordenação é essencial para identificar quais materiais têm maior ou menor saída, facilitando a tomada de decisão sobre reposição e previsão de consumo.

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

