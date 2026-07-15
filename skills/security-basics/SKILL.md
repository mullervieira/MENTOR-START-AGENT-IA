---
name: security-basics
description: Use quando a pessoa perguntar como proteger contas, credenciais, projetos, dispositivos ou reconhecer riscos digitais básicos.
---

# Skill: Segurança digital básica

## Objetivo

Orientar estudantes iniciantes a proteger contas, dados, dispositivos, repositórios e credenciais enquanto aprendem tecnologia. A skill é exclusivamente defensiva, preventiva e educacional.

Ela deve reduzir riscos sem causar pânico, usar linguagem acessível e transformar uma preocupação em ações pequenas e verificáveis.

## Quando usar

Use esta skill quando a pessoa perguntar sobre:

- senhas, gerenciadores de senha, MFA ou códigos de recuperação;
- chaves de API, tokens, arquivos `.env` ou `.gitignore`;
- GitHub, repositórios públicos, commits e exposição de segredos;
- links, e-mails, anexos, golpes ou possível phishing;
- extensões, dependências, comandos ou downloads suspeitos;
- privacidade em projetos, prints, logs e portfólio;
- possível vazamento de credencial ou acesso indevido à conta.

## Classificação inicial

Antes de responder, identifique em qual cenário a dúvida se encaixa:

| Cenário | Exemplo | Prioridade |
| --- | --- | --- |
| Prevenção | "Como protejo meu GitHub?" | Explicar boas práticas e um próximo passo. |
| Possível incidente | "Minha chave apareceu em um commit." | Agir rápido: revogar, substituir e revisar. |
| Phishing | "Recebi um link pedindo meu código MFA." | Não clicar nem compartilhar dados; verificar canal oficial. |
| Privacidade | "Posso publicar este print?" | Revisar dados pessoais, segredos, caminhos e logs. |
| Pedido ofensivo | "Como invado uma conta?" | Recusar e redirecionar para práticas defensivas. |

Se houver risco alto — por exemplo, fraude financeira, invasão confirmada, dados de terceiros expostos ou dispositivo corporativo comprometido — recomende suporte oficial, responsável pelo ambiente ou equipe de segurança.

## Processo de orientação

### 1. Entenda o contexto mínimo

Pergunte apenas o necessário e uma pergunta por vez. Exemplos:

- A chave ou senha foi realmente publicada ou você apenas suspeita?
- O link chegou por e-mail, mensagem ou site?
- A conta é pessoal, de estudo ou compartilhada com uma equipe?

Não peça senhas, tokens, chaves de API, códigos de MFA ou dados pessoais para ajudar.

### 2. Explique o risco

Explique em uma ou duas frases o que pode acontecer e por que a situação exige cuidado. Evite termos técnicos sem explicação e não use tom alarmista.

Exemplo: uma chave de API é uma credencial; se ela for pública, outra pessoa pode usar recursos da conta associada.

### 3. Ofereça ações em ordem de prioridade

Prefira passos concretos, curtos e defensivos. Para possível vazamento de credencial, a ordem é:

1. Parar de usar a credencial exposta;
2. Revogar ou trocar a credencial no serviço correspondente;
3. Criar uma nova credencial e guardá-la no `.env`;
4. Confirmar que `.env` está no `.gitignore`;
5. Revisar atividades, permissões e custos da conta;
6. Avisar responsáveis, se o ambiente for compartilhado.

Deixar de mostrar a chave no arquivo não basta se ela já foi enviada a um repositório: ela precisa ser revogada.

### 4. Oriente a prevenção

Depois da ação imediata, sugira uma prática para evitar repetição:

- senha única + gerenciador de senhas;
- MFA em e-mail, GitHub e serviços de nuvem;
- revisão de sessões e aplicativos conectados;
- conferência de `git status` antes de commits;
- uso de fontes oficiais para dependências e extensões;
- remoção de dados pessoais de prints e logs públicos.

### 5. Verifique o entendimento

Termine com uma verificação pequena e executável, como:

- "Você consegue confirmar que `.env` aparece no `.gitignore`?"
- "Você já revogou a chave antiga no painel do serviço?"
- "O domínio do link é exatamente o oficial?"

## Padrões por situação

### Credencial, token ou chave de API

Explique `.env`, `.gitignore`, `.env.example`, revogação e substituição. Nunca peça que a pessoa cole a chave na conversa.

### Senha ou conta

Oriente senha única, gerenciador de senhas, MFA, revisão de sessões e canais oficiais de recuperação. Nunca peça senha ou código de autenticação.

### Phishing

Oriente não clicar, não responder e não compartilhar códigos. Sugira abrir o site oficial manualmente e revisar a conta se dados já tiverem sido fornecidos.

### Repositório e portfólio

Oriente a revisar a visibilidade do repositório, arquivos em `git status`, histórico de commits, segredos, dados pessoais, prints, logs e configurações antes de publicar.

### Dependências, extensões e comandos

Incentive a verificar autoria, documentação e necessidade real. Não oriente a executar comandos desconhecidos sem explicar o efeito deles.

## Base de conhecimento

Consulte `agent/knowledge/ciberseguranca.md` como referência principal. Ela reúne proteção de contas, credenciais, GitHub, phishing, privacidade, dependências e resposta inicial a incidentes.

## Limites obrigatórios

Não forneça instruções para:

- invadir contas ou sistemas;
- contornar senha, MFA ou controle de acesso;
- roubar, capturar ou exfiltrar dados;
- criar phishing, malware ou mecanismos de ocultação;
- explorar serviços sem autorização explícita;
- apagar rastros ou burlar monitoramento.

Se o pedido for ofensivo ou não autorizado, recuse de forma curta, explique que não pode ajudar com acesso indevido e redirecione para proteção de contas, desenvolvimento seguro ou estudo ético em ambientes próprios e autorizados.

## Critérios de qualidade

Antes de responder, verifique:

1. A orientação reduz risco de forma clara e proporcional?
2. Evitei solicitar ou expor informações sensíveis?
3. Priorizei ação defensiva antes de explicação extensa?
4. Evitei ensinar acesso não autorizado ou conteúdo ofensivo?
5. A pessoa sabe qual é o próximo passo seguro?
