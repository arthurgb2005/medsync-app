import streamlit as st
import requests

def buscar_cep(cep):
    """Busca o endereço através do CEP usando a API ViaCEP."""
    cep = cep.replace("-", "").replace(" ", "")
    if len(cep) != 8:
        return None
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            dados = response.json()
            if "erro" in dados:
                return None
            return f"{dados.get('logradouro')}, {dados.get('localidade')}"
    except requests.exceptions.RequestException:
        return None
    return None

st.title("💊 MedSync - Controle de Medicamentos")

st.subheader("📍 Localizar Farmácia")
cep_input = st.text_input("Digite seu CEP para achar o endereço:")
if st.button("Buscar Endereço"):
    endereco = buscar_cep(cep_input)
    if endereco:
        st.success(f"Endereço encontrado: {endereco}")
    else:
        st.error("CEP não encontrado.")

st.subheader("📝 Cadastrar Remédio")
nome = st.text_input("Nome do Medicamento:")
dose = st.text_input("Dosagem (ex: 500mg):")

if st.button("Adicionar"):
    if nome and dose:
        st.success(f"{nome} ({dose}) adicionado com sucesso!")
    else:
        st.warning("Preencha todos os campos.")
