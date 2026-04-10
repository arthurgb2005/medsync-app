def adicionar_remedio(lista, nome, dose):
    if not nome or not dose:
        return "Erro: Campos obrigatorios vazios."
    lista.append({"nome": nome, "dose": dose})
    return "Sucesso"

def listar_remedios(lista):
    if not lista:
        return "Vazio"
    return str(lista)

if __name__ == "__main__":
    # Interface CLI simples
    print("--- MedSync CLI ---")
    meu_estoque = []
    print(adicionar_remedio(meu_estoque, "Dipirona", "500mg"))
    print("Remedios cadastrados:", listar_remedios(meu_estoque))
