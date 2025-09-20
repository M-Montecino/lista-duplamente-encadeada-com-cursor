class Elemento:
    def __init__(self, dado):
        self.dado = dado
        self.__proximo = None
        self.__anterior = None

    @property
    def proximo(self) -> "Elemento":
        return self.__proximo
    
    @proximo.setter
    def proximo(self, proximo:"Elemento"):
        if isinstance(proximo, Elemento):
            self.__proximo = proximo
    
    @property
    def anterior(self) -> "Elemento":
        return self.__anterior
    
    @anterior.setter
    def anterior(self, anterior:"Elemento"):
        if isinstance(anterior, Elemento):
            self.__anterior = anterior

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__tamanho = 0
        self.__cursor = None

    def __avancar_k_posicoes(self, k:int):
        for i in range(k):
            if self.__cursor and self.__cursor.proximo:
                self.__cursor = self.__cursor.proximo
            else:
                break
    
    def __retroceder_k_posicoes(self, k:int):
        for i in range(k):
            if self.__cursor and self.__cursor.anterior:
                self.__cursor = self.__cursor.anterior
            else:
                break

    def __ir_para_o_primeiro(self):
        self.__cursor = self.__primeiro

    def __ir_para_o_ultimo(self):
        self.__cursor = self.__ultimo

    def acessar_atual(self):
        return self.__cursor
    
    def inserir_antes_do_atual(self, k):
        novo = Elemento(k)

        if self.__cursor is None:
            self.__primeiro = self.__ultimo = self.__cursor = novo

        elif self.__cursor == self.__primeiro:
            self.__inserir_como_primeiro(k)

        else:
            antes = self.__cursor.anterior
            novo.proximo = self.__cursor
            novo.anterior = antes
            self.__cursor.anterior = novo
            antes.proximo = novo
            self.__tamanho += 1
    
    def inserir_apos_atual(self, k):
        novo = Elemento(k)

        if self.__cursor is None:
            self.__primeiro = self.__ultimo = self.__cursor = novo
        
        elif self.__cursor == self.__ultimo:
            self.__inserir_como_ultimo(k)

        else:
            depois = self.__cursor.proximo
            novo.anterior = self.__cursor
            novo.proximo = depois
            self.__cursor.proximo = novo
            depois.anterior = novo
            self.__tamanho += 1

    def inserir_como_primeiro(self, k):
        novo = Elemento(k)

        if self.__cursor is None:
                self.__primeiro = self.__ultimo = self.__cursor = novo
        
        else:
            self.__ir_para_o_primeiro()
            self.__primeiro = novo
            novo.proximo = self.__cursor
            self.__cursor.anterior = novo
            self.__ir_para_o_primeiro()
            self.__tamanho +=1

    def inserir_como_ultimo(self, k):
        novo = Elemento(k)

        if self.__cursor is None:
                self.__primeiro = self.__ultimo = self.__cursor = novo

        else:
            self.__ir_para_o_ultimo()
            self.__ultimo = novo
            novo.anterior = self.__cursor
            self.__cursor.proximo = novo
            self.__ir_para_o_ultimo()
            self.__tamanho += 1
    
    def excluir_atual(self):
        if self.__cursor == None:
            return
        elif self.__cursor == self.__primeiro:
            self.excluir_primeiro()
        elif self.__cursor == self.__ultimo:
            self.excluir_ultimo()
        else:
            anterior = self.__cursor.anterior
            proximo = self.__cursor.proximo
            anterior.proximo = proximo
            proximo.anterior = anterior
            self.__cursor = anterior
            self.__tamanho -= 1

    def excluir_primeiro(self):
        if self.__primeiro == self.__ultimo:
            self.__primeiro = None
            self.__ultimo = None
            self.__cursor = None
            self.__tamanho = 0
        else:
            self.__ir_para_o_primeiro()
            self.__cursor.proximo = self.__primeiro
            self.__ir_para_o_primeiro()
            self.__tamanho -= 1
    
    def excluir_ultimo(self):
        self.__ir_para_o_ultimo()
        self.__cursor.anterior = self.__ultimo
        self.__ir_para_o_ultimo()
        self.__tamanho -= 1

    def buscar(self, chave):