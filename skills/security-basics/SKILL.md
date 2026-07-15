---
name: security-basics
description: Use quando a pessoa perguntar como proteger contas, credenciais, projetos, dispositivos ou reconhecer riscos digitais básicos.
---

# Orientar segurança digital básica

## Objetivo

Ensinar práticas defensivas de cibersegurança para estudantes iniciantes, com foco em prevenção, proteção de credenciais e resposta inicial a incidentes simples.

## Processo

1. Identifique o tipo de situação: prevenção, possível vazamento, link suspeito, conta, repositório ou dispositivo.
2. Classifique a urgência: orientação geral, possível incidente ou risco alto que exige suporte oficial.
3. Explique o risco em linguagem simples, sem alarmismo.
4. Dê ações defensivas de menor risco primeiro e em ordem clara.
5. Quando houver possível vazamento, priorize revogar ou trocar a credencial, revisar MFA, sessões, permissões e atividade da conta.
6. Quando houver risco alto, recomende suporte oficial, responsável pelo ambiente ou equipe de segurança.
7. Indique o conteúdo relevante em `agent/knowledge/ciberseguranca.md`.
8. Termine com uma verificação simples: por exemplo, confirmar se o `.env` está no `.gitignore` ou se MFA foi ativado.

## Respostas esperadas

- Para chaves de API: orientar `.env`, `.gitignore`, revogação e substituição quando necessário.
- Para phishing: orientar não clicar, não fornecer códigos, conferir o domínio oficial e procurar suporte.
- Para senhas: recomendar senhas únicas, gerenciador de senhas e MFA.
- Para dependências: recomendar fontes oficiais e entendimento do comando antes da execução.
- Para repositórios: orientar revisão de visibilidade, `git status`, segredos e MFA no GitHub.
- Para privacidade: orientar remoção de dados pessoais de prints, logs e arquivos públicos.

## Limites obrigatórios

Não forneça instruções para:

- invadir contas ou sistemas;
- contornar senha, MFA ou controle de acesso;
- roubar, capturar ou exfiltrar dados;
- criar malware, phishing ou mecanismos de ocultação;
- explorar serviços sem autorização explícita.

Se o pedido for ofensivo ou não autorizado, recuse de forma breve e redirecione para práticas defensivas, segurança de contas ou estudos éticos em ambientes próprios.
