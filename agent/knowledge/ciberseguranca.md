# Cibersegurança para iniciantes

## Objetivo e escopo

Este material ensina hábitos defensivos para quem está começando em tecnologia. O foco é proteger contas, dados pessoais, dispositivos, repositórios e credenciais usadas em projetos.

O Mentor Start não substitui equipes de segurança, suporte institucional ou resposta profissional a incidentes. Em situações de alto risco, como fraude financeira, invasão confirmada ou exposição de dados de terceiros, o estudante deve contatar o suporte do serviço e os responsáveis pelo ambiente.

## Princípios essenciais

### Defesa em camadas

Uma única proteção pode falhar. Por isso, segurança combina práticas: senha única, MFA, atualização, revisão de permissões e cuidado com links. Cada camada reduz o impacto de um erro ou vazamento.

### Menor privilégio

Dê a uma conta, aplicação ou pessoa somente o acesso necessário para a tarefa atual. Uma chave de API usada para estudo não deve ter permissões maiores que o necessário.

### Verificar antes de confiar

Mensagens, links, comandos e extensões podem parecer legítimos. Antes de clicar, executar ou instalar, confirme a fonte, o domínio e o propósito.

### Segurança desde o início

Boas práticas não são uma etapa final. Elas começam ao criar o repositório, configurar o `.gitignore`, organizar variáveis de ambiente e ativar MFA.

## Proteção de contas

### Senhas e gerenciador de senhas

Uma senha deve ser longa, exclusiva para cada serviço e difícil de adivinhar. Reutilizar a mesma senha amplia o impacto de um vazamento.

Um gerenciador de senhas ajuda a criar e guardar senhas únicas. Proteja-o com uma senha mestra forte e MFA quando disponível.

### Autenticação em dois fatores (MFA)

MFA adiciona uma confirmação além da senha, como aplicativo autenticador ou chave de segurança. Ela reduz o risco de acesso indevido mesmo quando a senha é descoberta.

Ative MFA em e-mail, GitHub, serviços de nuvem e plataformas de desenvolvimento. Nunca compartilhe códigos de MFA, códigos de recuperação ou aprovações de login por mensagem.

### Revisão de sessões e permissões

Revise periodicamente dispositivos conectados, sessões ativas, aplicativos autorizados e permissões de integrações. Remova acessos que não reconheça ou não use mais.

## Proteção de projetos e credenciais

### Chaves de API, tokens e arquivos `.env`

Chaves de API, tokens e senhas são credenciais. Quem as possui pode usar recursos em nome da conta, dependendo das permissões concedidas.

Práticas obrigatórias:

- nunca publicar chaves, tokens, senhas ou dados pessoais no GitHub;
- guardar segredos no arquivo `.env` ou em variáveis de ambiente;
- incluir `.env` no `.gitignore` antes do primeiro commit;
- usar `.env.example` apenas com nomes de variáveis, sem valores reais;
- restringir permissões e rotacionar chaves quando possível;
- revogar e substituir imediatamente uma chave exposta.

**Exemplo no Mentor Start:** `OPENAI_API_KEY` fica em `.env`; o `.gitignore` impede que esse arquivo seja enviado ao repositório.

### GitHub seguro

- Ative MFA na conta do GitHub;
- revise se o repositório deve ser público ou privado antes de publicar;
- confira os arquivos listados em `git status` antes de fazer `git add` e `git push`;
- não aceite convites, pull requests ou integrações desconhecidas sem revisar;
- use descrições claras de commits para facilitar auditoria do histórico.

### Dependências, extensões e downloads

Dependências são códigos de terceiros usados pelo projeto. Instale apenas o que for necessário e dê preferência a fontes oficiais e documentação do projeto.

Antes de executar um comando encontrado online, entenda o que ele faz. Evite comandos que baixam e executam conteúdo automaticamente, especialmente se vierem de mensagens, comentários ou sites desconhecidos.

Extensões do editor também merecem atenção: verifique autoria, avaliações, permissões e necessidade real antes de instalar.

## Phishing e engenharia social

Phishing é uma tentativa de enganar alguém para obter senhas, códigos, dados ou acesso. Pode fingir ser uma empresa, colega, banco ou plataforma conhecida.

Sinais de atenção:

- urgência excessiva, ameaça ou promessa boa demais para ser verdadeira;
- endereço de e-mail, domínio ou link parecido — mas não igual — ao oficial;
- pedido de senha, código MFA, chave de API ou pagamento;
- anexo inesperado;
- pressão para ignorar procedimentos de segurança.

Antes de clicar, confirme o remetente e digite o endereço oficial no navegador. Não informe códigos de autenticação, chaves ou senhas por mensagem.

## Atualizações, privacidade e dispositivos

- mantenha sistema operacional, navegador, editor e bibliotecas atualizados;
- instale programas apenas de fontes confiáveis;
- bloqueie a tela quando se afastar do computador;
- evite salvar senhas ou chaves em arquivos de texto desprotegidos;
- compartilhe apenas os dados necessários em projetos públicos;
- remova informações pessoais de prints, logs e arquivos antes de publicar.

## Resposta inicial a incidentes

### Chave, token ou senha expostos

1. Pare de usar a credencial exposta.
2. Revogue ou altere a credencial no serviço correspondente.
3. Crie uma nova credencial e atualize o `.env` local.
4. Revise atividade recente, permissões e custos da conta.
5. Remova o segredo do código e do histórico público quando possível.
6. Informe responsáveis, equipe ou suporte se o ambiente for compartilhado.

Remover uma chave de um arquivo não é suficiente se ela já foi enviada ao GitHub: ela deve ser revogada.

### Link suspeito ou possível phishing

1. Não clique nem responda.
2. Não informe códigos, senhas ou dados.
3. Abra o site oficial manualmente para verificar a situação.
4. Se você inseriu dados, altere a senha pelo site oficial e revise MFA e sessões ativas.
5. Reporte a mensagem ao serviço ou organização que ela tentou imitar.

### Dispositivo possivelmente comprometido

Desconecte-o de redes compartilhadas quando houver suspeita séria, execute verificações de segurança confiáveis e procure suporte técnico. Evite tentar investigar sistemas de terceiros ou apagar evidências.

## Limites éticos e de segurança

O Mentor Start oferece apenas orientação defensiva, preventiva e educacional. Ele não ensina nem detalha como:

- invadir contas ou sistemas;
- contornar senha, MFA ou controle de acesso;
- roubar, capturar ou exfiltrar dados;
- criar phishing, malware ou mecanismos de ocultação;
- explorar serviços sem autorização explícita.

Quando receber esse tipo de pedido, o agente deve recusar de forma breve e redirecionar para segurança de contas, desenvolvimento seguro ou estudo ético em ambientes próprios e autorizados.
