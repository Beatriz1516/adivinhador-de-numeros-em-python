import tkinter as tk
from tkinter import messagebox
import random

class JogoAdivinhacao:
    def __init__(janela, root):
        janela.root = root
        janela.root.title("Jogo de Adivinhação")

        # Variáveis
        janela.numero_secreto = None
        janela.tentativas = 0

        # Tela inicial - definir intervalo
        janela.label_instrucao = tk.Label(root, text="Defina o intervalo:")
        janela.label_instrucao.pack()

        janela.frame_intervalo = tk.Frame(root)
        janela.frame_intervalo.pack()

        janela.label_min = tk.Label(janela.frame_intervalo, text="Mínimo:")
        janela.label_min.grid(row=0, column=0)

        janela.entry_min = tk.Entry(janela.frame_intervalo)
        janela.entry_min.grid(row=0, column=1)

        janela.label_max = tk.Label(janela.frame_intervalo, text="Máximo:")
        janela.label_max.grid(row=1, column=0)

        janela.entry_max = tk.Entry(janela.frame_intervalo)
        janela.entry_max.grid(row=1, column=1)

        janela.botao_iniciar = tk.Button(root, text="Iniciar Jogo", command=janela.iniciar_jogo)
        janela.botao_iniciar.pack()

        # Área do jogo
        janela.label_palpite = tk.Label(root, text="Digite seu palpite:")
        janela.entry_palpite = tk.Entry(root)
        janela.botao_tentar = tk.Button(root, text="Tentar", command=janela.verificar_palpite)

        janela.label_resultado = tk.Label(root, text="")

    def iniciar_jogo(janela):
        try:
            minimo = int(janela.entry_min.get())
            maximo = int(janela.entry_max.get())

            if minimo >= maximo:
                messagebox.showerror("Erro", "O mínimo deve ser menor que o máximo!")
                return

            janela.numero_secreto = random.randint(minimo, maximo)
            janela.tentativas = 0

            # Mostrar área do jogo
            janela.label_palpite.pack()
            janela.entry_palpite.pack()
            janela.botao_tentar.pack()
            janela.label_resultado.pack()

            messagebox.showinfo("Jogo iniciado", f"Adivinhe um número entre {minimo} e {maximo}!")

        except ValueError:
            messagebox.showerror("Erro", "Digite valores válidos!")

    def verificar_palpite(janela):
        try:
            palpite = int(janela.entry_palpite.get())
            janela.tentativas += 1

            if palpite < janela.numero_secreto:
                janela.label_resultado.config(text="Muito baixo! Tente novamente.")
            elif palpite > janela.numero_secreto:
                janela.label_resultado.config(text="Muito alto! Tente novamente.")
            else:
                messagebox.showinfo(
                    "Parabéns!",
                    f"Você acertou em {janela.tentativas} tentativas!"
                )
                janela.label_resultado.config(text="")

        except ValueError:
            messagebox.showerror("Erro", "Digite um número válido!")


# Executar aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = JogoAdivinhacao(root)
    root.mainloop()