

import pandas as pd
import streamlit as st
from typing import Tuple

from config.tema import CORES, TRADUCAO_KPI


def renderizar_header(titulo: str, subtitulo: str, cor: str) -> None:

    st.markdown(f"""
        <div class="fu-header">
            <div class="fu-live">
                <div class="fu-live-dot"></div>
                ao vivo
            </div>
            <div class="fu-eyebrow">Planet Express UFO Archive</div>
            <div class="fu-title">{titulo}</div>
            <div class="fu-subtitle">{subtitulo}</div>
        </div>
    """, unsafe_allow_html=True)


def renderizar_kpis(df: pd.DataFrame, cor: str) -> None:


    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
            <div class="fu-kpi">
                <div class="fu-kpi-label">Registros encontrados</div>
                <div class="fu-kpi-value">{df.shape[0]:,}</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        if not df.empty:
            top       = df["ufo_shape"].mode()[0].upper()
            label_fmt = TRADUCAO_KPI.get(top, top.capitalize())
        else:
            label_fmt = "—"

        st.markdown(f"""
            <div class="fu-kpi" style="border-top-color:{CORES['ciano']}">
                <div class="fu-kpi-label">Formato predominante</div>
                <div class="fu-kpi-value sm">{label_fmt}</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        mediana = f"{df['encounter_length'].median():.0f}s" if not df.empty else "—"
        st.markdown(f"""
            <div class="fu-kpi" style="border-top-color:{CORES['verde']}">
                <div class="fu-kpi-label">Mediana de duração</div>
                <div class="fu-kpi-value" style="color:{CORES['verde']}">{mediana}</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)


def titulo_secao(texto: str) -> None:

    st.markdown(
        f'<div class="fu-section-label">{texto}</div>',
        unsafe_allow_html=True,
    )


def montar_titulo_pagina(
    escopo: str,
    filtrar_pais: str,
    nome_pais: str,
    filtro_anos: tuple,
) -> Tuple[str, str]:

    ano_i, ano_f = filtro_anos

    if escopo == "Monitoramento Brasil":
        titulo    = "Brasil — Avistamentos"
        subtitulo = f"Registros no território brasileiro entre {ano_i} e {ano_f}"

    elif filtrar_pais == "todos":
        titulo    = "Arquivo Global"
        subtitulo = f"Todos os avistamentos registrados de {ano_i} a {ano_f}"

    else:
        titulo    = nome_pais.split("(")[0].strip()
        subtitulo = f"Registros filtrados para {nome_pais} — {ano_i} a {ano_f}"

    return titulo, subtitulo
