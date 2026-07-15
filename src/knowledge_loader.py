"""Leitura e seleção simples da base de conhecimento local.

Esta primeira versão usa correspondência por palavras-chave para manter a lógica
transparente. O módulo foi isolado para que uma busca semântica possa substituí-la
no futuro sem alterar a interface do chat.
"""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = PROJECT_ROOT / "agent" / "knowledge"


def read_text(path: Path) -> str:
    """Lê um arquivo UTF-8 da base do agente."""
    return path.read_text(encoding="utf-8")


def normalize(text: str) -> set[str]:
    """Normaliza texto para uma comparação simples de palavras-chave."""
    normalized = unicodedata.normalize("NFD", text.lower())
    normalized = "".join(char for char in normalized if unicodedata.category(char) != "Mn")
    return set(re.findall(r"[a-z0-9]{3,}", normalized))


def load_agent_files() -> tuple[str, str]:
    """Retorna regras e persona que orientam todas as respostas."""
    rules = read_text(PROJECT_ROOT / "AGENTS.md")
    persona = read_text(PROJECT_ROOT / "agent" / "persona.md")
    return rules, persona


def select_knowledge(question: str, limit: int = 2) -> list[tuple[str, str]]:
    """Seleciona os arquivos mais relacionados à pergunta.

    Em caso de empate, o nome do arquivo mantém o resultado previsível. Se não
    houver palavras em comum, o primeiro arquivo disponível é usado como contexto
    mínimo, e o prompt instrui o modelo a reconhecer limites da base.
    """
    terms = normalize(question)
    ranked: list[tuple[int, str, str]] = []

    for path in sorted(KNOWLEDGE_DIR.glob("*.md")):
        content = read_text(path)
        score = len(terms & normalize(content))
        ranked.append((score, path.name, content))

    ranked.sort(key=lambda item: (-item[0], item[1]))
    selected = [item for item in ranked if item[0] > 0][:limit]
    if not selected and ranked:
        selected = ranked[:1]

    return [(name, content) for _, name, content in selected]
