import streamlit as st

def show_cadastro(adicionar_cliente):
    with st.form('capacitacao', clear_on_submit=False, border=True):
        nome = st.text_input('Nome completo')
        matricula = st.text_input('Matricula')
        setor = st.selectbox('Selecione o Setor', ['SUNEC', 'SUPOP', 'SUPES'])
        diretoria = st.selectbox('Selecione a Diretoria', 
                                 ['SUssNEC', 'SUssPOP', 'SUPESss'])
        regiao = st.selectbox('Capacitação Desejada', ['SUNEsC', 'SUsPOP', 'SUPsS'])
        nomeDaCapacitacao = st.selectbox('Capacitação Desejada', ['SUNEssssC',
                                                                  'SsssUsPOP',
                                                                  'SsssUPsS'])
        email = st.text_input('Email')
        
        if st.form_submit_button('CADASTRAR'):
            adicionar_cliente(nome, matricula, setor, diretoria, regiao, nomeDaCapacitacao, email)
            st.success('Cadastro realizado com sucesso!')
