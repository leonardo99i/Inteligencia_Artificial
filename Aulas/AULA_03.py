{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOycawO68TNFz9WVd0JKvzk",
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
        "<a href=\"https://colab.research.google.com/github/leonardo99i/Inteligencia_Artificial/blob/main/AULA_03.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def soma(x, y):\n",
        "  soma = x + y\n",
        "  x = 100\n",
        "  return soma, x\n"
      ],
      "metadata": {
        "id": "8tM8SPhcDfr5"
      },
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "x = 10 \n",
        "y = 20 \n",
        "z, x = soma(x, y)\n",
        "print(z)\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lESZfc92EUcC",
        "outputId": "5afc4dbf-0fb4-4c3a-a5aa-a2ff1dfef387"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "30\n",
            "100\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "x = 0 \n",
        "\n",
        "def teste():\n",
        "  global x\n",
        "  x = 10\n",
        "  print(\"Teste\")\n",
        "\n",
        "def teste_2():\n",
        "  global x\n",
        "  x = 20\n",
        "  print(\"Teste\")\n",
        "\n",
        "print(x)\n",
        "x = 5\n",
        "print(x)\n",
        "teste()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7Rdv5PwNIeWq",
        "outputId": "0320a276-a8cd-4fe3-a4ee-5e6874c80282"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "5\n",
            "Teste\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "WHILE()"
      ],
      "metadata": {
        "id": "JHsZ27DTLZnP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x = 1\n",
        "while(x <= 5):\n",
        "  print(\"PC DA XUXA!\")\n",
        "  x = x + 1"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1hB7Pp-FLXun",
        "outputId": "bb81115e-db5f-4103-9535-97fdaa2be17b"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "PC DA XUXA!\n",
            "PC DA XUXA!\n",
            "PC DA XUXA!\n",
            "PC DA XUXA!\n",
            "PC DA XUXA!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "FOR()"
      ],
      "metadata": {
        "id": "cjeia2koLd_v"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,5,3):\n",
        "  print(i)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_eFNU5k7LQ2v",
        "outputId": "d4130e03-f986-470d-e17e-0c94e020be9b"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1\n",
            "4\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "LISTA"
      ],
      "metadata": {
        "id": "0uEnDc6BLrjv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#list \n",
        "x = [10, 40, 1]\n",
        "y = [\"Xuxa\", \"Ben10\", \"Hello Kitty\"]\n",
        "\n",
        "for batata in y:\n",
        "  print(batata)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CANlXrwZLtQv",
        "outputId": "6e69cb0c-7c0e-4795-8ec9-88ec45703443"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Xuxa\n",
            "Ben10\n",
            "Hello Kitty\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(len(x)):\n",
        "  print(x[i])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YwZcHHv2L9Ye",
        "outputId": "3841a902-b394-4d8f-a2c4-37b2d41759b1"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10\n",
            "40\n",
            "1\n"
          ]
        }
      ]
    }
  ]
}