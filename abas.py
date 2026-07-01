

import pandas as pd
import streamlit as st

from charts.graficos import grafico_temporal, grafico_morfologico, grafico_mineracao
from ui.componentes  import titulo_secao




def aba_mapa(df: pd.DataFrame, cor: str, modo_brasil: bool, filtrar_pais: str) -> None:

    titulo_secao("Coordenadas geográficas dos avistamentos")

    df_mapa = df[["latitude", "longitude"]].dropna()

    if df_mapa.empty:
        st.info("Nenhuma coordenada disponível para os filtros selecionados.")
        return

    if (not modo_brasil) and (filtrar_pais == "todos"):
        df_mapa = df_mapa.head(6_000)

    st.map(df_mapa)




def aba_temporal(df: pd.DataFrame, cor: str) -> None:

    titulo_secao("Distribuição temporal dos avistamentos")

    if df.empty:
        st.info("Sem dados para o período selecionado.")
        return

    st.pyplot(grafico_temporal(df, cor))




def aba_morfologica(df: pd.DataFrame, cor: str) -> None:

    titulo_secao("Classificação morfológica dos objetos")

    if df.empty:
        st.info("Sem dados para análise morfológica.")
        return

    st.pyplot(grafico_morfologico(df, cor))




def aba_mineracao(df: pd.DataFrame, cor: str) -> None:

    titulo_secao("Análise de texto — descrições dos avistamentos")

    if df.empty:
        st.info("Sem descrições para analisar.")
        return

    st.pyplot(grafico_mineracao(df))



def aba_dados_brutos(df: pd.DataFrame, cor: str) -> None:

    titulo_secao("Registros brutos filtrados")

    st.caption(f"{min(len(df), 500):,} de {len(df):,} registros exibidos")

    if df.empty:
        st.info("Nenhum registro disponível.")
        return

    colunas_desejadas  = ["date_time", "city", "state", "country",
                          "ufo_shape", "encounter_length", "description"]
    colunas_existentes = [c for c in colunas_desejadas if c in df.columns]

    st.dataframe(df[colunas_existentes].head(500), use_container_width=True)
