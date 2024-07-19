from tkinter import *
###########################

root = Tk()

class Application(): #responsavel por abrir a janela (Inicio)
    def __init__(self):
        self.root = root
        self.Screen() # puxa a função Screen()
        self.widgets() # puxa a função widgets()

        root.mainloop() #mantem a janela aberta


    # -# ############# Autoclicker ############## #- #
    def autoclick(self):
        autoclick = Tk()

        autoclick.title("Autoclicker")
        autoclick.minsize(390, 282)
        autoclick.resizable(False, False)

        autoclick.configure(background='#023059')

        root.destroy()
    # -# ############# Autoclicker ############## #- #

    def Screen(self): # tamanho da tela ; Titulo ; limite de tela ; Cor de Fundo ;
        self.root.title("Fish-In-a-Bucket => Autoclick")
        self.root.minsize(380, 264)
        self.root.resizable(False, False)

        self.root.configure(background='#023059')


    def widgets(self): # botoes ; Label ;
        self.lb_click = Label(text="leva para a tela de Autoclick")
        self.lb_click.place(relx=0.4, rely=0.02, relwidth=0.5, relheight=0.1)

        self.bt_CLICK = Button(root, text='[Tela] AUTOCLICK', command=self.autoclick) #
        self.bt_CLICK.place(relx=0.02, rely=0.02, relwidth=0.4, relheight=0.1)


        self.lb_click = Label(text="leva para a tela de Auto-Typer")
        self.lb_click.place(relx=0.4, rely=0.15, relwidth=0.5, relheight=0.1)

        self.bt_typer = Button(text='[Tela] AUTO-TYPER')
        self.bt_typer.place(relx=0.02, rely=0.15, relwidth=0.4, relheight=0.1) #

        self.lb_automation = Label(text="leva para a tela de Automação")
        self.lb_automation.place(relx=0.4, rely=0.28, relwidth=0.5, relheight=0.1) #

        self.bt_automation = Button(text='[Tela] Automação')
        self.bt_automation.place(relx=0.02, rely=0.28, relwidth=0.4, relheight=0.1)







# _____________________________________________ #
Application() #abre a janela para o usuario
# _____________________________________________ #