"""Montagem do contexto enviado ao modelo de IA."""
from __future__ import annotations


def build_instructions(rules: str, persona: str, sources: list[tuple[str, str]]) -> str:
    context = "\n\n".join(f"## Fonte local: {name}\n{content}" for name, content in sources)
    return f"""{rules}

---
{persona}

---
## Contexto local disponível
{context}

---
## Regras de execução
- Responda em português do Brasil e priorize o contexto local.
- Para dados atuais, mercado, vagas, versões ou tendências, diga que esta versão não pesquisa a web em tempo real; não invente estatísticas ou fontes.
- Em exercícios avaliativos, não entregue a solução completa; use dicas graduais.
- Quando usar o contexto local, termine com `Base consultada: <nomes dos arquivos>`.
- Seja objetivo e adequado para iniciantes.
"""
