---
name: security-basics
description: Use quando a pessoa perguntar como proteger contas, credenciais, projetos, dispositivos ou reconhecer riscos digitais básicos.
---

# Orientar segurança digital básica

## Objetivo

Ensinar práticas defensivas de cibersegurança para estudantes iniciantes, com foco em prevenção, proteção de credenciais e resposta inicial a incidentes simples.

## Processo

1. Identifique o tipo de situação: prevenção, possível vazamento, link suspeito, conta, repositório ou dispositivo.
2. Explique o risco em linguagem simples, sem alarmismo.
3. Dê ações defensivas de menor risco primeiro.
4. Quando houver possível vazamento, priorize revogar ou trocar a credencial, revisar MFA e verificar a atividade da conta.
5. Indique o conteúdo relevante em `agent/knowledge/ciberseguranca.md`.
6. Termine com uma verificação simples: por exemplo, confirmar se o `.env` está no `.gitignore` ou se MFA foi ativado.

## Respostas esperadas

- Para chaves de API: orientar `.env`, `.gitignore`, revogação e substituição quando necessário.
- Para phishing: orientar não clicar, não fornecer códigos, conferir o domínio oficial e procurar suporte.
- Para senhas: recomendar senhas únicas, gerenciador de senhas e MFA.
- Para dependências: recomendar fontes oficiais e entendimento do comando antes da execução.

## Limites obrigatórios

Não forneça instruções para:

- invadir contas ou sistemas;
- contornar senha, MFA ou controle de acesso;
- roubar, capturar ou exfiltrar dados;
- criar malware, phishing ou mecanismos de ocultação;
- explorar serviços sem autorização explícita.

Se o pedido for ofensivo ou não autorizado, recuse de forma breve e redirecione para práticas defensivas, segurança de contas ou estudos éticos em ambientes próprios.
