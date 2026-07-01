

import streamlit as st
from config.tema import CORES


def injetar_css(cor_principal: str, cor_glow: str) -> None:
    st.markdown(_css(cor_principal, cor_glow), unsafe_allow_html=True)
    st.markdown(_ovni_html(), unsafe_allow_html=True)




def _css(cor: str, glow: str) -> str:
    fundo       = CORES["fundo_app"]
    fundo_card  = CORES["fundo_card"]
    fundo_sb    = CORES["fundo_sidebar"]
    borda       = CORES["borda"]
    txt1        = CORES["texto_primario"]
    txt2        = CORES["texto_secundario"]
    txt_muted   = CORES["texto_muted"]

    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Space+Grotesk:wght@400;500;700&display=swap');

    /* ── FUNDO GERAL ── */
    .stApp {{
        background-color: {fundo} !important;
        background-image:
            radial-gradient(ellipse at 20% 10%, rgba(255,107,0,0.04) 0%, transparent 50%),
            radial-gradient(ellipse at 80% 80%, rgba(0,212,255,0.04) 0%, transparent 50%);
        font-family: 'Space Grotesk', sans-serif !important;
    }}

    /* ── SIDEBAR ── */
    [data-testid="stSidebar"] {{
        background-color: {fundo_sb} !important;
        border-right: 2px solid {cor} !important;
    }}
    [data-testid="stSidebar"] * {{
        font-family: 'Space Grotesk', sans-serif !important;
        color: {txt2} !important;
    }}
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {{
        color: {cor} !important;
    }}

    /* ── INPUTS / SLIDERS / RADIO ── */
    [data-testid="stSidebar"] .stRadio label,
    [data-testid="stSidebar"] .stSlider label {{
        color: {txt2} !important;
        font-size: 12px !important;
        font-weight: 600 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
    }}
    [data-testid="stSidebar"] .stSlider [data-baseweb="slider"] {{
        color: {cor} !important;
    }}
    div[data-baseweb="slider"] div[role="slider"] {{
        background-color: {cor} !important;
        border-color: {cor} !important;
    }}

    /* ── HEADER PRINCIPAL ── */
    .fu-header {{
        background: {fundo_card};
        border-top: 4px solid {cor};
        border-bottom: 1px solid {borda};
        padding: 28px 32px 22px;
        margin-bottom: 24px;
        position: relative;
    }}
    .fu-eyebrow {{
        font-family: 'Space Grotesk', monospace;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 4px;
        text-transform: uppercase;
        color: {cor};
        margin-bottom: 8px;
    }}
    .fu-title {{
        font-family: 'Orbitron', monospace;
        font-size: 28px;
        font-weight: 900;
        color: {txt1};
        letter-spacing: 2px;
        line-height: 1.1;
        margin-bottom: 6px;
    }}
    .fu-subtitle {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: 13px;
        color: {txt2};
        letter-spacing: 0.5px;
    }}
    .fu-live {{
        position: absolute;
        top: 24px;
        right: 28px;
        display: flex;
        align-items: center;
        gap: 7px;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: {txt_muted};
    }}
    .fu-live-dot {{
        width: 8px; height: 8px;
        border-radius: 50%;
        background: {cor};
        animation: fu-pulse 2s ease-in-out infinite;
    }}
    @keyframes fu-pulse {{
        0%, 100% {{ opacity: 0.4; transform: scale(0.9); }}
        50%       {{ opacity: 1;   transform: scale(1.1); }}
    }}

    /* ── CARDS DE KPI ── */
    .fu-kpi {{
        background: {fundo_card};
        border: 1px solid {borda};
        border-top: 3px solid {cor};
        padding: 18px 20px 16px;
    }}
    .fu-kpi-label {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 2.5px;
        text-transform: uppercase;
        color: {txt_muted};
        margin-bottom: 8px;
    }}
    .fu-kpi-value {{
        font-family: 'Orbitron', monospace;
        font-size: 30px;
        font-weight: 700;
        color: {cor};
        line-height: 1;
    }}
    .fu-kpi-value.sm {{
        font-size: 16px;
        padding-top: 6px;
        color: {txt1};
        font-family: 'Space Grotesk', sans-serif;
        font-weight: 700;
        letter-spacing: 1px;
    }}

    /* ── ABAS ── */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 0;
        background: {fundo_card};
        border-bottom: 2px solid {borda};
    }}
    .stTabs [data-baseweb="tab"] {{
        background: transparent !important;
        border: none !important;
        border-bottom: 2px solid transparent !important;
        border-radius: 0 !important;
        padding: 12px 20px !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-size: 11px !important;
        font-weight: 700 !important;
        letter-spacing: 1.5px !important;
        text-transform: uppercase !important;
        color: {txt_muted} !important;
        margin-bottom: -2px !important;
    }}
    .stTabs [aria-selected="true"] {{
        color: {cor} !important;
        border-bottom: 2px solid {cor} !important;
    }}

    /* ── PAINEL DE SEÇÃO ── */
    .fu-section-label {{
        font-family: 'Space Grotesk', sans-serif;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 3px;
        text-transform: uppercase;
        color: {txt_muted};
        border-left: 3px solid {cor};
        padding-left: 10px;
        margin-bottom: 16px;
        margin-top: 4px;
    }}

    /* ── DATAFRAME ── */
    [data-testid="stDataFrame"] {{
        border: 1px solid {borda} !important;
    }}

    /* ── OVNI ANIMADO ── */
    .fu-ovni {{
        position: fixed;
        pointer-events: none;
        z-index: 9999;
        font-size: 22px;
        opacity: 0.5;
        top: 15%;
        left: -80px;
        animation: fu-fly 30s linear infinite;
    }}
    @keyframes fu-fly {{
        0%   {{ left: -80px;  transform: translateY(0px); }}
        30%  {{ transform: translateY(-18px); }}
        60%  {{ transform: translateY(12px); }}
        100% {{ left: 105vw; transform: translateY(0px); }}
    }}

    hr {{ border-color: {borda}; margin: 20px 0; }}

    /* texto geral mais claro */
    .stApp p, .stApp span, .stApp div {{
        color: {txt1};
    }}
    </style>
    """


def _ovni_html() -> str:
    return '<div class="fu-ovni" aria-hidden="true">&#x1F6F8;</div>'
