

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

from config.tema import CORES, PALETA_GRAFICOS, TRADUCAO_FORMATOS



def grafico_temporal(df: pd.DataFrame, cor: str) -> plt.Figure:
  

    fig, (ax_pizza, ax_linha) = plt.subplots(1, 2, figsize=(15, 4.5))

    dados_periodo = df["periodo_dia"].value_counts()
    wedge_props   = dict(width=0.45, edgecolor=CORES["fundo_app"], linewidth=3)

    ax_pizza.pie(
        dados_periodo,
        labels=dados_periodo.index,
        autopct="%1.0f%%",
        startangle=90,
        colors=PALETA_GRAFICOS[:len(dados_periodo)],
        wedgeprops=wedge_props,
        textprops={"fontsize": 11, "color": CORES["texto_primario"]},
    )
    ax_pizza.set_title(
        "Período do dia",
        fontsize=12, fontweight="bold", pad=14,
        color=CORES["texto_primario"],
    )

    df_anos = df.groupby("ano").size().reset_index(name="total")
    ax_linha.fill_between(df_anos["ano"], df_anos["total"], color=cor, alpha=0.12)
    ax_linha.plot(df_anos["ano"], df_anos["total"], color=cor, linewidth=2.5)
    ax_linha.set_title(
        "Volume histórico de avistamentos",
        fontsize=12, fontweight="bold", pad=14,
        color=CORES["texto_primario"],
    )
    ax_linha.grid(True, linestyle="--", alpha=0.1)
    ax_linha.set_xlabel("Ano", fontsize=10)
    ax_linha.set_ylabel("Avistamentos", fontsize=10)

    fig.tight_layout(pad=2)
    return fig




def grafico_morfologico(df: pd.DataFrame, cor: str) -> plt.Figure:


    fig, (ax_barras, ax_heat) = plt.subplots(1, 2, figsize=(15, 4.5))

    top_shapes = df["ufo_shape"].value_counts().head(6)
    labels     = [TRADUCAO_FORMATOS.get(x, x.capitalize()) for x in top_shapes.index]
    cores_barras = PALETA_GRAFICOS[:len(top_shapes)]

    bars = ax_barras.barh(labels, top_shapes.values, color=cores_barras,
                          edgecolor=CORES["fundo_app"], height=0.6)
    ax_barras.invert_yaxis()
    ax_barras.set_title("Formatos mais reportados", fontsize=12,
                         fontweight="bold", pad=14, color=CORES["texto_primario"])
    ax_barras.grid(True, axis="x", linestyle="--", alpha=0.1)

    for bar in bars:
        w = bar.get_width()
        ax_barras.text(
            w * 1.01, bar.get_y() + bar.get_height() / 2,
            f"{int(w):,}",
            va="center", ha="left", fontsize=9,
            color=CORES["texto_primario"], fontweight="bold",
        )

    df_corr = df[["hora", "mes", "ano", "encounter_length", "latitude"]].copy()
    df_corr.columns = ["Hora", "Mês", "Ano", "Duração", "Latitude"]

    matriz_corr = df_corr.corr(numeric_only=True)

    mask = np.triu(np.ones_like(matriz_corr).astype(bool))

    sns.heatmap(
        ax=ax_heat,
        data=matriz_corr,
        mask=mask,
        annot=True, fmt=".2f",
        cmap="Blues", cbar=False, square=True,
        vmin=-1, vmax=1,
        annot_kws={"size": 10, "weight": "bold", "color": CORES["texto_primario"]},
    )
    ax_heat.set_title("Correlação entre variáveis", fontsize=12,
                       fontweight="bold", pad=14, color=CORES["texto_primario"])

    fig.tight_layout(pad=2)
    return fig



def grafico_mineracao(df: pd.DataFrame) -> plt.Figure:
   

    fig, (ax_cores, ax_comp) = plt.subplots(1, 2, figsize=(15, 4.5))

    dados_cores = {
        "Verde":    df["contem_verde"].sum(),
        "Vermelho": df["contem_vermelho"].sum(),
        "Azul":     df["contem_azul"].sum(),
    }
    cores_barras = ["#39FF14", "#FF4444", "#00D4FF"]
    ax_cores.bar(
        dados_cores.keys(), dados_cores.values(),
        color=cores_barras, edgecolor=CORES["fundo_app"], width=0.5,
    )
    ax_cores.set_title("Cores mencionadas nas descrições", fontsize=12,
                        fontweight="bold", pad=14, color=CORES["texto_primario"])
    ax_cores.grid(True, axis="y", linestyle="--", alpha=0.1)

    dados_comp = {
        "Alta velocidade":  df["contem_rapido"].sum(),
        "Ruído":            df["contem_barulho"].sum(),
        "Silencioso":       df["contem_silencioso"].sum(),
    }
    ax_comp.bar(
        dados_comp.keys(), dados_comp.values(),
        color=CORES["laranja"], edgecolor=CORES["fundo_app"], width=0.5,
    )
    ax_comp.set_title("Comportamentos reportados", fontsize=12,
                       fontweight="bold", pad=14, color=CORES["texto_primario"])
    ax_comp.grid(True, axis="y", linestyle="--", alpha=0.1)

    fig.tight_layout(pad=2)
    return fig
