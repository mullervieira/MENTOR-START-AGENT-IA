# Como executar o Mentor Start

## O que você precisa

- Python 3.10 ou superior;
- acesso ao terminal na pasta do projeto;
- uma chave da API da OpenAI com cota disponível;
- conexão com a internet para a chamada ao modelo.

> ChatGPT e a API da OpenAI são serviços separados. Ter uma conta ou assinatura do ChatGPT não garante saldo para uso da API.

## 1. Abra a pasta do projeto

No PowerShell, navegue até a pasta onde o repositório foi clonado. Confirme que você vê arquivos como `README.md`, `requirements.txt` e a pasta `src`.

## 2. Crie e ative o ambiente virtual

O ambiente virtual isola as bibliotecas deste projeto das bibliotecas de outros projetos Python.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se o comando `python` não for reconhecido, instale o Python e marque a opção para adicioná-lo ao PATH, ou use o launcher `py` caso ele esteja disponível.

## 3. Instale as dependências

```powershell
pip install -r requirements.txt
```

As bibliotecas instaladas são Streamlit, SDK da OpenAI e suporte ao arquivo `.env`.

## 4. Configure a chave com segurança

Crie a configuração local:

```powershell
Copy-Item .env.example .env
```

Abra `.env` e preencha apenas a linha abaixo com sua chave real:

```text
OPENAI_API_KEY=sua_chave_aqui
```

Não coloque aspas e não compartilhe a chave em mensagens, prints, commits ou vídeos. O arquivo `.env` já está no `.gitignore`.

## 5. Inicie o chat

```powershell
streamlit run src/app.py
```

O terminal mostrará um endereço local, geralmente `http://localhost:8501`. Abra esse endereço no navegador.

## 6. Execute testes manuais

Comece por três perguntas:

```text
O que é Git e GitHub?
Quero estudar desenvolvimento web quatro horas por semana.
Posso publicar minha chave de API no GitHub?
```

Depois, consulte `tests/casos_avaliacao.md` e registre notas em `tests/resultados.md`.

## Teste reproduzível de integração

Com a chave e a cota configuradas, execute:

```powershell
.\.venv\Scripts\python.exe tests\smoke_test.py
```

O script envia três cenários de teste: explicação, plano de estudos e integridade acadêmica.

## Solução de problemas

| Problema | Como resolver |
| --- | --- |
| `python` não é reconhecido | Instale o Python ou teste `py --version`. |
| Erro ao ativar `.venv` | Confirme que você está na raiz do projeto e que o ambiente foi criado. |
| `ModuleNotFoundError` | Ative `.venv` e execute `pip install -r requirements.txt`. |
| Chave não encontrada | Confirme que o arquivo se chama `.env` e contém `OPENAI_API_KEY`. |
| `insufficient_quota` | Revise faturamento e cota da API; uma chave válida não garante saldo. |
| A resposta não usa a base esperada | Revise palavras da pergunta e os arquivos em `agent/knowledge/`. |

## Segurança antes da demonstração

- Confira `git status` antes de fazer commits;
- confirme que `.env` não aparece na lista de arquivos;
- não grave a chave de API em telas ou vídeos;
- use perguntas sem dados pessoais para demonstrar o agente.
