import streamlit as st
import requests
from supabase import create_client

# Inicializa a conexão com o Supabase usando as chaves guardadas nos Secrets
@st.cache_resource
def iniciar_conexao():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

try:
    supabase = iniciar_conexao()
except Exception:
    st.error("Erro ao conectar ao Banco de Dados.")

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
            if "erro" not in dados:
                return f"{dados.get('logradouro')}, {dados.get('localidade')}"
    except requests.exceptions.RequestException:
        return None
    return None

def salvar_no_banco(nome, dose, cep):
    """Insere um novo medicamento na tabela do Supabase."""
    if not nome or not dose:
        return False
    data = {"nome": nome, "dose": dose, "cep": cep}
    supabase.table("medicamentos").insert(data).execute()
    return True

def listar_do_banco():
    """Busca todos os medicamentos cadastrados na nuvem."""
    resposta = supabase.table("medicamentos").select("*").order("criado_em").execute()
    return resposta.data

# Interface Gráfica (Streamlit)
st.title("💊 MedSync - Sistema de Medicamentos")

st.subheader("📝 Cadastrar Novo Medicamento")
nome = st.text_input("Nome do Medicamento:")
dose = st.text_input("Dosagem (ex: 500mg):")
cep_input = st.text_input("CEP da Farmácia de Retirada (Opcional):")

if st.button("Salvar no Banco de Dados"):
    endereco_completo = ""
    if cep_input:
        endereco_completo = buscar_cep(cep_input) or "CEP não localizado"
    
    if salvar_no_banco(nome, dose, endereco_completo):
        st.success(f"Sucesso! {nome} foi salvo de forma permanente na nuvem.")
    else:
        st.warning("Preencha os campos obrigatórios (Nome e Dosagem).")

st.subheader("📋 Medicamentos Cadastrados (Dados Reais da Nuvem)")
try:
    itens = listar_do_banco()
    if itens:
        for item in itens:
            st.write(f"• **{item['nome']}** ({item['dose']}) - Local: {item['cep'] or 'Não informado'}")
    else:
        st.info("Nenhum medicamento listado no banco.")
except Exception:
    st.warning("Aguardando configuração de chaves para listar dados.")
