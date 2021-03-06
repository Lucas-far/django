

"""
Módulo: curso_pytools.py

Palavra chave: curso pytools
"""

###################################
"Pytools"  # Criação de Repositório
###################################

"Título"  # Procedimentos para criar um repositório no GitHub com módulos básicos relevantes
def parte1():
    """
    1. https://github.com/
    2. +                  || canto superior direito da tela, próximo ao avatar
    3. New repository     || link do menu dropdown para iniciar a criação de um repositório
    4. Owner              || pode ser uma pessoa ou organização
    5. Description        || descrição do repositório
    6. Tipo               || repositórios costumam ser configurados como: PUBLIC
    7. README.md          || módulo que serve como documentação de explicação do projeto (linguagem markdown)
    8. .gitignore         || escolher sua linguagem de programação
    9. License            || normalmente, é do tipo: agpl (GNU Affero General Public License)
    10. Create repository || botão para criar um repositório
    """

#######################
"Pytools"  # Chaves SSH
#######################

"Título"  # Procedimentos para clonar um repositório
"5"       # ao executar, cria-se um dir em /home/seu_user/nome_do_rep_clonado"
def parte1():
    """
    1 - Uma vez criado um repositório, este passa a ter um link: (https) ou (ssh)
    2 - No segundo caso, é preciso criar uma chave (explicado posteriormente)
    3 - O link de acesso encontra-se no botão (code)
    4 - Copia-se esse link
    5 - [ OPÇÃO 1 ] git clone link html ou ssh
    5 - [ OPÇÃO 2 ] git clone link html ou ssh nome do rep.
    """

"Título"  # Comandos para salvar mudanças para o repositório
"1"       # Ao executar, se for a primeira vez, será requisitado o login da sua conta GitHub
def parte2():
    """
    1 - [ OPÇÃO 1 ] git push
    1 - [ OPÇÃO 2 ] git push origin master
    2 - Fornecer dados da sua conta Github
    """

"OBS"  # Essa etapa é feita para gerar no seu OS, um dir que contém sua chave SSH pública,
"OBS"  # Essa chave é copiada e salva no seu GitHub, que permitirá clonagem de repositórios pela opção SSH
"OBS"  # A intenção de usar uma chave SSH, é para evitar requisições repetitivas de senha ao fazer commit
def parte3():
    """
    1 - [ Ubuntu  ] ssh-keygen -t rsa
    1 - [ Windows ] ssh-keygen.exe -t rsa
    2 - Apertar ENTER
    3 - Em seguida, será requisitado uma passphrase

       EXEMPLO:
               umafrasepodevalermuitacoisamasaomesmotempopodenaovalernada

    4 - Apertar ENTER
    5 - Serão criados: (public key) (key fingerprint = SHA256) (key's randomart)
    6 - Acessar seu avatar no site do Github (canto superior direito da tela)
    7 - Dropdown (Settings)
    8 - Botão (SSH and GPG keys)
    9 - Botão (New ssh key)
    10 - Na página de criação da chave, temos: (title) (key)
    11 - Ir para: [ /home/seu_user/.ssh ]
    12 - Procurar: [ cat id_rsa.pub ]
    13 - Abrir e copiar a chave

    PROCEDIMENTOS 11 até 13 VIA TERMINAL:
                                         cd /home/seu_user/.ssh >>> cat id_rsa.pub >>> copiar retorno

    14 - Retornar à página de criação da chave SSH
    15 - Colar a chave copiada no campo: [ key ]
    16 - Salvar
    17 - Agora, você estará apto a clonar repositórios por sua chave SSH [ ver def git_clonar() ]
    """

#################
"Pytools"  # Fork
#################

"1"  # Há diferença entre CLONE e FORK?
"2"  # O que seria CLONE?
"3"  # O que seria FORK?
"4"  # Como FORK conecta-se com o projeto original?
"5"  # Como CLONE conecta-se com o projeto original?
"6"  # Há algum padrão envolvendo CLONE e FORK?

"1"  # sim
"2"  # Copiar um projeto de um repositório, para enviá-lo para sua máquina, sem gerar uma cópia na sua conta Github
"3"  # Copiar um projeto de um repositório como um repositório novo na sua conta Github
"4"  # Através de um PULL REQUEST, que é enviado ao autor original, e avaliado se a mudança será efetuada
"5"  # Se você possui a chave SSH do repositório do projeto, a mudança já acontece através do COMMIT/PUSH
"6"  # Se for um repositório alheio, primeiro executa-se FORK, depois CLONE (html) ou (ssh). Pycharm [ get from VCS ]

####################################
"Pytools"  # Pull Request Não Aceito
####################################

"Título"  # Funcionalidades da linguagem Markdown
def parte1():
    """
    1. Adicionar título para link: [título]
    2. Adicionar o link: (link)
    """

"Título"  # Uso do recurso GitHub "Issue" como registrador de ações de correção em projetos, solo ou em grupo
def parte2():
    """
    1 - Link do "Issues" é visível na página de qualquer repositórios, na parte de cima
    2 - Ao clicar no link, direciona-se à página, que disponibiliza uma área de postagem,
    3 - Ao enviar, sua postagem é exibida como um tópico e contêm ao final do seu título, uma #id
    4 - Esse id pode ser mencionado em IDEs (ex: Pycharm) na área de commit, pela sintaxe: [ close #id ]
    5 - Após o COMMIT/PUSH, requisita-se um PULL REQUEST, que é outro recurso GitHub
    6 - Na postagem do PULL REQUEST, pode-se mencionar a sintaxe novamente: [ close #id ]
    """

###########################
"Pytools"  # Feature Branch
###########################

"Breach"  # Ramos de códigos distintos a partir de um ponto no seu histórico
"Tipos"   # LOCAL BRANCH (projeto) [master ou origin/master] / REMOTE BRANCH (GitHub) [origin/master]
"Acesso"  # No Pycharm: [ Git / Branches... ] ou canto inferior direito da tela da IDE

"Título"  # Comando relacionados a branch pelo terminal do projeto
def parte1():
    """
    listar todas branches locais                                   [ git branch ]
    listar todas branches, incluindo remotas                       [ git branch --all ]
    listar todos repositórios remotos conectados                   [ git remote -v ]
    conectar um repositório remoto                                 [ git remote add ] <apelido> <link do rep.>
    desconectar um repositório remoto                              [ git remote rm    ] <apelido>
    atualizar todas as branches remotas de todos rep. remotos      [ git fetch --all ]
    atualizar todas as branches remotas de determinado rep. remoto [ git fetch ] <repositorio>
    criar uma branch local                                         [ git branch ] <nome-da-branch>
    carregar os módulos de uma branch especifica                   [ git checkout <nome-da-branch> ]
    """

"Título"  # Comando relacionados a branch pelas ferramentas da IDE (Pycharm) no projeto
def parte2():
    """
    [ Git / Manage Remotes... ]          # conectar um repositório remoto (Pycharm)
    [ Git / Fetch ]                      # atualizar todas as branches remotas de todos rep. remotos (Pycharm)
    [ Git / Branches... / + New branch ] # criar uma branch local (Pycharm)
    [ Git / Show Git Log ]               # verificar logs de braches feitas
    """

##############################
"Pytools"  # Arquivo Gitignore
##############################

"Título"  # Configuração de um módulo gitignore global
def parte1():
    """
    1 - [ /home/seu_user/ ] local recomendado para criar o módulo git
    2 - [ .gitignore_global ] recomendação de nome do módulo git
    3 - Conteúdo do módulo:
                           .idea/
                           bin/
                           *.sqlite3
    4 - No terminal:
                    git config --global core.excludesfile ~/.gitignore_global
    """

############################
"Pytools"  # Pyenv no Ubuntu
############################

"Título"  # Bibliotecas relevantes para ter uma configuração completa para Python no OS Ubuntu
def parte1():
    """
    sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm gettext libncurses5-dev tk-dev tcl-dev blt-dev libgdbm-dev git python-dev python3-dev aria2 vim libnss3-tools python3-venv liblzma-dev
    """

"Título"  # Instalação do Pyenv
"OBS"     # Pyenv instala Python no OS, sem afetar o Python existente no OS
def parte2():
    """
    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    """

"Título"  # Configuração dos binários do Pyenv
def parte3():
    """
    1 - Ir à rota: [ /home/seu_user/.bashrc ]
    2 - Abrir o módulo
    3 - Inserir no final do módulo:
                                   export PATH="/home/lucas/.pyenv/bin:$PATH"
                                   eval "$(pyenv init -)"
                                   eval "$(pyenv virtualenv-init -)"
    4 - Salvar
    5 - Fechar o terminal
    6 - Reabrir o terminal
    7 - pyenv
    8 - Se a instalação teve êxito, o Pyenv será chamado no terminal
    9 - pyenv install -l
    10 - Procurar na listagem, a versão inteiramente numérica mais atual
        EXEMPLO:
                3.9.1
    11 - pyenv install 3.9.1
    """

#######################
"Pytools"  # Virtualenv
#######################

"Título"  # Objetivos para instalar o virtualenv para o Python
def parte1():
    """
    1 - Criar ambientes virtuais isolados no OS
    2 - Tratar projetos com versões diferentes do Python
    3 - Permitir que projetos tenham versões diferentes de library (projetos legado) (versões bem anteriores)
    """

###################
"Pytools"  # Flake8
###################
"FONTE"  # /home/lucas/PycharmProjects/recursos/PYTHON/f/flake8.py

##############################################
"Pytools"  # Integração Contínua com Travis CI
##############################################

def parte1():
    """
    1 - Travis é uma integração contínua (continuous integration) para evitar execução de tarefas manuais reincidentes
    2 - https://travis-ci.org/
    3 - Signup com sua conta GitHub [ https://travis-ci.org/getting_started / activate all repositories... (botão) ]
    4 - No projeto, criar um diretório: [ raiz / botão direito / new / file / .travis.yml ]
    5 - Configuração o módulo .yml para Python

        language:
          - Python
        version:
          - 3.8
        install:
          - pip install -r requirements.txt
        script:
          - flake8

    6 - Commit
    7 - Push
    8 - Ir ao Travis website
    9 - Ir ao repositório do projeto alvo
    10 - Atualizar a página
    11 - Verificar se o processo de build é executado
    """

####################################
"Pytools"  # Upgrade de Dependências
####################################

"Título"  # Instalação e utilização do Pyup
def parte1():
    """
    1 - Pyup mantêm as dependências de um projeto atualizadas
    2 - https://pyup.io/ -----> Signup pelo Github
    3 - Dar a permissão de acessar repositórios da conta
    4 - Adicionar repositório a ser checado
    5 - O repositório será checado e se haver dependências desatualizadas, estas serão mostradas no website do Pyup
    6 - Além da lista de dependências desatualizadas, serão criados PULL REQUESTS para fazê-las
    7 - Pyup também possuem badges (não funcionaram no momento desse tutorial)
    8 - Configurar módulo no projeto:

        raiz / new / file / .pyup.yml

    9 - Conteúdo do módulo:

        9.1 - Eu tentei de tudo e não consegui achar solução
        9.2 - O exemplo oficial da documentação não é apropriado para o meu contexto, pois não quero atualizar o Django
        9.3 - https://pyup.io/docs/bot/config/#specifying-files
        9.4 - https://pyup.io/docs/bot/filter/
        9.5 - Eu não consigo fazer os exemplos da documentação da ferramenta funcionar

    10 - Tendo as etapas 8 e 9 falhado para mim, a opção 5 ainda é uma realidade
    """

def parte2():
    """
    11 - Sendo assim, vê-se as dependências com badge "outdated" e copia-se o que está no cabeçalho "package"
    12 - Ir ao módulo [ requirements.txt ] e fazer [ ctrl + f ] para procurar
    13 - Colar e ir até a dependência selecionada
    14 - Copiar toda a dependência (incluindo a versão)
    15 - Executar: [ pip uninstall ctrl + v ]
    16 - Fazer isso com todas as dependências desatualizadas, separando-as cada uma por um espaço

         EXEMPLO:
                 pip unisinstall beautifulsoup4==4.9.3 django-bootstrap4==2.3.1 pyflakes==2.2.0

    17 - Antes de executar, copiar todas essas
    """

"OBS"  # Procedimentos para o módulo requirements.txt customizado e do projeto
"OBS"  # Começar da linha 1 e não deixar linhas sobrando ao final, para evitar problemas com leitura de módulos

# Módulo criado a partir de dados filtrados do website Pyup, e organizados em um módulo .txt
def parte3():
    """
    1 - Criar um módulo [ requirements.txt ]
    2 - https://pyup.io/account/repos/github/Lucas-far/attempt_api/

    3 - Copiar segurando (ctrl + botão esquerdo descendo) para selecionar cada <td></td> que seja do seu interesse
    3 - Copiar segurando (ctrl + botão esquerdo) para selecionar cada <td></td> que seja do seu interesse
    3 - Não é possível fazer o primeiro 3 duas vezes seguidas, por isso há o segundo 3

    4 - Colar dados selecionados no módulo .txt
    5 - Organizar os dados (mesmo layout do módulo requirements.txt de um projeto Django)
    6 - Salvar o módulo
    7 - Pegar a rota do módulo, pois essa será usada na parte 4
    """

# Módulo criado na raiz do projeto Django (pode ser deletado após a coleta dos resultados)
def parte4():
    """
    1 - Criar um módulo [ requirements.py ]
    2 - Eu criei um algoritmo me poupa o trabalho de desintalar e instalar as dependências manualmente
    3 - Para o funcionamento desse método, é preciso:

        rota do módulo requirements.txt do projeto (incluindo o módulo.formato)
        rota do módulo .txt (incluindo o módulo.formato)

    ALGORITMO

        def checar_dependencias(dependencia_projeto, dependencia_pyup):

            # Dependências atualmente no projeto
            with open(dependencia_projeto, 'r') as doc:
                var = sorted(list(str(doc.read()).split('\n')), reverse=True)

            # Dependências atualizadas do projeto, pegas do site Pyup e organizadas em um módulo .txt
            with open(dependencia_pyup, 'r') as doc:
                var2 = sorted(list(str(doc.read()).split('\n')), reverse=True)

            "OBS"  # sorted está sendo usado para ordenar dados para evitar possíveis irregularidades do projeto ou do website Pyup

            var3 = ['pip uninstall -y', ]  # lista de índices que receberá pacote desatualziado a ser desinstalado
            var4 = ['pip install', ]    # lista de índices que receberá cada pacote atualizado a ser instalado

            "Objetivo"  # Se var e var2 são iguais, não há o que atualizar, então apenas imprime-se 'OK' + incremento
            "Objetivo"  # Se não, adicionar em var3, o pacote a ser desintalado, e em var4, o pacote a ser instalado + incremento
            index = 0
            while index < len(var):
                if var[index] == var2[index]:
                    print('OK', end=' ')
                    index += 1
                else:
                    var3.append(var[index])
                    var4.append(var2[index])
                    index += 1

            print('\n')
            print('Pacotes desatualizados')
            for obj in var3:
                print(obj, end=' ')  # Copia-se o retorno dessa linha e execute ela no terminal do projeto

            print('\n')
            print('Pacotes atualizados')
            for obj in var4:
                print(obj, end=' ')  # Depois, copia-se o retorno dessa linha e execute ela no terminal do projeto

        checar_dependencias(
            '/home/lucas/PycharmProjects/attempt_api/requirements.txt',
            '/home/lucas/PycharmProjects/recursos/teste.txt'
        )
    """
