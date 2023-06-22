class Calculos:
    def __init__(self, numero1='', numero2='', operador='', resultado=''):
        self.numero1 = numero1
        self.numero2 = numero2
        self.operador = operador
        self.resultado = resultado

    def converte_virgula_para_ponto(self, numero=None):
        """
        Recebe o decimal com vírgula e o converte para decimal com ponto.
        """
        if ',' in self.numero1:
            self.numero1 = self.numero1.replace(',', '.')
        if ',' in self.numero2:
            self.numero2 = self.numero2.replace(',', '.')
        if ',' in self.resultado:
            self.resultado = self.resultado.replace(',', '.')
        try:
            if ',' in numero:
                numero = numero.replace(',', '.')
                return numero
        except TypeError:
            pass

    def converte_ponto_para_virgula(self, numero=None):
        """
        Recebe a resposta decimal com ponto e a converte para decimal com vírgula.
        """
        if '.' in self.numero1:
            self.numero1 = self.numero1.replace('.', ',')
        if '.' in self.numero2:
            self.numero2 = self.numero2.replace('.', ',')
        if '.' in self.resultado:
            self.resultado = self.resultado.replace('.', ',')
        try:
            if ',' in numero:
                numero = numero.replace(',', '.')
                return numero
        except TypeError:
            pass

    def faz_conta(self):
        """
        Este método retorna os resultados das seguintes operações:
        Adição, Multiplicação, Subtração e Divisão.
        """
        self.converte_virgula_para_ponto()
        if '×' in self.numero1:
            conta = eval(f'{self.numero1.replace("×", "*")}{self.numero2}')
            self.resultado = self.formata_resultado(conta)
            self.converte_ponto_para_virgula()
            return self.resultado
        if '÷' in self.numero1:
            conta = eval(f'{self.numero1.replace("÷", "/")}{self.numero2}')
            self.resultado = self.formata_resultado(conta)
            self.converte_ponto_para_virgula()
            return self.resultado
        else:
            conta = eval(f'{self.numero1}{self.numero2}')
            self.resultado = self.formata_resultado(conta)
            self.converte_ponto_para_virgula()
            return self.resultado

    def faz_op_potencia(self, numero=None):
        """
        Retorna a potência quadrada do número pedido.
        """
        if numero is None:
            potencia = eval(f'{self.numero2}**2')
            self.converte_ponto_para_virgula()
            return potencia
        else:
            numero = self.converte_ponto_para_virgula(numero)
            potencia = eval(f'{numero}**2')
            self.resultado = self.formata_resultado(potencia)
            return self.resultado

    def faz_op_porcentagem(self, numero):
        """
        Retorna a porcentagem do número recebido como parâmetro para a realização do cálculo escolhido.
        """
        if ',' in numero:
            numero = self.converte_virgula_para_ponto(numero)
        conta = float(numero) / 100
        numero = str((conta * float(self.numero1.replace(self.numero1[-1], ''))))
        return self.formata_resultado(numero)

    def faz_op_raiz(self, numero=None):
        """
        Retorna a raiz quadrada do número pedido.
        """
        self.converte_virgula_para_ponto()
        if numero is None:
            conta = float(self.numero1) ** 0.5
            self.resultado = self.formata_resultado(conta)
            self.converte_ponto_para_virgula()
            return self.resultado
        else:
            if ',' in numero:
                numero = self.converte_virgula_para_ponto(numero)
            conta = float(numero) ** 0.5
            return self.formata_resultado(str(conta))

    def formata_resultado(self, resultado):
        """
        Formata os resultados que ultrapassam o limite de caracteres para uma notação científica.
        """
        resultado = str(resultado)

        resultado = self.arredonda(resultado)

        if len(resultado) > 16:
            resultado = f'{float(resultado):.9e}'
        return resultado

    @staticmethod
    def arredonda(numero):
        """
        Método utilizado exclusivamente para transformar em inteiros os decimais com apenas zeros após o ponto.
        """
        if '.' in numero:
            ponto = numero.find('.')
            pos_ponto = numero[ponto:]
            tamanho = len(pos_ponto)
            if tamanho == 2 and pos_ponto == '.0':
                numero = round(float(numero))
        return str(numero)
