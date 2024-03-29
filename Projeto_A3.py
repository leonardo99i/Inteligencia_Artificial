{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "private_outputs": true,
      "provenance": [],
      "authorship_tag": "ABX9TyPinq/Uf/1augJx5zEiel3c",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/leonardo99i/Inteligencia_Artificial/blob/main/Projeto_A3.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%pip install seaborn\n",
        "%pip install missingno\n",
        "%pip install -U scikit-learn\n",
        "%pip install -U sklearn\n",
        "%pip install scikit-plot\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')"
      ],
      "metadata": {
        "id": "ll_eqgzD92ti"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ICZQSZe9rqTL"
      },
      "outputs": [],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive/')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np"
      ],
      "metadata": {
        "id": "YMyjfD2Vw8Kp"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv('/content/drive/My Drive/IA/water_potability.csv')\n",
        "df"
      ],
      "metadata": {
        "id": "HctHRHVrxJkd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.info()"
      ],
      "metadata": {
        "id": "t6ftp8p0yKYR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.describe()"
      ],
      "metadata": {
        "id": "zlBM8DDpyc2W"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.isnull().sum()"
      ],
      "metadata": {
        "id": "BHPWOARyygHh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df['ph'].fillna(df['ph'].mean(), inplace = True)\n",
        "df['Sulfate'].fillna(df['Sulfate'].mean(), inplace = True)\n",
        "df['Trihalomethanes'].fillna(df['Trihalomethanes'].mean(), inplace = True)\n",
        "df.isnull().sum()\n"
      ],
      "metadata": {
        "id": "-wv_M08gylI1"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Potabilidade\n",
        "import seaborn as sns\n",
        "sns.countplot(data = df, x = 'Potability')"
      ],
      "metadata": {
        "id": "FKG8DVgiy_jr"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df.columns"
      ],
      "metadata": {
        "id": "F_WiLjRS08XV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Criando Outliers\n"
      ],
      "metadata": {
        "id": "pqEpZ7gI2L2a"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "import warnings\n",
        "warnings.filterwarnings('ignore')\n",
        "\n",
        "#Outlier do PH\n",
        "ph_baixo = np.percentile(df['ph'], [1])\n",
        "ph_alto = np.percentile(df['ph'], [99])\n",
        "df['ph'] [df['ph'].values < ph_baixo] = ph_baixo\n",
        "df['ph'] [df['ph'].values > ph_alto] = ph_alto\n",
        "\n",
        "#Outlier do Hardness\n",
        "hard_baixo = np.percentile(df['Hardness'], [1])\n",
        "hard_alto = np.percentile(df['Hardness'], [99])\n",
        "df['Hardness'] [df['Hardness'].values < hard_baixo] = hard_baixo\n",
        "df['Hardness'] [df['Hardness'].values > hard_alto] = hard_alto\n",
        "\n",
        "#Outlier do Solids\n",
        "solid_baixo = np.percentile(df['Solids'], [1])\n",
        "solid_alto = np.percentile(df['Solids'], [99])\n",
        "df['Solids'][df['Solids'].values < solid_baixo] = solid_baixo\n",
        "df['Solids'][df['Solids'].values > solid_alto] = solid_alto\n",
        "\n",
        "#Outlier do Chloramines\n",
        "chloramine_baixo = np.percentile(df['Chloramines'], [1])\n",
        "chloramine_alto = np.percentile(df['Chloramines'], [99])\n",
        "df['Chloramines'][df['Chloramines'].values < chloramine_baixo] = chloramine_baixo\n",
        "df['Chloramines'][df['Chloramines'].values > chloramine_alto] = chloramine_alto\n",
        "\n",
        "#Outlier do Sulfato\n",
        "sulfato_baixo = np.percentile(df['Sulfate'], [1])\n",
        "sulfato_alto = np.percentile(df['Sulfate'], [99])\n",
        "df['Sulfate'][df['Sulfate'].values < sulfato_baixo] = sulfato_baixo\n",
        "df['Sulfate'][df['Sulfate'].values > sulfato_alto] = sulfato_alto\n",
        "\n",
        "#Outlier carbono\n",
        "carbono_baixo = np.percentile(df['Organic_carbon'], [1])\n",
        "carbono_alto = np.percentile(df['Organic_carbon'], [99])\n",
        "df['Organic_carbon'][df['Organic_carbon'].values < carbono_baixo] = carbono_baixo\n",
        "df['Organic_carbon'][df['Organic_carbon'].values > carbono_alto] = carbono_alto\n",
        "\n",
        "#Outlier Trihalomethanes\n",
        "tri_baixo = np.percentile(df['Trihalomethanes'], [1])\n",
        "tri_alto = np.percentile(df['Trihalomethanes'], [99])\n",
        "df['Trihalomethanes'][df['Trihalomethanes'].values < tri_baixo] = tri_baixo\n",
        "df['Trihalomethanes'][df['Trihalomethanes'].values > tri_alto] = tri_alto\n",
        "\n",
        "#Outlier de Turbilidade\n",
        "turbi_baixo = np.percentile(df['Turbidity'], [1])\n",
        "turbi_alto = np.percentile(df['Turbidity'], [99])\n",
        "df['Turbidity'][df['Turbidity'].values < turbi_baixo] = turbi_baixo\n",
        "df['Turbidity'][df['Turbidity'].values > turbi_alto] = turbi_alto\n",
        "\n",
        "plt.figure(figsize = (15,10), tight_layout = True)\n",
        "for i, feature in enumerate(df.columns):\n",
        "    if feature != 'Potability':\n",
        "        plt.subplot(3,3,i+1)\n",
        "        sns.boxplot(data = df, x =feature)"
      ],
      "metadata": {
        "id": "kTzC13lN1Fz9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "nao_potevel = df.query(\"Potability == 0\")\n",
        "potavel = df.query(\"Potability == 1\")\n",
        "\n",
        "plt.figure(figsize = (15,15))\n",
        "for ax, col in enumerate(df.columns[:9]):\n",
        "    plt.subplot(3,3, ax + 1)\n",
        "    plt.title(col)\n",
        "    sns.kdeplot(x = nao_potevel[col], label = \"Não é Potável\")\n",
        "    sns.kdeplot(x = potavel[col], label = \"Potável\")\n",
        "    plt.legend()\n",
        "plt.tight_layout()"
      ],
      "metadata": {
        "id": "iFOKD373-tHX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Distribuição do PH\n",
        "import plotly.express as px\n",
        "fig=px.histogram(df,x=\"ph\",nbins=30,color_discrete_sequence=[\"#0000ff\"],title=\"<b>Distribuição do PH\",text_auto=True)\n",
        "fig.show()"
      ],
      "metadata": {
        "id": "gH_LZZLXIG1J"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Distribuição do Dureza\n",
        "import plotly.express as px\n",
        "fig=px.histogram(df,x=\"Hardness\",nbins=30,color_discrete_sequence=[\"#0000ff\"],title=\"<b>Distribuição do Dureza\",text_auto=True)\n",
        "fig.show()"
      ],
      "metadata": {
        "id": "g3ku9QudKcmv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Distribuição do Solidos\n",
        "import plotly.express as px\n",
        "fig=px.histogram(df,x=\"Solids\",nbins=30,color_discrete_sequence=[\"#0000ff\"],title=\"<b>Distribuição de Solidos\",text_auto=True)\n",
        "fig.show()"
      ],
      "metadata": {
        "id": "6Q57abt8Ko_j"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Distribuição do Cloro\n",
        "import plotly.express as px\n",
        "fig=px.histogram(df,x=\"Chloramines\",nbins=30,color_discrete_sequence=[\"#0000ff\"],title=\"<b>Distribuição do Cloro\",text_auto=True)\n",
        "fig.show()"
      ],
      "metadata": {
        "id": "au3m_IMBKymi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Distribuição do Sulfato\n",
        "import plotly.express as px\n",
        "fig=px.histogram(df,x=\"Sulfate\",nbins=30,color_discrete_sequence=[\"#0000ff\"],title=\"<b>Distribuição de Sulfato\",text_auto=True)\n",
        "fig.show()"
      ],
      "metadata": {
        "id": "2jxG6czmLHq6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Distribuição do Condutividade\n",
        "import plotly.express as px\n",
        "fig=px.histogram(df,x=\"Conductivity\",nbins=30,color_discrete_sequence=[\"#0000ff\"],title=\"<b>Distribuição de Condutividae\",text_auto=True)\n",
        "fig.show()"
      ],
      "metadata": {
        "id": "AjTHvUCBLPJG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Distribuição do Carbono Organico\n",
        "import plotly.express as px\n",
        "fig=px.histogram(df,x=\"Organic_carbon\",nbins=30,color_discrete_sequence=[\"#0000ff\"],title=\"<b>Distribuição de Carbono Organico\",text_auto=True)\n",
        "fig.show()"
      ],
      "metadata": {
        "id": "AxImjJyQLpsj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Distribuição do Trihalometanos\n",
        "import plotly.express as px\n",
        "fig=px.histogram(df,x=\"Trihalomethanes\",nbins=30,color_discrete_sequence=[\"#0000ff\"],title=\"<b>Distribuição de Trihalometanos\",text_auto=True)\n",
        "fig.show()"
      ],
      "metadata": {
        "id": "W3fsKQGKMIJQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Distribuição do Turbidez\n",
        "import plotly.express as px\n",
        "fig=px.histogram(df,x=\"Turbidity\",nbins=30,color_discrete_sequence=[\"#0000ff\"],title=\"<b>Distribuição de Turbidez\",text_auto=True)\n",
        "fig.show()"
      ],
      "metadata": {
        "id": "14sZ0tI4MVEU"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}