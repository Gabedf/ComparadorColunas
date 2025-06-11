from visuals.visual import *
import pandas as pd 
import os

# INICIALIZAÇÃO OBJETOS
visualizacao   = SelecionadorArquivos()

# INICIAR VISUALIZAÇÃO E ABRIR ARQUIVOS
visualizacao.iniciar()
arquivos = visualizacao.get_arquivos()  
arq_comparado = pd.read_excel(arquivos[1])

# TRANSFORMAÇÃO EM LISTA
nomesA = arq_comparado['COLUNA A'].to_list()
nomesB = arq_comparado['COLUNA B'].to_list()

# COMPARAÇÃO e ESCRITA
with open("nomes_faltantes.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("=====NOMES FALTANTES=====\n\n")
    for i in nomesA:
        if i not in nomesB:
            arquivo.write(i + "\n")

# ABRIR ARQUIVO E ENCERRAR O SCRIPT
os.startfile("nomes_faltantes.txt")