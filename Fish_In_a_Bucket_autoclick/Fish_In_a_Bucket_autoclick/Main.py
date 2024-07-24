import tkinter
from tkinter import *
import time
import pyautogui
###########################

root = Tk()

intervalo = 0
duracao = 0
espera = 0

class Application():  #responsavel por abrir a janela - Inicio
    def __init__(self):
        self.root = root
        self.Screen() #puxa a função Screen()
        self.widgets() #puxa a função widgets()


        root.mainloop() #mantem a janela aberta

        # -# ############# Autoclicker: ############## #- #
    def autoclick(self):
        autoclick = tkinter.Toplevel()

        autoclick.title("Autoclicker")
        autoclick.minsize(400, 300)
        autoclick.resizable(False, False)

        autoclick.configure(background='#023059')

        Button(autoclick, text='[Excluir pagina]', command=autoclick.destroy).place(relx=0.02, rely=0.02, relwidth=0.2, relheight=0.1)
        #--#
        self.au_click = Button(autoclick, text='iniciar autoclick', foreground='red')
        self.au_click.place(relx=0.099, rely=0.2, relwidth=0.7, relheight=0.2)
    def autoclick_code(self):

        tempo_inicial = time.time()

        time.sleep(espera)
        try:
            while True:
                if (time.time() -
                        tempo_inicial > duracao):
                    break

                pyautogui.click()

                time.sleep(intervalo)

        except KeyboardInterrupt:
            print("auto-click interrompido")

        #print("auto-clicker finalizado")

    # -# ############# Auto-Type: ############## #- #
    def autotype(self):
        autotype = Tk()

        autotype.title("Auto-Typer")
        autotype.minsize(390, 282)
        autotype.resizable(False, False)

        autotype.configure(background='#023059')

        Button(autotype, text='[Excluir pagina]', command=autotype.destroy).place(relx=0.02, rely=0.02, relwidth=0.2, relheight=0.1)


    # -# ############# Automacao: ############## #- #
    def automation(self):
        automation = Tk()

        automation.title("Automação")
        automation.minsize(500, 500)
        automation.resizable(True, True)

        automation.configure(background='#030833')

        Button(automation, text='[Excluir pagina]', command=automation.destroy).place(relx=0.02, rely=0.02, relwidth=0.2, relheight=0.1)
        #--#

    def Screen(self): # tamanho da tela ; Titulo ; limite de tela ; Cor de Fundo ;
        self.root.title("Fish-In-a-Bucket => Autoclick")
        self.root.minsize(380, 264)
        self.root.resizable(False, False)

        self.root.configure(background='#023059')


    def widgets(self): # botoes ; Label ;
        self.lb_click = Label(text="leva para a tela de Autoclick")
        self.lb_click.place(relx=0.4, rely=0.02, relwidth=0.5, relheight=0.1)

        self.bt_CLICK = Button(root, text='[Tela] AUTOCLICK', command=self.autoclick)#
        self.bt_CLICK.place(relx=0.02, rely=0.02, relwidth=0.4, relheight=0.1)


        self.lb_click = Label(text="leva para a tela de Auto-Typer")
        self.lb_click.place(relx=0.4, rely=0.15, relwidth=0.5, relheight=0.1)

        self.bt_typer = Button(root, text='[Tela] AUTO-TYPER', command=self.autotype)#
        self.bt_typer.place(relx=0.02, rely=0.15, relwidth=0.4, relheight=0.1)

        self.lb_automation = Label(text="leva para a tela de Automação")
        self.lb_automation.place(relx=0.4, rely=0.28, relwidth=0.5, relheight=0.1)

        self.bt_automation = Button(root, text='[Tela] Automação', command=self.automation)#
        self.bt_automation.place(relx=0.02, rely=0.28, relwidth=0.4, relheight=0.1)






# _____________________________________________ #
Application() #abre a janela para o usuario
# _____________________________________________ #