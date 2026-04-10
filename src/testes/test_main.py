from src.main import adicionar_remedio, listar_remedios

def test_adicionar_sucesso():
    lista = []
    assert adicionar_remedio(lista, "Aspirina", "100mg") == "Sucesso"

def test_adicionar_erro():
    lista = []
    assert adicionar_remedio(lista, "", "") == "Erro: Campos obrigatorios vazios."

def test_lista_vazia():
    lista = []
    assert listar_remedios(lista) == "Vazio"
