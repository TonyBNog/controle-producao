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

import streamlit as st
from backend import carregar, cadastrar, listar, atualizar, excluir, listar_por_tipo

st.set_page_config(page_title="Controle de Produção", layout="wide")

st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        h1 {
            color: #212529;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🏭 Controle de Produção")

produtos = carregar()

with st.sidebar:
    st.header("📋 Menu")
    menu = st.radio("Escolha uma opção:", [
        "Cadastrar Produto",
        "Listar Todos",
        "Filtrar por Status",
        "Atualizar Status",
        "Excluir Produto",
        "Filtrar por Tipo"
    ])

st.divider()

if menu == "Cadastrar Produto":
    st.subheader("➕ Cadastrar Novo Produto")
    col1, col2 = st.columns(2)
    with col1:
        id_ = st.number_input("ID do produto", min_value=1, step=1)
        cor = st.text_input("Cor")
    with col2:
        tam = st.text_input("Tamanho")
        tipo = st.text_input("Tipo")

    if st.button("Cadastrar Produto"):
        try:
            produto = cadastrar(produtos, id_, cor, tam, tipo)
            st.success(f"✔ Produto cadastrado: {produto}")
        except Exception as e:
            st.error(f"Erro: {e}")

elif menu == "Listar Todos":
    st.subheader("📦 Todos os Produtos")
    lista = listar(produtos)
    st.dataframe(lista, use_container_width=True)

elif menu == "Filtrar por Status":
    st.subheader("🔍 Filtrar por Status")
    status = st.selectbox("Escolha o status", ['estoque', 'processamento', 'vendido'])
    lista = listar(produtos, status=status)
    st.dataframe(lista, use_container_width=True)

elif menu == "Atualizar Status":
    st.subheader("📝 Atualizar Status de Produto")
    id_ = st.number_input("ID do produto", min_value=1, step=1)
    novo = st.selectbox("Novo status", ['estoque', 'processamento', 'vendido'])
    if st.button("Atualizar Status"):
        if atualizar(produtos, id_, novo):
            st.success("Status atualizado com sucesso!")
        else:
            st.error("Produto não encontrado.")

elif menu == "Excluir Produto":
    st.subheader("🗑️ Excluir Produto")
    id_ = st.number_input("ID do produto a excluir", min_value=1, step=1)
    if st.button("Excluir"):
        if excluir(produtos, id_):
            st.success("Produto excluído com sucesso.")
        else:
            st.error("Produto não encontrado.")

elif menu == "Filtrar por Tipo":
    st.subheader("🔍 Filtrar por Tipo")
    tipo = st.text_input("Digite o tipo (ex: camiseta, bolsa, etc.):")
    if tipo:
        lista = listar_por_tipo(produtos, tipo)
        st.dataframe(lista, use_container_width=True)
