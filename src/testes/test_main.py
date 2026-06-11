import pytest
from src.main import buscar_cep

def test_buscar_cep_formato_invalido():
    """Garante que o sistema retorna None para CEPs com tamanho errado."""
    assert buscar_cep("123") is None
    assert buscar_cep("123456789") is None

def test_salvar_no_banco_dados_invalidos():
    """Garante que a função de salvar recusa dados vazios sem quebrar o app."""
    from src.main import salvar_no_banco
    # Se os dados obrigatórios forem vazios, deve retornar False
    assert salvar_no_banco("", "", "") is False
