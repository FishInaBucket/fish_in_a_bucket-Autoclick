import tkinter
from tkinter import *
import time
import pyautogui

root = Tk()

intervalo = 0
duracao = 0

class Application: #responsavel por abrir a janela - Inicio
    def __init__(self):
        self.root = root
        self.Screen()
        self.widgets()

        root.mainloop() #mantem a janela aberta

    def autoclick_code(self): #autoclick codigo
        espera = float(self.enty_espe_var.get())  # Recupera o valor do Entry e converte para inteiro
        intervalo = float(self.enty_inter_var.get())  # Recupera o valor do Entry e converte para inteiro
        duracao = float(self.enty_dura_var.get())  # Recupera o valor do Entry e converte para inteiro

        tempo_inicial = time.time()
        time.sleep(espera)

        try:
            while True:
                if (time.time() - tempo_inicial > duracao):
                    break
                pyautogui.click()
                time.sleep(intervalo)
        except KeyboardInterrupt:
            print("auto-click interrompido")

    def autotype_code(self):
        global atraso, rep, text

        atraso = float(self.enty_atra_var.get())
        rep = float(self.enty_rep_var.get())
        text = str(self.enty_text_var.get())



    def autoclick(self): #autoclick
        autoclick = tkinter.Toplevel()
        autoclick.title("Autoclicker")
        autoclick.minsize(530, 430)
        autoclick.resizable(False, False)
        autoclick.configure(background='#023059')

        Button(autoclick, text='[Excluir pagina]', command=autoclick.destroy).place(relx=0.02, rely=0.02, relwidth=0.2, relheight=0.1)

        self.au_click = Button(autoclick, text='iniciar autoclick', foreground='red', command=self.autoclick_code)
        self.au_click.place(relx=0.099, rely=0.2, relwidth=0.7, relheight=0.2)

        Label(autoclick, text="tempo antes de começar (segundo(s))").place(relx=0.05, rely=0.5, relwidth=0.4, relheight=0.1)
        #espera
        self.enty_espe_var = StringVar()
        self.enty_espe = Entry(autoclick, width=30, textvariable=self.enty_espe_var)
        self.enty_espe.insert(0, "10")
        self.enty_espe.place(relx=0.05, rely=0.6, relwidth=0.4, relheight=0.1)

        Label(autoclick, text="intervalo entre os clicks (segundo(s))").place(relx=0.05, rely=0.8, relwidth=0.4, relheight=0.1)
        #intervalo
        self.enty_inter_var = StringVar()
        self.enty_inter = Entry(autoclick, width=30, textvariable=self.enty_inter_var)
        self.enty_inter.insert(0, "10")
        self.enty_inter.place(relx=0.05, rely=0.9, relwidth=0.4, relheight=0.1)

        Label(autoclick, text="duração do autoclick (segundo(s))").place(relx=0.5, rely=0.8, relwidth=0.4, relheight=0.1)
        #duração
        self.enty_dura_var = StringVar()
        self.enty_dura = Entry(autoclick, width=30, textvariable=self.enty_dura_var)
        self.enty_dura.insert(0, "10")
        self.enty_dura.place(relx=0.5, rely=0.9, relwidth=0.4, relheight=0.1)

    def autotype(self): #autotype
        autotype = Tk()
        autotype.title("Auto-Typer")
        autotype.minsize(590, 482)
        autotype.resizable(False, False)
        autotype.configure(background='#023059')

        Button(autotype, text='[Excluir pagina]', command=autotype.destroy).place(relx=0.02, rely=0.02, relwidth=0.2, relheight=0.1)

        self.au_type = Button(autotype, text="INICIAR AUTO-TYPE", foreground="red", command=self.autotype_code)
        self.au_type.place(relx=0.099, rely=0.2, relwidth=0.7, relheight=0.2)

        # atraso antes de comecar o auto-type
        self.enty_atra_var = StringVar()
        Label(autotype, text="atraso antes de começar (segundo(s))").place(relx=0.05, rely=0.5, relwidth=0.4, relheight=0.1)
        self.enty_atraso = Entry(autotype, width=30, textvariable=self.enty_atra_var)
        self.enty_atraso.place(relx=0.05, rely=0.6, relwidth=0.4, relheight=0.1)

        # total de repeticoes
        self.enty_rep_var = StringVar()
        Label(autotype, text="Repetir").place(relx=0.05, rely=0.8, relwidth=0.4, relheight=0.1)
        self.enty_rep = Entry(autotype, width=30, textvariable=self.enty_rep_var)
        self.enty_rep.place(relx=0.05, rely=0.9, relwidth=0.4, relheight=0.1)

        #coloque a sequencia de letras
        self.enty_text_var = StringVar()
        Label(autotype, text="caracteres/texto").place(relx=0.5, rely=0.8, relwidth=0.4, relheight=0.1)
        self.enty_text = Entry(autotype, width=30, textvariable=self.enty_text_var)
        self.enty_text.place(relx=0.5, rely=0.9, relwidth=0.4, relheight=0.1)

    def automation(self): #automacao
        automation = Tk()
        automation.title("Automação")
        automation.minsize(500, 500)
        automation.resizable(True, True)
        automation.configure(background='#030833')

        Button(automation, text='[Excluir pagina]', command=automation.destroy).place(relx=0.02, rely=0.02, relwidth=0.2, relheight=0.1)

    def Screen(self): #tela principal
        self.root.title("Fish-In-a-Bucket => Autoclick")
        self.root.minsize(380, 264)
        self.root.resizable(False, False)
        self.root.configure(background='#023059')

    def widgets(self): #tela principal
        self.lb_click = Label(text="leva para a tela de Autoclick")
        self.lb_click.place(relx=0.4, rely=0.02, relwidth=0.5, relheight=0.1)

        self.bt_CLICK = Button(root, text='[Tela] AUTOCLICK', command=self.autoclick)
        self.bt_CLICK.place(relx=0.02, rely=0.02, relwidth=0.4, relheight=0.1)

        self.lb_click = Label(text="leva para a tela de Auto-Typer")
        self.lb_click.place(relx=0.4, rely=0.15, relwidth=0.5, relheight=0.1)

        self.bt_typer = Button(root, text='[Tela] AUTO-TYPER', command=self.autotype)
        self.bt_typer.place(relx=0.02, rely=0.15, relwidth=0.4, relheight=0.1)

        self.lb_automation = Label(text="leva para a tela de Automação")
        self.lb_automation.place(relx=0.4, rely=0.28, relwidth=0.5, relheight=0.1)

        self.bt_automation = Button(root, text='[Tela] Automação', command=self.automation)
        self.bt_automation.place(relx=0.02, rely=0.28, relwidth=0.4, relheight=0.1)

Application()