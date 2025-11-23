import os
import re
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def treinar_modelo():
    textos = [
        "comprovante de endereço da criança",
        "autorização do responsável",
        "ficha médica alergias",
        "documento dos pais",
        "cadastro do tutor",
        "dados do fornecedor brinquedos",
        "nota fiscal do brinquedo",
        "manual de instruções dos brinquedos"
    ]

    rotulos = [
        "cadastro criança",
        "cadastro responsável",
        "cadastro criança",
        "cadastro responsável",
        "cadastro tutor",
        "cadastro fornecedor",
        "cadastro fornecedor",
        "documentação brinquedos"
    ]

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(textos)

    modelo = MultinomialNB()
    modelo.fit(X, rotulos)

    return modelo, vectorizer

def carregar_modelo():
    if os.path.exists("models/model.pkl") and os.path.exists("models/vectorizer.pkl"):
        with open("models/model.pkl", "rb") as f:
            modelo = pickle.load(f)
        with open("models/vectorizer.pkl", "rb") as f:
            vectorizer = pickle.load(f)
        return modelo, vectorizer

    modelo, vectorizer = treinar_modelo()

    os.makedirs("models", exist_ok=True)
    with open("models/model.pkl", "wb") as f:
        pickle.dump(modelo, f)
    with open("models/vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    return modelo, vectorizer

def analisar_documento(texto: str):
    modelo, vectorizer = carregar_modelo()

    padroes = {
        "CPF": r"\b\d{3}\.\d{3}\.\d{3}\-\d{2}\b",
        "CNPJ": r"\b\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}\b",
        "Telefone": r"\(?\d{2}\)?\s?\d{4,5}\-?\d{4}",
        "Email": r"[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9\.\-]+\.[a-z]{2,4}"
    }

    encontrados = {}
    for nome, rgx in padroes.items():
        resultados = re.findall(rgx, texto)
        encontrados[nome] = resultados

    previsao = modelo.predict(vectorizer.transform([texto]))[0]

    risco = "Baixo"
    if len(encontrados.get("CPF", [])) > 0 or len(encontrados.get("CNPJ", [])) > 0:
        risco = "Alto"
    elif len(encontrados.get("Email", [])) > 0:
        risco = "Médio"

    return {
        "categoria": previsao,
        "padroes": encontrados,
        "risco": risco
    }

if __name__ == "__main__":
    caminho = input("Digite o caminho do arquivo para análise: ")

    if not os.path.exists(caminho):
        print("Arquivo não encontrado!")
        exit()

    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read()

    resultado = analisar_documento(conteudo)

    print("\n=== RESULTADO DA ANÁLISE ===")
    print("Categoria prevista:", resultado["categoria"])
    print("Risco:", resultado["risco"])
    print("\nPadrões encontrados:")

    for k, v in resultado["padroes"].items():
        print(f"- {k}: {v}")
