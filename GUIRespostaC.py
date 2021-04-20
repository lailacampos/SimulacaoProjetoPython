from tkinter import  *
import CalculoCargas as cc

class ToplevelRespostaC:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x519+365+64")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Representação de Cargas")
        top.configure(background="#d9d9d9")

        self.Imagem_ResultadoC = Frame(top)
        self.Imagem_ResultadoC.place(relx=0.1, rely=0.116, relheight=0.578
                , relwidth=0.8)
        self.Imagem_ResultadoC.configure(relief='groove')
        self.Imagem_ResultadoC.configure(borderwidth="2")
        self.Imagem_ResultadoC.configure(relief="groove")
        self.Imagem_ResultadoC.configure(background="#d9d9d9")

        self.Label_ImagemResposta = Label(self.Imagem_ResultadoC)
        self.Label_ImagemResposta.place(relx=0.0, rely=0.0, height=300, width=480)
        self.Label_ImagemResposta.configure(background="#d9d9d9")
        self.Label_ImagemResposta.configure(disabledforeground="#a3a3a3")
        self.Label_ImagemResposta.configure(foreground="#000000")
        imagepath = "RespostaC.png"
        global img
        img = PhotoImage(file=imagepath)
        self.Label_ImagemResposta.configure(image=img)

        self.Label_Carga1Resultante = Label(top)
        self.Label_Carga1Resultante.place(relx=0.1, rely=0.771, height=21
                , width=127)
        self.Label_Carga1Resultante.configure(background="#d9d9d9")
        self.Label_Carga1Resultante.configure(disabledforeground="#a3a3a3")
        self.Label_Carga1Resultante.configure(foreground="#000000")
        self.Label_Carga1Resultante.configure(text='''Intensidade da carga 1:''')

        self.Label_Carga2Resultante = Label(top)
        self.Label_Carga2Resultante.place(relx=0.1, rely=0.848, height=21
                , width=127)
        self.Label_Carga2Resultante.configure(background="#d9d9d9")
        self.Label_Carga2Resultante.configure(disabledforeground="#a3a3a3")
        self.Label_Carga2Resultante.configure(foreground="#000000")
        self.Label_Carga2Resultante.configure(text='''Intensidade da carga 2:''')

        self.Label_ValorCarga1 = Label(top)
        self.Label_ValorCarga1.place(relx=0.317, rely=0.771, height=21, width=55)

        self.Label_ValorCarga1.configure(anchor='w')
        self.Label_ValorCarga1.configure(background="#d9d9d9")
        self.Label_ValorCarga1.configure(disabledforeground="#a3a3a3")
        self.Label_ValorCarga1.configure(foreground="#000000")
        self.Label_ValorCarga1.configure(text='''Label''')

        self.Label_ValorCarga2 = Label(top)
        self.Label_ValorCarga2.place(relx=0.317, rely=0.848, height=21, width=55)

        self.Label_ValorCarga2.configure(anchor='w')
        self.Label_ValorCarga2.configure(background="#d9d9d9")
        self.Label_ValorCarga2.configure(disabledforeground="#a3a3a3")
        self.Label_ValorCarga2.configure(foreground="#000000")
        self.Label_ValorCarga2.configure(text='''Label''')

        self.Label_DistanciaCarga1 = Label(top)
        self.Label_DistanciaCarga1.place(relx=0.433, rely=0.771, height=21
                , width=208)
        self.Label_DistanciaCarga1.configure(background="#d9d9d9")
        self.Label_DistanciaCarga1.configure(disabledforeground="#a3a3a3")
        self.Label_DistanciaCarga1.configure(foreground="#000000")
        self.Label_DistanciaCarga1.configure(text='''Distância onde a carga 1 será aplicada:''')

        self.Label_DistanciaCarga2 = Label(top)
        self.Label_DistanciaCarga2.place(relx=0.433, rely=0.848, height=21
                , width=208)
        self.Label_DistanciaCarga2.configure(background="#d9d9d9")
        self.Label_DistanciaCarga2.configure(disabledforeground="#a3a3a3")
        self.Label_DistanciaCarga2.configure(foreground="#000000")
        self.Label_DistanciaCarga2.configure(text='''Distância onde a carga 2 será aplicada:''')

        self.Label_ValorDistanciaCarga1 = Label(top)
        self.Label_ValorDistanciaCarga1.place(relx=0.783, rely=0.771, height=21
                , width=55)
        self.Label_ValorDistanciaCarga1.configure(anchor='w')
        self.Label_ValorDistanciaCarga1.configure(background="#d9d9d9")
        self.Label_ValorDistanciaCarga1.configure(disabledforeground="#a3a3a3")
        self.Label_ValorDistanciaCarga1.configure(foreground="#000000")
        self.Label_ValorDistanciaCarga1.configure(text='''Label''')

        self.Label_ValorDistanciaCarga2 = Label(top)
        self.Label_ValorDistanciaCarga2.place(relx=0.783, rely=0.848, height=21
                , width=55)
        self.Label_ValorDistanciaCarga2.configure(anchor='w')
        self.Label_ValorDistanciaCarga2.configure(background="#d9d9d9")
        self.Label_ValorDistanciaCarga2.configure(disabledforeground="#a3a3a3")
        self.Label_ValorDistanciaCarga2.configure(foreground="#000000")
        self.Label_ValorDistanciaCarga2.configure(text='''Label''')

        self.Label_DistanciaValorCarga1_Imagem = Label(top)
        self.Label_DistanciaValorCarga1_Imagem.place(relx=0.25, rely=0.559
                , height=21, width=100)
        self.Label_DistanciaValorCarga1_Imagem.configure(activebackground="#ffffff")
        self.Label_DistanciaValorCarga1_Imagem.configure(activeforeground="#ffffff")
        self.Label_DistanciaValorCarga1_Imagem.configure(background="#ffffff")
        self.Label_DistanciaValorCarga1_Imagem.configure(disabledforeground="#ffffff")
        self.Label_DistanciaValorCarga1_Imagem.configure(foreground="#000000")
        self.Label_DistanciaValorCarga1_Imagem.configure(highlightbackground="#ffffff")
        self.Label_DistanciaValorCarga1_Imagem.configure(highlightcolor="#000000")
        self.Label_DistanciaValorCarga1_Imagem.configure(text='''Distancia 1''')

        self.Label_CargaResultanteValor1_Imagem = Label(top)
        self.Label_CargaResultanteValor1_Imagem.place(relx=0.3, rely=0.347
                , height=21, width=100)
        self.Label_CargaResultanteValor1_Imagem.configure(background="#ffffff")
        self.Label_CargaResultanteValor1_Imagem.configure(disabledforeground="#a3a3a3")
        self.Label_CargaResultanteValor1_Imagem.configure(foreground="#000000")
        self.Label_CargaResultanteValor1_Imagem.configure(text='''Carga 1''')

        self.Label_DistanciaValorCarga2_Imagem = Label(top)
        self.Label_DistanciaValorCarga2_Imagem.place(relx=0.633, rely=0.559
                , height=21, width=100)
        self.Label_DistanciaValorCarga2_Imagem.configure(activebackground="#ffffff")
        self.Label_DistanciaValorCarga2_Imagem.configure(activeforeground="#ffffff")
        self.Label_DistanciaValorCarga2_Imagem.configure(background="#ffffff")
        self.Label_DistanciaValorCarga2_Imagem.configure(disabledforeground="#ffffff")
        self.Label_DistanciaValorCarga2_Imagem.configure(foreground="#000000")
        self.Label_DistanciaValorCarga2_Imagem.configure(highlightbackground="#ffffff")
        self.Label_DistanciaValorCarga2_Imagem.configure(highlightcolor="#000000")
        self.Label_DistanciaValorCarga2_Imagem.configure(text='''Distancia 2''')

        self.Label_CargaResultanteValor2_Imagem = Label(top)
        self.Label_CargaResultanteValor2_Imagem.place(relx=0.635, rely=0.347
                , height=21, width=100)
        self.Label_CargaResultanteValor2_Imagem.configure(activebackground="#f9f9f9")
        self.Label_CargaResultanteValor2_Imagem.configure(activeforeground="black")
        self.Label_CargaResultanteValor2_Imagem.configure(background="#ffffff")
        self.Label_CargaResultanteValor2_Imagem.configure(disabledforeground="#a3a3a3")
        self.Label_CargaResultanteValor2_Imagem.configure(foreground="#000000")
        self.Label_CargaResultanteValor2_Imagem.configure(highlightbackground="#d9d9d9")
        self.Label_CargaResultanteValor2_Imagem.configure(highlightcolor="black")
        self.Label_CargaResultanteValor2_Imagem.configure(text='''Carga 2''')


    def setarValoresLabels(self, intensidadeCarga1, intensidadeCarga2, distanciaForca1, distanciaForca2):
        self.Label_ValorCarga1.configure(text=intensidadeCarga1)
        self.Label_CargaResultanteValor1_Imagem.configure(text=intensidadeCarga1)
        self.Label_ValorCarga2.configure(text=intensidadeCarga2)
        self.Label_CargaResultanteValor2_Imagem.configure(text=intensidadeCarga2)
        self.Label_ValorDistanciaCarga1.configure(text=distanciaForca1)
        self.Label_DistanciaValorCarga1_Imagem.configure(text=distanciaForca1)
        self.Label_ValorDistanciaCarga2.configure(text=distanciaForca2)
        self.Label_DistanciaValorCarga2_Imagem.configure(text=distanciaForca2)

w = None

def createToplevelRespostaC(rt, intensidadeCarga1, intensidadeCarga2, distanciaCarga1, distanciaCarga2):
    global w
    if w:
        w.destroy()
    w = Toplevel(rt)
    top = ToplevelRespostaC(w)
    top.setarValoresLabels(intensidadeCarga1, intensidadeCarga2, distanciaCarga1, distanciaCarga2)
    return w, top