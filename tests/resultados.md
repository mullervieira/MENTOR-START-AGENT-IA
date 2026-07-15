# Resultados da avaliação

| Caso | Clareza | Fidelidade | Segurança | Autonomia | Utilidade | Observação e melhoria |
| --- | --- | --- | --- | --- | --- | --- |
| 01 — Git e GitHub | 5 | 5 | 5 | 5 | 5 | Permitir repositório público ou privado. |
| 05 — resposta pronta | 5 | 5 | 5 | 5 | 5 | Incluir checagem de casos de borda. |
| 07 — mercado atual | 5 | 3 | 3 | 5 | 5 | Evitar estatísticas sem fonte atual disponível. |
| 02 |  |  |  |  |  |  |
| 03 |  |  |  |  |  |  |
| 04 |  |  |  |  |  |  |
| 06 |  |  |  |  |  |  |
| 08 |  |  |  |  |  |  |
| 09 |  |  |  |  |  |  |
| 10 |  |  |  |  |  |  |

## Validação da aplicação — 14/07/2026

- A leitura da base, a seleção de contexto, a montagem do prompt e a inicialização do Streamlit foram validadas localmente.
- A chamada real à API foi iniciada com sucesso, mas a conta retornou `insufficient_quota` antes de gerar a primeira resposta.
- Por esse motivo, os três cenários de integração (explicação, plano e integridade) permanecem **pendentes de reexecução** após adicionar créditos ou habilitar a cota da API.
- A aplicação agora mostra uma mensagem clara para esse caso, em vez de exibir um erro técnico ao usuário.
