# Arquitetura do Mentor Start

## Versão portátil

O Mentor Start funciona em harnesses compatíveis com `AGENTS.md`, usando regras, persona, base local e skills.

## Aplicação funcional

```text
Pergunta no Streamlit
        |
        v
Seleção por palavras-chave em agent/knowledge
        |
        v
AGENTS.md + persona + contexto selecionado + histórico recente
        |
        v
Responses API da OpenAI
        |
        v
Resposta no chat + arquivos consultados
```

A seleção por palavras-chave foi escolhida por ser simples de explicar e suficiente para a base inicial. Uma evolução futura pode usar embeddings e busca vetorial.
