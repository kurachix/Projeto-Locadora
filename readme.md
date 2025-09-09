# 🎬 Sistema de Locadora de Filmes e Jogos

Este projeto consiste em um **sistema de locadora** que permite cadastrar clientes, registrar filmes e jogos, e controlar empréstimos de itens.

---

## 📌 Funcionalidades

O sistema possui as seguintes funcionalidades:

- Cadastro de **clientes** com nome e CPF.
- Registro de **itens** para locação, incluindo filmes e jogos.
- Controle de **empréstimos e devoluções** de itens.
- Visualização dos itens alugados por cada cliente.
- Demonstração do uso de **herança** com as classes `Filme` e `Jogo` herdando de `Item`.

---

## 📌 Estrutura de Classes

### **Classe Item**
Classe base para filmes e jogos.

**Atributos**

| Atributo    | Tipo  | Descrição                  |
|------------|-------|----------------------------|
| codigo     | int   | Código único do item       |
| titulo     | str   | Título do filme/jogo       |
| disponivel | bool  | Disponibilidade do item    |

**Métodos**

| Nome     | Parâmetros | Retorno | Descrição                       |
|----------|------------|---------|---------------------------------|
| alugar   | -          | None    | Marca o item como alugado       |
| devolver | -          | None    | Marca o item como disponível    |

---

### **Classe Filme** (herda de Item)

**Atributos**

| Atributo | Tipo | Descrição           |
|----------|------|-------------------|
| genero   | str  | Gênero do filme     |
| duracao  | int  | Duração em minutos  |

**Métodos**

| Nome   | Parâmetros                | Retorno | Descrição               |
|--------|---------------------------|---------|-------------------------|
| __init__ | codigo, titulo, genero, duracao | None    | Construtor da classe    |

---

### **Classe Jogo** (herda de Item)

**Atributos**

| Atributo    | Tipo | Descrição                   |
|-------------|------|----------------------------|
| plataforma  | str  | Plataforma do jogo          |
| faixaEtaria | int  | Faixa etária recomendada    |

**Métodos**

| Nome   | Parâmetros                       | Retorno | Descrição               |
|--------|----------------------------------|---------|-------------------------|
| __init__ | codigo, titulo, plataforma, faixaEtaria | None    | Construtor da classe    |

---

### **Classe Cliente**

**Atributos**

| Atributo     | Tipo          | Descrição                         |
|-------------|---------------|-----------------------------------|
| nome        | str           | Nome do cliente                  |
| cpf         | str           | CPF do cliente                   |
| itensLocados| list[Item]    | Lista de itens alugados          |

**Métodos**

| Nome        | Parâmetros | Retorno | Descrição                     |
|------------|------------|---------|--------------------------------|
| locar      | item: Item | None    | Cliente aluga um item         |
| devolver   | item: Item | None    | Cliente devolve um item       |
| listarItens| -          | None    | Mostra todos os itens alugados|

---

### **Classe Locadora**

**Atributos**

| Atributo | Tipo         | Descrição                      |
|----------|--------------|--------------------------------|
| clientes | list[Cliente]| Lista de clientes cadastrados  |
| itens    | list[Item]   | Lista de itens disponíveis     |

**Métodos**

| Nome             | Parâmetros          | Retorno | Descrição                                |
|-----------------|-------------------|---------|------------------------------------------|
| cadastrarCliente | cliente: Cliente  | None    | Adiciona um cliente à locadora           |
| cadastrarItem    | item: Item        | None    | Adiciona um item (filme ou jogo)        |
| listarClientes   | -                 | None    | Mostra todos os clientes cadastrados     |
| listarItens      | -                 | None    | Mostra todos os itens cadastrados        |

---

## 📌 Como usar

1. Clone o repositório:
```bash
git clone <https://github.com/kurachix/Projeto-Locadora>

Importe as classes no seu projeto Python e crie instâncias de Cliente, Filme e Jogo.

Utilize a classe Locadora para gerenciar clientes e itens.

📌 Tecnologias

Python 3.x

Orientação a Objetos (Classes, Herança, Encapsulamento)

📌 Autor

Kurachi
