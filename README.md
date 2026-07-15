# Mentor Start

> Um agente de IA educacional que orienta pessoas iniciantes em tecnologia com explicações claras, planos de estudo realistas e dicas graduais para exercícios.

> **Diferencial:** o Mentor Start também ensina cibersegurança defensiva desde o início, ajudando a proteger contas, chaves de API, projetos e dados pessoais.

## Sobre o projeto

Começar em tecnologia pode ser confuso: há muitas linguagens, ferramentas e trilhas possíveis, enquanto dúvidas básicas frequentemente parecem difíceis de fazer. O **Mentor Start** foi criado para reduzir essa barreira inicial.

Ele atua como um mentor de estudos: adapta a comunicação para iniciantes, explica o raciocínio por trás dos conceitos e incentiva a prática. O objetivo não é apenas dar respostas, mas ajudar a pessoa a ganhar autonomia para continuar aprendendo.

Este projeto foi desenvolvido como parte de uma jornada de estudos em agentes de IA e está em evolução contínua.

## Destaque: cibersegurança para iniciantes

Além da orientação de estudos, o Mentor Start ensina práticas defensivas de cibersegurança: proteção de credenciais, uso de `.env` e `.gitignore`, MFA, reconhecimento de phishing, privacidade e cuidados com dependências. O agente não oferece instruções de invasão, fraude ou acesso não autorizado.

## Para quem é

O Mentor Start foi pensado principalmente para:

- pessoas em seu primeiro contato com programação e tecnologia;
- estudantes de bootcamps e cursos introdutórios;
- pessoas em transição de carreira que precisam de uma direção inicial;
- quem quer entender conceitos como Git, variáveis, funções e APIs sem excesso de jargão.

## O que o agente faz

| Necessidade do estudante | Como o Mentor Start ajuda |
| --- | --- |
| "Não entendi esse conceito" | Explica em linguagem simples, com exemplo pequeno e próximo passo prático. |
| "Por onde começo?" | Organiza uma sequência inicial de estudos de acordo com objetivo, nível e tempo disponível. |
| "Travei neste exercício" | Oferece dicas graduais para desenvolver o raciocínio sem entregar a solução final. |
| "Não sei se a informação é confiável" | Usa a base local como referência e reconhece claramente quando ela não é suficiente. |
| "Posso publicar esta chave no GitHub?" | Ensina práticas defensivas para proteger credenciais, contas e projetos. |
| "Recebi um link suspeito" | Ajuda a reconhecer phishing e indica ações seguras, sem alarmismo. |

## Princípios do Mentor Start

- **Aprender antes de responder:** o agente explica o caminho, não apenas o resultado.
- **Clareza para iniciantes:** termos técnicos são explicados no momento em que aparecem.
- **Autonomia:** a resposta deve deixar o estudante mais capaz de resolver situações futuras.
- **Honestidade:** o agente não inventa informações, links ou recursos.
- **Integridade acadêmica:** não entrega respostas prontas de desafios, provas ou atividades avaliativas.
- **Segurança desde o início:** orienta práticas defensivas e recusa pedidos de invasão ou acesso não autorizado.

## Como funciona

Nesta primeira versão, o Mentor Start é um agente portátil baseado em arquivos de instrução. Um harness compatível com `AGENTS.md` lê as regras do projeto, a persona, a base de conhecimento e a skill adequada antes de gerar uma resposta.

```text
Pergunta do estudante
        |
        v
Harness compatível com AGENTS.md
        |
        +--> Regras do agente (AGENTS.md)
        +--> Persona (agent/persona.md)
        +--> Base de conhecimento (agent/knowledge/)
        +--> Skill adequada (skills/)
        |
        v
Resposta didática + próximo passo prático
```

Isso permite usar a mesma definição do agente em diferentes ambientes de IA compatíveis com esse padrão, sem prender o projeto a uma única ferramenta.

## Estrutura do repositório

```text
MENTOR-START-AGENT-IA/
├── README.md                 # Visão geral e guia do projeto
├── AGENTS.md                 # Regras, escopo, limites e tom do agente
├── agent/
│   ├── persona.md            # Personalidade e princípios pedagógicos
│   └── knowledge/            # Base de conhecimento curada
│       ├── fundamentos.md
│       ├── ferramentas.md
│       └── trilhas.md
├── skills/                   # Processos especializados do agente
│   ├── explain-concept/
│   ├── study-plan/
│   └── unblock-exercise/
├── docs/                     # Arquitetura, prompts e avaliação
└── src/                      # Reservado para a futura aplicação web
```

## Skills disponíveis

### Explicar conceitos

Usada quando o estudante pede ajuda com um termo ou tecnologia. A explicação segue uma sequência: definição simples, exemplo, possível confusão comum e prática sugerida.

### Criar plano de estudos

Usada para transformar um objetivo em uma rotina possível. O agente pergunta o objetivo, o nível atual e o tempo disponível antes de sugerir uma trilha.

### Destravar exercícios

Usada quando há bloqueio em um exercício. O agente aumenta a ajuda gradualmente: conceito, direção, estratégia, pseudocódigo e comentários sobre o código do estudante.

## Base de conhecimento inicial

A base é local e deliberadamente pequena para ser verificável e evoluir com qualidade. Ela já abrange:

- fundamentos de programação: algoritmos, variáveis, condições, repetições e funções;
- ferramentas iniciais: editor de código, terminal, Git e GitHub;
- rotas de estudo para fundamentos e desenvolvimento web.

Novos conteúdos devem ser incluídos somente após pesquisa e revisão, mantendo a regra de que o agente não deve afirmar como fato algo que não consegue sustentar.

## Como usar

1. Clone o repositório:

   ```bash
   git clone https://github.com/mullervieira/MENTOR-START-AGENT-IA.git
   ```

2. Para usar o agente em um harness, abra a pasta em um ambiente de IA que suporte instruções de projeto via `AGENTS.md`.

3. Faça perguntas em linguagem natural, por exemplo:

   ```text
   Nunca programei. O que é uma variável?
   ```

   ```text
   Quero começar a estudar desenvolvimento web e tenho quatro horas por semana.
   ```

   ```text
   Travei em um exercício com condicionais. Posso mostrar o que tentei?
   ```

3. Para executar a aplicação web independente, siga o guia em [`docs/execucao.md`](docs/execucao.md). Ela usa Streamlit, a Responses API da OpenAI e a base local do projeto.

## Estado atual e próximos passos

| Etapa | Situação |
| --- | --- |
| Identidade, persona e regras do agente | Concluída |
| Base inicial de conhecimento | Concluída |
| Skills pedagógicas | Concluída |
| Casos de avaliação e métricas | Concluída — versão inicial |
| Interface de chat independente | Concluída |
| Integração com modelo de linguagem e recuperação de contexto | Implementada — validação real pendente de cota da API |

As próximas evoluções técnicas são ampliar a base de conhecimento, adicionar recuperação mais precisa e incorporar pesquisa web com fontes verificáveis para perguntas que dependem de informações atuais.

## Avaliação da qualidade

O projeto prevê testes com perguntas reais de iniciantes. Cada resposta será avaliada de 1 a 5 nos seguintes critérios:

- clareza para o público iniciante;
- fidelidade à base de conhecimento;
- segurança ao reconhecer limitações;
- estímulo à autonomia;
- utilidade do próximo passo recomendado.

Os detalhes estão em [`docs/metricas.md`](docs/metricas.md).

## Autor

Desenvolvido por [Muller Vieira](https://github.com/mullervieira) como projeto de estudo sobre agentes de IA aplicados à educação em tecnologia.
