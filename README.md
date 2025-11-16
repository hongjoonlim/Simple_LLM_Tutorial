# Simple_LLM_Tutorial
This repository contains python scripts to start a simple LLM


## Prerequisites
### 1. Prepare a development environment based on a Jetson Nano board. 
This tutorial is based on a Jetson Nano board. You can set up an environment from this link[Jetson-Nano-Ubuntu-20-image](https://github.com/Qengineering/Jetson-Nano-Ubuntu-20-image).  
Download the Jeson Nano image there and set up the Jetson Nano board according to the link.

### 2. Install VS Code
If you want to use the VS Code on a Jetson Nano board, you can install it from this [Visual Studio Code](https://jetsonhacks.com/2024/10/23/visual-studio-code-update-2024/) from the JetsonHacks page. It wouldn't work if you install it from the official page due to a Jeson board's limitation.

### 3. Prepare training data
In this tutorial, Harry potter text book will be used as training data. 
Down load the text book from this [link](https://www.kaggle.com/datasets/shubhammaindola/harry-potter-books).  

* create a ./source_txt folder
* place all text files in the created ./source_txt folder


## Clean text files
First, we need to clean the text files to use them as training data.  
Run this script
```python
python3 text_oneliner.py
```

This scritp will create the cleaned text files under /source/cleaned/