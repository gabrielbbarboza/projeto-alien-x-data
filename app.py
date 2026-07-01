

import streamlit as st

from config.tema     import obter_cores, aplicar_tema_graficos
from data.pipeline   import carregar_e_processar
from ui.estilos      import injetar_css
from ui.sidebar      import renderizar_sidebar
from ui.componentes  import renderizar_header, renderizar_kpis, montar_titulo_pagina
from ui.abas         import aba_mapa, aba_temporal, aba_morfologica, aba_mineracao, aba_dados_brutos



st.set_page_config(
    page_title="UFO.DATA — Planet Express Archive",
    page_icon="assets/icon.png" if False else "🛸",
    layout="wide",
    initial_sidebar_state="expanded",
)



filtros     = renderizar_sidebar()
escopo      = filtros["escopo"]
codigo_pais = filtros["codigo_pais"]
nome_pais   = filtros["nome_pais"]
anos        = filtros["filtro_anos"]
duracao     = filtros["filtro_duracao"]
modo_brasil = escopo == "Monitoramento Brasil"



cores         = obter_cores(escopo)
cor_principal = cores["principal"]
cor_glow      = cores["glow"]

aplicar_tema_graficos(cor_principal)
injetar_css(cor_principal, cor_glow)



try:
    df = carregar_e_processar(modo_brasil, codigo_pais, anos, duracao)
except FileNotFoundError:
    st.error("Arquivo 'ufo_sightings.csv' não encontrado. Coloque-o na raiz do projeto.")
    st.stop()
except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
    st.stop()



titulo, subtitulo = montar_titulo_pagina(escopo, codigo_pais, nome_pais, anos)
renderizar_header(titulo, subtitulo, cor_principal)
renderizar_kpis(df, cor_principal)

st.markdown("<hr>", unsafe_allow_html=True)



aba1, aba2, aba3, aba4, aba5 = st.tabs([
    "Mapa geográfico",
    "Linha do tempo",
    "Morfologia",
    "Análise de texto",
    "Registros brutos",
])

with aba1: aba_mapa(df, cor_principal, modo_brasil, codigo_pais)
with aba2: aba_temporal(df, cor_principal)
with aba3: aba_morfologica(df, cor_principal)
with aba4: aba_mineracao(df, cor_principal)
with aba5: aba_dados_brutos(df, cor_principal)
