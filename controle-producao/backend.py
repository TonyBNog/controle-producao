import csv

ARQUIVO_CSV = 'produtos.csv'

def carregar():
    produtos = []
    try:
        with open(ARQUIVO_CSV, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                produtos.append(row)
    except FileNotFoundError:
        pass
    return produtos

def salvar(produtos):
    with open(ARQUIVO_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'cor', 'tamanho', 'tipo', 'status'])
        writer.writeheader()
        writer.writerows(produtos)

def cadastrar(produtos, id_, cor, tam, tipo):
    produto = {
        'id': id_,
        'cor': cor,
        'tamanho': tam,
        'tipo': tipo,
        'status': 'estoque'
    }
    produtos.append(produto)
    salvar(produtos)
    return produto

def listar(produtos, status=None):
    return [p for p in produtos if not status or p['status'] == status]

def atualizar(produtos, id_, novo_status):
    for p in produtos:
        if p['id'] == id_:
            p['status'] = novo_status
            salvar(produtos)
            return True
    return False

def excluir(produtos, id_):
    for i, p in enumerate(produtos):
        if p['id'] == id_:
            del produtos[i]
            salvar(produtos)
            return True
    return False

def listar_por_tipo(produtos, tipo):
    return [p for p in produtos if p['tipo'].lower() == tipo.lower()]
