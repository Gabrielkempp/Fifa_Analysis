import streamlit as st

# configuracao da pagina
st.set_page_config('Jogadores', '🏃‍♂️', 'wide')

# Carrega o Session state 'data'
df_data = st.session_state['data']

# Filtra os clubes disponiveis 
clubes = df_data['Club'].unique()

# Define selectbox
club = st.sidebar.selectbox("Clube", clubes)

# Seleciona os players comparando clubes com base na variavel club
df_players = df_data[df_data['Club'] == club]

# Filtra os jogadores disponiveis 
players = df_players['Name'].unique()

# Definindo selectbox
player = st.sidebar.selectbox("Jogador", players)

# Seleciona o jogador definido no selectbox
player_statistic = df_data[df_data['Name'] == player].iloc[0]

# Seleciona e exibe a imagem do jogador 
st.image(player_statistic['Photo'])

# Seleciona e exibe o nome do jogador
st.title(player_statistic['Name'])

# Selecion e exibe o Clube
st.markdown(f'Clube: **{player_statistic["Club"]}**')

# Definindo as colunas de informacoes
col1, col2, col3, col4 = st.columns(4)

col1.markdown(f'Posição: **{player_statistic["Position"]}**')
col2.markdown(f'Idade: **{player_statistic["Age"]}**')
col3.markdown(f'Altura: **{player_statistic["Height(cm.)"] / 100}**')
col4.markdown(f'Peso: **{player_statistic["Weight(lbs.)"] * 0.453:.2f}**')

# Insere linha divisora
st.divider()

# Exibe o Overall do jogador
st.subheader(f'Overall **{player_statistic['Overall']}**')

# Exibe a barra de progresso do Overall
st.progress(int(player_statistic['Overall']))

# Definindo as colunas de informacoes
col1, col2, col3= st.columns(3)

values = {}
values = {'Value': f"£: {player_statistic['Value(£)']:,}", 
          'Wage' : f"£: {player_statistic['Wage(£)']:,}",
          'Clause': f"£: {player_statistic['Release Clause(£)']:,}"}

for k, v in values.items():
    formatted_value = values[k].replace('.', 'x').replace(',', '.').replace('x', ',')
    values[k] = formatted_value

col1.metric('Valor de mercado', values['Value'])
col2.metric('Remuneração semanal', values['Wage'])
col3.metric('Cláusula de recisão', values['Clause'])