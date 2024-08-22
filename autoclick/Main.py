import tkinter as tk
from tkinter import *
import time
import pyautogui

root = Tk()

class Application: # responsável por abrir a janela - Início
    def __init__(self):
        self.root = root
        self.Screen()
        self.widgets()

        root.mainloop() # mantém a janela aberta

    def autoclick_code(self): # código do autoclick
        espera = float(self.enty_espe_var.get())  # Recupera o valor do Entry e converte para float
        intervalo = float(self.enty_inter_var.get())  # Recupera o valor do Entry e converte para float
        duracao = float(self.enty_dura_var.get())  # Recupera o valor do Entry e converte para float

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
        atraso = float(self.enty_atra_var.get())
        rep = int(self.enty_rep_var.get())
        text = str(self.enty_text_var.get())
        intervalo = float(self.enty_inter_char_var.get())

        time.sleep(atraso)

        try:
            for _ in range(rep):
                pyautogui.typewrite(text, interval=intervalo)
                time.sleep(atraso)
        except KeyboardInterrupt:
            print("auto-type interrompido")

    def autoclick(self): # autoclick
        autoclick = tk.Toplevel()
        autoclick.title("Autoclicker")
        autoclick.minsize(530, 430)
        autoclick.resizable(False, False)
        autoclick.configure(background='#023059')

        Button(autoclick, text='[Excluir pagina]', command=autoclick.destroy).place(relx=0.02, rely=0.02, relwidth=0.2, relheight=0.1)

        self.au_click = Button(autoclick, text='iniciar autoclick', foreground='red', command=self.autoclick_code)
        self.au_click.place(relx=0.099, rely=0.2, relwidth=0.7, relheight=0.2)

        Label(autoclick, text="tempo antes de começar (segundo(s))").place(relx=0.05, rely=0.5, relwidth=0.4, relheight=0.1)
        # espera
        self.enty_espe_var = StringVar()
        self.enty_espe = Entry(autoclick, width=30, textvariable=self.enty_espe_var)
        self.enty_espe.insert(0, "10")
        self.enty_espe.place(relx=0.05, rely=0.6, relwidth=0.4, relheight=0.1)

        Label(autoclick, text="intervalo entre os clicks (segundo(s))").place(relx=0.05, rely=0.8, relwidth=0.4, relheight=0.1)
        # intervalo
        self.enty_inter_var = StringVar()
        self.enty_inter = Entry(autoclick, width=30, textvariable=self.enty_inter_var)
        self.enty_inter.insert(0, "10")
        self.enty_inter.place(relx=0.05, rely=0.9, relwidth=0.4, relheight=0.1)

        Label(autoclick, text="duração do autoclick (segundo(s))").place(relx=0.5, rely=0.8, relwidth=0.4, relheight=0.1)
        # duração
        self.enty_dura_var = StringVar()
        self.enty_dura = Entry(autoclick, width=30, textvariable=self.enty_dura_var)
        self.enty_dura.insert(0, "10")
        self.enty_dura.place(relx=0.5, rely=0.9, relwidth=0.4, relheight=0.1)

    def autotype(self): # autotype
        autotype = tk.Toplevel()
        autotype.title("Auto-Typer")
        autotype.minsize(590, 482)
        autotype.resizable(False, False)
        autotype.configure(background='#023059')

        Button(autotype, text='[Excluir pagina]', command=autotype.destroy).place(relx=0.02, rely=0.02, relwidth=0.2, relheight=0.1)

        self.au_type = Button(autotype, text="INICIAR AUTO-TYPE", foreground="red", command=self.autotype_code)
        self.au_type.place(relx=0.099, rely=0.2, relwidth=0.7, relheight=0.2)

        # atraso antes de começar o auto-type
        self.enty_atra_var = StringVar()
        Label(autotype, text="atraso antes de começar (segundo(s))").place(relx=0.05, rely=0.5, relwidth=0.4, relheight=0.1)
        self.enty_atraso = Entry(autotype, width=30, textvariable=self.enty_atra_var)
        self.enty_atraso.place(relx=0.05, rely=0.6, relwidth=0.4, relheight=0.1)

        # total de repetições
        self.enty_rep_var = StringVar()
        Label(autotype, text="Repetir").place(relx=0.05, rely=0.8, relwidth=0.4, relheight=0.1)
        self.enty_rep = Entry(autotype, width=30, textvariable=self.enty_rep_var)
        self.enty_rep.place(relx=0.05, rely=0.9, relwidth=0.4, relheight=0.1)

        # intervalo entre caracteres
        self.enty_inter_char_var = StringVar()
        Label(autotype, text="intervalo entre caracteres (segundo(s))").place(relx=0.5, rely=0.5, relwidth=0.4, relheight=0.1)
        self.enty_inter_char = Entry(autotype, width=30, textvariable=self.enty_inter_char_var)
        self.enty_inter_char.place(relx=0.5, rely=0.6, relwidth=0.4, relheight=0.1)

        # coloque a sequência de letras
        self.enty_text_var = StringVar()
        Label(autotype, text="caracteres/texto").place(relx=0.5, rely=0.8, relwidth=0.4, relheight=0.1)
        self.enty_text = Entry(autotype, width=30, textvariable=self.enty_text_var)
        self.enty_text.place(relx=0.5, rely=0.9, relwidth=0.4, relheight=0.1)

    def automation(self): # automação
        automation = tk.Toplevel()
        automation.title("Automação")
        automation.minsize(1100, 600)
        automation.resizable(True, True)
        automation.configure(background='#030833')

        Button(automation, text='[Excluir pagina]', command=automation.destroy).place(relx=0.02, rely=0.02, relwidth=0.2, relheight=0.1)

        #iniciar automation
        self.auto_ini = Button(automation, text="Iniciar Automation", foreground="blue")
        self.auto_ini.place(relx=0.00, rely=0.2, relwidth=0.3, relheight=0.1)


        # add acao mouse
        self.au_acao_mouse = Button(automation, text="adicionar Ação (mover mouse)", foreground="green")
        self.au_acao_mouse.place(relx=0.00, rely=0.3, relwidth=0.3, relheight=0.1)
        # add acao entry
        self.enty_auto_mousex = Entry(automation)
        self.enty_auto_mousex.place(relx=0.3, rely=0.3, relwidth=0.1, relheight=0.1)
        self.enty_auto_mousex.insert(0, "xxx")

        self.enty_auto_mousey = Entry(automation)
        self.enty_auto_mousey.place(relx=0.4, rely=0.3, relwidth=0.1, relheight=0.1)
        self.enty_auto_mousey.insert(0, "yyy")


        #click mouse
        self.auto_click_mouse = Button(automation, text="adicionar ação (click mouse)", foreground="green")
        self.auto_click_mouse.place(relx=0.00, rely=0.4, relwidth=0.3, relheight=0.1)


        #digitar texto
        self.auto_digit = Button(automation, text="adicionar Ação (digitar texto)", foreground="green")
        self.auto_digit.place(relx=0.00, rely=0.5, relwidth=0.3, relheight=0.1)
        self.enty_texto_auto = Entry(automation)
        self.enty_texto_auto.place(relx=0.3, rely=0.5, relwidth=0.2, relheight=0.1)

        # DEL ação
        self.au_ini = Button(automation, text="Deletar Ação", foreground="red")
        self.au_ini.place(relx=0.00, rely=0.6, relwidth=0.3, relheight=0.1)


        #Lista de açôes
        self.au_list = Listbox(automation)
        self.au_list.place(relx=0.6, rely=0.03, relwidth=0.4, relheight=0.9)

        self.au_list.insert(1, "inform1") #teste


    def Screen(self): # tela principal
        self.root.title("Fish-In-a-Bucket => Autoclick")
        self.root.minsize(380, 264)
        self.root.resizable(False, False)
        self.root.configure(background='#023059')

    def widgets(self): # tela principal
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
