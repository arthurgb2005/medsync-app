import requests

def buscar_cep(cep):
    cep = cep.replace("-", "").replace(" ", "")
    if len(cep) != 8:
        return None
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            dados = response.json()
            return f"{dados.get('logradouro')}, {dados.get('localidade')}" if "erro" not in dados else None
    except:
        return None
    return None

def adicionar_remedio(lista, nome, dose):
    if not nome or not dose:
        return "Erro: Campos obrigatorios vazios."
    lista.append({"nome": nome, "dose": dose})
    return "Sucesso"

def listar_remedios(lista):
    return str(lista) if lista else "Vazio"
