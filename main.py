from tabulate import tabulate
import json
import os


def carregar_lista():
    lista = {}
    if os.path.exists('lista.json'):
        with open('lista.json', 'r') as f:
            lista = json.load(f)
    return lista


def gravar_lista(lista):
    with open('lista.json', 'w') as f:
        json.dump(lista, f)


def imprimir_lista(lista, chaves):
    list = []
    for chave in chaves:
        list.append([
            lista[chave]["produto"],
            lista[chave]["unidade"],
            lista[chave]["preco"]
        ])

    print(tabulate(list, headers=["Produto", "Unid.", "Preço"], tablefmt="grid", floatfmt=".2f"))


def buscar_chaves(dic, produto):
    chaves = []
    for chave in dic:
        if chave.startswith(produto):
            chaves.append(chave)
    return chaves


lista = carregar_lista()

comando = "continue"

while comando != "0":
    print("")
    comando = input("1-Listar 2-Cadastrar 3-Alterar 4 Apagar 0-Sair: ")

    if comando == "1":
        ordenado = sorted(lista, key=lambda produtos: lista[produtos]['produto'])
        imprimir_lista(lista, ordenado)

    if comando == "2":
        produto = input("Produto: ").strip().upper()
        unidade = input("Unidade: ").strip().upper()
        preco = input("Preço: ").strip()
        lista[produto] = {
            "produto": produto,
            "unidade": unidade,
            "preco": preco
        }
        gravar_lista(lista)
        print("Produto cadastrado")

    if comando == "3":
        produto = input("Produto: ").strip().upper()
        chaves_encontradas = buscar_chaves(lista, produto)
        if len(chaves_encontradas) > 0:
            imprimir_lista(lista, chaves_encontradas)
            temp = input("Qual o novo preço: ").strip()
            print("")
            print("Preço alterado")
            print(lista)
            print(chaves_encontradas)
        else:
            print("Produto não cadastrado")

    if comando == "4":
        produto = input("Qual produto apagar? ").strip().upper()
        chaves_encontradas = buscar_chaves(lista, produto)
        if len(chaves_encontradas) > 0:
            imprimir_lista(lista, chaves_encontradas)
            print(f"Deseja apagar produto {chaves_encontradas}? ")
            resposta = input("Digite S ou N: ").strip().upper()
            if resposta == "S":
                apagado = (f"lista{chaves_encontradas}")
                print(apagado)
				del apagado
                #del lista['BANANA']
                print(f"Produto {chaves_encontradas} apagada.")
            else:
                print("Opção cancelada.")

    if comando == "x":
        print(lista)


        #del lista['BANANA']
