# Programa QUIZ (Pense-Bem)
# 17/09/20 -
# Grupo PSG

# Módulo
from tkinter import *
from random import randint

# Variáveis Global


qCount = 0
usedQuestions = []
actualAnswer = 0
usersAnswer = 0
points = 0

def readFile():
    # Função para Ler o Arquivo.txt

    data = []   # 2d Matriz (Lista)
    file = open("Questions.txt", mode = "r")

    #iterar (loop), cada linha do arquivo e completar matriz
    for line in file:
        data.append(line.strip().split(','))

    return data

def displayQuestion():
    # Questões Tela

    data = readFile()

    global qCount, usedQuestions, actualAnswer, points

    # Gerador das Questões
    randomQ = randint(0, len(data) - 1)
    currentQuestion = str(data[randomQ][0])

    while currentQuestion in usedQuestions and len(usedQuestions) < len(data):
        randomQ = randint(0, len(data) - 1)
        currentQuestion = str(data[randomQ][0])

    if qCount < len(data):

        # Display das Questões
        resetBtns()
        qNum.config(text = "Questão: {0}".format(qCount + 1))
        question.config(text = data[randomQ][1])
        btnA.config(text = data[randomQ][2])
        btnB.config(text = data[randomQ][3])
        btnC.config(text = data[randomQ][4])
        btnD.config(text = data[randomQ][5])

        qCount += 1
        usedQuestions.append(currentQuestion)
        actualAnswer = data[randomQ][6]
    else:
        gameOver.config(text = "Game Over\n\nPontuação Final: %s" % points)
        gameOver.place(relwidth = 1, relheight = 1, relx = 0, rely = 0)
        resetGame.place(relx = 0.32,
                        rely = 0.85,
                        relwidth = 0.35,
                        relheight = 0.1)

def checkAnswer():
    # Resposta Selecionada e Aumento no número de pontos

    global points

    if int(actualAnswer) == usersAnswer:
        points += 1
        score.config(text = "Pontuação: %s" % points)
    resetBtns()
    displayQuestion()

def resetgameBtn():

    global qCount ,usedQuestions, usersAnswer, points, actualAnswer

    qCount = 0
    usedQuestions = []
    actualAnswer = 0
    usersAnswer = 0
    points = 0
    resetBtns()
    displayQuestion()
    removeGameover()

def removeGameover():

    gameOver.place(relwidth=1, relheight=1, relx = 1, rely = 1)
    resetGame.place(relx=0.32,
                    rely=1,
                    relwidth=0.35,
                    relheight=0.1)

def btnPressed(answer):
    # Botão selecionado

    resetBtns()   # Função para resetar

    if answer == 1:
        btnA.config(fg = "#FFFFFF")
    elif answer == 2:
        btnB.config(fg = "#FFFFFF")
    elif answer == 3:
        btnC.config(fg = "#FFFFFF")
    elif answer == 4:
        btnD.config(fg = "#FFFFFF")

    global usersAnswer
    usersAnswer = answer

def resetBtns():
    # Resetar texto Botões

    btnA.config(fg="#000000")
    btnB.config(fg="#000000")
    btnC.config(fg="#000000")
    btnD.config(fg="#000000")

def gui():
# Gráficos para o Programa

    global btnA, btnB, btnC, btnD, qNum, question, score, gameOver, resetGame

    # Configuração Básica de Janela
    win = Tk()  # Interface da Janela
    win.title("Pense-Bem")  # Título da Janela
    fgColour = "#FFFFFF"  # Cor da Fonte
    bgColour = "#000000"  # Cor de Fundo
    text1 = ("Comic Sans MS", 25)
    text3 = ("Comic Sans MS", 35)
    text2 = ("Comic Sans MS", 20)
    text = ("Comic Sans MS", 18)
    #win.configure(bg="#326fa8")  # Configuração da Janela
    win.geometry("900x600")  # Dimensões da Janela

    # Imagem de Fundo
    bgImage = PhotoImage(file = r"SonicBg.gif")
    Label(win, image = bgImage).place(relwidth = 1, relheight = 0.65)

    # Quadro do Título
    titleFrame = Frame(win, bg="#000000")
    titleFrame.place(relwidth=1, relheight=0.08)

    # Rótulo do Título
    Label(titleFrame,
            text="Pense-Bem: Uma Aventura Científica com Sonic",
            font=text,
            anchor=CENTER,
            fg=fgColour,
            bg=bgColour).place(relx=0, relheight=1)

    # Rótulo da Pontuação
    score = Label(titleFrame,
                    text="Pontuação: 0",
                    font=text,
                    anchor=E,
                    fg=fgColour,
                    bg=bgColour)

    score.place(relx=0.82,
                relwidth=0.18,
                relheight=1)

    # Rótulo do Número do Programa
    qNum = Label(win,
                fg=fgColour,
                bg=bgColour,
                font=text)

    qNum.place(relx=0.35,
                rely=0.19,
                relwidth=0.3,
                relheight=0.050)

    # Rótulo da Questão
    question = Label(win,
                    fg="#ff0000",
                    bg="#303030",
                    font=text3)

    question.place(relx=0.35,
                rely=0.24,
                relwidth=0.3,
                relheight=0.3)

    # Botão Próximo
    btnImg = PhotoImage(file=r"seta.gif")

    nextBtn = Button(win,
                    image=btnImg,
                     command = checkAnswer)

    # Qr Code
    btnQrimg = PhotoImage(file = r"qrcode12.gif")

    btnQr = Button(win,
                   image = btnQrimg)

    btnQr.place(relx=0.35,
                rely=0.19,
                relwidth=0.30,
                relheight=0.35)

    # Botão Vermelho
    btnRed = PhotoImage(file=r"vermelho.gif")

    btnA = Button(win,
                compound = CENTER,
                font = text2,
                text="A",
                image=btnRed,
                command=lambda: btnPressed(1))

    btnA.place(relx=0.00019,
                rely=0.6,
                relwidth=0.50,
                relheight=0.2)

    # Botão Amarelo
    btnYellow = PhotoImage(file=r"amarelo.gif")

    btnB = Button(win,
                compound = CENTER,
                font = text2,
                text="B",
                image=btnYellow,
                command=lambda: btnPressed(2))

    btnB.place(relx=0.50,
                rely=0.6,
                relwidth=0.50,
                relheight=0.2)

    # Botão Azul
    btnBlue = PhotoImage(file=r"azul.gif")

    btnC = Button(win,
                compound = CENTER,
                font = text2,
                text="C",
                image=btnBlue,
                command=lambda: btnPressed(3))

    btnC.place(relx=0.00019,
                rely=0.8,
                relwidth=0.50,
                relheight=0.2)

    # Botão Verde
    btnGreen = PhotoImage(file=r"verde.gif")

    btnD = Button(win,
                compound = CENTER,
                font = text2,
                text="D",
                image=btnGreen,
                command=lambda: btnPressed(4))

    btnD.place(relx=0.50,
                rely=0.8,
                relwidth=0.50,
                relheight=0.2)

    # Função de destruir btns e Rodar Questões
    def hideStart():
        btnStart.destroy()
        btnQr.destroy()
        displayQuestion()

        nextBtn.place(relx=0.91,
                      rely=0.35,
                      relwidth=0.08,
                      relheight=0.1)

    # Botão Começar
    btnStart = Button(win,
                      text = "Escaneie o QR Code acima para abrir o livro\n\nClique aqui para Começar",
                      compound = CENTER,
                      font = text1,
                      bg = bgColour,
                      fg = fgColour,
                      command = hideStart)

    btnStart.place(relx = 0.00001,
                   rely = 0.6,
                   relwidth = 1,
                   relheight = 0.4,)

    gameOver = Label(win,
                     fg = "#FFFFFF",
                     bg = "#000000",
                     font = ("Comic Sans MS",50))

    resetGame = Button(win,
                       text = "Recomeçar",
                       compound = CENTER,
                       command = resetgameBtn,
                       font = ("Comic Sans MS",20))

    win.mainloop()

# Chama Função
gui()
