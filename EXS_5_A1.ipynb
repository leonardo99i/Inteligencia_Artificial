{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "private_outputs": true,
      "provenance": [],
      "authorship_tag": "ABX9TyNPmz+FlXTJ7Sao2n5XG3u4",
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
        "<a href=\"https://colab.research.google.com/github/leonardo99i/Inteligencia_Artificial/blob/main/EXS_5_A1.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "ey4X_LNGbxbK"
      },
      "outputs": [],
      "source": [
        "!pip install -U scikit-fuzzy"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install matplotlib"
      ],
      "metadata": {
        "id": "sHttyuXYb94d"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "import skfuzzy as fuzz\n",
        "from skfuzzy import control as ctrl"
      ],
      "metadata": {
        "id": "cjqpLMz5cB4W"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "if __name__==\"__main__\":\n",
        "  \n",
        "  #Trecho de definição de Variaveis de entrada\n",
        "  tempoJogo = ctrl.Antecedent(np.arange(0, 4, 1), \"Tempo de jogo\")\n",
        "  socialVida = ctrl.Antecedent(np.arange(1,3, 1), \"Afeta o estilo de vida/social\")\n",
        "  insonia = ctrl.Antecedent(np.arange(1,3, 1), \"Diminuição do tempo de sono\")\n",
        "  irritabilidade = ctrl.Antecedent(np.arange(0,5, 1), \"Irritabilidade\")\n",
        "\n",
        "  #Trecho de definição de Variavel de saida\n",
        "  gravidade = ctrl.Consequent(np.arange(0,10, 1), \"Gravidade do vicio em games\")\n",
        "\n",
        "  #Trecho de definição de Processo de fuzzificação\n",
        "  #tempo\n",
        "  tempoJogo['pouco'] = fuzz.trimf(tempoJogo.universe, [0, 1, 2])\n",
        "  tempoJogo['razoavel'] = fuzz.trimf(tempoJogo.universe, [1, 2, 3])\n",
        "  tempoJogo['muito'] = fuzz.trimf(tempoJogo.universe, [2,3,3])\n",
        "  #social\n",
        "  socialVida['sim'] = fuzz.trimf(socialVida.universe, [2,2,2])\n",
        "  socialVida['nao'] = fuzz.trimf(socialVida.universe, [1, 1,1])  \n",
        "  insonia['presente'] = fuzz.trimf(insonia.universe, [2, 2, 2])\n",
        "  insonia['ausente'] = fuzz.trimf(insonia.universe, [1, 1, 1])\n",
        "  #irritabilidade\n",
        "  irritabilidade['nenhuma'] = fuzz.trimf(irritabilidade.universe, [0, 1, 1])\n",
        "  irritabilidade['moderada'] = fuzz.trimf(irritabilidade.universe, [1, 2, 3])\n",
        "  irritabilidade['alta'] = fuzz.trimf(irritabilidade.universe, [2, 3, 4])\n",
        "  #gravidade\n",
        "  gravidade['leve'] = fuzz.trapmf(gravidade.universe, [0,0 ,4, 4])\n",
        "  gravidade['moderado'] = fuzz.trapmf(gravidade.universe, [4, 5, 6, 6])\n",
        "  gravidade['alta'] = fuzz.trapmf(gravidade.universe, [6, 7, 8, 8])\n",
        "  gravidade['grave'] = fuzz.trapmf(gravidade.universe, [8, 9, 10, 10])\n",
        "\n",
        "  #Trecho de definição das regras  \n",
        "  regra_1 = ctrl.Rule(tempoJogo['pouco'] & socialVida['nao'] & insonia['ausente'] & irritabilidade['nenhuma'], gravidade['leve'])\n",
        "  regra_2 = ctrl.Rule(tempoJogo['razoavel'] & socialVida['nao']& insonia['ausente']& irritabilidade['nenhuma'], gravidade['moderado'])\n",
        "  regra_3 = ctrl.Rule(tempoJogo['muito'] & socialVida['nao'] & insonia['ausente'] & irritabilidade['nenhuma'], gravidade['moderado'])\n",
        "  regra_36 = ctrl.Rule(tempoJogo['muito'] & socialVida['sim'] & insonia['presente'] & irritabilidade['alta'], gravidade['grave'])\n",
        "\n",
        "  #Trecho de definição de Regras\n",
        "  controleRisco = ctrl.ControlSystem([regra_1, regra_2, regra_3, regra_36])\n",
        "  simuladorRisco = ctrl.ControlSystemSimulation(controleRisco)\n",
        "  simuladorRisco.input['Tempo de jogo'] = 3\n",
        "  simuladorRisco.input['Afeta o estilo de vida/social'] = 2\n",
        "  simuladorRisco.input['Diminuição do tempo de sono'] = 2\n",
        "  simuladorRisco.input['Irritabilidade'] = 3\n",
        "\n",
        "  #Trecho de Impressão do gráfico\n",
        "  simuladorRisco.compute()\n",
        "  gravidade.view(sim=simuladorRisco)\n",
        "  plt.show()"
      ],
      "metadata": {
        "id": "IxxfLNK4cTHm"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}