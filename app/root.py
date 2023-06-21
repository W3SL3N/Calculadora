from tkinter import Tk, Frame, Entry, Label, PhotoImage, Button, font, RIGHT
from ctypes import windll, c_int, byref, sizeof
from math import pi
from app.calculos import *


class Root(Calculos):
    def __init__(self):
        super().__init__()
        self.root = Tk()

        self.root.withdraw()  # Oculta a janela temporariamente.

        self.cria_tela()
        self.entry_numeros = None
        self.fonte_entry = None
        self.label_operacao = None
        self.frame_botoes = None
        self.frame_numeros = None
        self.frame_operacoes = None
        self.cria_frames()
        self.cria_widgets()

        self.root.deiconify()  # Exibe a janela após os métodos anteriores serem executados.

        self.root.mainloop()

    def cria_tela(self):
        """
        Definição da janela
        """

        largura, altura = 304, 433

        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()

        x = (ws / 2) - (largura / 2)
        y = (hs / 2) - (altura / 2)

        self.root.geometry('%dx%d+%d+%d' % (largura, altura, x, y))
        self.root.title('Calculadora')
        self.root.iconbitmap("icon\icone.ico")

        self.root.configure(background='#202020')
        self.root.resizable(False, False)

        # Faz a topbar seguir o tema de cores do windows.
        set_window_attribute = windll.dwmapi.DwmSetWindowAttribute
        get_parent = windll.user32.GetParent
        hwnd = get_parent(self.root.winfo_id())
        rendering_policy = 20
        value = 2
        value = c_int(value)
        set_window_attribute(hwnd, rendering_policy, byref(value), sizeof(value))

    def cria_frames(self):
        """
        Divide a janela em containers
        """

        # Frame reservado para a operação em andamento
        self.frame_operacoes = Frame(self.root, bg='#202020', padx=6)
        self.frame_operacoes.place(width=304, height=50)

        # Frame reservado para receber a entrada do usuário
        self.frame_numeros = Frame(self.root, bg='#202020', padx=5)
        self.frame_numeros.place(width=304, height=70, rely=0.1)

        # Frame reservado para todos os botões
        self.frame_botoes = Frame(self.root, bg='#1d1d1d')
        self.frame_botoes.place(width=304, height=317, rely=0.27)

    def cria_widgets(self):
        """
        Engloba criação, configuração e posicionamento da label, entry e buttons
        """

        # Label: Criação, Configuração, Fonte
        self.label_operacao = Label(self.frame_operacoes)
        fonte_label = font.Font(family='Arial Unicode MS', size=11, weight='bold')
        self.label_operacao.config(font=fonte_label, fg='#606060', background='#202020', anchor='e')
        self.label_operacao.place(relwidth=1, relheight=1)

        # Entry: Criação, Configuração, Fonte
        self.entry_numeros = Entry(self.frame_numeros)
        self.entry_numeros.bind('<Key>', func=lambda x: 'break')
        self.fonte_entry = font.Font(family='Arial Unicode MS', size=27, weight='bold')
        self.entry_numeros.config(background='#1d1d1d', fg='white', bd=0, justify=RIGHT, font=self.fonte_entry)
        self.entry_numeros.config(insertbackground='#1d1d1d')
        self.entry_numeros.place(relwidth=1, relheight=1)
        self.entry_numeros.insert(0, '0')

        # números: Criação
        bt7 = Button(self.frame_botoes)
        bt8 = Button(self.frame_botoes)
        bt9 = Button(self.frame_botoes)
        bt4 = Button(self.frame_botoes)
        bt5 = Button(self.frame_botoes)
        bt6 = Button(self.frame_botoes)
        bt1 = Button(self.frame_botoes)
        bt2 = Button(self.frame_botoes)
        bt3 = Button(self.frame_botoes)
        bt0 = Button(self.frame_botoes)

        # números: Imagens
        self.root.img_bt0 = PhotoImage(file="img/bt0.png")
        self.root.img_bt1 = PhotoImage(file="img/bt1.png")
        self.root.img_bt2 = PhotoImage(file="img/bt2.png")
        self.root.img_bt3 = PhotoImage(file="img/bt3.png")
        self.root.img_bt4 = PhotoImage(file="img/bt4.png")
        self.root.img_bt5 = PhotoImage(file="img/bt5.png")
        self.root.img_bt6 = PhotoImage(file="img/bt6.png")
        self.root.img_bt7 = PhotoImage(file="img/bt7.png")
        self.root.img_bt8 = PhotoImage(file="img/bt8.png")
        self.root.img_bt9 = PhotoImage(file="img/bt9.png")

        # números: Configuração
        bt0.config(bg='#1D1D1D', bd=0, image=self.root.img_bt0, activebackground='#1d1d1d')
        bt1.config(bg='#1D1D1D', bd=0, image=self.root.img_bt1, activebackground='#1d1d1d')
        bt2.config(bg='#1D1D1D', bd=0, image=self.root.img_bt2, activebackground='#1d1d1d')
        bt3.config(bg='#1D1D1D', bd=0, image=self.root.img_bt3, activebackground='#1d1d1d')
        bt4.config(bg='#1D1D1D', bd=0, image=self.root.img_bt4, activebackground='#1d1d1d')
        bt5.config(bg='#1D1D1D', bd=0, image=self.root.img_bt5, activebackground='#1d1d1d')
        bt6.config(bg='#1D1D1D', bd=0, image=self.root.img_bt6, activebackground='#1d1d1d')
        bt7.config(bg='#1D1D1D', bd=0, image=self.root.img_bt7, activebackground='#1d1d1d')
        bt8.config(bg='#1D1D1D', bd=0, image=self.root.img_bt8, activebackground='#1d1d1d')
        bt9.config(bg='#1D1D1D', bd=0, image=self.root.img_bt9, activebackground='#1d1d1d')

        # números: Configuração(comandos):
        bt0.config(command=lambda: self.set_valor_entrada('0'))
        bt1.config(command=lambda: self.set_valor_entrada('1'))
        bt2.config(command=lambda: self.set_valor_entrada('2'))
        bt3.config(command=lambda: self.set_valor_entrada('3'))
        bt4.config(command=lambda: self.set_valor_entrada('4'))
        bt5.config(command=lambda: self.set_valor_entrada('5'))
        bt6.config(command=lambda: self.set_valor_entrada('6'))
        bt7.config(command=lambda: self.set_valor_entrada('7'))
        bt8.config(command=lambda: self.set_valor_entrada('8'))
        bt9.config(command=lambda: self.set_valor_entrada('9'))

        # números: Binds
        self.root.bind('<Key-0>', lambda x: self.set_valor_entrada('0'))
        self.root.bind('<Key-1>', lambda x: self.set_valor_entrada('1'))
        self.root.bind('<Key-2>', lambda x: self.set_valor_entrada('2'))
        self.root.bind('<Key-3>', lambda x: self.set_valor_entrada('3'))
        self.root.bind('<Key-4>', lambda x: self.set_valor_entrada('4'))
        self.root.bind('<Key-5>', lambda x: self.set_valor_entrada('5'))
        self.root.bind('<Key-6>', lambda x: self.set_valor_entrada('6'))
        self.root.bind('<Key-7>', lambda x: self.set_valor_entrada('7'))
        self.root.bind('<Key-8>', lambda x: self.set_valor_entrada('8'))
        self.root.bind('<Key-9>', lambda x: self.set_valor_entrada('9'))

        # números: Posição
        bt1.grid(row=4, column=0, ipady=2)
        bt2.grid(row=4, column=1)
        bt3.grid(row=4, column=2)
        bt4.grid(row=3, column=0)
        bt5.grid(row=3, column=1)
        bt6.grid(row=3, column=2)
        bt7.grid(row=2, column=0, ipadx=2, ipady=2)
        bt8.grid(row=2, column=1)
        bt9.grid(row=2, column=2, ipadx=2)
        bt0.grid(row=5, column=1)

        # operações: Criação
        bt_maismenos = Button(self.frame_botoes)
        bt_porcent = Button(self.frame_botoes)
        bt_raiz = Button(self.frame_botoes)
        bt_divisao = Button(self.frame_botoes)
        bt_multiplicacao = Button(self.frame_botoes)
        bt_subtracao = Button(self.frame_botoes)
        bt_adicao = Button(self.frame_botoes)
        bt_ponto = Button(self.frame_botoes)
        bt_igual = Button(self.frame_botoes)
        bt_eleva = Button(self.frame_botoes)
        bt_pi = Button(self.frame_botoes)

        # operações: Fontes
        fonte_pi = font.Font(family='Symbol', size=16, weight='bold')
        fonte = font.Font(family='Arial Unicode MS', size=16, weight='bold')
        fonte_raiz = font.Font(family='@Arial Unicode MS', size=16, weight='bold')

        # operações: Configuração
        bt_maismenos.config(bd=0, text='±', font=fonte)
        bt_porcent.config(bd=0, text='%', font=fonte)
        bt_raiz.config(bd=0, text='²√', font=fonte_raiz)
        bt_divisao.config(bd=0, text='÷', font=fonte)
        bt_multiplicacao.config(bd=0, text='×', font=fonte)
        bt_subtracao.config(bd=0, text='-', font=fonte)
        bt_adicao.config(bd=0, text='+', font=fonte)
        bt_ponto.config(bd=0, text=',', font=fonte)
        bt_igual.config(bd=0, text='=', font=fonte)
        bt_eleva.config(bd=0, text='x²', font=fonte)
        bt_pi.config(bd=0, text='π', font=fonte_pi)

        # operações: Cores
        bt_maismenos.config(bg='#1D1D1D', fg='white', activebackground='#1d1d1d', activeforeground='#606060')
        bt_porcent.config(bg='#1D1D1D', fg='white', activebackground='#1d1d1d', activeforeground='#606060')
        bt_raiz.config(bg='#1D1D1D', fg='white', activebackground='#1d1d1d', activeforeground='#606060')
        bt_divisao.config(bg='#1D1D1D', fg='white', activebackground='#1d1d1d', activeforeground='#606060')
        bt_multiplicacao.config(bg='#1D1D1D', fg='white', activebackground='#1D1D1D', activeforeground='#606060')
        bt_subtracao.config(bg='#1D1D1D', fg='white', activebackground='#1D1D1D', activeforeground='#606060')
        bt_adicao.config(bg='#1D1D1D', fg='white', activebackground='#1D1D1D', activeforeground='#606060')
        bt_ponto.config(bg='#1D1D1D', fg='white', activebackground='#1d1d1d', activeforeground='#606060')
        bt_igual.config(bg='#1D1D1D', fg='white', activebackground='#1D1D1D', activeforeground='#606060')
        bt_eleva.config(bg='#1D1D1D', fg='white', activebackground='#1d1d1d', activeforeground='#606060')
        bt_pi.config(bg='#1D1D1D', fg='white', activebackground='#1d1d1d', activeforeground='#606060')

        # operações: Configuração(comandos)
        bt_adicao.config(command=lambda: self.set_operadores('+'))
        bt_subtracao.config(command=lambda: self.set_operadores('-'))
        bt_multiplicacao.config(command=lambda: self.set_operadores('×'))
        bt_divisao.config(command=lambda: self.set_operadores('÷'))
        bt_raiz.config(command=lambda: self.faz_raiz())
        bt_igual.config(command=lambda: self.faz_calculo())
        bt_ponto.config(command=lambda: self.add_ponto_flutuante())
        bt_porcent.config(command=lambda: self.faz_porcentagem())
        bt_maismenos.config(command=lambda: self.set_negativo())
        bt_pi.config(command=lambda: self.set_valor_entrada(str(pi).replace('.', ',')))
        bt_eleva.config(command=lambda: self.faz_potencia())

        # operações: Binds
        self.root.bind('<asterisk>', lambda x: self.set_operadores('×'))
        self.root.bind('<slash>', lambda x: self.set_operadores('÷'))
        self.root.bind('<plus>', lambda x: self.set_operadores('+'))
        self.root.bind('<minus>', lambda x: self.set_operadores('-'))
        self.root.bind('<percent>', lambda x: self.faz_porcentagem())
        self.root.bind('<comma>', lambda x: self.add_ponto_flutuante())
        self.root.bind('<period>', lambda x: self.add_ponto_flutuante())
        self.root.bind('<Return>', lambda x: self.faz_calculo())
        self.root.bind('<equal>', lambda x: self.faz_calculo())
        self.root.bind('<Control-c>', lambda x: self.root.clipboard_append(self.entry_numeros.get()))

        # operações: Posição
        bt_maismenos.grid(row=5, column=0, sticky='nsew')
        bt_porcent.grid(row=1, column=1, sticky='nsew')
        bt_raiz.grid(row=1, column=2, sticky='nsew')
        bt_divisao.grid(row=1, column=3, sticky='nsew')
        bt_multiplicacao.grid(row=2, column=3, sticky='nsew')
        bt_subtracao.grid(row=3, column=3, sticky='nsew')
        bt_adicao.grid(row=4, column=3, sticky='nsew')
        bt_ponto.grid(row=5, column=2, sticky='nsew')
        bt_igual.grid(row=5, column=3, sticky='nsew')
        bt_eleva.grid(row=1, column=0, sticky='nsew')
        bt_pi.grid(row=0, column=0, sticky='nsew')

        # redefinição: Criação
        bt_c = Button(self.frame_botoes)
        bt_ce = Button(self.frame_botoes)
        bt_del = Button(self.frame_botoes)

        # redefinição: Fonte
        fonte_redef = font.Font(family='@Arial Unicode MS', size=16, weight='bold')

        # redefinição: Configuração
        bt_c.config(bd=0, text='C', font=fonte_redef)
        bt_ce.config(bd=0, text='CE', font=fonte_redef)
        bt_del.config(bd=0, text='⌫', font=fonte_redef)

        # redefinição: Cores
        bt_c.config(bg='#1D1D1D', fg='white', activebackground='#1d1d1d', activeforeground='#606060')
        bt_ce.config(bg='#1D1D1D', fg='white', activebackground='#1d1d1d', activeforeground='#606060')
        bt_del.config(bg='#1D1D1D', fg='white', activebackground='#1d1d1d', activeforeground='#a51b0b')

        # redefinição: Configuração(comandos)
        bt_c.config(command=lambda: self.deleta_c())
        bt_ce.config(command=lambda: self.deleta_ce())
        bt_del.config(command=lambda: self.deleta_digito())

        # redefinição: Bind
        self.root.bind('<BackSpace>', lambda x: self.deleta_digito())

        # redefinição: Posição
        bt_c.grid(row=0, column=1, sticky='nsew')
        bt_ce.grid(row=0, column=2, sticky='nsew')
        bt_del.grid(row=0, column=3, sticky='nsew', padx=10)

    def deleta_digito(self):
        """
        Deleta um caractere por clique,
        verifica se há uma resposta para uma operação, se sim ativa o método "deleta_c()".
        """
        if len(self.resultado) > 0:
            self.deleta_c()
        else:
            self.entry_numeros.delete(len(self.entry_numeros.get()) - 1)
            self.altera_fonte()
            if len(self.entry_numeros.get()) == 0 and len(self.numero1) < 1:
                self.entry_numeros.insert(0, '0')

            if len(self.numero1) < 1:
                if self.entry_numeros.get() == '-':
                    self.entry_numeros.delete(0, len(self.entry_numeros.get()))
                    self.entry_numeros.insert(0, '0')
                elif self.entry_numeros.get() == '-0,':
                    self.entry_numeros.delete(0, len(self.entry_numeros.get()))
                    self.entry_numeros.insert(0, '0,')

            elif len(self.numero1) > 0:
                if self.entry_numeros.get() == '-':
                    self.entry_numeros.delete(0, len(self.entry_numeros.get()))
                elif self.entry_numeros.get() == '-0,':
                    self.entry_numeros.delete(0, len(self.entry_numeros.get()))
                    self.entry_numeros.insert(0, '0,')

    def deleta_c(self):
        """
        Limpa a tela e todas as variáveis
        """
        self.label_operacao.config(text='')
        self.entry_numeros.delete(0, len(self.entry_numeros.get()))
        self.numero1 = ''
        self.numero2 = ''
        self.resultado = ''
        self.entry_numeros.insert(0, '0')
        self.altera_fonte()

    def deleta_ce(self):
        """
        Limpa a entry, verifica se há uma resposta para uma operação, se sim o método "deleta_c()".
        """
        if len(self.resultado) > 0:
            self.deleta_c()
        else:
            if len(self.numero1) > 0:
                self.entry_numeros.delete(0, len(self.entry_numeros.get()))
            if len(self.numero1) < 1:
                self.entry_numeros.delete(0, len(self.entry_numeros.get()))
                self.entry_numeros.insert(0, '0')
            self.altera_fonte()

    def set_negativo(self):
        """
        Insere e remove o símbolo de negação dos números da entry.
        Executa verificações diversas para evitar erros.
        """
        self.verifica_entry(False)

        if 'e' in self.entry_numeros.get():
            if '-' in self.entry_numeros.get()[0]:
                self.label_operacao.config(text='')
                self.entry_numeros.delete(0, 1)
                self.numero1 = ''
                self.numero2 = ''
            elif '-' not in self.entry_numeros.get()[0]:
                self.label_operacao.config(text='')
                self.entry_numeros.insert(0, '-')
                self.numero1 = ''
                self.numero2 = ''

        elif ',' in self.entry_numeros.get():
            testa = sum([int(self.entry_numeros.get().replace(',', ''))])
            if testa > 0:
                if len(self.resultado) > 0:
                    self.label_operacao.config(text='')
                    self.numero1 = ''
                    self.numero2 = ''
                    self.resultado = ''
                    self.altera_fonte()
                self.entry_numeros.insert(0, '-')
            elif '-' in self.entry_numeros.get():
                if len(self.resultado) > 0:
                    self.label_operacao.config(text='')
                    self.numero1 = ''
                    self.numero2 = ''
                    self.resultado = ''
                    self.altera_fonte()
                self.entry_numeros.delete(0, 1)

        elif len(self.resultado) > 0 \
                and self.define_tamanho_max(self.entry_numeros.get()) \
                and self.entry_numeros.get() != "":
            if '-' in self.entry_numeros.get():
                self.label_operacao.config(text='')
                self.entry_numeros.delete(0, 1)
                self.numero1 = ''
                self.numero2 = ''
                self.resultado = ''
            elif '-' not in self.entry_numeros.get() and self.entry_numeros.get() != '0':
                self.label_operacao.config(text='')
                self.entry_numeros.insert(0, '-')
                self.numero1 = ''
                self.numero2 = ''
                self.resultado = ''

        elif len(self.resultado) < 1 \
                and (self.entry_numeros.get() != '0'
                     and len(self.entry_numeros.get()) > 0) \
                and self.define_tamanho_max(self.entry_numeros.get()) \
                and '-' not in self.entry_numeros.get()[0] \
                and self.entry_numeros.get != "":
            self.entry_numeros.insert(0, '-')

        elif len(self.resultado) < 1 \
                and '-' in self.entry_numeros.get():
            self.entry_numeros.delete(0, 1)

        self.altera_fonte()

    def faz_calculo(self):
        """
        Executa a operação.
        O método "self.set_operadores()" é responsável por captar o primeiro número digitado,
        por tanto o segundo é captado neste método, que decidirá qual ação será tomada conforme a possibilidade.
        """
        self.verifica_entry()
        try:
            if len(self.numero1) != 0 or len(self.numero2) > 0:
                if len(self.resultado) < 1 or len(self.numero2) < 1:
                    self.numero2 = self.entry_numeros.get()
                if len(self.resultado) > 0 and len(self.numero2) != 0:
                    self.numero1 = f'{self.resultado}{self.operador}'
                    self.entry_numeros.insert(0, self.faz_conta())
                    self.label_operacao.config(text=f'{self.numero1}{self.numero2}')
                if len(self.numero2) != 0:
                    self.entry_numeros.delete(0, len(self.entry_numeros.get()))
                    self.entry_numeros.insert(0, self.faz_conta())
                    self.label_operacao.config(text=f'{self.numero1}{self.numero2}')
                    self.numero1 = ''
        except ZeroDivisionError:
            self.resultado = 'Impos. dividir por 0'
            self.entry_numeros.delete(0, len(self.entry_numeros.get()))
            self.entry_numeros.insert(0, self.resultado)
        self.altera_fonte()

    def faz_potencia(self):
        """
        Executa a potência quadrada do número prévia mente digitado.
        Verifica se o primeiro número ja foi captado pelo método self.set_operadores(), se sim,
        neste caso este método executará a potência no segundo número digitado, após isso seguirá o cálculo
        conforme o operador pré-definido pelo usuário.
        """
        self.verifica_entry()
        try:
            if len(self.entry_numeros.get()) > 0:
                if len(self.numero1) == 0:
                    self.label_operacao.config(text=f'{self.entry_numeros.get()}²')
                    self.numero1 = self.entry_numeros.get()
                    self.entry_numeros.delete(0, len(self.entry_numeros.get()))
                    self.entry_numeros.insert(0, self.faz_op_potencia(self.numero1))
                    self.numero1 = ''
                    self.numero2 = ''
                    self.altera_fonte()
                elif len(self.numero1) > 0:
                    self.numero2 = self.faz_op_potencia(self.entry_numeros.get())
                    self.label_operacao.config(text=f'{self.numero1}{self.numero2}')
                    self.entry_numeros.delete(0, len(self.entry_numeros.get()))
                    self.entry_numeros.insert(0, self.faz_conta())
                    self.numero1 = ''
                    self.altera_fonte()
        except OverflowError:
            self.resultado = 'Estouro'
            self.numero1 = ''
            self.entry_numeros.delete(0, len(self.entry_numeros.get()))
            self.entry_numeros.insert(0, self.resultado)

    def faz_raiz(self):
        """
        Executa a raiz quadrada do número prévia mente digitado.
        Verifica se o primeiro número ja foi captado pelo método self.set_operadores(), se sim,
        neste caso este método executará a raiz do segundo número digitado, após isso seguirá o cálculo de acordo
        com o operador pré-definido pelo usuário.
        """
        self.verifica_entry()
        if '-' in self.entry_numeros.get():
            self.resultado = 'Use um número real'
            self.label_operacao.config(text='')
            self.entry_numeros.delete(0, len(self.entry_numeros.get()))
            self.entry_numeros.insert(0, self.resultado)
            self.altera_fonte()
        elif self.entry_numeros.get() != '0' and len(self.entry_numeros.get()) > 0:
            if len(self.numero1) == 0:
                self.numero1 = self.entry_numeros.get()
                self.label_operacao.config(text=f'√{self.entry_numeros.get()}')
                self.entry_numeros.delete(0, len(self.entry_numeros.get()))
                self.entry_numeros.insert(0, self.faz_op_raiz())
                self.altera_fonte()
                self.numero1 = ''
                self.numero2 = ''
            elif len(self.numero1) > 0:
                self.numero2 = self.faz_op_raiz(self.entry_numeros.get())
                self.label_operacao.config(text=f'{self.numero1}{self.numero2}')
                self.entry_numeros.delete(0, len(self.entry_numeros.get()))
                self.entry_numeros.insert(0, self.faz_conta())
                self.altera_fonte()
                self.numero1 = ''

    def faz_porcentagem(self):
        """
        Executa calculos de porcentagem do primeiro número pré-definido pelo usuário.
        Só funcionará quando um segundo número for digitado.
        """
        self.verifica_entry()
        if len(self.numero1) > 0 and len(self.entry_numeros.get()) > 0:
            self.numero2 = self.faz_op_porcentagem(self.entry_numeros.get())
            self.label_operacao.config(text=f'{self.numero1.replace(".", ",")}{self.numero2.replace(".", ",")}')
            self.entry_numeros.delete(0, len(self.entry_numeros.get()))
            self.entry_numeros.insert(0, self.faz_conta())
            self.numero1 = ''
            self.altera_fonte()

    def set_operadores(self, operador):
        """
        Função responsável por captar o primeiro número e receber o operador definido pelo usuário.
        Executa uma série de verificações para tomada de decisões como:
        Mudança de operador antes de o segundo número ser digitado;
        Cálculo automático sem a necessidade de apertar o botão de igualdade caso um segundo número
        ja tenha sido digitado antes de o próximo operador ser escolhido.
        """
        self.verifica_entry()
        self.operador = operador
        try:
            if len(self.numero1) == 0:
                self.label_operacao.config(text=f'{self.entry_numeros.get()}{operador}')
                self.numero1 = f'{self.entry_numeros.get()}{operador}'
                self.entry_numeros.delete(0, len(self.entry_numeros.get()))
                self.numero2 = ''
            elif len(self.numero1) > 0:
                if len(self.entry_numeros.get()) > 0 and len(self.resultado) < 1:
                    self.numero2 = self.entry_numeros.get()
                    conta = self.faz_conta()
                    self.numero1 = f'{conta}{operador}'
                    self.entry_numeros.delete(0, len(self.entry_numeros.get()))
                    self.label_operacao.config(text=self.numero1)
                    self.entry_numeros.insert(0, self.resultado)
                    self.numero2 = ''
                elif len(self.entry_numeros.get()) > 0:
                    self.numero1 = self.numero1.removesuffix(self.numero1[-1])
                    self.numero1 = f'{self.numero1}{operador}'
                    self.label_operacao.config(text=self.numero1)
                elif len(self.entry_numeros.get()) < 1:
                    self.numero1 = self.numero1.removesuffix(self.numero1[-1])
                    self.numero1 = f'{self.numero1}{operador}'
                    self.label_operacao.config(text=self.numero1)
        except ZeroDivisionError:
            self.resultado = 'Impos. dividir por 0'
            self.entry_numeros.delete(0, len(self.entry_numeros.get()))
            self.entry_numeros.insert(0, self.resultado)
        self.altera_fonte()

    def set_valor_entrada(self, valor):
        """
        Responsável por mostrar os números digitados na entry.
        Realiza algumas verificações para tomar algumas decisões como:
        Limpar a entry e a label se algum há um resultado anterior armazenado;
        Substituir todos os valores inseridos na entry pelo número pi.
        """

        qtd_numeros = len(self.entry_numeros.get())

        if valor == str(pi).replace('.', ','):
            self.entry_numeros.delete(0, qtd_numeros)

        if self.entry_numeros.get() == '0' and valor != ',':
            self.entry_numeros.delete(0, qtd_numeros)
            self.entry_numeros.insert(qtd_numeros, valor)
            self.altera_fonte()

        elif valor == ',' or self.entry_numeros.get() != '0' and self.define_tamanho_max(self.entry_numeros.get()):
            if len(self.resultado) > 0:
                if len(self.numero2) < 1:
                    self.entry_numeros.delete(0, qtd_numeros)
                    self.label_operacao.config(text=self.numero1)
                    self.resultado = ''
                elif len(self.numero2) > 0:
                    self.deleta_c()
                    self.entry_numeros.delete(0, qtd_numeros)
            self.entry_numeros.insert(qtd_numeros, valor)
            self.altera_fonte()

    def add_ponto_flutuante(self):
        """
        Adiciona uma vírgula.
        """
        if self.define_tamanho_max(self.entry_numeros.get()):
            if len(self.entry_numeros.get()) == 0:
                self.set_valor_entrada('0,')
            elif ',' not in self.entry_numeros.get():
                if len(self.resultado) > 0:
                    self.resultado = ''
                    self.numero1 = ''
                    self.numero2 = ''
                    self.set_valor_entrada(',')
                    self.label_operacao.config(text='')
                else:
                    self.set_valor_entrada(',')

    def altera_fonte(self):
        """
        Altera o tamanho da fonte dinamicamente conforme o usuário adiciona números na entry,
        isso possibilita ter mais números em um espaço menor, além do charme.
        """
        if len(self.entry_numeros.get()) < 15:
            self.entry_numeros.config(font=self.fonte_entry.config(size=27))
        elif 15 >= len(self.entry_numeros.get()):
            self.entry_numeros.config(font=self.fonte_entry.config(size=26))
        elif 16 >= len(self.entry_numeros.get()):
            self.entry_numeros.config(font=self.fonte_entry.config(size=25))
        elif 17 >= len(self.entry_numeros.get()):
            self.entry_numeros.config(font=self.fonte_entry.config(size=23))
        elif len(self.entry_numeros.get()) >= 18:
            self.entry_numeros.config(font=self.fonte_entry.config(size=22))

    def verifica_entry(self, comma_check=True):
        """
        Verifica se há uma vírgula isolada a direta do dígito, se sim ela é removida para o cálculo.
        Verifica se textos de erro ocorreram na entry, se sim, o método "deleta_c()" é executado.
        """

        if comma_check is True and len(self.entry_numeros.get()) > 0 and ',' == self.entry_numeros.get()[-1]:
            self.entry_numeros.delete(len(self.entry_numeros.get()) - 1)

        elif self.resultado == 'Estouro' \
                or self.resultado == 'Impos. dividir por 0' \
                or self.resultado == 'inf' \
                or self.resultado == '-inf' \
                or self.resultado == 'Use um número real':
            self.deleta_c()

    @staticmethod
    def define_tamanho_max(entrada):
        """
        Define a quantidade máxima de caracteres da entry.
        """
        if len(str(entrada)) >= 17:
            return False
        return True
