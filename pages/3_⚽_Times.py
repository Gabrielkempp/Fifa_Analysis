import streamlit as st

# Configuracao da pagina
st.set_page_config('Times', '⚽', 'wide')

# Carrega o Session state 'data'
df_data = st.session_state['data']

# Filtra os clubes disponiveis 
clubes = df_data['Club'].unique()

# Define selectbox
club = st.sidebar.selectbox("Clube", clubes)

# Seta a coluna Name como index
df_filtered = df_data[df_data["Club"] == club].set_index('Name')

# Exibe foto do clube
st.image(df_filtered.iloc[0]['Club Logo'])

# Exibe nome do clube
st.markdown(f"## {club}")

# Colunas
columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

st.dataframe(df_filtered[columns], 
             column_config={
                "Age": st.column_config.Column('Idade'),
                "Value(£)": st.column_config.Column('Valor de mercado'),
                "Overall": st.column_config.ProgressColumn("Overall", format= '%d', min_value=0, max_value=100),
                "Wage(£)": st.column_config.ProgressColumn("Receita semanal", format= '£%f', min_value=0, max_value=df_filtered['Wage(£)'].max()),
                "Photo": st.column_config.ImageColumn('Foto'),
                "Flag": st.column_config.ImageColumn('País'),
                "Joined": st.column_config.Column('Entrada'),
                "Height(cm.)": st.column_config.Column('Altura(cm)'),
                "Weight(lbs.)": st.column_config.Column('Peso(lbs)'),
                "Contract Valid Until": st.column_config.Column('Validade do contrato', format= '%d'),
                "Release Clause(£)": st.column_config.Column('Recisão')
             })