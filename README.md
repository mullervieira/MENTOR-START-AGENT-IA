# Mentor Start

> Um agente de IA educacional que ajuda pessoas iniciantes em tecnologia a entender conceitos, organizar estudos, destravar exercícios e adotar hábitos de cibersegurança defensiva.

## Status do projeto

O Mentor Start possui documentação, base de conhecimento, skills, testes e uma aplicação web em Streamlit. A integração com a API da OpenAI está implementada; a validação completa de respostas depende de cota disponível na conta da API.

## O problema

Começar em tecnologia pode ser confuso: há muitas linguagens, ferramentas e trilhas possíveis, enquanto dúvidas básicas frequentemente parecem difíceis de fazer. Além disso, estudantes iniciantes precisam aprender desde cedo a proteger contas, projetos e credenciais.

O Mentor Start reduz essa barreira inicial com uma orientação clara, prática e responsável. Ele não tenta substituir o esforço do estudante: ajuda a transformar dúvidas em entendimento, entendimento em prática e prática em autonomia.

## Para quem é

- Pessoas no primeiro contato com programação e tecnologia;
- estudantes de bootcamps e cursos introdutórios;
- pessoas em transição de carreira que precisam de uma direção inicial;
- quem quer aprender com linguagem simples, exemplos pequenos e próximos passos possíveis.

## O que o agente faz

| Necessidade do estudante | Como o Mentor Start ajuda |
| --- | --- |
| "Não entendi esse conceito" | Explica com definição simples, exemplo, confusão comum e prática curta. |
| "Por onde começo?" | Organiza uma sequência inicial conforme objetivo, nível e tempo disponível. |
| "Travei neste exercício" | Oferece dicas graduais sem entregar a solução final. |
| "Posso publicar esta chave no GitHub?" | Ensina `.env`, `.gitignore`, MFA e proteção de credenciais. |
| "Recebi um link suspeito" | Ajuda a reconhecer phishing e indica ações defensivas. |
| "Não sei se essa informação está na base" | Reconhece limites e evita inventar fontes ou dados. |

## Diferencial: segurança desde o início

O Mentor Start trata cibersegurança como parte do aprendizado técnico. Ele orienta práticas defensivas como proteção de chaves de API, MFA, privacidade em repositórios, cuidados com dependências e reconhecimento de phishing.

O agente não fornece instruções de invasão, fraude, roubo de dados ou acesso não autorizado.

## Princípios

- **Aprender antes de responder:** ensina o caminho, não apenas o resultado;
- **Clareza para iniciantes:** explica termos técnicos quando eles aparecem;
- **Autonomia:** ajuda a pessoa a conseguir resolver situações futuras;
- **Honestidade:** reconhece limitações e não inventa informações;
- **Integridade acadêmica:** não entrega respostas prontas de desafios e avaliações;
- **Segurança e privacidade:** protege credenciais e orienta apenas práticas defensivas.

## Como funciona

O projeto pode ser usado de duas formas:

1. Como agente portátil em um harness que leia `AGENTS.md`;
2. Como aplicação web independente em Streamlit.

```text
Pergunta do estudante
        |
        v
Interface ou harness compatível
        |
        +--> Regras do agente (AGENTS.md)
        +--> Persona (agent/persona.md)
        +--> Base de conhecimento (agent/knowledge/)
        +--> Skill adequada (skills/)
        |
        v
Contexto local + modelo de IA
        |
        v
Resposta didática + próximo passo prático + fontes locais consultadas
```

Na aplicação web, uma seleção simples por palavras-chave escolhe os arquivos mais relacionados à pergunta antes de montar o contexto enviado ao modelo.

## Tecnologias e conceitos aplicados

- Python;
- Streamlit para a interface de chat;
- OpenAI Responses API para geração de respostas;
- `python-dotenv` para configuração local segura;
- Git e GitHub para versionamento;
- Base de conhecimento em Markdown;
- Engenharia de prompts, recuperação de contexto, avaliação de agentes e cibersegurança defensiva.

## Estrutura do repositório

```text
MENTOR-START-AGENT-IA/
├── README.md
├── AGENTS.md                    # Regras, escopo, limites e tom do agente
├── .env.example                 # Modelo de configuração, sem segredo real
├── .gitignore                   # Protege .env e arquivos locais
├── requirements.txt             # Dependências Python
├── agent/
│   ├── persona.md               # Postura pedagógica e comunicação
│   └── knowledge/
│       ├── fundamentos.md
│       ├── ferramentas.md
│       ├── trilhas.md
│       └── ciberseguranca.md
├── skills/
│   ├── explain-concept/
│   ├── study-plan/
│   ├── unblock-exercise/
│   └── security-basics/
├── docs/
│   ├── arquitetura.md
│   ├── execucao.md
│   ├── metricas.md
│   ├── pitch.md
│   └── prompts.md
├── src/
│   ├── app.py
│   ├── knowledge_loader.py
│   └── prompts.py
└── tests/
    ├── casos_avaliacao.md
    ├── resultados.md
    └── smoke_test.py
```

## Skills disponíveis

| Skill | Finalidade |
| --- | --- |
| [`explain-concept`](skills/explain-concept/SKILL.md) | Explicar conceitos, termos e ferramentas de forma progressiva. |
| [`study-plan`](skills/study-plan/SKILL.md) | Transformar objetivos em planos de estudo realistas. |
| [`unblock-exercise`](skills/unblock-exercise/SKILL.md) | Destravar exercícios com dicas graduais e casos de borda. |
| [`security-basics`](skills/security-basics/SKILL.md) | Orientar proteção de contas, projetos, credenciais e privacidade. |

## Base de conhecimento

A base é local, curada e organizada para ser fácil de revisar. Ela abrange:

- lógica de programação, variáveis, condições, repetições, funções e depuração;
- editor de código, terminal, Git, GitHub, dependências e ambientes virtuais;
- trilhas para fundamentos, desenvolvimento web e segurança digital;
- chaves de API, `.env`, `.gitignore`, MFA, phishing, privacidade e resposta inicial a incidentes.

## Como usar

### Opção 1 — Harness compatível com `AGENTS.md`

1. Clone o repositório:

   ```bash
   git clone https://github.com/mullervieira/MENTOR-START-AGENT-IA.git
   ```

2. Abra a pasta em um ambiente de IA compatível com instruções de projeto;
3. Faça uma pergunta em linguagem natural, por exemplo:

   ```text
   Nunca programei. O que é uma variável?
   ```

### Opção 2 — Aplicação web

Siga o guia completo em [`docs/execucao.md`](docs/execucao.md). Em resumo:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
streamlit run src/app.py
```

Antes de executar, preencha `OPENAI_API_KEY` no arquivo `.env`. Nunca publique essa chave ou envie o arquivo `.env` ao GitHub.

## Avaliação

O projeto possui casos de teste para explicação, plano de estudos, integridade acadêmica, limites da base e cibersegurança.

Os critérios de avaliação são:

- clareza;
- fidelidade à base;
- segurança;
- autonomia;
- utilidade;
- segurança defensiva;
- privacidade.

Consulte [`tests/casos_avaliacao.md`](tests/casos_avaliacao.md), [`tests/resultados.md`](tests/resultados.md) e [`docs/metricas.md`](docs/metricas.md).

## Documentação

| Documento | Conteúdo |
| --- | --- |
| [`docs/arquitetura.md`](docs/arquitetura.md) | Camadas, fluxo, privacidade, falhas esperadas e evoluções. |
| [`docs/prompts.md`](docs/prompts.md) | Estratégia de contexto, regras e cenários de segurança. |
| [`docs/metricas.md`](docs/metricas.md) | Critérios, escala e processo de avaliação. |
| [`docs/execucao.md`](docs/execucao.md) | Configuração, execução, testes e solução de problemas. |
| [`docs/pitch.md`](docs/pitch.md) | Roteiro de apresentação de até três minutos. |

## Limitações atuais e próximos passos

- A base ainda cobre um conjunto inicial de temas;
- a seleção de conhecimento usa palavras-chave, não busca semântica;
- não há pesquisa web em tempo real;
- a validação de respostas reais depende de cota disponível na API;
- não há login, banco de dados ou memória permanente.

Possíveis evoluções: ampliar a base, usar embeddings, adicionar fontes verificáveis para temas atuais, criar feedback por resposta e publicar a aplicação online.

## Checklist de entrega

- [x] Documentação do agente;
- [x] Base de conhecimento;
- [x] Prompts e skills;
- [x] Aplicação funcional estruturada;
- [x] Métricas e casos de avaliação;
- [x] Pitch final;
- [x] Orientação defensiva de cibersegurança;
- [ ] Executar a validação de respostas reais após habilitar cota na API.

## Autor

Desenvolvido por [Muller Vieira](https://github.com/mullervieira) como projeto de estudo sobre agentes de IA aplicados à educação em tecnologia.
