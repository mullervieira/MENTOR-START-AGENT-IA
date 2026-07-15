# Aplicação funcional do Mentor Start

## Objetivo

Esta pasta contém a aplicação web do Mentor Start. Ela transforma a definição portátil do agente — regras, persona, conhecimento e skills — em uma experiência de chat acessível pelo navegador.

## Componentes

| Arquivo | Responsabilidade |
| --- | --- |
| `app.py` | Cria a interface Streamlit, mantém o histórico da conversa e exibe as respostas. |
| `knowledge_loader.py` | Lê a base de conhecimento e seleciona os arquivos mais relacionados à pergunta. |
| `prompts.py` | Combina regras, persona e fontes locais nas instruções enviadas ao modelo. |

## Fluxo de uma pergunta

```text
1. Estudante envia uma pergunta pelo chat
2. app.py recebe a pergunta
3. knowledge_loader.py seleciona até dois arquivos relevantes
4. prompts.py monta as instruções do agente e o contexto local
5. A aplicação chama a Responses API da OpenAI
6. A resposta é exibida com os nomes dos arquivos consultados
```

## Escolhas técnicas

### Streamlit

O Streamlit foi escolhido para o MVP porque permite criar uma interface de chat simples com Python, sem exigir conhecimentos prévios de front-end. Isso mantém o foco do projeto no comportamento do agente e na base de conhecimento.

### Recuperação por palavras-chave

A primeira versão compara as palavras da pergunta com o conteúdo dos arquivos `.md`. É uma implementação leve, transparente e adequada para uma base pequena. Ela não substitui uma solução de RAG completa, mas demonstra o princípio de recuperar contexto antes de pedir uma resposta ao modelo.

### Configuração por ambiente

A chave da API é carregada pelo arquivo `.env`, que não é versionado pelo Git. O projeto inclui apenas `.env.example`, sem dados secretos. Nunca coloque uma chave diretamente nos arquivos Python ou no repositório.

### Privacidade

A chamada à API usa `store=False`. O histórico fica somente na sessão atual do Streamlit e é limitado às seis mensagens mais recentes enviadas ao modelo.

## Como executar

As instruções completas estão em [`../docs/execucao.md`](../docs/execucao.md). Em resumo:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
streamlit run src/app.py
```

Antes de iniciar, preencha `OPENAI_API_KEY` no arquivo `.env`. A conta também precisa ter cota disponível para chamadas à API.

## Limitações atuais

- A base cobre apenas fundamentos, ferramentas e trilhas iniciais;
- A seleção por palavras-chave pode não reconhecer perguntas com termos muito diferentes do conteúdo;
- O projeto não faz pesquisa web em tempo real;
- A aplicação ainda não possui login, memória permanente ou banco de dados.

Essas limitações são deliberadas no MVP e ajudam a manter a solução simples, verificável e adequada ao objetivo educacional do projeto.

## Próximas evoluções

- Busca semântica com embeddings;
- Mais materiais revisados na base de conhecimento;
- Pesquisa web com fontes citadas para informações atuais;
- Registro opcional de feedback e métricas por resposta;
- Publicação da aplicação em uma plataforma de hospedagem.
