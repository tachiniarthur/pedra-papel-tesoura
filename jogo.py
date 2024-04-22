import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from PIL import Image, ImageTk
from random import choices

idade = None

def obter_probabilidade_jogadas(idade):
    if idade < 18:
        return {'Pedra': 0.3, 'Papel': 0.4, 'Tesoura': 0.3}  
    elif 18 <= idade < 25:
        return {'Pedra': 0.4, 'Papel': 0.3, 'Tesoura': 0.3}  
    elif 25 <= idade < 35:
        return {'Pedra': 0.3, 'Papel': 0.4, 'Tesoura': 0.3}  
    elif 35 <= idade < 45:
        return {'Pedra': 0.2, 'Papel': 0.5, 'Tesoura': 0.3}  
    elif 45 <= idade < 55:
        return {'Pedra': 0.3, 'Papel': 0.3, 'Tesoura': 0.4}  
    elif 55 <= idade <= 60:
        return {'Pedra': 0.3, 'Papel': 0.3, 'Tesoura': 0.4}  
    else:
        return {'Pedra': 0.4, 'Papel': 0.3, 'Tesoura': 0.3} 

def comecar_jogo():
    global idade
    idade = simpledialog.askinteger("Idade", "Qual é a sua idade?")
    if idade is None:
        messagebox.showerror("Erro", "Por favor, insira uma idade válida.")
    else:
        jogar_novamente()

def jogar(jogada_jogador):
    global idade
    if idade is None:
        messagebox.showerror("Erro", "Por favor, clique no botão Começar")
        return

    probabilidade_jogadas = obter_probabilidade_jogadas(idade)
    jogada_computador = choices(['Pedra', 'Papel', 'Tesoura'], weights=[probabilidade_jogadas['Pedra'], probabilidade_jogadas['Papel'], probabilidade_jogadas['Tesoura']])[0]
    resultado = determinar_resultado(jogada_jogador, jogada_computador)
    resultado_label.config(text=f"Computador: {jogada_computador}\nResultado: {resultado}")
    
    jogada_jogador_label.config(text=f"Jogador: {jogada_jogador}")
    jogada_computador_label.config(text=f"Computador: {jogada_computador}")
    
    imagem_jogada_computador = Image.open(f"imagens/{jogada_computador.lower()}.png")
    imagem_jogada_computador = imagem_jogada_computador.resize((100, 100), Image.ANTIALIAS)
    imagem_jogada_computador = ImageTk.PhotoImage(imagem_jogada_computador)
    imagem_computador_label.config(image=imagem_jogada_computador)
    imagem_computador_label.image = imagem_jogada_computador

    imagem_jogada_jogador = Image.open(f"imagens/{jogada_jogador.lower()}.png")
    imagem_jogada_jogador = imagem_jogada_jogador.resize((100, 100), Image.ANTIALIAS)
    imagem_jogada_jogador = ImageTk.PhotoImage(imagem_jogada_jogador)
    imagem_jogador_label.config(image=imagem_jogada_jogador)
    imagem_jogador_label.image = imagem_jogada_jogador

def determinar_resultado(jogada_jogador, jogada_computador):
    if jogada_jogador == jogada_computador:
        return "Empate"
    elif (jogada_jogador == 'Pedra' and jogada_computador == 'Tesoura') or \
         (jogada_jogador == 'Papel' and jogada_computador == 'Pedra') or \
         (jogada_jogador == 'Tesoura' and jogada_computador == 'Papel'):
        return "Jogador Vence"
    else:
        return "Computador Vence"

def parar_jogo():
    global idade
    idade = None
    resultado_label.config(text="Jogo parado")
    jogada_jogador_label.config(text="")
    jogada_computador_label.config(text="")
    imagem_computador_label.config(image="")
    imagem_computador_label.image = None
    imagem_jogador_label.config(image="")
    imagem_jogador_label.image = None

def jogar_novamente():
    resultado_label.config(text="Escolha uma jogada para começar")
    jogada_jogador_label.config(text="")
    jogada_computador_label.config(text="")
    imagem_computador_label.config(image="")
    imagem_computador_label.image = None
    imagem_jogador_label.config(image="")
    imagem_jogador_label.image = None

root = tk.Tk()
root.title("Jogo de Pedra, Papel, Tesoura")
root.configure(bg='lightblue')

pedra_btn = ttk.Button(root, text="Pedra", width=10, command=lambda: jogar('Pedra'))
papel_btn = ttk.Button(root, text="Papel", width=10, command=lambda: jogar('Papel'))
tesoura_btn = ttk.Button(root, text="Tesoura", width=10, command=lambda: jogar('Tesoura'))
parar_btn = ttk.Button(root, text="Parar", command=parar_jogo)
jogar_novamente_btn = ttk.Button(root, text="Jogar Novamente", command=jogar_novamente)
comecar_btn = ttk.Button(root, text="Começar", command=comecar_jogo)

resultado_label = ttk.Label(root, text="Escolha uma jogada para começar", font=("Helvetica", 12), background='lightyellow', relief='groove')

imagem_computador_label = ttk.Label(root)

imagem_jogador_label = ttk.Label(root)

jogada_jogador_label = ttk.Label(root)
jogada_computador_label = ttk.Label(root)

pedra_btn.grid(row=0, column=0, padx=10, pady=10)
papel_btn.grid(row=0, column=1, padx=10, pady=10)
tesoura_btn.grid(row=0, column=2, padx=10, pady=10)
resultado_label.grid(row=1, columnspan=3, padx=10, pady=10, sticky='nsew')
imagem_computador_label.grid(row=2, column=2, padx=10, pady=10)
imagem_jogador_label.grid(row=2, column=0, padx=10, pady=10)
jogada_jogador_label.grid(row=3, column=0, padx=10, pady=5)
jogada_computador_label.grid(row=3, column=2, padx=10, pady=5)
parar_btn.grid(row=4, column=0, padx=10, pady=10)
jogar_novamente_btn.grid(row=4, column=1, padx=10, pady=10)
comecar_btn.grid(row=4, column=2, padx=10, pady=10)

root.mainloop()
