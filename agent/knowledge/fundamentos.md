# Fundamentos de programação

## Objetivo deste material

Este arquivo reúne conceitos iniciais para explicações destinadas a quem está começando. Ele prioriza entendimento conceitual, não uma linguagem específica. Ao usá-lo, adapte os exemplos à linguagem que o estudante está aprendendo e deixe claro quando a sintaxe muda entre linguagens.

## Algoritmo

Um algoritmo é uma sequência ordenada de instruções para resolver um problema ou alcançar um resultado. Na programação, ele descreve a lógica antes ou junto do código.

**Analogia:** uma receita usa ingredientes, passos e um resultado esperado. Um programa também recebe dados de entrada, processa-os seguindo passos e produz uma saída.

**Exemplo:** para descobrir a média de duas notas, os passos são: receber as notas, somá-las, dividir o resultado por dois e mostrar a média.

**Confusão comum:** algoritmo não é necessariamente código. Ele pode ser escrito em linguagem natural, fluxograma, pseudocódigo ou código.

## Variável

Uma variável é um nome que representa um valor armazenado pelo programa. Esse valor pode ser consultado e, dependendo da situação, atualizado durante a execução.

**Exemplo conceitual:** `pontuacao` pode guardar o número de pontos de um jogador. Quando ele acerta uma questão, o programa pode atualizar esse valor.

**Confusão comum:** variável não é uma "caixa mágica"; ela tem um nome, um valor e regras da linguagem sobre o tipo de dado que pode guardar.

## Tipos de dados

Tipos de dados classificam os valores com que o programa trabalha. Os mais comuns para iniciantes são:

- texto, como um nome;
- número inteiro, como quantidade de itens;
- número decimal, como uma média;
- lógico (verdadeiro ou falso), como o resultado de uma comparação.

Cada linguagem tem nomes e regras próprias para esses tipos. O importante no início é identificar que tipo de informação um problema precisa manipular.

## Operadores

Operadores são símbolos ou palavras que realizam ações sobre valores. Eles podem fazer cálculos, comparar valores ou combinar condições.

Exemplos conceituais: somar dois valores, verificar se uma idade é maior que 18 ou testar se duas informações são iguais.

**Confusão comum:** o símbolo usado para comparar igualdade pode ser diferente do símbolo usado para atribuir um valor a uma variável. Verifique a sintaxe da linguagem estudada.

## Condição

Uma condição permite que o programa escolha entre caminhos diferentes conforme uma expressão seja verdadeira ou falsa.

**Exemplo:** se a senha informada estiver correta, permitir acesso; caso contrário, mostrar uma mensagem de erro.

**Boa prática de raciocínio:** antes de escrever código, formule a pergunta que o programa precisa responder e quais ações devem acontecer em cada resultado.

## Repetição

Uma estrutura de repetição executa uma tarefa várias vezes. Ela é útil quando a mesma ação precisa ser aplicada a vários elementos ou enquanto uma condição for atendida.

**Exemplo:** mostrar os nomes de todos os estudantes de uma lista ou pedir uma opção novamente enquanto ela for inválida.

**Atenção:** uma repetição precisa de uma condição de parada. Sem ela, o programa pode entrar em um loop infinito.

## Função

Uma função agrupa uma tarefa com um nome para que ela possa ser chamada quando necessário. Ela ajuda a organizar o código, reduzir repetição e tornar a intenção mais clara.

Uma função pode receber dados de entrada, realizar uma ação e devolver um resultado.

**Exemplo conceitual:** uma função `calcularMedia` recebe duas notas e devolve a média delas.

## Entrada, processamento e saída

Muitos problemas de programação podem ser entendidos com três perguntas:

1. **Entrada:** quais informações o programa recebe?
2. **Processamento:** que regra, cálculo ou decisão ele executa?
3. **Saída:** qual resultado deve mostrar ou devolver?

Antes de programar, escrever essas três partes em português ajuda a organizar a lógica e torna erros mais fáceis de localizar.

## Depuração básica

Depurar é investigar por que o programa não faz o que era esperado. Para iniciantes, um processo simples é:

1. Ler a mensagem de erro com calma;
2. testar com uma entrada pequena;
3. comparar resultado esperado e resultado obtido;
4. verificar uma parte da lógica por vez;
5. alterar uma coisa e testar novamente.

Um erro não prova falta de capacidade; ele é uma informação sobre o que ainda precisa ser ajustado.

## Pseudocódigo e teste de mesa

Pseudocódigo descreve a solução em passos, sem se preocupar com a sintaxe de uma linguagem. Teste de mesa é simular esses passos com valores simples, anotando o que acontece em cada etapa.

Essas duas técnicas ajudam a separar a dificuldade de lógica da dificuldade de sintaxe.

## Próximos conceitos para incluir

Ao evoluir esta base, considere adicionar estruturas de dados, entrada e saída, tratamento de erros, orientação a objetos e testes. Inclua conteúdo somente após pesquisa e revisão.
