import streamlit as st
import time 
import webbrowser as wb
import pandas as pd
import locale

# config 
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
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
clube = st.sidebar.selectbox("Clube", clubes)

df_jogadores = df_data[df_data['Club'] == clube]['Name'].unique()
jogadores = df_jogadores
jogador = st.sidebar.selectbox("Jogador", df_jogadores)


# select jogador
stats = df_data[df_data['Name']==jogador].iloc[0]

st.image(stats['Photo'])
st.title(stats['Name'])
st.markdown(f'**Clube:** {stats['Name']}')
st.markdown(f'**Posição:** {stats['Position']}')

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f'**Altura:** {stats['Height(cm.)']/100:.2f} m')
col2.markdown(f'**Idade:** {stats['Age']}')
col3.markdown(f'**Peso:** {int(stats['Weight(lbs.)']*0.453)} Kg')

st.divider()

st.subheader(f'Nota {stats['Overall']}')
st.progress(int(stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de Mercado", value=f'£ {locale.format_string("%.0f", stats["Value(£)"], grouping=True)}')
col2.metric(label="Remuneração Semanal", value=f'£ {locale.format_string("%.0f", stats["Wage(£)"], grouping=True)}')
col3.metric(label="Recisão", value=f'£ {locale.format_string("%.0f", stats["Release Clause(£)"], grouping=True)}')
