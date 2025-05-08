import streamlit as st
import webbrowser as wb
import pandas as pd
from datetime import datetime
from pathlib import Path

# dados
if "data" not in st.session_state:
    dir = Path('Dados')
    df_data = pd.read_csv(dir / "CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data.loc[(df_data["Contract Valid Until"] >= datetime.today().year) 
                          & (df_data["Value(£)"] > 0)
                          ]\
                        .sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data


# config
st.set_page_config(layout='wide')

# sidebar
st.sidebar.markdown('Demo por **Vetor 4**')

# conteudo
st.markdown('# ⚽ FIFA 2023')
st.markdown("""
FIFA 23 contará com diversos modos de jogo, são eles: Modo Carreira, Ultimate Team, Pro Clubs e Volta Football. \n
O jogo também será o primeiro da série a contar com a tecnologia de crossplay no lançamento. \n
Isto significa que jogadores de Xbox Series, PlayStation e Microsoft Windows poderão competir entre si.
            """)

bt_origem = st.button('Origem de Dados')
if bt_origem:
    wb.open_new_tab("https://www.kaggle.com")