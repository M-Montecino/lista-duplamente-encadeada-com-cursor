Relatório do trabalhinho 1 da disciplina de INE5609 - Estrutura de dados!

Atenção! Este repositório contém imagens lindíssimas (só que não) dos esquemas que eu fiz para tentar entender melhor a lógica por trás das funções, então peço encarecidamente que releve que as imagens foram feitas no paint as duas da manhã.

1) implementando a classe Elemento:
Tentei manter ela o mais enxuta possível, conforme visto em sala de aula, como a lista é duplamente encadeada ela tem:
- valor 
- anterior 
- próximo 
Mas também adicionei o boolean "fake" para as buscas, acredito que isso poderia ser implementado de outra forma, mas eu quis deixar as inserções com algum tipo de verificação mesmo que básica, então foi essa saída que eu encontrei

2) funções privadas do cursor:
Implementadas as funções:
- avançarKPosições( K )
- retrocederKPosições( K )
- irParaPrimeiro()
- irParaUltimo()
Que acabaram ficando bem simples, fiz um sistema para prevenção que ele vá além do limite de tamanho da lista, mas não fui muito criativa procurando exceções e admito que talvez alguns casos possam não estar sendo contemplados. Também adicionei a função mostra lista, principalmente para me ajudar a debugar.

3) Funções de inserção:
Implementadas as funções:
- Inserção em lista vazia
- Inserção no início
- Inserção no fim
- Inserção antes ou depois do elemento atual

Eu me baseei nos slides disponibilizados no moodle e também algumas anotações que eu fiz em sala. Os desenhos estão como apoio, e explicam a maior parte da minha lógica por trás do código, cada função de inserção tem o excepcional de inserir o primeiro elemento da lista como único, caso contrário ele vai tentar seguir a lógica da melhor forma possível dados os elementos ao redor. Também em inserir antes do atual, ele tem o erro caso você esteja tentando inserir um novo primeiro elemento, ou após, o erro de inserir como último, que direciona o comando para a função correta.


4) Funções de exclusão:
As funções de exclusão consideram os seguintes casos:
- Exclusão do único elemento (lista fica vazia, cursor = `None`)
- Exclusão do primeiro elemento (cursor passa a apontar para o novo primeiro)
- Exclusão do último elemento (cursor passa a apontar para o novo último)
- Exclusão do elemento atual em posição intermediária (cursor passa para o próximo válido)

Também me baseei nas anotações e no esquema que eu fiz para excluir o atual. Como decisão de projeto, excluir primeiro e último também servem para excluir o único elemento da lista, o que deixaria ela completamente vazia, desaterrando o cursor, que também não vai ter ninguém para apontar. Fora isso, tentei sempre manter o cursor na lista corretamente, uma vez que eu não acho que faça sentido fazer ele sumir porque eu exclui o item que ele está atrelado.

5) Busca:
Fiz a minha busca baseada no "protocólo fantasma" que foi apresentado em sala, adaptado para lógica do meu código (como eu adicionei o self.__ fake: bool) ele conta como essa característica para checar se o fake é fake mesmo. Além disso, a lógica é realmente o que vimos em sala:
- Adicionar o fake
- Procurar o elemento em um loop
- Remover o fake
- Analisar se o elemento pego pelo loop é o verdadeiro
- Retorna o elemento ou none, dependendo da resposta anterior

6) Conlusão:
Implementei a lista cumprindo com os requisitos da atividade. Também tentei incrementar com:
- Reaproveitando o código o máximo possível
- Tratar alguns casos extremos
No geral, a implementação cumpre o objetivo de exercitar a lógica de ponteiros, manipulação de encadeamento e uso de cursor em listas.