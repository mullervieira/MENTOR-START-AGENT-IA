# Ferramentas iniciais de desenvolvimento

## Objetivo deste material

Este arquivo apresenta ferramentas que costumam aparecer no começo da jornada de desenvolvimento. O foco é explicar o papel de cada uma; instruções específicas devem considerar o sistema operacional e a ferramenta escolhida pela pessoa.

## Editor de código

Um editor de código é o programa usado para criar, editar e organizar arquivos de um projeto. Ele costuma oferecer recursos como destaque de sintaxe, sugestões, busca, terminal integrado e extensões.

O Visual Studio Code (VS Code) é um exemplo popular, mas o princípio vale para outros editores. O editor ajuda a escrever código; ele não substitui o entendimento da lógica.

## Terminal

O terminal é uma interface em que você digita comandos para interagir com o computador. Entre usos comuns estão navegar entre pastas, criar arquivos, instalar dependências, executar programas e usar o Git.

**Cuidados para iniciantes:** comandos podem ter efeitos diferentes conforme o sistema operacional. Antes de orientar uma sequência de comandos, descubra se a pessoa está usando Windows, macOS ou Linux e explique o que cada comando fará.

## Git

Git é um sistema de controle de versão. Ele registra mudanças em arquivos ao longo do tempo, permitindo entender o histórico do projeto, comparar versões, colaborar e recuperar uma alteração quando necessário.

Conceitos iniciais importantes:

- **repositório:** pasta de projeto acompanhada pelo Git;
- **commit:** registro nomeado de um conjunto de alterações;
- **branch:** linha de trabalho paralela ou alternativa;
- **remote:** repositório hospedado em outro serviço, como o GitHub;
- **push:** envio de commits locais para o repositório remoto;
- **pull:** obtenção e integração de mudanças remotas no repositório local.

**Boa prática:** antes de comandos que alteram ou apagam algo, explique o efeito e incentive a pessoa a verificar o estado com `git status`.

## GitHub

GitHub é uma plataforma online para hospedar repositórios Git. Ela permite compartilhar projetos, colaborar por meio de pull requests e issues, acompanhar alterações e construir um portfólio público.

Git e GitHub não são a mesma coisa: Git é a ferramenta de controle de versão; GitHub é um serviço que pode hospedar repositórios Git.

Antes de publicar um repositório, revise se ele contém arquivos de configuração, chaves, dados pessoais, logs ou prints que não deveriam ficar públicos. O arquivo `.gitignore` ajuda a evitar que arquivos locais sensíveis sejam incluídos por acidente.

## Dependências e gerenciadores de pacotes

Muitos projetos usam código produzido por outras pessoas, chamado de dependências ou bibliotecas. Um gerenciador de pacotes instala e registra essas dependências para o projeto.

Exemplos variam conforme a linguagem: `pip` em projetos Python e `npm` em projetos JavaScript. Antes de sugerir uma instalação, explique por que ela é necessária e onde o comando deve ser executado.

## Ambiente virtual

Em algumas linguagens, um ambiente virtual isola as dependências de cada projeto. Isso evita que uma atualização de biblioteca em um projeto interfira em outro.

No início, a ideia central é: cada projeto deve conseguir declarar as ferramentas de que precisa para ser reproduzido por outra pessoa.

## Checklist antes de executar um projeto

1. Leia o README do projeto;
2. confirme a linguagem e a versão necessárias;
3. crie ambiente isolado quando a linguagem usar dependências;
4. instale apenas o que está documentado;
5. nunca cole chaves ou senhas em comandos;
6. execute uma etapa por vez e observe o resultado.

## Organização de um projeto iniciante

Mesmo projetos pequenos ficam mais fáceis de entender quando têm um README, nomes de arquivos claros, dependências registradas e commits descritivos. Essa organização permite que outra pessoa — ou você no futuro — consiga reproduzir o projeto e acompanhar sua evolução.
