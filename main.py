import streamlit as st
import pandas as pd


st.set_page_config(page_title="Finanças", page_icon='💰')

st.markdown("""
            
# Seja Bem-vindo
            
## APP Financeiro
            
            
    """)

#Widget de Upload de arquivos
file_upload=st.file_uploader(label="Faça Upload dos dados aqui", type=["csv"])

if file_upload:

    #Leitura dos dados
    df = pd.read_csv(file_upload)
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%Y", errors="coerce").dt.date
  

    #Exibição dos dados
    exp1 = st.expander('Dados Brutos')
    columns_fnt = {"Valor": st.column_config.NumberColumn("Valor",format="$%.2f")}
    exp1.dataframe(df, hide_index=True, column_config=columns_fnt)

    #Visão Instituição
    exp2 = st.expander('Instituições')
    df_instituicao = df.pivot_table(index="Data", columns="Instituição", values="Valor")
    
    tab_data, tab_history, tab_share = exp2.tabs(["Dados","Histórico","Distribuição"])

    with tab_data:
        st.dataframe(df_instituicao)

    with tab_history:
        st.line_chart(df_instituicao)

    with tab_share:

        date = st.selectbox("Filtro Data", options=df_instituicao.index)

        #Obtém a última data de dados
        last_dt = df_instituicao.sort_index().iloc[date]
        st.bar_chart(last_dt)

