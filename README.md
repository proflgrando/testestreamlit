# 📚 Portfólio de Algoritmos em Python com Streamlit

Este projeto é um **portfólio didático** desenvolvido em **Python**, com interface web criada usando o **Streamlit**.

O app contém exemplos de:

* Estruturas de **decisão e repetição** (tabuada).
* **Recursividade** (fatorial).
* **Consumo de API** (imagem de gato 🐱).

---

## 🚀 Como rodar localmente

### 1. Pré-requisitos

* Ter o **Python 3.8+** instalado.
* Ter o **pip** (gerenciador de pacotes do Python).

### 2. Clonar o repositório (ou baixar os arquivos)

```bash
git clone https://github.com/seu-usuario/portfolio-algoritmos.git
cd portfolio-algoritmos
```

### 3. Criar um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
```

Ativar o ambiente virtual:

* **Windows (PowerShell):**

  ```bash
  venv\Scripts\activate
  ```
* **Linux/Mac:**

  ```bash
  source venv/bin/activate
  ```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

Se não existir o arquivo `requirements.txt`, basta rodar:

```bash
pip install streamlit requests
```

### 5. Executar a aplicação

```bash
streamlit run app.py
```

Após rodar, abra o navegador no endereço (por padrão):
👉 `http://localhost:8501`

---

## 🌐 Como publicar no Streamlit Community Cloud

O **Streamlit Community Cloud** permite rodar sua aplicação **na nuvem gratuitamente**, a partir de um repositório no GitHub.

### 1. Criar uma conta

* Acesse: [https://streamlit.io/cloud](https://streamlit.io/cloud)
* Clique em **"Sign in with GitHub"**.
* Autorize o acesso aos repositórios.

### 2. Subir o código no GitHub

No repositório, você precisa ter:

* `app.py` → código principal do Streamlit
* `requirements.txt` → lista de dependências
* `README.md` → documentação

### 3. Exemplo de `requirements.txt`

```txt
streamlit
requests
```

### 4. Fazer o deploy

* Vá até: [https://share.streamlit.io/](https://share.streamlit.io/)
* Clique em **"New app"**
* Escolha o repositório e a branch (ex.: `main`)
* Informe o arquivo principal: `app.py`
* Clique em **Deploy 🚀**

### 5. Compartilhar seu app

O Streamlit vai gerar um link parecido com:

```
https://seu-usuario-portfolio-algoritmos.streamlit.app
```

Esse link pode ser usado como parte do portfólio para mostrar seus trabalhos.

---

## 📂 Estrutura do Projeto

```
portfolio-algoritmos/
│-- app.py              # Código principal do Streamlit
│-- requirements.txt    # Dependências do projeto
│-- README.md           # Instruções do projeto
```

---

## 🧩 Funcionalidades

### Tema 1 – Decisão e Repetição

* Gera a tabuada de um número informado pelo usuário.

### Tema 2 – Recursividade

* Calcula o **fatorial** de um número usando função recursiva.

### Tema 3 – Acesso a API

* Consome uma API pública de gatos (TheCatAPI).
* Exibe uma imagem aleatória na tela.

---

## 📌 Tecnologias utilizadas

* [Python 3](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [Requests](https://pypi.org/project/requests/)

---

## 💡 Dicas para os alunos

1. Teste localmente antes de publicar na nuvem.
2. Documente cada tema no código ou em relatório separado.
3. Use o **Streamlit Cloud** para mostrar seus projetos na web.

---
