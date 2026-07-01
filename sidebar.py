

import streamlit as st
from config.tema  import CORES
from config.opcoes import (
    PAISES_DISPONIVEIS,
    ANO_MIN, ANO_MAX, ANO_PADRAO,
    DURACAO_MIN, DURACAO_MAX, DURACAO_PADRAO,
)


def renderizar_sidebar() -> dict:


    cor = CORES["laranja"]

    st.sidebar.markdown(f"""
        <div style="padding: 20px 0 12px;">
            <div style="font-family:'Space Grotesk',sans-serif; font-size:9px; font-weight:700;
                        letter-spacing:4px; text-transform:uppercase; color:{cor}; margin-bottom:6px;">
                Planet Express
            </div>
            <div style="font-family:'Orbitron',monospace; font-size:18px; font-weight:900;
                        color:#E8EDF5; letter-spacing:2px;">
                UFO.DATA
            </div>
            <div style="font-size:10px; color:{CORES['texto_muted']}; margin-top:4px;
                        letter-spacing:1px;">
                Base de dados · ~80.000 avistamentos
            </div>
        </div>
        <hr style="border-color:{CORES['borda']}; margin: 8px 0 20px;">
    """, unsafe_allow_html=True)

    # -- Escopo --
    st.sidebar.markdown(
        f"<div style='font-size:9px; font-weight:700; letter-spacing:3px; "
        f"text-transform:uppercase; color:{CORES['texto_muted']}; margin-bottom:8px;'>"
        f"Escopo</div>",
        unsafe_allow_html=True,
    )
    escopo = st.sidebar.radio(
        label="escopo",
        options=["Monitoramento Mundial", "Monitoramento Brasil"],
        label_visibility="collapsed",
    )

    codigo_pais = "todos"
    nome_pais   = "Todos os países"

    if escopo == "Monitoramento Mundial":
        st.sidebar.markdown("<hr style='border-color:#1A3455; margin:16px 0;'>", unsafe_allow_html=True)
        st.sidebar.markdown(
            f"<div style='font-size:9px; font-weight:700; letter-spacing:3px; "
            f"text-transform:uppercase; color:{CORES['texto_muted']}; margin-bottom:8px;'>"
            f"País</div>",
            unsafe_allow_html=True,
        )
        nome_pais   = st.sidebar.selectbox("país", list(PAISES_DISPONIVEIS.keys()), label_visibility="collapsed")
        codigo_pais = PAISES_DISPONIVEIS[nome_pais]

    st.sidebar.markdown("<hr style='border-color:#1A3455; margin:16px 0;'>", unsafe_allow_html=True)
    st.sidebar.markdown(
        f"<div style='font-size:9px; font-weight:700; letter-spacing:3px; "
        f"text-transform:uppercase; color:{CORES['texto_muted']}; margin-bottom:12px;'>"
        f"Filtros</div>",
        unsafe_allow_html=True,
    )

    filtro_anos = st.sidebar.slider(
        "Período (anos)",
        ANO_MIN, ANO_MAX, ANO_PADRAO,
    )


    filtro_duracao = st.sidebar.slider(
        "Duração máx. (segundos)",
        min_value=DURACAO_MIN,
        max_value=DURACAO_MAX,
        value=DURACAO_PADRAO,
        step=60,
        format="%d s",
    )

    st.sidebar.markdown("<hr style='border-color:#1A3455; margin:24px 0 8px;'>", unsafe_allow_html=True)
    st.sidebar.markdown(f"""
        <div style="padding:0 4px 16px;
                    font-size:9px; color:{CORES['texto_muted']}; letter-spacing:1px;">
            UFO Sightings Archive · Dados públicos<br>
            <span style="color:{cor};">PLANET EXPRESS</span> // NY 10009
        </div>
    """, unsafe_allow_html=True)

    return {
        "escopo":         escopo,
        "codigo_pais":    codigo_pais,
        "nome_pais":      nome_pais,
        "filtro_anos":    filtro_anos,
        "filtro_duracao": filtro_duracao,
    }
