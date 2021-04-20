from tkinter import  *

class ToplevelRespostaAeB:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x519+385+151")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Representação de Cargas")
        top.configure(background="#d9d9d9")

        self.Frame_ImagemResultado = Frame(top)
        self.Frame_ImagemResultado.place(relx=0.1, rely=0.116, relheight=0.578
                , relwidth=0.8)
        self.Frame_ImagemResultado.configure(relief='groove')
        self.Frame_ImagemResultado.configure(borderwidth="2")
        self.Frame_ImagemResultado.configure(relief="groove")
        self.Frame_ImagemResultado.configure(background="#d9d9d9")
        self.Frame_ImagemResultado.configure(cursor="fleur")

        self.Label_ImagemResposta = Label(self.Frame_ImagemResultado)
        self.Label_ImagemResposta.place(relx=0.0, rely=0.0, height=300, width=480)
        self.Label_ImagemResposta.configure(background="#d9d9d9")
        self.Label_ImagemResposta.configure(cursor="fleur")
        self.Label_ImagemResposta.configure(disabledforeground="#a3a3a3")
        self.Label_ImagemResposta.configure(foreground="#000000")
        imagepathA = "RespostaA.png"
        global imgA
        imgA = PhotoImage(file=imagepathA)

        imagepathB = "RespostaB.png"
        global imgB
        imgB = PhotoImage(file=imagepathB)

        self.Label_CargaResultante = Label(top)
        self.Label_CargaResultante.place(relx=0.1, rely=0.771, height=21
                , width=173)
        self.Label_CargaResultante.configure(background="#d9d9d9")
        self.Label_CargaResultante.configure(disabledforeground="#a3a3a3")
        self.Label_CargaResultante.configure(foreground="#000000")
        self.Label_CargaResultante.configure(text='''Intensidade da carga resultante:''')

        self.Label_DistanciaCarga = Label(top)
        self.Label_DistanciaCarga.place(relx=0.1, rely=0.848, height=21
                , width=245)
        self.Label_DistanciaCarga.configure(background="#d9d9d9")
        self.Label_DistanciaCarga.configure(disabledforeground="#a3a3a3")
        self.Label_DistanciaCarga.configure(foreground="#000000")
        self.Label_DistanciaCarga.configure(text='''Distância onde a carga será aplicada na barra:''')

        self.Label_CargaResultanteValor = Label(top)
        self.Label_CargaResultanteValor.place(relx=0.4, rely=0.771, height=21
                , width=134)
        self.Label_CargaResultanteValor.configure(background="#d9d9d9")
        self.Label_CargaResultanteValor.configure(disabledforeground="#a3a3a3")
        self.Label_CargaResultanteValor.configure(foreground="#000000")
        self.Label_CargaResultanteValor.configure(text='''Label''')

        self.Label_DistanciaCargaValor = Label(top)
        self.Label_DistanciaCargaValor.place(relx=0.533, rely=0.848, height=21
                                             , width=134)
        self.Label_DistanciaCargaValor.configure(background="#d9d9d9")
        self.Label_DistanciaCargaValor.configure(disabledforeground="#a3a3a3")
        self.Label_DistanciaCargaValor.configure(foreground="#000000")
        self.Label_DistanciaCargaValor.configure(text='''Label''')

        self.Label_DistanciaValor_Imagem = Label(top)
        self.Label_DistanciaValor_Imagem.place(relx=0.25, rely=0.617, height=21
                                               , width=100)
        self.Label_DistanciaValor_Imagem.configure(activebackground="#ffffff")
        self.Label_DistanciaValor_Imagem.configure(activeforeground="#ffffff")
        self.Label_DistanciaValor_Imagem.configure(background="#ffffff")
        self.Label_DistanciaValor_Imagem.configure(disabledforeground="#ffffff")
        self.Label_DistanciaValor_Imagem.configure(foreground="#000000")
        self.Label_DistanciaValor_Imagem.configure(highlightbackground="#ffffff")
        self.Label_DistanciaValor_Imagem.configure(highlightcolor="#000000")
        self.Label_DistanciaValor_Imagem.configure(text='''Distancia''')

        self.Label_CargaResultanteValor_Imagem = Label(top)
        self.Label_CargaResultanteValor_Imagem.place(relx=0.3, rely=0.347
                                                     , height=21, width=100)
        self.Label_CargaResultanteValor_Imagem.configure(background="#ffffff")
        self.Label_CargaResultanteValor_Imagem.configure(disabledforeground="#a3a3a3")
        self.Label_CargaResultanteValor_Imagem.configure(foreground="#000000")
        self.Label_CargaResultanteValor_Imagem.configure(text='''Carga''')


    def setarImagem(self, buttonvalue):
        if buttonvalue == 1:
            self.Label_ImagemResposta.configure(image=imgA)
        elif buttonvalue == 2:
            self.Label_ImagemResposta.configure(image=imgB)

    def setarValoresLabels(self, intensidadeCarga, distanciaCarga):
        self.Label_CargaResultanteValor.configure(text=intensidadeCarga)
        self.Label_CargaResultanteValor_Imagem.configure(text=intensidadeCarga)
        self.Label_DistanciaCargaValor.configure(text=distanciaCarga)
        self.Label_DistanciaValor_Imagem.configure(text=distanciaCarga)

w = None

def createToplevelRespostaAeB(rt, buttonvalue, intensidadeCarga, distanciaCarga):
    global w
    if w:
        w.destroy()
    w = Toplevel(rt)
    top = ToplevelRespostaAeB(w)
    top.setarImagem(buttonvalue)
    top.setarValoresLabels(intensidadeCarga, distanciaCarga)
    return w, top


def destroy_GUIResposta():
    global w
    w.destroy()
    w = None