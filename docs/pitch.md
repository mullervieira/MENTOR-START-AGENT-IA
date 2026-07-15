# Pitch final — Mentor Start

## Objetivo da apresentação

Apresentar, em até três minutos, o problema enfrentado por iniciantes em tecnologia, a proposta do Mentor Start, sua arquitetura, o diferencial de cibersegurança e o processo de avaliação.

## Roteiro de até 3 minutos

### 1. Abertura e problema — 30 segundos

"Quem começa em tecnologia encontra muitas linguagens, ferramentas e trilhas ao mesmo tempo. Isso gera dúvidas básicas, insegurança e a sensação de não saber por onde começar. Além disso, a pessoa precisa aprender a proteger contas, projetos e chaves de API desde o início. Uma IA que só entrega respostas prontas ou ignora segurança pode atrapalhar esse processo."

### 2. Solução — 30 segundos

"Por isso criei o Mentor Start, um agente de IA educacional para iniciantes em tecnologia. Ele explica conceitos com linguagem simples, ajuda a criar planos de estudo possíveis, orienta exercícios com dicas graduais e ensina práticas básicas de cibersegurança, sem fazer a atividade no lugar do estudante."

### 3. Como funciona — 40 segundos

"O projeto foi organizado em quatro camadas. O AGENTS.md define regras, limites e tom de voz. A persona define a postura pedagógica. A base de conhecimento reúne fundamentos, ferramentas, trilhas e cibersegurança. Por fim, as skills orientam tarefas específicas, como explicar conceitos, montar planos, destravar exercícios e orientar proteção de credenciais."

### 4. Diferencial de cibersegurança — 35 segundos

"O diferencial do Mentor Start é tratar segurança como parte do aprendizado técnico. Por exemplo, ele explica por que uma chave de API não pode ir para o GitHub, como usar `.env` e `.gitignore`, como ativar MFA e o que fazer se uma chave vazar: revogar, substituir e revisar a conta. O agente trabalha apenas de forma defensiva e recusa pedidos de invasão ou acesso não autorizado."

### 5. Demonstração — 25 segundos

"Na aplicação, a pessoa pode perguntar: 'Posso publicar minha chave de API no GitHub?'. O Mentor Start identifica o risco, explica que a chave é uma credencial, orienta a usar `.env` e `.gitignore` e sugere revogação imediata se ela já tiver sido exposta. A resposta informa quais arquivos locais foram consultados."

### 6. Avaliação e encerramento — 20 segundos

"Eu defini casos de avaliação para clareza, fidelidade à base, segurança, autonomia, privacidade e utilidade. O Mentor Start não tenta responder tudo: ele reconhece limites, evita conteúdo ofensivo e transforma dúvidas em próximos passos práticos e seguros."

## Demonstração recomendada

Use uma destas perguntas:

1. **"Nunca programei. Qual a diferença entre Git e GitHub?"**
2. **"Posso publicar minha chave de API no GitHub?"**

A segunda demonstra melhor o diferencial de cibersegurança.

## Dicas de apresentação

- Mostre o README por alguns segundos para apresentar a organização do projeto.
- Mostre `agent/knowledge/ciberseguranca.md` e `skills/security-basics/SKILL.md` ao explicar o diferencial.
- Não exponha sua chave de API durante a gravação ou em prints.
- Se a API estiver sem cota, apresente a arquitetura, os casos de teste e uma resposta já validada no harness, deixando clara a limitação externa.
