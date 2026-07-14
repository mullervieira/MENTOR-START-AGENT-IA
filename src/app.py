"""Interface Streamlit do Mentor Start."""
from __future__ import annotations

import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

from knowledge_loader import load_agent_files, select_knowledge
from prompts import build_instructions

load_dotenv()
st.set_page_config(page_title="Mentor Start", page_icon="🎓")


def get_answer(question: str) -> tuple[str, list[str]]:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("Chave não encontrada. Crie .env a partir de .env.example e informe OPENAI_API_KEY.")

    rules, persona = load_agent_files()
    sources = select_knowledge(question)
    history = st.session_state.messages[-6:]
    messages = [{"role": item["role"], "content": item["content"]} for item in history]
    messages.append({"role": "user", "content": question})
    response = OpenAI(api_key=api_key).responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.6-luna"),
        instructions=build_instructions(rules, persona, sources),
        input=messages,
        store=False,
    )
    return response.output_text, [name for name, _ in sources]


def main() -> None:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    st.title("Mentor Start")
    st.caption("Seu mentor de estudos para começar em tecnologia com mais clareza.")
    with st.sidebar:
        st.header("Como o agente responde")
        st.write("Usa a base local, explica para iniciantes e não entrega respostas prontas de atividades avaliativas.")
        if st.button("Limpar conversa"):
            st.session_state.messages = []
            st.rerun()

    if not st.session_state.messages:
        st.info("Experimente: “O que é Git?” ou “Por onde começo a estudar desenvolvimento web?”")

    for item in st.session_state.messages:
        with st.chat_message(item["role"]):
            st.markdown(item["content"])

    question = st.chat_input("Digite sua dúvida de tecnologia")
    if not question:
        return

    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
    with st.chat_message("assistant"):
        with st.spinner("O Mentor Start está preparando uma resposta..."):
            try:
                answer, source_names = get_answer(question)
                st.markdown(answer)
                st.caption("Arquivos selecionados: " + ", ".join(source_names))
            except Exception as error:
                answer = f"Não foi possível gerar a resposta agora. Detalhe: {error}"
                st.error(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})


if __name__ == "__main__":
    main()
