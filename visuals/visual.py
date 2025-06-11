import tkinter as tk
from tkinter import filedialog
import os  # Para pegar só o nome do arquivo

class SelecionadorArquivos:
    def __init__(self):
        self.janela = self._criar_janela()
        self.status_labels = []
        self.arquivos_selecionados = {}
        self._criar_botoes()

    def _criar_janela(self):
        janela = tk.Tk()
        janela.title("Selecionar Arquivos")
        janela.geometry("400x250")
        janela.configure(bg="#000000")
        return janela

    def _criar_botoes(self):
        self.status_labels.append(self._criar_botao_anexar("SELECIONAR ARQUIVO", numero_botao=1))

    def _criar_botao_anexar(self, texto, numero_botao):
        container = tk.Frame(self.janela, bg="#000000")
        container.pack(pady=20)

        botao = tk.Button(container, text=texto,
                          font=("Verdana", 10),
                          fg="white", bg="#000000",
                          width=25, height=2,
                          command=lambda: self._pegar_arquivo(numero_botao))
        botao.pack()

        status = tk.Label(container, text="", font=("Arial", 10), fg="white", bg="#000000")
        status.pack(pady=(5, 0))  # Coloca logo abaixo do botão

        return status

    def _pegar_arquivo(self, numero_botao):
        arquivo = filedialog.askopenfilename(title=f"Selecionar arquivo {numero_botao}")
        if arquivo:
            nome_arquivo = os.path.basename(arquivo)
            print(f"[Botão {numero_botao}] Arquivo: {arquivo}")
            self.arquivos_selecionados[numero_botao] = arquivo
            self.status_labels[numero_botao - 1].config(text=f"Arquivo \"{nome_arquivo}\" selecionado!\n(feche a janela para continuar com o programa)")
        else:
            print(f"[Botão {numero_botao}] Nenhum arquivo selecionado.")

    def iniciar(self):
        self.janela.mainloop()

    def get_arquivos(self):
        return self.arquivos_selecionados
