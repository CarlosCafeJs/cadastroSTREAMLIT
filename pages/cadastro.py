import streamlit as st
st.page_link("app.py", label="Home")

with st.form('capacitacao', clear_on_submit=False, border=True):
    nome = st.text_input('Nome completo')
    matricula = st.text_input('Matricula')
    setor = st.selectbox('Selecione o Setor', ['SUNEC', 'SUPOP', 'SUPES'])
    diretoria = st.selectbox('Selecione a Diretoria', 
                             ['SUssNEC', 'SUssPOP',
                              'SUPESss'])
    regiao = st.selectbox('Capacitação Desejada', ['SUNEsC','SUsPOP','SUPsS'])
    nomeDaCapacitacao = st.selectbox('Capacitação Desejada', ['SUNEssssC',
                                                              'SsssUsPOP',
                                                              'SsssUPsS'])
    st.text_input('Email')
    st.form_submit_button('CADASTRAR')