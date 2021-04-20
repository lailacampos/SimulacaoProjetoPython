from tkinter import *
import tkinter.ttk as ttk
import CalculoCargas as cc
from GUIRespostaC import *
from GUIResposta import *

class MainGUIWindow:
    def __init__(self, top=None):
        '''Configura e  toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("911x600+283+35")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)
        top.title("Simulacao")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.TNotebook1.configure(takefocus="")
        self.abaRepresentacaoCargas_1 = Frame(self.TNotebook1)
        self.TNotebook1.add(self.abaRepresentacaoCargas_1, padding=3)
        self.TNotebook1.tab(0, text="Representação das Cargas", compound="left"
                ,underline="-1", )
        self.abaRepresentacaoCargas_1.configure(background="#d9d9d9")
        self.abaRepresentacaoCargas_1.configure(highlightbackground="#d9d9d9")
        self.abaRepresentacaoCargas_1.configure(highlightcolor="black")

        self.Label1 = Label(self.abaRepresentacaoCargas_1)
        self.Label1.place(relx=0.044, rely=0.052, height=21, width=264)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Qual a representação das cargas sobre o corpo?''')

        self.Frame_ImageA = Frame(self.abaRepresentacaoCargas_1)
        self.Frame_ImageA.place(relx=0.044, rely=0.209, relheight=0.436
                , relwidth=0.276)
        self.Frame_ImageA.configure(relief='groove')
        self.Frame_ImageA.configure(borderwidth="2")
        self.Frame_ImageA.configure(relief="groove")
        self.Frame_ImageA.configure(background="#d9d9d9")
        self.Frame_ImageA.configure(highlightbackground="#d9d9d9")
        self.Frame_ImageA.configure(highlightcolor="black")

        self.Label_ImageA = Label(self.Frame_ImageA)
        self.Label_ImageA.place(relx=0.0, rely=0.0, height=250, width=250)
        self.Label_ImageA.configure(activebackground="#f9f9f9")
        self.Label_ImageA.configure(activeforeground="black")
        self.Label_ImageA.configure(background="#d9d9d9")
        self.Label_ImageA.configure(disabledforeground="#a3a3a3")
        self.Label_ImageA.configure(foreground="#000000")
        self.Label_ImageA.configure(highlightbackground="#d9d9d9")
        self.Label_ImageA.configure(highlightcolor="black")
        imagepathA = "OpcaoA.png"
        global img_A
        img_A = PhotoImage(file=imagepathA)
        self.Label_ImageA.configure(image=img_A)

        self.Frame_ImageB = Frame(self.abaRepresentacaoCargas_1)
        self.Frame_ImageB.place(relx=0.364, rely=0.209, relheight=0.436
                , relwidth=0.276)
        self.Frame_ImageB.configure(relief='groove')
        self.Frame_ImageB.configure(borderwidth="2")
        self.Frame_ImageB.configure(relief="groove")
        self.Frame_ImageB.configure(background="#d9d9d9")
        self.Frame_ImageB.configure(highlightbackground="#d9d9d9")
        self.Frame_ImageB.configure(highlightcolor="black")

        self.Label_ImageB = Label(self.Frame_ImageB)
        self.Label_ImageB.place(relx=0.0, rely=0.0, height=250, width=250)
        self.Label_ImageB.configure(activebackground="#f9f9f9")
        self.Label_ImageB.configure(activeforeground="black")
        self.Label_ImageB.configure(background="#d9d9d9")
        self.Label_ImageB.configure(disabledforeground="#a3a3a3")
        self.Label_ImageB.configure(foreground="#000000")
        self.Label_ImageB.configure(highlightbackground="#d9d9d9")
        self.Label_ImageB.configure(highlightcolor="black")
        imagepathB = "OpcaoB.png"
        global img_B
        img_B = PhotoImage(file=imagepathB)
        self.Label_ImageB.configure(image=img_B)

        self.Frame_ImageC = Frame(self.abaRepresentacaoCargas_1)
        self.Frame_ImageC.place(relx=0.684, rely=0.209, relheight=0.436
                , relwidth=0.276)
        self.Frame_ImageC.configure(relief='groove')
        self.Frame_ImageC.configure(borderwidth="2")
        self.Frame_ImageC.configure(relief="groove")
        self.Frame_ImageC.configure(background="#d9d9d9")
        self.Frame_ImageC.configure(highlightbackground="#d9d9d9")
        self.Frame_ImageC.configure(highlightcolor="black")

        self.Label_ImageC = Label(self.Frame_ImageC)
        self.Label_ImageC.place(relx=0.0, rely=0.0, height=250, width=250)
        self.Label_ImageC.configure(activebackground="#f9f9f9")
        self.Label_ImageC.configure(activeforeground="black")
        self.Label_ImageC.configure(background="#d9d9d9")
        self.Label_ImageC.configure(disabledforeground="#a3a3a3")
        self.Label_ImageC.configure(foreground="#000000")
        self.Label_ImageC.configure(highlightbackground="#d9d9d9")
        self.Label_ImageC.configure(highlightcolor="black")
        imagepathC = "OpcaoC.png"
        global img_C
        img_C = PhotoImage(file=imagepathC)
        self.Label_ImageC.configure(image=img_C)

        global frameAeBPlaceInfo
        self.Frame_PerguntaAeB = Frame(self.abaRepresentacaoCargas_1)
        self.Frame_PerguntaAeB.place(relx=0.044, rely=0.714, relheight=0.235
                , relwidth=0.915)
        frameAeBPlaceInfo = self.Frame_PerguntaAeB.place_info()
        self.Frame_PerguntaAeB.configure(relief='groove')
        self.Frame_PerguntaAeB.configure(borderwidth="2")
        self.Frame_PerguntaAeB.configure(relief="groove")
        self.Frame_PerguntaAeB.configure(background="#d9d9d9")
        self.Frame_PerguntaAeB.configure(highlightbackground="#d9d9d9")
        self.Frame_PerguntaAeB.configure(highlightcolor="black")

        self.Label_ComprimentoBarraPergunta = Label(self.Frame_PerguntaAeB)
        self.Label_ComprimentoBarraPergunta.place(relx=0.024, rely=0.222
                , height=21, width=174)
        self.Label_ComprimentoBarraPergunta.configure(activebackground="#f9f9f9")
        self.Label_ComprimentoBarraPergunta.configure(activeforeground="black")
        self.Label_ComprimentoBarraPergunta.configure(background="#d9d9d9")
        self.Label_ComprimentoBarraPergunta.configure(disabledforeground="#a3a3a3")
        self.Label_ComprimentoBarraPergunta.configure(foreground="#000000")
        self.Label_ComprimentoBarraPergunta.configure(highlightbackground="#d9d9d9")
        self.Label_ComprimentoBarraPergunta.configure(highlightcolor="black")
        self.Label_ComprimentoBarraPergunta.configure(text='''Digite o comprimento da barra:''')

        self.Entry_ComprimentoBarra = Entry(self.Frame_PerguntaAeB)
        self.Entry_ComprimentoBarra.place(relx=0.253, rely=0.222, height=20
                , relwidth=0.101)
        self.Entry_ComprimentoBarra.configure(background="white")
        self.Entry_ComprimentoBarra.configure(disabledforeground="#a3a3a3")
        self.Entry_ComprimentoBarra.configure(font="TkFixedFont")
        self.Entry_ComprimentoBarra.configure(foreground="#000000")
        self.Entry_ComprimentoBarra.configure(highlightbackground="#d9d9d9")
        self.Entry_ComprimentoBarra.configure(highlightcolor="black")
        self.Entry_ComprimentoBarra.configure(insertbackground="black")
        self.Entry_ComprimentoBarra.configure(selectbackground="#c4c4c4")
        self.Entry_ComprimentoBarra.configure(selectforeground="black")
        self.Entry_ComprimentoBarra.insert(0, "0")

        self.Label_PerguntaValorCarga = Label(self.Frame_PerguntaAeB)
        self.Label_PerguntaValorCarga.place(relx=0.024, rely=0.593, height=21
                , width=127)
        self.Label_PerguntaValorCarga.configure(activebackground="#f9f9f9")
        self.Label_PerguntaValorCarga.configure(activeforeground="black")
        self.Label_PerguntaValorCarga.configure(background="#d9d9d9")
        self.Label_PerguntaValorCarga.configure(disabledforeground="#a3a3a3")
        self.Label_PerguntaValorCarga.configure(foreground="#000000")
        self.Label_PerguntaValorCarga.configure(highlightbackground="#d9d9d9")
        self.Label_PerguntaValorCarga.configure(highlightcolor="black")
        self.Label_PerguntaValorCarga.configure(text='''Digite o valor da carga:''')

        self.Entry_ValorCarga = Entry(self.Frame_PerguntaAeB)
        self.Entry_ValorCarga.place(relx=0.253, rely=0.593, height=20
                , relwidth=0.101)
        self.Entry_ValorCarga.configure(background="white")
        self.Entry_ValorCarga.configure(disabledforeground="#a3a3a3")
        self.Entry_ValorCarga.configure(font="TkFixedFont")
        self.Entry_ValorCarga.configure(foreground="#000000")
        self.Entry_ValorCarga.configure(highlightbackground="#d9d9d9")
        self.Entry_ValorCarga.configure(highlightcolor="black")
        self.Entry_ValorCarga.configure(insertbackground="black")
        self.Entry_ValorCarga.configure(selectbackground="#c4c4c4")
        self.Entry_ValorCarga.configure(selectforeground="black")
        self.Entry_ValorCarga.insert(0, "0")

        self.ButtonCalcular = Button(self.Frame_PerguntaAeB)
        self.ButtonCalcular.place(relx=0.687, rely=0.444, height=24, width=127)
        self.ButtonCalcular.configure(activebackground="#ececec")
        self.ButtonCalcular.configure(activeforeground="#000000")
        self.ButtonCalcular.configure(background="#d9d9d9")
        self.ButtonCalcular.configure(disabledforeground="#a3a3a3")
        self.ButtonCalcular.configure(foreground="#000000")
        self.ButtonCalcular.configure(highlightbackground="#d9d9d9")
        self.ButtonCalcular.configure(highlightcolor="black")
        self.ButtonCalcular.configure(pady="0")
        self.ButtonCalcular.configure(text='''Calcular''')
        self.ButtonCalcular.configure(command=lambda: self.criarGUIRespostaAeB(top))

        global radiobuttonvariable
        radiobuttonvariable = IntVar()
        radiobuttonvariable.get()

        self.buttonEscolha1 = Radiobutton(self.abaRepresentacaoCargas_1)
        self.buttonEscolha1.place(relx=0.044, rely=0.139, relheight=0.044
                , relwidth=0.189)
        self.buttonEscolha1.configure(activebackground="#ececec")
        self.buttonEscolha1.configure(activeforeground="#000000")
        self.buttonEscolha1.configure(background="#d9d9d9")
        self.buttonEscolha1.configure(disabledforeground="#a3a3a3")
        self.buttonEscolha1.configure(foreground="#000000")
        self.buttonEscolha1.configure(highlightbackground="#d9d9d9")
        self.buttonEscolha1.configure(highlightcolor="black")
        self.buttonEscolha1.configure(justify='left')
        self.buttonEscolha1.configure(variable=radiobuttonvariable)
        self.buttonEscolha1.configure(value=1)
        self.buttonEscolha1.configure(text='''Uniformemente distribuída''')
        self.buttonEscolha1.configure(command=self.getsetarVariavelBotaoEscolha)

        self.buttonEscolha2 = Radiobutton(self.abaRepresentacaoCargas_1)
        self.buttonEscolha2.place(relx=0.364, rely=0.139, relheight=0.044
                , relwidth=0.163)
        self.buttonEscolha2.configure(activebackground="#ececec")
        self.buttonEscolha2.configure(activeforeground="#000000")
        self.buttonEscolha2.configure(background="#d9d9d9")
        self.buttonEscolha2.configure(disabledforeground="#a3a3a3")
        self.buttonEscolha2.configure(foreground="#000000")
        self.buttonEscolha2.configure(highlightbackground="#d9d9d9")
        self.buttonEscolha2.configure(highlightcolor="black")
        self.buttonEscolha2.configure(justify='left')
        self.buttonEscolha2.configure(variable=radiobuttonvariable)
        self.buttonEscolha2.configure(value=2)
        self.buttonEscolha2.configure(text='''Uniformemente variável''')
        self.buttonEscolha2.configure(command=self.getsetarVariavelBotaoEscolha)

        self.buttonEscolha3 = Radiobutton(self.abaRepresentacaoCargas_1)
        self.buttonEscolha3.place(relx=0.684, rely=0.139, relheight=0.044
                , relwidth=0.163)
        self.buttonEscolha3.configure(activebackground="#ececec")
        self.buttonEscolha3.configure(activeforeground="#000000")
        self.buttonEscolha3.configure(background="#d9d9d9")
        self.buttonEscolha3.configure(disabledforeground="#a3a3a3")
        self.buttonEscolha3.configure(foreground="#000000")
        self.buttonEscolha3.configure(highlightbackground="#d9d9d9")
        self.buttonEscolha3.configure(highlightcolor="black")
        self.buttonEscolha3.configure(justify='left')
        self.buttonEscolha3.configure(variable=radiobuttonvariable)
        self.buttonEscolha3.configure(value=3)
        self.buttonEscolha3.configure(text='''Uniformemente variável''')
        self.buttonEscolha3.configure(command=self.getsetarVariavelBotaoEscolha)

        global frameCPlaceInfo
        self.Frame_PerguntaC = Frame(self.abaRepresentacaoCargas_1)
        self.Frame_PerguntaC.place(relx=0.044, rely=0.714, relheight=0.235
                , relwidth=0.915)
        frameCPlaceInfo = self.Frame_PerguntaC.place_info()
        self.Frame_PerguntaC.configure(relief='groove')
        self.Frame_PerguntaC.configure(borderwidth="2")
        self.Frame_PerguntaC.configure(relief="groove")
        self.Frame_PerguntaC.configure(background="#d9d9d9")
        self.Frame_PerguntaC.configure(highlightbackground="#d9d9d9")
        self.Frame_PerguntaC.configure(highlightcolor="black")
        self.Frame_PerguntaC.place_forget()

        self.Label_ComprimentoBarraPerguntaC = Label(self.Frame_PerguntaC)
        self.Label_ComprimentoBarraPerguntaC.place(relx=0.024, rely=0.148
                , height=21, width=174)
        self.Label_ComprimentoBarraPerguntaC.configure(activebackground="#f9f9f9")
        self.Label_ComprimentoBarraPerguntaC.configure(activeforeground="black")
        self.Label_ComprimentoBarraPerguntaC.configure(background="#d9d9d9")
        self.Label_ComprimentoBarraPerguntaC.configure(disabledforeground="#a3a3a3")
        self.Label_ComprimentoBarraPerguntaC.configure(foreground="#000000")
        self.Label_ComprimentoBarraPerguntaC.configure(highlightbackground="#d9d9d9")
        self.Label_ComprimentoBarraPerguntaC.configure(highlightcolor="black")
        self.Label_ComprimentoBarraPerguntaC.configure(text='''Digite o comprimento da barra:''')

        self.Entry_ComprimentoBarraC = Entry(self.Frame_PerguntaC)
        self.Entry_ComprimentoBarraC.place(relx=0.253, rely=0.148, height=20
                , relwidth=0.101)
        self.Entry_ComprimentoBarraC.configure(background="white")
        self.Entry_ComprimentoBarraC.configure(disabledforeground="#a3a3a3")
        self.Entry_ComprimentoBarraC.configure(font="TkFixedFont")
        self.Entry_ComprimentoBarraC.configure(foreground="#000000")
        self.Entry_ComprimentoBarraC.configure(highlightbackground="#d9d9d9")
        self.Entry_ComprimentoBarraC.configure(highlightcolor="black")
        self.Entry_ComprimentoBarraC.configure(insertbackground="black")
        self.Entry_ComprimentoBarraC.configure(selectbackground="#c4c4c4")
        self.Entry_ComprimentoBarraC.configure(selectforeground="black")
        self.Entry_ComprimentoBarraC.insert(0, "0")

        self.Label_PerguntaValorCarga1 = Label(self.Frame_PerguntaC)
        self.Label_PerguntaValorCarga1.place(relx=0.024, rely=0.407, height=21
                , width=139)
        self.Label_PerguntaValorCarga1.configure(activebackground="#f9f9f9")
        self.Label_PerguntaValorCarga1.configure(activeforeground="black")
        self.Label_PerguntaValorCarga1.configure(background="#d9d9d9")
        self.Label_PerguntaValorCarga1.configure(disabledforeground="#a3a3a3")
        self.Label_PerguntaValorCarga1.configure(foreground="#000000")
        self.Label_PerguntaValorCarga1.configure(highlightbackground="#d9d9d9")
        self.Label_PerguntaValorCarga1.configure(highlightcolor="black")
        self.Label_PerguntaValorCarga1.configure(text='''Digite o valor da carga 1 :''')

        self.Entry_ValorCarga1 = Entry(self.Frame_PerguntaC)
        self.Entry_ValorCarga1.place(relx=0.253, rely=0.407, height=20
                , relwidth=0.101)
        self.Entry_ValorCarga1.configure(background="white")
        self.Entry_ValorCarga1.configure(disabledforeground="#a3a3a3")
        self.Entry_ValorCarga1.configure(font="TkFixedFont")
        self.Entry_ValorCarga1.configure(foreground="#000000")
        self.Entry_ValorCarga1.configure(highlightbackground="#d9d9d9")
        self.Entry_ValorCarga1.configure(highlightcolor="black")
        self.Entry_ValorCarga1.configure(insertbackground="black")
        self.Entry_ValorCarga1.configure(selectbackground="#c4c4c4")
        self.Entry_ValorCarga1.configure(selectforeground="black")
        self.Entry_ValorCarga1.insert(0, "0")

        self.Button_CalcularC = Button(self.Frame_PerguntaC)
        self.Button_CalcularC.place(relx=0.687, rely=0.444, height=24, width=127)

        self.Button_CalcularC.configure(activebackground="#ececec")
        self.Button_CalcularC.configure(activeforeground="#000000")
        self.Button_CalcularC.configure(background="#d9d9d9")
        self.Button_CalcularC.configure(disabledforeground="#a3a3a3")
        self.Button_CalcularC.configure(foreground="#000000")
        self.Button_CalcularC.configure(highlightbackground="#d9d9d9")
        self.Button_CalcularC.configure(highlightcolor="black")
        self.Button_CalcularC.configure(pady="0")
        self.Button_CalcularC.configure(text='''Calcular''')
        self.Button_CalcularC.configure(command=lambda: self.criarGUIRespostaC(top))
        '''self.Button_CalcularC.configure(command=self.realizarCalculoC)'''

        self.Entry_ValorCarga2 = Entry(self.Frame_PerguntaC)
        self.Entry_ValorCarga2.place(relx=0.253, rely=0.667, height=20
                , relwidth=0.101)
        self.Entry_ValorCarga2.configure(background="white")
        self.Entry_ValorCarga2.configure(disabledforeground="#a3a3a3")
        self.Entry_ValorCarga2.configure(font="TkFixedFont")
        self.Entry_ValorCarga2.configure(foreground="#000000")
        self.Entry_ValorCarga2.configure(highlightbackground="#d9d9d9")
        self.Entry_ValorCarga2.configure(highlightcolor="black")
        self.Entry_ValorCarga2.configure(insertbackground="black")
        self.Entry_ValorCarga2.configure(selectbackground="#c4c4c4")
        self.Entry_ValorCarga2.configure(selectforeground="black")
        self.Entry_ValorCarga2.insert(0, "0")

        self.Label_PerguntaValorCarga2 = Label(self.Frame_PerguntaC)
        self.Label_PerguntaValorCarga2.place(relx=0.024, rely=0.667, height=21
                , width=139)
        self.Label_PerguntaValorCarga2.configure(activebackground="#f9f9f9")
        self.Label_PerguntaValorCarga2.configure(activeforeground="black")
        self.Label_PerguntaValorCarga2.configure(background="#d9d9d9")
        self.Label_PerguntaValorCarga2.configure(disabledforeground="#a3a3a3")
        self.Label_PerguntaValorCarga2.configure(foreground="#000000")
        self.Label_PerguntaValorCarga2.configure(highlightbackground="#d9d9d9")
        self.Label_PerguntaValorCarga2.configure(highlightcolor="black")
        self.Label_PerguntaValorCarga2.configure(text='''Digite o valor da carga 2:''')


    def clicarBotaoCalcularAeB(self, rt):
        comprimento = self.Entry_ComprimentoBarra.get()
        carga = self.Entry_ValorCarga.get()

        checkComprimentoForLetters = comprimento.lower()
        checkCargaForLetters = carga.lower()
        comprimentoBool = checkComprimentoForLetters.islower()
        cargaBool = checkCargaForLetters.islower()


        if comprimentoBool or cargaBool or comprimento == '' or carga == '':
            self.criarPopUp(rt, message="Por favor digite um valor válido")
            return ["eu"]

        elif float(comprimento) <= 0:
            self.criarPopUp(rt, message="Por favor digite um valor maior que 0 para o comprimento")
            return ["eu"]

        elif float(carga) == 0:
            self.criarPopUp(rt, message="Por favor digite um valor diferente de 0 para a carga")
            return ["eu"]

        if comprimento.find('.'):
            convertComprimento = float(comprimento)
        else:
            convertComprimento = int(comprimento)
        if carga.find('.'):
            convertCarga = float(carga)
        else:
            convertCarga = int(carga)
        resultado = [convertComprimento, convertCarga]
        return resultado

    def clicarBotaoCalcularC(self, rt):
        comprimento = self.Entry_ComprimentoBarraC.get()

        carga1 = self.Entry_ValorCarga1.get()

        carga2 = self.Entry_ValorCarga2.get()

        transformComprimentoToString = comprimento.lower()
        transformCarga1ToString = carga1.lower()
        transformCarga2ToString = carga2.lower()
        comprimentoBool = transformComprimentoToString.islower()
        carga1Bool = transformCarga1ToString.islower()
        carga2Bool = transformCarga2ToString.islower()

        # if comprimento.isdigit() or carga1.isdigit() or carga2.isdigit() or\
        #         comprimento == "" or carga1 == "" or carga2 == "":
        # if comprimento.replace('.','', 1).isdigit()

        if comprimentoBool or carga1Bool or carga2Bool or comprimento == '' or carga1 == '' or carga2 == '':

            self.criarPopUp(rt, message="Por favor digite um valor válido")
            return ["erro"]
        elif float(comprimento) <= 0:

            self.criarPopUp(rt, message="Por favor digite um valor maior que 0 para o comprimento")
            return ["erro"]
        elif float(carga1) == 0 or float(carga2) == 0:

            self.criarPopUp(rt, message="Por favor digite um valor diferente de 0 para a(s) carga(s)")
            return ["erro"]
        elif float(carga2) < float(carga1):

            self.criarPopUp(rt, message="Carga 2 precisa ser maior do que carga 1")
            return ["eu"]

        if comprimento.find('.'):
            convertComprimento = float(comprimento)
        else:
            convertComprimento = int(comprimento)
        if carga1.find('.'):
            convertCarga1 = float(carga1)
        else:
            convertCarga2 = int(carga2)
        if carga1.find('.'):
            convertCarga2 = float(carga2)
        else:
            convertCarga2 = int(carga2)

        resultado = [convertComprimento, convertCarga1, convertCarga2]
        return resultado

    def realizarCalculoA(self, rt):
        valores = self.clicarBotaoCalcularAeB(rt)
        if (len(valores) > 1):
            comprimento = valores[0]
            carga = valores[1]
            calculo = cc.CalculoCargas.calculoEscolhaA(comprimento, carga)
            return calculo
        else:
            return [0]

    def realizarCalculoB(self, rt):
        valores = self.clicarBotaoCalcularAeB(rt)
        if len(valores) > 1:
            comprimento = valores[0]
            carga = valores[1]
            calculo = cc.CalculoCargas.calculoEscolhaB(comprimento, carga)
            return calculo
        else:
            return [0]

    def realizarCalculoC(self, rt):
        valores = self.clicarBotaoCalcularC(rt)
        if len(valores) > 1:
            comprimento = valores[0]
            carga1 = valores[1]
            carga2 = valores[2]
            calculo = cc.CalculoCargas.calculoEscolhaC(comprimento, carga1, carga2)
            return calculo
        else:
            return [0]


    def getsetarVariavelBotaoEscolha(self):
        radiobuttonvariable.get()
        self.toogleFrames()
        return radiobuttonvariable

    def toogleFrames(self):
        if (radiobuttonvariable.get() == 1) or (radiobuttonvariable.get() == 2):
            self.Frame_PerguntaC.place_forget()
            self.Frame_PerguntaAeB.place(frameAeBPlaceInfo)
        elif radiobuttonvariable.get() == 3:
            self.Frame_PerguntaAeB.place_forget()
            self.Frame_PerguntaC.place(frameCPlaceInfo)

    def criarGUIRespostaAeB(self, rt):
        buttonvalue = self.getsetarVariavelBotaoEscolha().get()
        calculo = [0]
        if buttonvalue == 1:
            calculo = self.realizarCalculoA(rt)

        elif buttonvalue == 2:
            calculo = self.realizarCalculoB(rt)
        elif buttonvalue == 0:
            self.criarPopUp(rt, message="Por favor escolha uma opção válida")
        if len(calculo) > 1:
            try:
                cargastr = str(self.arredondarNumero(calculo[1])) + " N"
                distanciastr = str(self.arredondarNumero(calculo[0])) + " m"

                createToplevelRespostaAeB(rt, buttonvalue, cargastr, distanciastr)
            except Exception as e:
                print(e, "exceção alguma coisa")

    def criarPopUp(self, rt, message):
        popup = Toplevel(rt)
        popup.wm_title("Escolha inválida")
        label = Label(popup, text=message)
        label.pack(fill="x", pady=30, padx=10)
        button = Button(popup, text="Ok", command=popup.destroy)
        button.pack(pady=10)

    def criarGUIRespostaC(self, rt):
        calculo = self.realizarCalculoC(rt)
        if len(calculo) > 1:
            carga1str = str(self.arredondarNumero(calculo[0][0])) + " N"
            carga2str = str(self.arredondarNumero(calculo[1][0])) + " N"
            distancia1str = str(self.arredondarNumero(calculo[0][1])) + " m"
            distancia2str = str(self.arredondarNumero(calculo[1][1])) + " m"

            createToplevelRespostaC(rt, carga1str, carga2str, distancia1str, distancia2str)

    def arredondarNumero(self, num):
        resultado = round(num, 3)
        return resultado


def create_MainGUIWindow(rt):
    w = MainGUIWindow(rt)
    return w

def destroy_MainGUIWindow():
    global w
    w.destroy()
    w = None
