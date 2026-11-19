Projeto G2 — Sistema de Adoção de Animais
Documentação final

Grupo As meninas superpoderosas
Claudia Portes Bohn, Júlia Salvi Rataieski e Thais Alves Maria

1. Proposta

O abandono de animais é um problema que exige iniciativas que facilitem o encaminhamento de cães e gatos para lares responsáveis. Órgãos de proteção animal precisam organizar informações sobre os animais resgatados, seus tratamentos sanitários e os processos de adoção.
Nosso projeto propõe o desenvolvimento de um sistema de gerenciamento municipal de adoção de animais, com o objetivo de organizar e facilitar esse processo.
Para quem o sistema será desenvolvido? O sistema foi pensado para gestores públicos, veterinários e servidores que trabalham em órgãos municipais de proteção e bem-estar animal, otimizando o fluxo desde o recolhimento até a destinação final (adoção ou lar temporário).
Ambiente de desenvolvimento: Draw.io para UML, GitHub e Google Colab para compartilhamento do projeto, e VSCode e PyCharm para desenvolvimento do código.

Classes previstas

•	Animal: armazena informações como nome, espécie, idade e disponibilidade.
•	Cachorro: representa animais da espécie canina.
•	Gato: representa animais da espécie felina.
•	Adotante: armazena os dados das pessoas interessadas em adotar.
•	Adocao: registra o animal, o adotante e os dados da adoção.

Aplicação dos conceitos prevista

•	Herança: Cachorro e Gato herdarão características da classe Animal.
•	Polimorfismo: o método exibir_ficha_sanitaria(), definido na classe Animal, utiliza o método detalhe_especifico(), que é sobrescrito pelas classes Cachorro e Gato, permitindo apresentar informações específicas de cada espécie.
•	Associação: Adocao relacionará um animal ao respectivo adotante.
•	Atributo privado: será utilizado para controlar informações internas, como a situação de adoção.
•	Método privado: será utilizado para operações internas, como a geração de códigos de identificação dos animais.

Entrada e saída de dados previstas

•	Entrada: Cadastro de novos animais e cadastro de adotantes interessados com verificação de requisitos.
•	Saída: Relatório de Lotação (quantos animais estão alojados e quantos estão aptos para adoção) e Termo de Adoção (documento em formato de texto para assinatura do adotante).
Funcionalidades previstas
•	Controle de entrada e resgate: registrar a chegada de um animal, informando data, local do resgate e estado de saúde inicial.
•	Controle sanitário: atualizar informações sobre vacinas, status de castração e condições de saúde.
•	Gestão de adotantes: cadastrar possíveis adotantes e verificar se cumprem os critérios legais (maioridade e comprovante de residência).
•	Processo de adoção oficial: efetivar a adoção, mudando o status do animal para "Adotado" e gerando o registro do novo tutor.

Divisão das tarefas

•	Claudia Portes Bohn: classe Animal (atributos, atributo privado de situação de adoção, método privado de geração de código e ficha sanitária).
•	Júlia Salvi Rataieski: classes Cachorro e Gato (herança, polimorfismo e testes).
•	Thais Alves Maria: classes Adotante e Adocao (registro da adoção, atualização da disponibilidade e testes).
•	Todas: diagrama UML, integração do código, menu principal, testes gerais e revisão final.

2. Diagrama UML

O diagrama abaixo é a versão final, atualizada para refletir o código entregue.

Relações: Cachorro e Gato herdam de Animal (herança). Adocao se associa a um Animal e a um Adotante.


 
2.1 Adotante
Representa a pessoa que deseja adotar um animal, armazenando seus dados pessoais.
Atributos: nome, cpf, idade (inteiro), endereco, comprovante_residencia (verdadeiro ou falso) e telefone.
Métodos:
•	__init__(nome, cpf, idade, endereco, comprovante_residencia, telefone): inicializa o adotante.
•	verificar_requisitos(): devolve verdadeiro apenas se o adotante tem 18 anos ou mais e possui comprovante de residência.
2.2 Adocao
Gerencia o processo de adoção de um animal por um adotante.
Atributos: animal, adotante, data_adocao (data do dia, gerada automaticamente), termo_adocao (texto do termo) e status_adocao (começa como "Pendente" e passa a "Aprovada" quando a adoção é registrada).
Métodos:
•	__init__(animal, adotante): inicializa a adoção. A data é gerada automaticamente.
•	registrar_adocao(): verifica os requisitos do adotante e a disponibilidade do animal. Se tudo estiver certo, aprova a adoção, marca o animal como indisponível, gera o termo e devolve verdadeiro. Caso contrário, mostra uma mensagem de erro e devolve falso.
•	gerar_termo_adocao(): monta e exibe o termo de adoção em texto, com data, nome e CPF do adotante, animal adotado, status e campo de assinatura.
2.3 Animal
Classe base dos animais cadastrados. Controla a disponibilidade para adoção.
Atributos: nome, especie, idade, cor, raca, vacinas (verdadeiro ou falso), castrado (verdadeiro ou falso), disponibilidade (verdadeiro ou falso), codigo (gerado automaticamente) e - situacao_adocao (privado). Há também um contador de classe privado (__contador), usado para numerar os códigos.
Métodos:
•	__init__(nome, especie, idade, cor, raca, vacinas, castrado): inicializa o animal, que começa disponível e com situação "Disponível".
•	situacao_adocao (propriedade de leitura): permite consultar a situação sem alterá-la diretamente de fora da classe.
•	__gerar_codigo() (privado): gera o código de identificação, formado pelas três primeiras letras da espécie e um número sequencial (por exemplo, CAC-001 e GAT-002).
•	atualizar_disponibilidade(status): atualiza a disponibilidade e a situação ("Disponível" ou "Adotado").
•	detalhe_especifico(): método que cada espécie sobrescreve para informar o dado próprio dela.
•	exibir_ficha_sanitaria(): devolve o texto da ficha sanitária, usando detalhe_especifico() para incluir o dado da espécie.
2.4 Cachorro
Herda de Animal. Atributo próprio: porte. Construtor: __init__(nome, idade, porte, cor, raca, vacinas, castrado), que informa a espécie "Cachorro" à classe Animal. Sobrescreve detalhe_especifico(), que devolve o porte.
2.5 Gato
Herda de Animal. Atributo próprio: pelagem. Construtor: __init__(nome, idade, pelagem, cor, raca, vacinas, castrado), que informa a espécie "Gato" à classe Animal. Sobrescreve detalhe_especifico(), que devolve a pelagem.

3. Documentação do sistema entregue

3.1 Estrutura do projeto
•	main.py: menu principal e controle do fluxo do programa.
•	classes_animais.py: classes Animal, Cachorro e Gato.
•	adotante.py: classe Adotante.
•	adocao.py: classe Adocao.
•	cadastro.py: funções de cadastro de cachorro, gato e adotante, com validação das respostas (número inteiro para idade e Sim/Não para as perguntas).
•	relatorios.py: funções que geram o Relatório de Lotação e o Relatório de Saúde e exportam o resultado em JSON.
3.2 Funcionamento do menu
1.	Cadastrar animal: escolhe cachorro ou gato e informa nome, idade, características próprias (porte ou pelagem), cor, raça, se está vacinado e se é castrado. O sistema exibe a ficha sanitária com o código gerado.
2.	Cadastrar adotante: informa nome, CPF, idade, endereço, comprovante de residência e telefone.
3.	Registrar adoção: lista os animais disponíveis e os adotantes, o usuário escolhe um de cada pelo número, e o sistema valida os requisitos, registra a adoção e emite o termo.
4.	Consultar animais: filtra por cachorros, gatos ou todos e mostra a ficha sanitária e a situação da adoção de cada animal.
5.	Consultar adotantes: lista os dados dos adotantes cadastrados.
6.	Gerar relatórios municipais: Relatório de Lotação ou Relatório de Saúde, com opção de exportar para JSON.
7.	Sair.
3.3 Entradas, validações e saídas
•	Entradas: todos os dados são digitados pelo usuário no teclado.
•	Validações: a idade deve ser um número inteiro (o sistema pede de novo se não for); as perguntas de vacina, castração e comprovante só aceitam Sim ou Não; na escolha de animal e adotante só são aceitos números dentro da lista; o adotante precisa ser maior de idade e ter comprovante de residência; um animal já adotado não pode ser adotado de novo.
•	Saídas: fichas sanitárias, listagens de animais e adotantes, termo de adoção em texto, mensagens de sucesso ou erro e relatórios no terminal.
•	Relatório de Lotação: mostra o total de animais cadastrados, quantos estão disponíveis para adoção e quantos já foram adotados. No arquivo JSON inclui também a lista dos animais disponíveis (código, nome, espécie e raça).
•	Relatório de Saúde: lista os animais sem vacina ou sem castração, indicando a pendência de cada um (vacina pendente, castração pendente ou ambas).
3.4 Persistência e leitura de arquivos
O sistema não lê arquivos. Os dados de animais e adotantes ficam em listas na memória e são perdidos quando o programa é encerrado. Apenas os relatórios podem ser gravados em disco, em arquivos JSON (relatorio_lotacao.json e relatorio_saude.json), com data de geração.
3.5 Operações de CRUD
•	Create (criar): cadastro de animais e de adotantes, e registro de adoções.
•	Read (ler): consulta de animais (com filtro) e de adotantes, e geração de relatórios.
•	Update (atualizar): a adoção atualiza a disponibilidade e a situação do animal. Não há edição de outros dados já cadastrados.
•	Delete (excluir): não implementado.
3.6 Conceitos de programação orientada a objetos aplicados
•	Herança: Cachorro e Gato herdam de Animal e reaproveitam nome, espécie, idade, cor, raça, vacinas, castração, disponibilidade, situação e código, chamando super().__init__() em seus construtores.
•	Polimorfismo: o método exibir_ficha_sanitaria() é definido em Animal e chama self.detalhe_especifico(). Cachorro e Gato sobrescrevem detalhe_especifico() (porte e pelagem, respectivamente). No menu de consulta, o mesmo comando animal.exibir_ficha_sanitaria() é executado sobre uma lista que mistura cachorros e gatos, e cada objeto responde com a sua ficha, sem que o programa precise verificar o tipo.
•	Associação: Adocao guarda uma referência a um Animal e a um Adotante, ligando os dois.
•	Encapsulamento: a situação da adoção é um atributo privado (__situacao_adocao), lido por uma propriedade e alterado somente por atualizar_disponibilidade(). A geração do código é um método privado (__gerar_codigo()), usado apenas dentro de Animal.
•	Abstração: as classes modelam os conceitos do domínio (animal, adotante e adoção) com os dados e comportamentos necessários ao sistema.
3.7 Tecnologias utilizadas
Linguagem Python 3, com módulos da biblioteca padrão (datetime para a data da adoção e json para exportar os relatórios), sem bibliotecas externas. Menu em texto no terminal. Ferramentas: PyCharm e VS Code (código), GitHub (compartilhamento) e draw.io (UML).
3.8 Testes realizados
Os testes foram feitos executando o main.py e usando o menu:
•	Cadastro de cachorro com idade digitada em branco: o sistema pediu a idade novamente e concluiu o cadastro, mostrando a ficha com o porte.
•	Cadastro de gato: a ficha mostrou a pelagem e o código GAT-001.
•	Cadastro de adotante maior de idade e com comprovante: cadastrado com sucesso.
•	Registro de adoção válida: o termo foi gerado e o sistema informou "Adoção realizada com sucesso!".
•	Nova tentativa de adoção sem animais disponíveis: o sistema informou que não há animais disponíveis.
•	Consulta de animais após a adoção: a situação do animal apareceu como "Adotado".
•	Adoção por adotante sem comprovante de residência: o sistema recusou e exibiu a mensagem sobre os requisitos.
•	Escolha de animal com entrada não numérica: o sistema exibiu "Digite apenas números." sem encerrar o programa.
3.9 Diferenças em relação à proposta
•	Polimorfismo: o plano original previa que Cachorro e Gato sobrescrevessem exibir_ficha_sanitaria(). Na implementação, esse método ficou em Animal e chama detalhe_especifico(), que é sobrescrito por Cachorro e Gato, evitando repetir código. O efeito é o mesmo: cada espécie apresenta sua informação própria.
•	Relatórios: foram implementados como funções no módulo relatorios.py, e não como classes, e podem ser exportados em JSON.
•	Persistência: apenas os relatórios são gravados em arquivo. Animais e adotantes ficam apenas em memória.
•	Cadastro de resgate: o cadastro do animal não registra data, local, lote ou bairro de origem, nem estado de saúde inicial.
•	Controle sanitário: vacinas e castração são informadas no cadastro, como verdadeiro ou falso, e não podem ser atualizadas depois.
•	Situação do animal: o animal começa como "Disponível" (e não "Em Acolhimento Municipal") e passa a "Adotado" depois da adoção. O lar temporário não foi implementado.
•	Atributo cpf: é público no código, e o atributo privado do sistema é a situação da adoção.
3.10 Limitações e melhorias futuras
•	Gravar animais e adotantes em arquivo ou banco de dados para que os dados não se percam ao fechar o programa.
•	Incluir dados de resgate (data, local, lote ou bairro) e estado de saúde inicial no cadastro do animal.
•	Permitir atualizar vacinas, castração e condição de saúde, e editar ou excluir registros, completando o CRUD.
•	Validar CPF e telefone, que hoje são aceitos como texto livre.
•	Implementar o lar temporário como destinação alternativa à adoção.
•	Reduzir a repetição de código entre cadastrar_cachorro() e cadastrar_gato() no módulo cadastro.py.
