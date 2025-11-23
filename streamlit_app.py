import streamlit as st
import re
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier

# ---------------------------------------------
# EXPRESSÕES REGULARES PARA DETECÇÃO
# ---------------------------------------------
patterns = {
    "CPF": r"\b\d{3}\.\d{3}\.\d{3}\-\d{2}\b",
    "Telefone": r"\b\d{10,11}\b",
    "Email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "Alergia": r"\balergia\b|\balérgico\b",
    "Endereço": r"\brua\b|\bavenida\b|\btravessa\b",
    "Saúde": r"\bremédio\b|\bdoença\b|\bemergência\b|\btratamento\b"
}

# ---------------------------------------------
# TREINAR MODELO SIMPLES DE RISCO
# ---------------------------------------------
def train_model():
    X = np.array([[0], [2], [5], [8], [12], [20]])
    y = np.array([0, 0, 1, 1, 2, 2])
    model = MLPClassifier(hidden_layer_sizes=(5,), max_iter=800)
    model.fit(X, y)
    return model

# ---------------------------------------------
# CLASSIFICAR RISCO
# ---------------------------------------------
def classify_risk(model, total_hits):
    pred = model.predict(np.array([[total_hits]]))[0]
    if pred == 0:
        return "BAIXO", "🟢"
    elif pred == 1:
        return "MÉDIO", "🟡"
    else:
        return "ALTO", "🔴"

# ---------------------------------------------
# DETECÇÃO PELO TEXTO
# ---------------------------------------------
def detect_sensitive(text):
    found = {}
    total_hits = 0

    for key, pattern in patterns.items():
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        found[key] = matches
        total_hits += len(matches)

    return found, total_hits


# ==============================================================
#                    INTERFACE STREAMLIT
# ==============================================================

st.set_page_config(page_title="SafeScan Kids", page_icon="🛡️", layout="centered")

st.title("🛡️ SafeScan Kids")
st.write("Sistema de análise de segurança de dados da empresa Abrakadabra Kids.")

uploaded = st.file_uploader("Envie um arquivo .txt ou .csv", type=["txt", "csv"])

if uploaded:
    # Ler arquivo
    if uploaded.name.endswith(".txt"):
        text = uploaded.read().decode("utf-8", errors="ignore")
    elif uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)
        text = df.to_string()

    st.subheader("📄 Conteúdo detectado no arquivo:")
    st.code(text[:2000])  # mostra só o começo para não travar

    # Rodar detecção
    found, total_hits = detect_sensitive(text)
    model = train_model()
    risk, emoji = classify_risk(model, total_hits)

    st.subheader("📊 Resultado da análise")
    st.write(f"**Ocorrências encontradas:** {total_hits}")
    st.write(f"**Nível de risco:** {emoji} **{risk}**")

    st.subheader("🔍 Detalhamento:")
    for key, matches in found.items():
        st.write(f"**{key}:** {len(matches)} encontrados")

    # Botão para gerar relatório
    report_text = "SAFE SCAN KIDS - RELATÓRIO\n"
    report_text += "===========================\n\n"
    report_text += f"Arquivo: {uploaded.name}\n"
    report_text += f"Total de ocorrências encontradas: {total_hits}\n"
    report_text += f"Nível de risco: {risk}\n\n"
    report_text += "Detalhes:\n"

    for key, matches in found.items():
        report_text += f"{key}: {len(matches)}\n"

    report_bytes = report_text.encode("utf-8")

    st.download_button(
        label="📥 Baixar relatório",
        data=report_bytes,
        file_name=f"relatorio_{uploaded.name}.txt",
        mime="text/plain"
    )
