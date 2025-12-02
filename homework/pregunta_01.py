"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    import pandas as pd
    import matplotlib
    matplotlib.use('Agg')  # Backend sin interfaz gráfica
    import matplotlib.pyplot as plt
    import os

    # Obtener la ruta base del proyecto
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_dir = os.path.dirname(script_dir)

    # Cargar los datos
    df = pd.read_csv(os.path.join(base_dir, "files", "input", "news.csv"), index_col=0)

    # Crear la figura
    plt.Figure()

    colores = {"Television":"dimgray",
            "Newspaper":"grey",
            "Internet": "tab:blue",
            "Radio":"lightgrey"}

    orden = {"Television":1,
            "Newspaper":1,
            "Internet": 2,
            "Radio":1}

    grosor = {"Television":2,
            "Newspaper":2,
            "Internet": 3,
            "Radio":2}

    for i in df.columns:
        plt.plot(df[i],
                color = colores[i],
                zorder = orden[i],
                linewidth = grosor[i],
                label = i)
        
    for i in df.columns:
        first_year = df.index[0]
        plt.scatter(
            x = first_year,
            y = df[i].loc[first_year],
            color = colores[i],
            zorder = orden[i]
        )

    plt.text(
        first_year-0.2,
        df[i].loc[first_year],
        i + " "+str(df[i][first_year]) + "%",
        ha = "right",
        va = "center",
        color = colores[i])

    last_year = df.index[-1]
    plt.scatter(
        x = last_year,
        y = df[i].loc[last_year],
        color = colores[i],
        zorder = orden[i]
    )

    plt.text(
        last_year+0.2,
        df[i].loc[last_year],
        str(df[i][last_year]) + "%",
        ha = "left",
        va = "center",
        color = colores[i])  

    plt.xticks(
        ticks = df.index,
        labels = df.index,
        ha = "center"
    )  

    plt.title("How people get their news", fontsize=16)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)

    plt.title("How do people get their news?", fontsize=16)

    # Guardar la figura
    output_dir = os.path.join(base_dir, "files", "plots")
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(os.path.join(output_dir, "news.png"))
    plt.close()

pregunta_01()