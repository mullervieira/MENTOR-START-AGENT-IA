# Arquitetura do Mentor Start

## Visão geral

O Mentor Start possui duas formas complementares de uso:

1. **Versão portátil:** arquivos de instrução que podem ser lidos por harnesses compatíveis com `AGENTS.md`.
2. **Aplicação web:** um chat em Streamlit que lê a base local e envia contexto para um modelo de IA.

Essa separação mantém o comportamento do agente independente da interface. Regras, persona, conhecimento e skills podem evoluir sem reescrever a tela do chat.

## Componentes

| Camada | Arquivos | Responsabilidade |
| --- | --- | --- |
| Governança | `AGENTS.md` | Define missão, escopo, limites, segurança e tom. |
| Persona | `agent/persona.md` | Define postura pedagógica e comunicação. |
| Conhecimento | `agent/knowledge/*.md` | Fornece conteúdo revisado para fundamentar respostas. |
| Skills | `skills/*/SKILL.md` | Padroniza processos para tarefas recorrentes. |
| Recuperação | `src/knowledge_loader.py` | Seleciona arquivos relacionados à pergunta. |
| Prompt | `src/prompts.py` | Combina regras, persona, fontes e limites de execução. |
| Interface | `src/app.py` | Exibe o chat, mantém histórico temporário e chama o modelo. |
| Avaliação | `tests/` e `docs/metricas.md` | Define casos, critérios e registro de resultados. |

## Fluxo de resposta

```text
Estudante envia uma pergunta
        |
        v
Streamlit recebe a mensagem e preserva o histórico recente
        |
        v
knowledge_loader seleciona até dois arquivos da base por palavras-chave
        |
        v
prompts combina AGENTS.md + persona + fontes + regras de segurança
        |
        v
Responses API gera uma resposta
        |
        v
Aplicação mostra resposta e arquivos consultados
```

## Recuperação de contexto

A versão inicial utiliza correspondência por palavras-chave. Essa decisão foi intencional: é simples de explicar, transparente para entrevistas e adequada à base pequena do MVP.

Limitação: perguntas que usam termos muito diferentes do material podem selecionar uma fonte menos precisa. Evoluções possíveis incluem dividir documentos em trechos, usar embeddings, aplicar busca vetorial e registrar avaliações de relevância.

## Segurança e privacidade

- A chave da API é lida do `.env`, nunca do código-fonte;
- `.env` está no `.gitignore` e não deve ser enviado ao GitHub;
- a aplicação usa `store=False` na chamada ao modelo;
- o histórico mantido pela interface é apenas da sessão atual e envia no máximo seis mensagens recentes;
- a base contém orientação defensiva sobre credenciais, phishing e privacidade;
- pedidos ofensivos ou não autorizados devem ser recusados pelas regras do agente.

## Falhas esperadas e comportamento

| Situação | Comportamento da aplicação |
| --- | --- |
| Sem chave no `.env` | Exibe orientação para configurar `OPENAI_API_KEY`. |
| Sem cota na API | Exibe mensagem amigável para revisar faturamento e limites. |
| Tema fora da base | O prompt orienta o modelo a reconhecer a limitação. |
| Pergunta com dados atuais | O prompt informa que não há pesquisa web em tempo real. |
| Pedido de resposta pronta | O agente deve aplicar orientação gradual, não entregar solução final. |

## Evolução planejada

1. Ampliar e revisar a base de conhecimento;
2. Melhorar recuperação com busca semântica;
3. Adicionar avaliação automatizada dos casos de teste;
4. Incluir pesquisa web com fontes verificáveis para perguntas atuais;
5. Criar feedback por resposta e hospedagem da aplicação.
