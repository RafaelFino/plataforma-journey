# Plataforma-Journey
Um projeto de plataforma de ensino a distância, com o objetivo de ajudar pessoas a aprenderem novas habilidades e conhecimentos. Focando em preparar pessoas para o mercado de trabalho, tanto na parte técnica como na parte comportamental.

Para maiores informações sobre o projeto, acesse o nosso [site](https://plataformaimpact.org/)

## Contexto
Visando termos escalabilidade e impacto social, o projeto da Plataforma Journey foi criado para dar um caminho de forma automatizada e apoiar nossos estudantes usando ferramentas de tecnologia para que consigam se desenvolver e de forma autonoma e com qualidade. Queremos trazer para um ambiente virtual toda as qualidades que conseguimos entregar por meio de mentorias presenciais ou remotas.

## Objetivo
Queremos que toda a jornada que nossos estudantem devem trilhar sejam claros e objetivos e que com esse projeto, tenham todas as ferramentas necessárias para isso.

Queremos usando motorores de IA, gerar conteúdos de qualidade, exercícios e testes para orientar os próximos passos e pontos de foco nos estudos.

## Nossa trilha
```mermaid
gantt
    title Plataforma Journey    
    dateFormat  YYYY-MM-DD
    section Oracle One
        START: one_start, after eval_registry, 12w
        JAVA: one_java, after eval_registry, 12w
        MySQL: one_mysql, after eval_registry, 12w
    section Content Bot
        Bot basicss: bot_content_basic, after eval_registry, 12w
        Tests basics: bot_test_basic, after eval_registry, 12w
        Bot intermediate: bot_content_med, after eval_behave, 14w
        Tests intermediate: bot_test_med, after eval_behave, 14w
        Bot avanced: bot_content_adv, after bot_content_med, 14w
        Tests advanced: bot_test_adv, after bot_content_med, 14w
    section DevMatch
        Ingress-test: test_ingress, after bot_content_basic, 2w
        Final-test: test_final, after prj_tcc, 2w      
    section Equipe Plataforma
        Cadastro: eval_registry, 2025-01-01, 1w
        Seleção: eval_behave, after test_ingress, 2w
        Entrevista: eval_final, after test_final, 2w
        Feedback: team_feedback, after eval_final, 2w
    section Mentoria
        Intro: ment_intro, after eval_behave, 2w
        SO: ment_SO, after ment_intro, 2w
        Infra: ment_infra, after ment_SO, 1w
        Code: ment_coding, after ment_infra, 3w
        Arch basics: ment_arch_basic, after ment_coding, 2w
        Data struct: ment_data_structure, after ment_arch_basic, 3w
        Solution arch: ment_solution_arch, after ment_data_structure, 3w
        DB: ment_sql, after ment_solution_arch, 2w
        APIs: ment_apis, after ment_sql, 2w
        OOP: ment_oop, after ment_apis, 7w
        Tests: ment_tests, after ment_oop, 2w
        Automations: ment_automations, after ment_tests, 3w
    section Projetos        
        Chat-v1: prj_chat_v1, after ment_arch_basic, 2w
        Chat-v2: prj_chat_v2, after prj_chat_v1, 2w
        CRUD: prj_crud, after prj_chat_v2, 4w
        Chat-v3: prj_chat_v3, after ment_sql, 4w
        Library: prj_lib, after prj_chat_v3, 4w
        TCC: prj_tcc, after prj_lib, 6w  
```

## Estrutura do projeto
O projeto possui alguns módulos, que são:
- **Oracle One**: Trilha inicial, o estudante aqui precisa demonstrar comprometimento e dedicação. Mostrar que é capaz de aprender e se desenvolver sozinho usando recursos online.
- **Content Bot**: Plataforma de nossa autoria onde colocamos todos os conteúdos que entendemos que são a base do necessário para preparar os estudantes para o mercado de trabalho. Esses conteúdos foram desenvolvidos baseados nas experiências que tivemos com as turmas passadas e com o auxílio de IA conseguimos gerar conteúdos de qualidade.
- **DevMatch**: Plataforma que usamos para aplicar testes de simulação de cenários de trabalho real, para que possamos avaliar o conhecimento técnico dos estudantes.
- **Mentoria**: Programa extenso e intensivo de acompanhamento dos alunos que conseguirem passar pelas fases iniciais. Aqui é onde conseguimos extrair o melhor dos nossos alunos apresentando desafios reais e acompanhando o desenvolvimento deles. Especialistas renomados de mercado puxam essas mentorias, que vão muito além de serem apenas aulas técnicas, são aulas de vida e de carreira.

## Arch
### RegistryService
#### Classes
```mermaid
classDiagram
    class StudentDomain {
        + string ID
        + string Name
        + string Email
        + List<PasswordDomain> Passwords
        + datetime CreatedAt
        + datetime UpdatedAt
        + bool Active
        + ToJson() string
    }

    class PasswordDomain {
        + string Hash        
        + datetime CreatedAt
        + ToJson() string
    }

    class RegistryService {
        + repository data~StudentDomain~
        + Insert(StudentDomain) string
        + Update(StudentDomain) bool
        + Inactivate(string id) bool
        + Activate(string id) bool
        + GetByID(string id) StudentDomain
    }

    class AuthService {
        + repository data~PasswordDomain~
        + Insert(string id, string pass) void
        + Check(string id, string pass) bool        
    }
```
#### MER
```mermaid
erDiagram
    Student {
        string ID
        string Name
        string Email
        datetime CreatedAt
        datetime UpdatedAt
        bool Active
    }

    Password {
        string StudentID
        string Hash
        datetime CreatedAt
    }

    Student ||--|{ Password : contains

    LoginResult {
        string StudentID
        bool Success
        datetime CreatedAt
    }

    Student ||--|{ LoginResult : contains
```
### ContentService
#### Classes
```mermaid
classDiagram
    class Content {
        + string ID
        + string Title
        + string Description
        + datetime CreatedAt
        + List<Module> Modules
        + ToJson() string
    }

    class Module {
        + string ID
        + string ContentID
        + string Title
        + string Description
        + datetime CreatedAt
        + ToJson() string
    }

    class ContentService {
        + repository data~Content~
        + Insert(Content) string
        + Update(Content) bool
        + Delete(string id) bool
        + GetByID(string id) Content
        + List<Content> List()
    }
```
#### MER
```mermaid
erDiagram
    Content {
        string ID
        string Title
        string Description
        datetime CreatedAt
    }

    Module {
        string ID
        string ContentID
        int Order
        string Title
        string Description
        datetime CreatedAt
    }

    Content ||--|{ Module : contains
```

### QuestionService
#### Classes
```mermaid
classDiagram
    class Question {
        + string ID
        + string ModuleID        
        + string Text
        + string Code
        + string Lexer
        + datetime CreatedAt
        + List<Awser> Awsers
        + ToJson() string
    }

    class Awser {
        + string ID
        + string Text
        + string Code
        + string Lexer
        + bool IsCorrect
        + datetime CreatedAt
        + ToJson() string
    }

    Question -- Awser

    class QuestionService {
        + repository data~Question~
        + Insert(Question) string
        + Update(Question) bool
        + Delete(string id) bool
        + Get(string moduleId) List<Question>
    }
```
#### MER
```mermaid
erDiagram
    Question {
        string ID
        string ModuleID
        string Text
        string Code
        string Lexer
        datetime CreatedAt
    }

    Awnser {
        string ID
        string QuestionID
        string Text
        string Code
        string Lexer
        bool IsCorrect
        datetime CreatedAt
    }

    Question ||--|{ Awnser : contains
```

### ProgressService
#### Classes
```mermaid
classDiagram
    class ContentDomain {
        + string StudentID
        + string ModuleID
        + int Completed
        + datetime CreatedAt
        + ToJson() string
    }

    class QuestionDomain {
        + string StudentID
        + string QuestionID
        + string AwnserID
        + bool IsCorrect
        + datetime CreatedAt
        + ToJson() string
    }

    class ProgressService {
        + repository data~ContentDomain~
        + InsertContent(ContentDomain) void
        + InsertQuestion(QuestionDomain) void
    }
```
#### MER
```mermaid
erDiagram
    Content {
        datetime CreatedAt
        string ContentID
        string SudentID
        string ModuleID
        int Completed // percent    
    }

    Question {
        datetime CreatedAt
        string StudentID
        string QuestionID
        string AwnserID
        bool IsCorrect        
    }
```