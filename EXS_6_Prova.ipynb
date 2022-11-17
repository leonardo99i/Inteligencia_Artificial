{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "private_outputs": true,
      "provenance": [],
      "authorship_tag": "ABX9TyNDTq3r5gQjsilQYuhYlEbv",
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
        "<a href=\"https://colab.research.google.com/github/leonardo99i/Inteligencia_Artificial/blob/main/EXS_6_Prova.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "atributos = ['comprimentoSepala', 'larguraSepala', 'comprimentoPetala', 'largulaPetala', 'classe']\n",
        "df = pd.read_table('/IrisData.txt', names=atributos, delimiter = ',')\n",
        "\n",
        "# Definimos uma matriz \"X\" com as caracteristicas que representam uma flor Iris.\n",
        "X = df[df.columns.difference(['classe'])].values\n",
        "\n",
        "# E um vetor \"y\" com das classes de cada uma das flores.\n",
        "y = df['classe'].values\n",
        "\n",
        "display(X)\n",
        "display(y)"
      ],
      "metadata": {
        "id": "b3Q3Lx3ksqAh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_table('/IrisData.txt', names=atributos, delimiter = ',')\n",
        "display(df)"
      ],
      "metadata": {
        "id": "ozbW4JyDucuy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np \n",
        "import pandas as pd\n",
        "from sklearn.neighbors import KNeighborsClassifier\n",
        "from sklearn.model_selection import train_test_split  \n",
        "from sklearn import metrics\n",
        "\n",
        "names = ['comprimentoSepala', 'larguraSepala', 'comprimentoPetala', 'largulaPetala', 'classe']\n",
        "\n",
        "# Ler o dataSet com as informaçoes\n",
        "df = pd.read_table('/IrisData.txt', names=atributos, delimiter = ',')\n",
        "X = df.iloc[:, :-1]  \n",
        "y = df.iloc[:, -1]\n",
        "print(X.head())\n",
        "Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.10) \n",
        "\n",
        "classifier = KNeighborsClassifier(n_neighbors=5).fit(Xtrain, ytrain) \n",
        "\n",
        "ypred = classifier.predict(Xtest)\n",
        "\n",
        "i = 0\n",
        "print (\"\\n-------------------------------------------------------------------------\")\n",
        "print ('%-25s %-25s %-25s' % ('Original', 'preditiva', 'Correto/Errado'))\n",
        "print (\"-------------------------------------------------------------------------\")\n",
        "for label in ytest:\n",
        "    print ('%-25s %-25s' % (label, ypred[i]), end=\"\")\n",
        "    if (label == ypred[i]):\n",
        "        print (' %-25s' % ('Correto'))\n",
        "    else:\n",
        "        print (' %-25s' % ('Errado'))\n",
        "    i = i + 1\n",
        "print (\"-------------------------------------------------------------------------\")\n",
        "print(\"\\nFuzzy:\\n\",metrics.confusion_matrix(ytest, ypred))  \n",
        "print (\"-------------------------------------------------------------------------\")\n",
        "print(\"\\nClassificação:\\n\",metrics.classification_report(ytest, ypred)) \n",
        "print (\"-------------------------------------------------------------------------\")\n",
        "print('Acuracia %0.2f' % metrics.accuracy_score(ytest,ypred))\n",
        "print (\"-------------------------------------------------------------------------\")"
      ],
      "metadata": {
        "id": "_QMnDyJVwBDo"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}