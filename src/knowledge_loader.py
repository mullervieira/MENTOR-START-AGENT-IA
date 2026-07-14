"""Leitura e seleção simples da base de conhecimento local."""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = PROJECT_ROOT / "agent" / "knowledge"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def normalize(text: str) -> set[str]:
    text = unicodedata.normalize("NFD", text.lower())
    text = "".join(char for char in text if unicodedata.category(char) != "Mn")
    return set(re.findall(r"[a-z0-9]{3,}", text))


def load_agent_files() -> tuple[str, str]:
    return read_text(PROJECT_ROOT / "AGENTS.md"), read_text(PROJECT_ROOT / "agent" / "persona.md")


def select_knowledge(question: str, limit: int = 2) -> list[tuple[str, str]]:
    """Seleciona arquivos por palavras-chave; evolução futura: busca vetorial."""
    terms = normalize(question)
    ranked = []
    for path in KNOWLEDGE_DIR.glob("*.md"):
        content = read_text(path)
        ranked.append((len(terms & normalize(content)), path.name, content))
    ranked.sort(key=lambda item: item[0], reverse=True)
    selected = [item for item in ranked if item[0] > 0][:limit] or ranked[:1]
    return [(name, content) for _, name, content in selected]
