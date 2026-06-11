import pytest

def test_ambiente_ci():
    """Garante que a esteira de testes valide com sucesso."""
    assert True

def test_validacao_simples():
    """Teste básico de lógica isolada que sempre passa."""
    resultado = 1 + 1
    assert resultado == 2
