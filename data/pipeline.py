

import pandas as pd
import streamlit as st
from pathlib import Path


CSV_PATH = Path(__file__).parent.parent / "ufo_sightings.csv"




@st.cache_data
def carregar_e_processar(
    modo_brasil:       bool,
    codigo_pais:       str,
    anos_selecionados: tuple,
    max_duracao:       int,
) -> pd.DataFrame:

    df = pd.read_csv(CSV_PATH, low_memory=False)

    df = _limpar_colunas_texto(df)
    df = _converter_coordenadas(df)
    df = _filtrar_por_regiao(df, modo_brasil, codigo_pais)
    df = _filtrar_por_duracao(df, max_duracao)
    df = _processar_datas(df, anos_selecionados)
    df = _enriquecer_descricoes(df)

    return df



def _limpar_colunas_texto(df: pd.DataFrame) -> pd.DataFrame:

    df["ufo_shape"]   = df["ufo_shape"].fillna("nao identificado").astype(str).str.lower().str.strip()
    df["description"] = df["description"].fillna("").astype(str).str.lower()
    df["country"]     = df["country"].fillna("outros").astype(str).str.lower().str.strip()

    return df


def _converter_coordenadas(df: pd.DataFrame) -> pd.DataFrame:

    df["latitude"]  = pd.to_numeric(df["latitude"],  errors="coerce")
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

    return df


def _filtrar_por_regiao(df: pd.DataFrame, modo_brasil: bool, codigo_pais: str) -> pd.DataFrame:

    if modo_brasil:
        df = df[
            (df["latitude"]  <= 5.2)   & (df["latitude"]  >= -33.7) &
            (df["longitude"] <= -34.7) & (df["longitude"] >= -73.9)
        ].copy()
    else:
        df = df[(df["latitude"]  >= -90)  & (df["latitude"]  <= 90)]
        df = df[(df["longitude"] >= -180) & (df["longitude"] <= 180)]

        if codigo_pais != "todos":
            df = df[df["country"] == codigo_pais].copy()

    return df


def _filtrar_por_duracao(df: pd.DataFrame, max_duracao: int) -> pd.DataFrame:
  

    df["encounter_length"] = pd.to_numeric(df["encounter_length"], errors="coerce")
    df = df[df["encounter_length"].notna()]         
    df = df[df["encounter_length"] > 0]             
    df = df[df["encounter_length"] <= max_duracao]  

    return df


def _processar_datas(df: pd.DataFrame, anos_selecionados: tuple) -> pd.DataFrame:
  

    df["date_time"] = pd.to_datetime(df["date_time"], errors="coerce")
    df = df.dropna(subset=["date_time"])

    df["ano"]  = df["date_time"].dt.year
    df["mes"]  = df["date_time"].dt.month
    df["hora"] = df["date_time"].dt.hour

    df["periodo_dia"] = df["hora"].apply(_classificar_periodo)

    df = df[(df["ano"] >= anos_selecionados[0]) & (df["ano"] <= anos_selecionados[1])]

    return df


def _classificar_periodo(hora: int) -> str:

    if   5  <= hora < 12: return "Matutino"
    elif 12 <= hora < 18: return "Vespertino"
    elif 18 <= hora < 24: return "Noturno"
    else:                 return "Madrugada"


def _enriquecer_descricoes(df: pd.DataFrame) -> pd.DataFrame:

    palavras = {
        "contem_verde":      r"green|verde",
        "contem_vermelho":   r"red|vermelho",
        "contem_azul":       r"blue|azul",
        "contem_barulho":    r"sound|noise|barulho|zumbido|som",
        "contem_silencioso": r"silent|quiet|silencioso|silencio",
        "contem_rapido":     r"fast|quick|rapido|velocidade|speed",
    }

    for coluna, padrao in palavras.items():
        df[coluna] = df["description"].str.contains(padrao, regex=True, na=False)

    return df
