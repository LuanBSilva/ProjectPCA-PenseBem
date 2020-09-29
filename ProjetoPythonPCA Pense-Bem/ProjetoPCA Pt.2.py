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

    # Botão Próximo
    btnImg = PhotoImage(file = r"seta.gif")

    nextBtn = Button(win,
                     image = btnImg)

    nextBtn.place(relx = 0.91,
                  rely = 0.35,
                  relwidth = 0.08,
                  relheight = 0.1)

    # Botão Vermelho
    btnRed = PhotoImage(file=r"vermelho.gif")

    btnA = Button(win,
                text = "Vermelho",
                image = btnRed)

    btnA.place(relx = 0.00019,
               rely = 0.6,
               relwidth = 0.50,
               relheight = 0.2)

    # Botão Amarelo
    btnYellow = PhotoImage(file=r"amarelo.gif")

    btnB = Button(win,
                  text = "Amarelo",
                  image = btnYellow)

    btnB.place(relx = 0.50,
               rely = 0.6,
               relwidth = 0.50,
               relheight = 0.2)

    # Botão Azul
    btnBlue = PhotoImage(file=r"azul.gif")

    btnC = Button(win,
                  text = "Azul",
                  image = btnBlue)

    btnC.place(relx = 0.00019,
               rely = 0.8,
               relwidth = 0.50,
               relheight = 0.2)

    # Botão Verde
    btnGreen = PhotoImage(file=r"verde.gif")

    btnD = Button(win,
                  text = "Verde",
                  image = btnGreen)

    btnD.place(relx = 0.50,
               rely = 0.8,
               relwidth = 0.50,
               relheight = 0.2)

    win.mainloop()

# Chama Função
gui()