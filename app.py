import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ==============================================================================
# 1. CONFIGURAÇÕES DA INTERFACE E ANIMAÇÃO ALIENÍGENA PREMIUM (CSS + ANIMATIONS)
# ==============================================================================
st.set_page_config(
    page_title="ALIEN X-DATA | Matrix de Monitoramento", 
    page_icon="👽", 
    layout="wide"
)

# --- PAINEL LATERAL (ESTADO OPERACIONAL) ---
st.sidebar.markdown("""
    <h2 style='color: #39FF14; font-family: monospace; text-shadow: 0 0 12px #39FF14; margin-bottom: 0;'>🛸 CONTROL PANEL</h2>
    <span style='color: #64748B; font-family: monospace; font-size: 11px;'>STATUS: OPERACIONAL // CONEXÃO QUÂNTICA</span>
    <br><br>
""", unsafe_allow_html=True)

escopo = st.sidebar.radio(
    "Escopo do Varredura Espacial:",
    ["Monitoramento Mundial", "Monitoramento Brasil"]
)

# Inicialização de variáveis de filtragem avançada
filtrar_pais_especifico = "todos"
pais_selecionado_nome = "Todos os Paises"

if escopo == "Monitoramento Mundial":
    st.sidebar.markdown("<hr style='border-color: #8B5CF6;'>", unsafe_allow_html=True)
    st.sidebar.markdown("<h4 style='color: #8B5CF6; font-family: monospace; letter-spacing: 1px;'>🏳️ ISOLAMENTO GEOGRÁFICO</h4>", unsafe_allow_html=True)
    
    opcoes_paises = {
        "Todos os Países (Global)": "todos",
        "Estados Unidos (US)": "us",
        "Canadá (CA)": "ca",
        "Reino Unido (GB)": "gb",
        "Austrália (AU)": "au",
        "Alemanha (DE)": "de"
    }
    
    pais_selecionado_nome = st.sidebar.selectbox("Setor Planetário:", list(opcoes_paises.keys()))
    filtrar_pais_especifico = opcoes_paises[pais_selecionado_nome]

# Filtros Dinâmicos de Dados na Sidebar
st.sidebar.markdown("<hr style='border-color: #334155;'>", unsafe_allow_html=True)
st.sidebar.markdown("<h4 style='color: #94A3B8; font-family: monospace; letter-spacing: 1px;'>🎛️ FILTROS DE FREQUÊNCIA</h4>", unsafe_allow_html=True)

filtro_anos = st.sidebar.slider("Ciclos Temporais (Anos):", 1930, 2026, (1960, 2026))
filtro_duracao = st.sidebar.slider("Janela de Contato Máxima (Segundos):", 5, 7200, 3600)

# Definição Dinâmica de Cores do Ecossistema Alien baseado no escopo escolhido
if escopo == "Monitoramento Mundial":
    cor_alien = "#8B5CF6"          # Roxo Nebulosa
    cor_glow = "rgba(139, 92, 246, 0.4)"
else:
    cor_alien = "#39FF14"          # Verde Plasma
    cor_glow = "rgba(57, 255, 20, 0.4)"

# Injeção de CSS Customizado Avançado com Efeitos Holográficos
st.markdown(f"""
    <style>
    /* Mudança radical de fundo (Espaço Profundo com Imagem Atmosférica) */
    .stApp {{ 
        background-image: linear-gradient(rgba(5, 2, 15, 0.88), rgba(2, 4, 8, 0.96)), 
                          url('https://unsplash.com/pt-br/fotografias/azul-e-roxo-galaxia-papel-de-parede-digital-E0AHdsENmDg');
        background-size: cover !important;
        background-position: center !important;
        background-attachment: fixed !important;
        overflow-x: hidden;
    }}
    
    /* Configuração da Barra Lateral de Comando */
    [data-testid="stSidebar"] {{
        background-color: rgba(5, 8, 18, 0.9) !important;
        border-right: 1px solid {cor_alien} !important;
        box-shadow: 5px 0 15px rgba(0,0,0,0.5);
    }}
    
    /* ==========================================
       ANIMAÇÃO ORBITAL DOS OVNIS NA TELA
       ========================================== */
    .ufo-flyer-1, .ufo-flyer-2 {{
        position: fixed;
        pointer-events: none;
        z-index: 99999;
        font-size: 34px;
        opacity: 0.8;
        filter: drop-shadow(0 0 10px {cor_alien});
    }}
    
    .ufo-flyer-1 {{
        top: 20%;
        left: -100px;
        animation: vooHolograficoRapido 25s linear infinite;
    }}
    
    .ufo-flyer-2 {{
        top: 70%;
        left: -100px;
        animation: vooHolograficoLento 38s linear infinite;
        animation-delay: 6s;
    }}
    
    @keyframes vooHolograficoRapido {{
        0% {{ left: -100px; transform: translateY(0px) rotate(15deg); }}
        25% {{ transform: translateY(-30px) rotate(-10deg); }}
        50% {{ transform: translateY(20px) rotate(20deg); }}
        75% {{ transform: translateY(-15px) rotate(-5deg); }}
        100% {{ left: 110vw; transform: translateY(0px) rotate(15deg); }}
    }}
    
    @keyframes vooHolograficoLento {{
        0% {{ left: -100px; transform: translateY(0px) scale(0.7) rotate(-20deg); }}
        35% {{ transform: translateY(40px) scale(0.85) rotate(10deg); }}
        70% {{ transform: translateY(-35px) scale(0.7) rotate(-15deg); }}
        100% {{ left: 110vw; transform: translateY(0px) scale(0.7) rotate(-20deg); }}
    }}

    /* Cabeçalho do Terminal Central */
    .header-container {{
        background: rgba(4, 8, 20, 0.8);
        border: 2px solid {cor_alien};
        border-radius: 12px;
        padding: 30px;
        margin-bottom: 30px;
        box-shadow: 0 0 30px {cor_glow};
        backdrop-filter: blur(10px);
        text-align: center;
        position: relative;
    }}
    
    /* Indicador Pulsante Live */
    .live-indicator {{
        position: absolute;
        top: 15px;
        right: 20px;
        width: 10px;
        height: 10px;
        background-color: {cor_alien};
        border-radius: 50%;
        box-shadow: 0 0 10px {cor_alien};
        animation: pulsaSinal 1.5s infinite;
    }}
    @keyframes pulsaSinal {{
        0% {{ transform: scale(0.8); opacity: 0.5; }}
        50% {{ transform: scale(1.3); opacity: 1; }}
        100% {{ transform: scale(0.8); opacity: 0.5; }}
    }}
    
    .main-title {{ 
        font-family: 'Courier New', Courier, monospace; 
        font-size: 36px; 
        font-weight: 900; 
        color: #FFFFFF; 
        text-shadow: 0 0 15px {cor_alien};
        letter-spacing: 3px;
    }}
    .subtitle {{ 
        font-family: 'Courier New', Courier, monospace; 
        font-size: 13px; 
        color: #94A3B8; 
        margin-top: 8px;
        letter-spacing: 1px;
    }}
    
    /* Cartões de Telemetria Holográfica (KPIs) */
    .kpi-card {{
        background: rgba(3, 6, 14, 0.9);
        border: 1px dashed {cor_alien};
        padding: 22px;
        border-radius: 8px;
        text-align: center;
        backdrop-filter: blur(5px);
        box-shadow: inset 0 0 15px rgba(0,0,0,0.8);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .kpi-card:hover {{
        border-style: solid;
        transform: translateY(-4px);
        box-shadow: 0 8px 25px {cor_glow};
    }}
    .kpi-label {{ 
        font-family: 'Courier New', Courier, monospace; 
        font-size: 12px; 
        font-weight: bold; 
        color: #64748B; 
        letter-spacing: 2px;
    }}
    .kpi-value {{ 
        font-family: 'Courier New', Courier, monospace; 
        font-size: 34px; 
        font-weight: 900; 
        color: {cor_alien}; 
        margin-top: 5px;
        text-shadow: 0 0 10px {cor_alien};
    }}
    
    /* Abas em formato Command Shell */
    .stTabs [data-baseweb="tab-list"] {{ gap: 8px; background-color: transparent; }}
    .stTabs [data-baseweb="tab"] {{
        background-color: rgba(8, 12, 24, 0.6) !important;
        border: 1px solid #1E293B !important;
        border-radius: 4px 4px 0px 0px !important;
        padding: 12px 24px !important;
        font-family: 'Courier New', Courier, monospace !important;
        color: #64748B !important;
        font-weight: bold !important;
    }}
    .stTabs [aria-selected="true"] {{ 
        background-color: rgba(3, 6, 14, 0.95) !important;
        color: {cor_alien} !important; 
        border: 1px solid {cor_alien} !important;
        border-bottom: 1px solid transparent !important;
        box-shadow: 0 -4px 12px {cor_glow};
    }}
    
    hr {{ border-color: #1E293B; margin: 25px 0; }}
    .section-title {{ 
        font-family: 'Courier New', Courier, monospace; 
        font-size: 19px; 
        font-weight: bold; 
        color: #FFFFFF; 
        margin-bottom: 15px; 
        text-shadow: 0 0 6px {cor_alien};
    }}
    </style>

    <div class="ufo-flyer-1">🛸</div>
    <div class="ufo-flyer-2">🛸</div>
""", unsafe_allow_html=True)

# Configurações Avançadas e Corretas de Temas para Gráficos Matplotlib
plt.rcParams['figure.facecolor'] = '#03060E'  
plt.rcParams['axes.facecolor'] = (4/255, 8/255, 20/255, 0.5)    
plt.rcParams['text.color'] = '#FFFFFF'         
plt.rcParams['axes.labelcolor'] = '#94A3B8'    
plt.rcParams['xtick.color'] = '#64748B'       
plt.rcParams['ytick.color'] = '#64748B'       
plt.rcParams['axes.edgecolor'] = cor_alien     
plt.rcParams['grid.color'] = '#131B2E'
plt.rcParams['font.family'] = 'monospace'

# ==============================================================================
# 2. PIPELINE DE DATA ENGINEERING E EXTRAÇÃO
# ==============================================================================
@st.cache_data
def processar_pipeline_dados(modo_brasil, codigo_pais, anos_selecionados, max_duracao):
    df = pd.read_csv("ufo_sightings.csv", low_memory=False)
    
    # Saneamento e Limpeza Quântica
    df['ufo_shape'] = df['ufo_shape'].fillna('Não Identificado').astype(str).str.lower().str.strip()
    df['description'] = df['description'].fillna('').astype(str).str.lower()
    df['country'] = df['country'].fillna('outros').astype(str).str.lower().str.strip()
    
    df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
    df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
    
    # Tratamento de coordenadas geográficas baseadas no escopo
    if modo_brasil:
        df = df[
            (df['latitude'] <= 5.2) & (df['latitude'] >= -33.7) &
            (df['longitude'] <= -34.7) & (df['longitude'] >= -73.9)
        ].copy()
    else:
        df = df[(df['latitude'] >= -90) & (df['latitude'] <= 90)]
        df = df[(df['longitude'] >= -180) & (df['longitude'] <= 180)]
        if codigo_pais != "todos":
            df = df[df['country'] == codigo_pais].copy()
        
    # Filtro Dinâmico de Duração da Ocorrência
    df['encounter_length'] = pd.to_numeric(df['encounter_length'], errors='coerce')
    df = df[(df['encounter_length'] > 0) & (df['encounter_length'] <= max_duracao)]
    
    # Conversão Cronológica de Tempo
    df['date_time'] = pd.to_datetime(df['date_time'], errors='coerce')
    df = df.dropna(subset=['date_time'])
    
    df['ano'] = df['date_time'].dt.year
    df['mes'] = df['date_time'].dt.month
    df['hora'] = df['date_time'].dt.hour
    
    # Aplicação do Filtro Dinâmico de Anos passados pelo Slider da Sidebar
    df = df[(df['ano'] >= anos_selecionados[0]) & (df['ano'] <= anos_selecionados[1])]
    
    # Categorização Periódica Estelar
    def classificar_periodo(h):
        if 5 <= h < 12: return 'Matutino'
        elif 12 <= h < 18: return 'Vespertino'
        elif 18 <= h < 24: return 'Noturno'
        else: return 'Madrugada Recôndita'
    df['periodo_dia'] = df['hora'].apply(classificar_periodo)
    
    # Mineração Linguística Avançada
    df['contem_verde'] = df['description'].str.contains('green|verde', regex=True)
    df['contem_vermelho'] = df['description'].str.contains('red|vermelho', regex=True)
    df['contem_azul'] = df['description'].str.contains('blue|azul', regex=True)
    df['contem_barulho'] = df['description'].str.contains('sound|noise|barulho|zumbido|som', regex=True)
    df['contem_silencioso'] = df['description'].str.contains('silent|quiet|silencioso|silencio', regex=True)
    df['contem_rapido'] = df['description'].str.contains('fast|quick|rapido|velocidade|speed', regex=True)
    
    return df

opcao_brasil = (escopo == "Monitoramento Brasil")
try:
    df_dados = processar_pipeline_dados(opcao_brasil, filtrar_pais_especifico, filtro_anos, filtro_duracao)
except Exception as e:
    st.error(f"⚠️ FALHA CRÍTICA NA INTEGRALIDADE DA INTERCEPÇÃO: {e}")
    st.stop()

# ==============================================================================
# 3. RENDERIZAÇÃO E CONSTRUÇÃO INTERATIVA DOS RECURSOS
# ==============================================================================

if opcao_brasil:
    titulo_texto = "🛸 ALIEN DATA MATRIX: BRASIL SECTOR"
    sub_texto = f"[SCANNER]: Varredura de anomalias aéreas no Brasil entre {filtro_anos[0]} e {filtro_anos[1]}"
else:
    if filtrar_pais_especifico == "todos":
        titulo_texto = "🪐 TERRESTRIAL ARCHIVE INTERCEPT"
        sub_texto = f"[GLOBAL]: Captura massiva de registros na crosta da Terra ({filtro_anos[0]} - {filtro_anos[1]})"
    else:
        titulo_texto = f"📡 RECORTE DE FREQUÊNCIA: {pais_selecionado_nome.upper()}"
        sub_texto = f"[FEIXE SETORIAL]: Registro geolocalizado filtrado para a região de estudo"

st.markdown(f"""
    <div class="header-container">
        <div class="live-indicator"></div>
        <div class="main-title">{titulo_texto}</div>
        <div class="subtitle">{sub_texto}</div>
    </div>
""", unsafe_allow_html=True)

# Bloco Holográfico de Métricas Principais (KPIs)
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

with kpi_col1:
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">SINAIS IDENTIFICADOS</div>
            <div class="kpi-value">{df_dados.shape[0]:,}</div>
        </div>
    """, unsafe_allow_html=True)

with kpi_col2:
    if not df_dados.empty:
        formato_top = df_dados['ufo_shape'].mode()[0].upper()
        traducao_visual = {
            'LIGHT': 'EMISSÃO LUMINOSA', 'CIRCLE': 'GEOMETRIA CIRCULAR', 
            'TRIANGLE': 'VÉRTICE TRIANGULAR', 'SPHERE': 'MÓDULO ESFÉRICO', 
            'FIREBALL': 'NÚCLEO DE PLASMA', 'DISK': 'DIRETRIZ DISCOIDAL'
        }
        formato_exibir = traducao_visual.get(formato_top, formato_top)
    else:
        formato_exibir = "DESCONHECIDO"
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">PADRÃO MORFOLÓGICO</div>
            <div class="kpi-value" style="font-size: 20px; padding-top: 10px;">{formato_exibir}</div>
        </div>
    """, unsafe_allow_html=True)

with kpi_col3:
    mediana_tempo = f"{df_dados['encounter_length'].median():.1f}s" if not df_dados.empty else "0.0s"
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">MEDIANA DE CONTATO</div>
            <div class="kpi-value">{mediana_tempo}</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# Estrutura Organizacional de Abas Terminal Shell
aba_mapa, aba_temporal, aba_geometrica, aba_mineracao, aba_raw = st.tabs([
    "🛸 TELEMETRIA GEOGRÁFICA",
    "📈 LINHA DO TEMPO CRONOLÓGICA", 
    "📐 ANÁLISE MORFOLÓGICA ESPACIAL", 
    "🔍 ESPECTROMETRIA DE TEXTO",
    "💾 INTERCEPÇÃO DE REGISTROS BRUTOS"
])

with aba_mapa:
    st.markdown(f'<div class="section-title" style="color:{cor_alien};">⚡ Coordenadas Plotadas Via Satélite</div>', unsafe_allow_html=True)
    df_mapa = df_dados[['latitude', 'longitude']].dropna()
    if not df_mapa.empty:
        dados_plot = df_mapa.head(6000) if (not opcao_brasil and filtrar_pais_especifico == "todos") else df_mapa
        st.map(dados_plot)
    else:
        st.info("Nenhum feixe de coordenadas identificado dentro dos filtros atuais.")

with aba_temporal:
    st.markdown(f'<div class="section-title" style="color:{cor_alien};">⚡ Ciclos Rotacionais e Linhas Temporais Seculares</div>', unsafe_allow_html=True)
    if not df_dados.empty:
        fig1, ax1 = plt.subplots(1, 2, figsize=(16, 5))
        
        dados_periodo = df_dados['periodo_dia'].value_counts()
        ax1[0].pie(dados_periodo, labels=dados_periodo.index, autopct='%1.1f%%', startangle=90, 
                   colors=['#39FF14', '#8B5CF6', '#EC4899', '#06B6D4'], 
                   wedgeprops=dict(width=0.4, edgecolor='#03060E', linewidth=4))
        ax1[0].set_title('Incidência por Período Rotacional Terrestre', fontsize=12, fontweight='bold', pad=15)
        
        df_anos = df_dados.groupby('ano').size().reset_index(name='total')
        ax1[1].fill_between(df_anos['ano'], df_anos['total'], color=cor_alien, alpha=0.18)
        ax1[1].plot(df_anos['ano'], df_anos['total'], color=cor_alien, linewidth=3)
        ax1[1].set_title('Volume Histórico Interceptado na Janela Selecionada', fontsize=12, fontweight='bold', pad=15)
        ax1[1].grid(True, linestyle='--', alpha=0.08)
        
        st.pyplot(fig1)

with aba_geometrica:
    st.markdown(f'<div class="section-title" style="color:{cor_alien};">⚡ Classificação de Engenharia de Vetores e Matrizes</div>', unsafe_allow_html=True)
    if not df_dados.empty:
        fig2, ax2 = plt.subplots(1, 2, figsize=(16, 5))
        
        top_shapes = df_dados['ufo_shape'].value_counts().head(6)
        mapa_grafico = {'light': 'Luz Emitida', 'circle': 'Esfera/Disco', 'triangle': 'Delta Wing', 'fireball': 'Plasma Core', 'sphere': 'Orb Vector', 'disk': 'Nave Mãe'}
        indices_traduzidos = [mapa_grafico.get(x, x.upper()) for x in top_shapes.index]
        
        bars = ax2[0].barh(indices_traduzidos, top_shapes.values, color=cor_alien, edgecolor='#03060E', height=0.55)
        ax2[0].invert_yaxis()
        ax2[0].set_title('Morfologias Tecnológicas Mais Encontradas', fontsize=12, fontweight='bold', pad=15)
        ax2[0].grid(True, axis='x', linestyle='--', alpha=0.08)
        
        for bar in bars:
            width = bar.get_width()
            ax2[0].text(width + (width*0.01 if width > 0 else 0.1), bar.get_y() + bar.get_height()/2, f' {int(width):,}', 
                        va='center', ha='left', fontsize=9, color='#FFFFFF', fontweight='bold')

        df_corr = df_dados[['hora', 'mes', 'ano', 'encounter_length', 'latitude']].copy()
        df_corr.columns = ['Frequência', 'Mês', 'Ano', 'Duração', 'Vetor Lat']
        matriz_corr = df_corr.corr()
        mask = np.triu(np.ones_like(matriz_corr, dtype=bool))
        
        sns.heatmap(ax=ax2[1], data=matriz_corr, mask=mask, annot=True, fmt=".2f", 
                    cmap='Purples', cbar=False, square=True, vmin=-1, vmax=1,
                    annot_kws={"size": 10, "weight": "bold", "color": "#FFFFFF"})
        ax2[1].set_title('Matriz de Correlação Quântica de Variáveis', fontsize=12, fontweight='bold', pad=15)
        
        st.pyplot(fig2)

with aba_mineracao:
    st.markdown(f'<div class="section-title" style="color:{cor_alien};">⚡ Espectrometria de Linguagem de Depoimentos Criptografados</div>', unsafe_allow_html=True)
    if not df_dados.empty:
        fig3, ax3 = plt.subplots(1, 2, figsize=(16, 5))
        
        cores_contagem = {
            'Emissão Verde': df_dados['contem_verde'].sum(),
            'Emissão Vermelha': df_dados['contem_vermelho'].sum(),
            'Emissão Azul': df_dados['contem_azul'].sum()
        }
        ax3[0].bar(cores_contagem.keys(), cores_contagem.values(), color=['#39FF14', '#EF4444', '#00D2FF'], edgecolor='#03060E', width=0.45)
        ax3[0].set_title('Assinatura Dinâmica de Espectros de Luz', fontsize=12, fontweight='bold', pad=15)
        ax3[0].grid(True, axis='y', linestyle='--', alpha=0.08)
        
        # FIX DEFINITIVA: Variável instanciada em português 'comportamento_contagem'
        comportamento_contagem = {
            'Hiper Velocidade': df_dados['contem_rapido'].sum(),
            'Ruído Acústico': df_dados['contem_barulho'].sum(),
            'Propulsão Silenciosa': df_dados['contem_silencioso'].sum()
        }
        ax3[1].bar(comportamento_contagem.keys(), comportamento_contagem.values(), color='#8B5CF6', edgecolor='#03060E', width=0.45)
        ax3[1].set_title('Propriedades Operacionais de Motores', fontsize=12, fontweight='bold', pad=15)
        ax3[1].grid(True, axis='y', linestyle='--', alpha=0.08)
        
        st.pyplot(fig3)

with aba_raw:
    st.markdown(f'<div class="section-title" style="color:{cor_alien};">⚡ Registros Teleométricos Puros Filtrados (Database)</div>', unsafe_allow_html=True)
    st.markdown("Abaixo estão as linhas de logs originais descriptografadas prontas para análise textual direta:")
    
    if not df_dados.empty:
        colunas_desejadas = ['date_time', 'city', 'state', 'country', 'ufo_shape', 'encounter_length', 'description']
        colunas_existentes = [col for col in colunas_desejadas if col in df_dados.columns]
        
        st.dataframe(
            df_dados[colunas_existentes].head(500),
            use_container_width=True
        )
    else:
        st.info("Nenhum log disponível nos critérios de filtragem quântica atuais.")
