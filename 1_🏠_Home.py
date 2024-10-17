import streamlit as st
import pandas as pd
from datetime import datetime
import webbrowser

st.set_page_config('Home', '🏠', 'wide')

# Verificando se os dados ja foram carregados 
if 'data' not in st.session_state:
    # Carrega o arquivo passando a coluna 0 como indice
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    
    # Filtra o DataFrame selecionando jogadores com contrato ativo
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]

    # Filtra o DataFrame selecionando jogadores com salarios registrados
    df_data = df_data[df_data['Value(£)'] > 0]

    # Organiza o DataFrame em ordem decrescente pela coluna 'Overall'
    df_data = df_data.sort_values(by='Overall', ascending=False)

    # Define o session_state
    st.session_state['data'] = df_data


# header
st.markdown('# DADOS OFFICIAIS FIFA23!!! ⚽')
st.sidebar.markdown('Desenvolvido por Gabriel Kempp https://github.com/Gabrielkempp/')

# Criando botao de acesso
# btn = st.button('Acesse os dados no Kaggle') # sem deploy
btn = st.link_button('Acesse os dados no Kaggle', "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data") # Com deploy

#if btn:
#    webbrowser.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

# Informacao sobre os dados
st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações 
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos 
    do jogador, características físicas, estatísticas de jogo, detalhes do contrato e 
    afiliações de clubes. 
    
    Com **mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para 
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários 
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de 
    desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e 
    desenvolvimento do jogador ao longo do tempo.
"""
)    