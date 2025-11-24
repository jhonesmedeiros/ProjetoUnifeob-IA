# 🧒🎡 SafeScanKids  
### Sistema Inteligente de Classificação e Verificação de Documentos  
Projeto desenvolvido para a empresa fictícia **AbrakadabraKids**, integrando Inteligência Artificial e Segurança da Informação.

---

## 📘 Visão Geral

O **SafeScanKids** é uma solução de IA projetada para analisar documentos utilizados no cadastro e operação da AbrakadabraKids.  
Ele é capaz de:

- Classificar automaticamente o tipo de documento (criança, responsável, tutor, fornecedor, brinquedos);
- Detectar dados sensíveis (CPF, CNPJ, telefone, e-mail);
- Indicar o nível de risco de acordo com a LGPD;
- Funcionar tanto por **linha de comando** quanto através de uma **interface web** em Streamlit.

O sistema foi pensado para apoiar a segurança da informação, minimizar riscos e facilitar a organização documental.

---

## 🧠 Funcionalidades Principais

### ✔️ Classificação Automática  
Utiliza **Machine Learning (Naive Bayes)** para identificar a categoria mais provável do documento.

### ✔️ Detecção de Dados Sensíveis  
Reconhece automaticamente:
- CPF  
- CNPJ  
- Telefone  
- E-mail  

### ✔️ Cálculo de Risco  
Baseado nas informações encontradas:

| Dados Encontrados | Risco |
|------------------|-------|
| CPF ou CNPJ | 🔴 Alto |
| E-mail | 🟡 Médio |
| Nenhum dado sensível | 🟢 Baixo |

### ✔️ Interface Web  
Uma interface amigável feita em **Streamlit** para facilitar apresentações e demonstrações.

---

## 📂 Estrutura do Projeto

SafeScanKidsProjeto/
│
├── safescan_kids.py # Versão CLI (linha de comando)
├── streamlit_app.py # Interface web
├── requirements.txt # Dependências
├── README.md # Documentação
│
├── data/ # Arquivos de teste
│ ├── dados_clientes.txt
│ └── documento_inofensivo.txt
│
└── models/ # Gerado automaticamente
├── model.pkl
└── vectorizer.pkl

yaml
Copiar código

---

## 🛠️ Instalação

### 1️⃣ Clone o projeto
```bash
git clone https://github.com/jhonesmedeiros/ProjetoUnifeob-IA/edit/main/README.md
cd SafeScanKids
2️⃣ Instale dependências
bash
Copiar código
pip install -r requirements.txt
Python 3.10+ recomendado.

▶️ Como Usar
✔️ Modo 1 — Linha de Comando
Execute:

bash
Copiar código
python safescan_kids.py
Informe o caminho do arquivo:

kotlin
Copiar código
Digite o caminho do arquivo para análise: data\documento_teste.txt
Exemplo de saída:
yaml
Copiar código
=== RESULTADO DA ANÁLISE ===
Categoria prevista: cadastro responsável
Risco: Alto

Padrões encontrados:
- CPF: ['123.456.789-00']
- CNPJ: []
- Telefone: []
- Email: ['exemplo@teste.com']
✔️ Modo 2 — Interface Web (Streamlit)
Execute:

bash
Copiar código
streamlit run streamlit_app.py
Acesse no navegador:

arduino
Copiar código
http://localhost:8501
Você poderá colar textos e ver:

Categoria prevista

Nível de risco

Dados sensíveis detectados

📁 Criando Seus Próprios Arquivos
Coloque os arquivos no diretório:

kotlin
Copiar código
data/
Exemplo de conteúdo:

makefile
Copiar código
Nome: Ana Souza
CPF: 987.654.321-00
Email: ana.souza@example.com
🔒 Segurança da Informação
O SafeScanKids foi projetado seguindo princípios da LGPD:

Não envia dados para a internet

Funciona totalmente offline

Não armazena documentos analisados

Mantém apenas o modelo de IA necessário para classificação

👨‍💻 Tecnologias Utilizadas
Python 3

Scikit-learn

Streamlit

Expressões Regulares (Regex)

Pickle

VS Code

Git / GitHub



RA: 24000758 NOME: Thauan Thales Paulista
RA: 24000679 NOME: Gustavo Costa Jorge
RA: 24000544 NOME: Jhones Medeiros Martins
