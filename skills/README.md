# Skills do Mentor Start

## O que são skills

Skills são processos reutilizáveis que orientam o Mentor Start em tarefas recorrentes. Em vez de responder sempre de forma improvisada, o agente segue uma sequência adequada ao objetivo do estudante.

O estudante não precisa conhecer comandos ou nomes de skills. Ele apenas conversa naturalmente; o agente identifica a intenção e aplica o processo mais apropriado.

## Skills disponíveis

| Skill | Quando é usada | Resultado para o estudante |
| --- | --- | --- |
| [`explain-concept`](explain-concept/SKILL.md) | Quando há uma dúvida sobre termo, conceito ou ferramenta. | Explicação simples, exemplo e uma pequena prática. |
| [`study-plan`](study-plan/SKILL.md) | Quando a pessoa está perdida ou quer organizar uma rotina. | Plano de estudos realista e ajustável. |
| [`unblock-exercise`](unblock-exercise/SKILL.md) | Quando há travamento em exercício ou desafio. | Dicas graduais sem entregar uma solução final. |

## Como o agente escolhe uma skill

```text
Pergunta do estudante
        |
        +-- "O que é...?" / "Não entendi..." --> explain-concept
        |
        +-- "Por onde começo?" / "Como organizo...?" --> study-plan
        |
        +-- "Travei..." / "Meu código não funciona..." --> unblock-exercise
        |
        +-- outra necessidade --> resposta orientada pelas regras gerais do AGENTS.md
```

Se uma conversa mudar de objetivo, o agente pode combinar skills. Por exemplo, após explicar uma condição, ele pode ajudar a pessoa a aplicar o conceito em um exercício — sempre mantendo o foco em autonomia.

## Princípios compartilhados

Todas as skills devem:

- adaptar a resposta ao nível da pessoa;
- fazer no máximo uma pergunta de esclarecimento por vez;
- usar exemplos pequenos e práticos;
- evitar jargão ou explicá-lo imediatamente;
- reconhecer os limites da base de conhecimento;
- sugerir um próximo passo viável;
- respeitar a integridade acadêmica.

## Como evoluir uma skill

Ao criar uma nova skill, mantenha este padrão:

1. Crie uma pasta com um nome curto em inglês, como `review-project`.
2. Adicione um arquivo `SKILL.md` com nome, descrição, momento de uso e processo.
3. Documente o que a skill deve evitar, especialmente quando houver riscos de resposta pronta ou informação não verificada.
4. Inclua a nova skill na tabela de `AGENTS.md` e neste README.
5. Crie perguntas de teste para verificar se o agente escolhe e executa o processo corretamente.

Uma skill deve ser pequena, clara e focada em uma necessidade concreta. Se ela tentar fazer tudo, deixa de ajudar o agente a tomar boas decisões.
