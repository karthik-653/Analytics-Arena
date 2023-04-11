# Analytics-Arena

# Image Super Resolution using FSRCNN

This repository contains the code for Image Super Resolution using Fast Super-Resolution Convolutional Neural Network (FSRCNN) algorithm. The main goal of the algorithm is to enhance the quality of low-resolution images to high-resolution images.

## Requirements

- Python 3.x
- TensorFlow 2.x
- Numpy
- Scikit-image
- Matplotlib

## Dataset

The model is trained on the dataset, which can be found on this [link](https://drive.google.com/file/d/1dIV6jJRQOaVbSeq9ynGm4QgWbzReaijZ/view).

## Getting started

1. Clone the repository using the following command: git clone https://github.com/username/repo.git
2. Install the dependencies by running: pip install -r requirements.txt
3. Download the dataset and extract the files.
4. Modify the `SIR_FSRCNN.ipynb` notebook to set the path to the dataset.
5. Train the model by running the cells in the `SIR_FSRCNN.ipynb` notebook.
6. After training, test the model by running `test_script.py` script. This script takes an image file as an input and outputs the super-resolved image, in the required directory provided in the script.
