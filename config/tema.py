

import matplotlib.pyplot as plt



CORES = {
    "fundo_app":      "#0A1628",   
    "fundo_card":     "#0F2040",   
    "fundo_sidebar":  "#081220",   
    "fundo_header":   "#061018",   

    "laranja":        "#FF6B00",   
    "laranja_escuro": "#CC5500",   

    "ciano":          "#00D4FF",  
    "verde":          "#39FF14",  

    
    "texto_primario":   "#E8EDF5",
    "texto_secundario": "#7BA3CC",
    "texto_muted":      "#3A5A7A",

    "borda":          "#1A3455",
    "borda_suave":    "#0F2040",
}


TEMA_ESCOPO = {
    "Monitoramento Mundial": {
        "principal": CORES["laranja"],
        "glow":      "rgba(255, 107, 0, 0.25)",
    },
    "Monitoramento Brasil": {
        "principal": CORES["ciano"],
        "glow":      "rgba(0, 212, 255, 0.25)",
    },
}


def obter_cores(escopo: str) -> dict:
    return TEMA_ESCOPO.get(escopo, TEMA_ESCOPO["Monitoramento Mundial"])



def aplicar_tema_graficos(cor_principal: str) -> None:

    plt.rcParams["figure.facecolor"]  = CORES["fundo_card"]
    plt.rcParams["axes.facecolor"]    = CORES["fundo_app"]
    plt.rcParams["text.color"]        = CORES["texto_primario"]
    plt.rcParams["axes.labelcolor"]   = CORES["texto_secundario"]
    plt.rcParams["xtick.color"]       = CORES["texto_muted"]
    plt.rcParams["ytick.color"]       = CORES["texto_muted"]
    plt.rcParams["axes.edgecolor"]    = CORES["borda"]
    plt.rcParams["grid.color"]        = CORES["borda_suave"]
    plt.rcParams["font.family"]       = "monospace"
    plt.rcParams["axes.spines.top"]   = False
    plt.rcParams["axes.spines.right"] = False



PALETA_GRAFICOS = [
    "#FF6B00",  # laranja
    "#00D4FF",  # ciano
    "#39FF14",  # verde
    "#FF2D78",  # rosa
    "#FFD700",  # amarelo
    "#BF5FFF",  # roxo
]

TRADUCAO_FORMATOS = {
    "light":    "Luz",
    "circle":   "Circular",
    "triangle": "Triangular",
    "fireball": "Bola de fogo",
    "sphere":   "Esférico",
    "disk":     "Discoidal",
}

TRADUCAO_KPI = {
    "LIGHT":    "Emissão luminosa",
    "CIRCLE":   "Circular",
    "TRIANGLE": "Triangular",
    "SPHERE":   "Esférico",
    "FIREBALL": "Bola de fogo",
    "DISK":     "Discoidal",
}
