#
# Controle de Produção
#
# Copyright (c) 2025 Sal e Cia
#
# Este trabalho está licenciado sob a Creative Commons Atribuição-NãoComercial 4.0 Internacional.
# Para ver uma cópia desta licença, visite: https://creativecommons.org/licenses/by-nc/4.0/
#
# Você é livre para: Compartilhar e Adaptar, sob as condições de Atribuição e Não Comercial.
#
# O software é fornecido "como está", sem garantia de qualquer tipo, expressa ou implícita,
# incluindo, mas não se limitando a, garantias de comercialização, adequação a uma finalidade específica
# e não infração. Em nenhum caso os autores ou detentores dos direitos autorais serão responsáveis
# por qualquer reclamação, danos ou outra responsabilidade, seja em uma ação de contrato, ato ilícito
# ou de outra forma, decorrentes de, ou em conexão com o software ou o uso ou outras negociações no software.
#

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
