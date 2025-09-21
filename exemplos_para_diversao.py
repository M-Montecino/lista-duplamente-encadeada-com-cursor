from lista_duplamente_encadeada import *

l = ListaDuplamenteEncadeada()

#inserindo elementos:
l.inserir_como_primeiro(1)
l.inserir_apos_atual(3)
l.inserir_como_ultimo(2)
print({l.mostra_lista()})
l.inserir_na_posicao(2, 4)
l.inserir_apos_atual(5)
l.inserir_como_primeiro(6)
print({l.mostra_lista()})

#exclusão
l.excluir_primeiro()
print({l.mostra_lista()})

l.excluir_ultimo()
print({l.mostra_lista()})
