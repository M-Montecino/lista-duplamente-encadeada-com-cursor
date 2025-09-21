class Elemento:
    def __init__(self, dado):
        self.dado = dado
        self.__proximo = None
        self.__anterior = None
        self.__fake = False

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
    
    @property
    def fake(self) -> bool:
        return self.__fake
    
    @fake.setter
    def fake(self, fake:bool):
        if isinstance(fake, bool):
            self.__fake = fake

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.__primeiro = None
        self.__ultimo = None
        self.__tamanho = 0
        self.__cursor = None

    def __avancar_k_posicoes(self, k:int):
        if self.__cursor is None:
            return None
        
        for i in range(k):
            if self.__cursor and self.__cursor.proximo:
                self.__cursor = self.__cursor.proximo
            else:
                break
        return self.__cursor
    
    def __retroceder_k_posicoes(self, k:int):
        if self.__cursor is None:
            return None

        for i in range(k):
            if self.__cursor and self.__cursor.anterior:
                self.__cursor = self.__cursor.anterior
            else:
                break
            return self.__cursor

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
            self.inserir_como_primeiro(k)

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
            self.inserir_como_ultimo(k)

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

    def inserir_na_posicao(self, z:int, k):
        if z < 0 or z > self.__tamanho:
            return None
        
        novo = Elemento(k)

        if self.__tamanho == 0:
            self.__primeiro = self.__ultimo = self.__cursor = novo

        elif k == 0:
            self.inserir_como_primeiro()

        elif k == self.__tamanho:
            self.inserir_como_ultimo()
        
        else:
            antes = self.__cursor.anterior
            novo.proximo = self.__cursor
            novo.anterior = antes
            antes.proximo = novo
            self.__cursor.anterior = novo
            self.__cursor = novo

        self.__tamanho += 1

    
    def excluir_atual(self):
        if self.__cursor == None:
            return
        elif self.__cursor == self.__ultimo:
            self.excluir_ultimo()
        elif self.__cursor == self.__primeiro:
            self.excluir_primeiro()

        else:
            anterior = self.__cursor.anterior
            proximo = self.__cursor.proximo
            anterior.proximo = proximo
            proximo.anterior = anterior
            self.__cursor = anterior
            self.__tamanho -= 1

    def excluir_primeiro(self):
        if self.__primeiro is None:
            return
        if self.__primeiro == self.__ultimo:
            self.__primeiro = self.__ultimo = self.__cursor = None
        else:
            self.__ir_para_o_primeiro()
            self.__primeiro = self.__primeiro.proximo
            self.__primeiro.anterior = None
            self.__ir_para_o_primeiro()
        self.__tamanho -= 1
    
    def excluir_ultimo(self):
        if self.__ultimo is None:
            return
        if self.__primeiro == self.__ultimo:
            self.__primeiro = self.__ultimo = self.__cursor = None
        else:
            self.__ir_para_o_ultimo()
            self.__ultimo - self.__ultimo.anterior
            self.__ultimo.proximo = None
            self.__ir_para_o_ultimo()
        self.__tamanho -= 1

    def buscar(self, k):
        if self.__primeiro is None:
            return None
        
        fake = Elemento(k)
        fake.fake = True
        self.__ultimo.proximo = fake
        fake.anterior = self.__ultimo

        atual = self.__primeiro
        while atual.dado != k:
            atual = atual.proximo

        self.__ultimo.proximo = None
        fake.anterior = None

        if atual.fake == True:
            return None
        else:
            self.__cursor = atual
            return atual