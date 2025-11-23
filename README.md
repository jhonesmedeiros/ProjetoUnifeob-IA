SafeScan Kids – AbracadabraKids
IA + Segurança da Informação para Detecção de Dados Sensíveis Infantis (LGPD)

O SafeScan Kids é uma solução desenvolvida para apoiar a AbracadabraKids, oferecendo detecção automática de dados sensíveis e pessoais presentes em arquivos de texto ou planilhas. O sistema utiliza Expressões Regulares (Regex) combinadas com um modelo de IA (MLPClassifier) para identificar riscos em conformidade com a LGPD, especialmente no tratamento de dados de crianças.

🚀 Funcionalidades Principais

✔️ Detecção automática de:

CPF

E-mails

Telefones

Endereços

Datas de nascimento

Indícios de alergias e dados sensíveis

✔️ Classificação automática via IA em três níveis:

0 — Conteúdo comum

1 — Dado pessoal

2 — Dado sensível infantil

✔️ Sistema de avaliação de risco:

Baixo, Médio ou Alto

✔️ Geração automática de relatório com:

Dados encontrados

Trecho analisado

Classificação da IA

Nível de risco

📦 Tecnologias Utilizadas

Python 3.10+

scikit-learn (MLPClassifier)

pandas

re (regex)

🔧 Como Executar o Projeto
1. Clone o repositório
git clone https://github.com/seuusuario/safescan-kids.git
cd safescan-kids

2. Crie um ambiente virtual (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

3. Instale as dependências
pip install -r requirements.txt

4. Execute o analisador
python safescan_backend.py


O script carregará o modelo de IA, analisará os arquivos definidos e gerará o relatório final em texto.

📁 Estrutura do Projeto
/safescan-kids
│
├── safescan_backend.py     # Núcleo da IA + detecção de dados sensíveis
├── requirements.txt        # Dependências
└── README.md               # Documentação

🧠 Como Funciona a IA

O sistema cria um vetor de texto usando CountVectorizer

Treina um modelo MLPClassifier simples

Classifica o conteúdo em:

0 (comum), 1 (pessoal), 2 (sensível)

Combina IA + Regex para definir o nível final de risco

🛡️ Finalidade do Projeto

O SafeScan Kids busca auxiliar pequenas empresas — como a AbracadabraKids — a garantir práticas de segurança e privacidade no trato de informações, oferecendo uma solução acessível, educacional e alinhada à LGPD.
