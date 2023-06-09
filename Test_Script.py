{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOlRD6E+wh9bSW0rlbqRRZz"
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
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "from PIL import Image\n",
        "import keras"
      ],
      "metadata": {
        "id": "YB-Ns17SI0Bs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bKwyo_y8I5KT",
        "outputId": "c6e18547-5ae5-4a5b-da84-8736f1a7718c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "qy_gDc_XIegx",
        "outputId": "f2fc031d-e11e-4046-f05c-0b6c5e6c7962"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 163ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 64ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 59ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 66ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 63ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 63ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 59ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 69ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 64ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 63ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 65ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 69ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 72ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 93ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 98ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 96ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 91ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 98ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 58ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 64ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 63ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 65ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 63ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 69ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 69ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 71ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 69ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 91ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 101ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 103ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 98ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 97ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 63ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 59ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 67ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 63ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 64ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 59ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 59ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 75ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 70ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 59ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 59ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 59ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 59ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 65ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 76ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 100ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 109ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 97ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 75ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 63ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 58ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 64ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 58ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 66ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 69ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 65ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 63ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 63ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 70ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 78ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 87ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 64ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 94ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 99ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 122ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 101ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 100ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 101ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 65ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 71ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 69ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 66ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 64ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 59ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 73ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 66ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 60ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 59ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 64ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 59ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 65ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 61ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 68ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 63ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 62ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 63ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 66ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 66ms/step\n",
            "(1, 170, 170, 3)\n",
            "1/1 [==============================] - 0s 59ms/step\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "FileNotFoundError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-15-3aff7c1fa1f3>\u001b[0m in \u001b[0;36m<cell line: 2>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mi\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;36m151\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m     \u001b[0;31m# Load the low-resolution image\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m     \u001b[0mimg\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mImage\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34mf'/content/drive/MyDrive/AnalyticsArena_DataSet/Test_LR_Images/Test_LR_Images/lr_{i}.jpg'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m     \u001b[0mnp_img\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0marray\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mimg\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.9/dist-packages/PIL/Image.py\u001b[0m in \u001b[0;36mopen\u001b[0;34m(fp, mode, formats)\u001b[0m\n\u001b[1;32m   2973\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2974\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mfilename\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2975\u001b[0;31m         \u001b[0mfp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mbuiltins\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilename\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"rb\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2976\u001b[0m         \u001b[0mexclusive_fp\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;32mTrue\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2977\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: '/content/drive/MyDrive/AnalyticsArena_DataSet/Test_LR_Images/Test_LR_Images/lr_150.jpg'"
          ]
        }
      ],
      "source": [
        "model = keras.models.load_model(\"/content/drive/MyDrive/AnalyticsArena_DataSet/fsrcnn_hope/model_00010.h5\")\n",
        "for i in range(151):\n",
        "    # Load the low-resolution image\n",
        "    img = Image.open(f'/content/drive/MyDrive/AnalyticsArena_DataSet/Test_LR_Images/Test_LR_Images/lr_{i}.jpg')\n",
        "    np_img = np.array(img)\n",
        "\n",
        "    # Reshape the input array to (170, 170, 3)\n",
        "    np_img = np_img.reshape((1,170, 170, 3))\n",
        "    print(np_img.shape)\n",
        "    # Apply the model to the low-resolution image to generate the high-resolution image\n",
        "    pred = model.predict(np_img)\n",
        "\n",
        "    # Save the high-resolution image\n",
        "    hr_img = Image.fromarray(pred.reshape(510,510,3).astype('uint8'))\n",
        "    hr_img.save(f'/content/drive/MyDrive/AnalyticsArena_DataSet/HighResolution_Try/hr_{i}.jpg')"
      ]
    }
  ]
}