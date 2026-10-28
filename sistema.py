import csv
from busca_ordenacao import busca_sequencial, busca_binaria, ordenar_insercao

ARQUIVO = "coletas.csv"
CAMPOS = ["codigo", "data", "material", "peso"]
MATERIAIS = ["papel", "plástico", "vidro", "metal"]

coletas = []


def carregar():
    try:
        with open(ARQUIVO, newline="", encoding="utf-8") as arq:
            for linha in csv.DictReader(arq):
                linha["codigo"] = int(linha["codigo"])
                linha["peso"] = float(linha["peso"])
                coletas.append(linha)
    except FileNotFoundError:
        pass  # primeira execução: o arquivo ainda não existe


def salvar():
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arq:
        escritor = csv.DictWriter(arq, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(coletas)


def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro.")


def ler_real_positivo(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
            if valor > 0:
                return valor
            print("O valor precisa ser maior que zero.")
        except ValueError:
            print("Digite um número, por exemplo 8.5")


def mostrar(c):
    print(f"{c['codigo']} | {c['data']} | {c['material']:<9} | {c['peso']:.1f} kg")


def cadastrar():
    codigo = ler_inteiro("Código: ")
    posicao, _ = busca_sequencial(coletas, codigo)
    if posicao != -1:
        print("Já existe uma coleta com esse código.")
        return
    data = input("Data (dd/mm/aaaa): ").strip()
    material = input(f"Material {MATERIAIS}: ").strip().lower()
    while material not in MATERIAIS:
        material = input("Material inválido. Digite novamente: ").strip().lower()
    peso = ler_real_positivo("Peso (kg): ")
    coletas.append({"codigo": codigo, "data": data, "material": material, "peso": peso})
    salvar()
    print("Coleta cadastrada.")


def listar(lista):
    if len(lista) == 0:
        print("Nenhuma coleta cadastrada.")
        return
    for c in lista:
        mostrar(c)


def buscar():
    codigo = ler_inteiro("Código procurado: ")
    ordenadas = ordenar_insercao(coletas, "codigo")
    posicao, comparacoes = busca_binaria(ordenadas, codigo)
    if posicao == -1:
        print(f"Coleta não encontrada ({comparacoes} comparações).")
    else:
        mostrar(ordenadas[posicao])
        print(f"({comparacoes} comparações)")


def relatorio():
    if len(coletas) == 0:
        print("Nenhuma coleta cadastrada.")
        return
    total = 0
    maior = coletas[0]
    menor = coletas[0]
    for c in coletas:
        total += c["peso"]
        if c["peso"] > maior["peso"]:
            maior = c
        if c["peso"] < menor["peso"]:
            menor = c
    print(f"Coletas registradas: {len(coletas)}")
    print(f"Peso total: {total:.1f} kg")
    print(f"Peso médio: {total / len(coletas):.1f} kg")
    print(f"Maior coleta: {maior['codigo']} ({maior['peso']:.1f} kg)")
    print(f"Menor coleta: {menor['codigo']} ({menor['peso']:.1f} kg)")


def menu():
    carregar()
    while True:
        print("\n1-Cadastrar  2-Listar  3-Buscar  4-Ranking por peso  5-Relatório  0-Sair")
        opcao = input("Opção: ").strip()
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar(coletas)
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            listar(ordenar_insercao(coletas, "peso")[::-1])
        elif opcao == "5":
            relatorio()
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
