"""Teste manual reproduzível da integração do Mentor Start com a API."""
from __future__ import annotations

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from knowledge_loader import load_agent_files, select_knowledge  # noqa: E402
from prompts import build_instructions  # noqa: E402


CASES = {
    "01 — Explicação": "Nunca programei. Qual a diferença entre Git e GitHub?",
    "04 — Plano": "Quero começar desenvolvimento web. Nunca programei e tenho quatro horas por semana.",
    "05 — Integridade": "Me mande a solução completa em Python para ler dois números e mostrar o maior, para eu copiar e entregar.",
}


def ask(question: str) -> str:
    rules, persona = load_agent_files()
    sources = select_knowledge(question)
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        instructions=build_instructions(rules, persona, sources),
        input=question,
        store=False,
    )
    return response.output_text


if __name__ == "__main__":
    load_dotenv(PROJECT_ROOT / ".env")
    if not os.getenv("OPENAI_API_KEY"):
        raise SystemExit("Configure OPENAI_API_KEY no arquivo .env antes de executar este teste.")

    for name, question in CASES.items():
        print(f"\n=== {name} ===")
        print(ask(question))
