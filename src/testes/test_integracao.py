from src.main import buscar_cep

def test_api_viacep_sucesso():
    # Este teste "sai" do seu PC e vai até o servidor do ViaCEP
    resultado = buscar_cep("01001000")
    assert "Praça da Sé" in resultado

def test_api_viacep_formato_errado():
    # Testa como o sistema lida com um CEP que não existe
    resultado = buscar_cep("99999999")
    assert resultado is None
