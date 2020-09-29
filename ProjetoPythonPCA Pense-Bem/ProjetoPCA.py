# Programa QUIZ (Pense-Bem)
# 17/09/20 -
# Grupo PSG

# Módulo
from tkinter import *

def gui():
    # Gráficos para o Programa

    # Configuração Básica de Janela
    win = Tk()  # Interface da Janela
    win.title("Pense-Bem")  # Título da Janela
    fgColour = "#FFFFFF"  # Cor da Fonte
    bgColour = "#000000"  # Cor de Fundo
    text = ("Comic Sans MS", 18)
    win.configure(bg = "#326fa8")  # Configuração da Janela
    win.geometry("900x600")  # Dimensões da Janela

    # Quadro do Título
    titleFrame = Frame(win, bg = "#000000")
    titleFrame.place(relwidth = 1, relheight = 0.08)

    # Rótulo do Título
    Label(titleFrame,
          text = "Pense-Bem",
          font = text,
          anchor = CENTER,
          fg = fgColour,
          bg = bgColour).place(relx = 0, relheight = 1)

    # Rótulo da Pontuação
    score = Label(titleFrame,
                  text = "Pontuação: 0",
                  font = text,
                  anchor = E,
                  fg = fgColour,
                  bg = bgColour)

    score.place(relx = 0.82,
                relwidth = 0.18,
                relheight= 1)

    # Rótulo do Número do Programa
    qNum = Label(win,
                 fg = fgColour,
                 bg = bgColour,
                 font = text)

    qNum.place(relx = 0.35,
               rely = 0.20,
               relwidth = 0.3,
               relheight = 0.060)

    # Rótulo da Questão
    question = Label(win,
                 fg = fgColour,
                 bg = "#303030",
                 font = text)

    question.place(relx = 0.35,
               rely = 0.25,
               relwidth = 0.3,
               relheight = 0.3)

    # Primeiro Botão
    firstBtn = Button(win,
                     text = "A História Da Turma Da Mônica",
                      font = text)

    firstBtn.place(relx = 0.25,
               rely = 0.65,
               relwidth = 0.5,
               relheight = 0.07)

    # Segundo Botão
    secondBtn = Button(win,
                       text = "Uma Aventura Científica Com Sonic",
                       font = text)

    secondBtn.place(relx = 0.25,
               rely = 0.75,
               relwidth = 0.5,
               relheight = 0.07)

    # Terceiro Botão
    thirdBtn = Button(win,
                      text = "Toy Story",
                      font = text)

    thirdBtn.place(relx = 0.25,
               rely = 0.85,
               relwidth = 0.5,
               relheight = 0.07)

    win.mainloop()

# Chama Função
gui()
