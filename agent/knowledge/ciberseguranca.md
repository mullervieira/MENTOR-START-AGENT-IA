# Cibersegurança para iniciantes

## Objetivo deste material

Este conteúdo ajuda estudantes a adotarem hábitos seguros enquanto aprendem tecnologia. O foco é preventivo: proteger contas, dados pessoais, projetos e credenciais.

## Senhas e gerenciadores de senhas

Uma senha forte deve ser longa, exclusiva para cada serviço e difícil de adivinhar. Reutilizar a mesma senha em vários sites aumenta o impacto de um vazamento.

Um gerenciador de senhas ajuda a criar e guardar senhas únicas sem depender da memória. O estudante deve proteger o gerenciador com uma senha mestra forte e autenticação em dois fatores quando disponível.

## Autenticação em dois fatores (MFA)

Autenticação em dois fatores adiciona uma segunda confirmação além da senha, como um aplicativo autenticador ou uma chave de segurança. Ela reduz o risco de acesso indevido mesmo quando uma senha é descoberta.

Sempre que possível, ative MFA em e-mail, GitHub, serviços de nuvem e plataformas de desenvolvimento.

## Chaves de API, tokens e arquivos `.env`

Uma chave de API ou token funciona como uma credencial que permite a um programa acessar um serviço. Quem possui essa chave pode, dependendo das permissões, usar recursos em nome da conta.

Por isso:

- nunca publique chaves, tokens, senhas ou dados sensíveis no GitHub;
- guarde credenciais no arquivo `.env` ou em variáveis de ambiente;
- inclua `.env` no `.gitignore` antes de fazer commits;
- use um arquivo `.env.example` com nomes de variáveis, mas sem valores reais;
- se uma chave vazar, revogue-a no serviço imediatamente e crie outra.

**Exemplo no Mentor Start:** o arquivo `.env` guarda `OPENAI_API_KEY`; o `.gitignore` impede que ele seja enviado ao repositório.

## Phishing e links suspeitos

Phishing é uma tentativa de enganar alguém para obter senhas, códigos, dados pessoais ou acesso a contas. A mensagem pode fingir ser de uma empresa, colega ou plataforma conhecida.

Sinais de atenção:

- urgência excessiva, ameaça ou promessa boa demais para ser verdadeira;
- endereço de e-mail ou domínio estranho;
- pedido de senha, código de MFA ou chave de API;
- link encurtado ou diferente do site oficial;
- anexo inesperado.

Antes de clicar, verifique o remetente e abra o site oficial digitando o endereço no navegador. Nunca informe códigos de autenticação ou chaves por mensagem.

## Atualizações e dependências

Mantenha sistema operacional, navegador, editor e bibliotecas atualizados. Baixe programas e extensões de fontes oficiais e revise o que uma extensão pede para acessar.

Em projetos, instale dependências apenas quando souber por que elas são necessárias. Evite executar comandos encontrados aleatoriamente na internet sem entender seu efeito.

## Se algo der errado

Se uma senha, chave ou token for exposto:

1. Revogue ou altere a credencial no serviço correspondente.
2. Ative ou revise MFA.
3. Remova o segredo do código e do histórico público quando possível.
4. Verifique atividades recentes da conta.
5. Informe o responsável pela conta ou equipe, se for um ambiente compartilhado.

Se suspeitar de phishing, não responda nem forneça informações. Troque a senha pelo site oficial se houver risco de comprometimento e procure o suporte do serviço.

## Limites

Este material não ensina invasão, exploração de falhas ou acesso a sistemas de terceiros. O objetivo é construir hábitos seguros e orientar ações de proteção.
