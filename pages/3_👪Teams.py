import streamlit as st
import webbrowser as wb
import pandas as pd

# config 
st.set_page_config(layout='wide')

# dados 
if "data" in st.session_state:
    df_data = st.session_state["data"]
else:
    st.markdown('### Erro ao carregar dados. Página ininial incorreta.')
    st.switch_page("1_🏠Home.py")
    st.stop()



# filtros
clubes = df_data["Club"].unique()
clubes = list(["-"]) + list(clubes)
clube = st.sidebar.selectbox("Clube", clubes)
jogadorBusca = st.sidebar.text_input("Pesquisar Jogador", placeholder="Digite o nome do jogador")


indClubeSelecionado = clube != "-"
if indClubeSelecionado:
    df_clube = df_data[(df_data['Club'] == clube) & (df_data['Name'].str.contains(jogadorBusca, case=False))]
    # corpo
    if not df_clube.empty:
        st.image(df_clube['Club Logo'].values[0])
        st.markdown(f'## {clube}')
else:
    df_clube = df_data[(df_data['Name'].str.contains(jogadorBusca, case=False))]


# Dados do clube
colunas = ['Name', 'Age', 'Photo', "Flag", 'Overall',
            'Value(£)','Height(cm.)', 'Weight(lbs.)',  'Wage(£)',
            'Joined', 'Contract Valid Until',
            'Release Clause(£)'
            ]
colunasTime = ['Club', 'Club Logo']
if not indClubeSelecionado:
    colunas = colunasTime + colunas

df_jogadores = df_clube[colunas]
if df_jogadores.empty:
    st.markdown('### Jogador não encontrado')
    st.stop()
else:
    nclub = len(df_clube['Club'].unique())
    njog = len(df_clube)
    st.markdown(f'### {nclub} Times e {njog} Jogadores listados')

st.dataframe(df_jogadores,
             height=600,
             column_config={
                'Idade': st.column_config.NumberColumn(
                    format="£ %d",
                    help="Idade"
                ),
                'Club Logo': st.column_config.ImageColumn(
                    'Logo',
                    
                ),
                'Photo': st.column_config.ImageColumn(
                    'Foto'
                ),
                'Flag': st.column_config.ImageColumn(
                    'Nacionalidade',
                ),
                'Overall': st.column_config.ProgressColumn(
                    "Nota Geral",
                    min_value=0,
                    max_value=100,
                    format="%d", # inteiro
                    help="Nota geral do jogador"
                ),
                'Value(£)': st.column_config.NumberColumn(
                    'Valor de Mercado',
                    format="localized",
                    help="Valor de mercado do jogador"
                ),
                'Wage(£)': st.column_config.ProgressColumn(
                    'Remuneração Semanal',
                    min_value=0,
                    max_value=df_jogadores['Wage(£)'].max(),
                    format="localized",
                    help="Remuneração semanal do jogador"
                ),
                'Release Clause(£)': st.column_config.ProgressColumn(
                    'Recisão',
                    min_value=0,
                    max_value=df_jogadores['Release Clause(£)'].max(),
                    format="localized",
                    help="Remuneração semanal do jogador"
                ),
             }
             )

