import streamlit as st
from cadastro import show_cadastro
from databases import adicionar_cliente

st.sidebar.subpage("Cadastro de Capacitação", show_cadastro(adicionar_cliente))
