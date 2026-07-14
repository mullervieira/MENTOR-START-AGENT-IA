# Como executar a aplicação

## Pré-requisitos

- Python 3.10 ou superior.
- Uma chave da API da OpenAI.

> Uma assinatura do ChatGPT e o acesso à API são produtos separados. Mantenha sua chave apenas no computador.

## Configuração

No terminal, na raiz do repositório:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```

Abra o arquivo `.env` e substitua `sua_chave_aqui` pela sua chave. Não envie esse arquivo ao GitHub; ele está no `.gitignore`.

## Iniciar

```powershell
streamlit run src/app.py
```

Abra o endereço local mostrado no terminal para conversar com o Mentor Start.

## Testar

Execute os casos de `tests/casos_avaliacao.md` e preencha `tests/resultados.md`. Para a demonstração, use as perguntas sobre Git/GitHub, plano de estudos e recusa de resposta pronta.

## Nota técnica

A aplicação usa o SDK oficial da OpenAI e a Responses API. Ela envia as instruções do agente, os arquivos locais relevantes e o histórico recente da conversa ao modelo. O parâmetro `store=False` evita solicitar armazenamento da resposta pela API.
