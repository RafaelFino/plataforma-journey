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
    tickInterval 1week
    title Plataforma Journey    
    section Oracle One
        Cadastro: one_cad, 0, 1w
        Trilha básica: one_bas, after one_cad, 2w
        Trilha básica: one_med, after one_bas, 2w
        Trilha básica: one_adv, after one_med, w2
    section Content Bot
        Bot Basic: bot_content_basic, after one_adv, 12w
        PG basic: bot_pg_basic, after one_adv, 12w
        Bot medium: bot_content_med, after bot_content_basic, 12w
        PG medium: bot_pg_med, after bot_content_basic, 12w
        Bot Avançado: bot_content_adv, after bot_content_med, 12w
        PG advanced: bot_pg_adv, after bot_content_med, 12w
    section Equipe Plataforma
        Seleção: behave_eval, after bot_content_basic, 2w
    section Mentoria
        Intro: ment_intro, after behave_eval, 2w
        SO: ment_SO, after ment_intro, 2w
        Infra: ment_infra, after ment_SO, 1w
        Code: ment_coding, after ment_infra, 2w
        Arch Básica: ment_arch_basic, after ment_coding, 2w
        Data Struct: ment_data_structure, after ment_arch_basic, 2w        
        Solution Arch: ment_solution_arch, after ment_data_structure, 2w
        Data base: ment_sql, after ment_solution_arch, 1w
        APIs: ment_apis, after ment_sql, 2w
        OOP: ment_oop, after ment_apis, 4w
        Tests: ment_tests, after ment_oop, 2w
        Arch Avançada: ment_arch_adv, after ment_tests, 2w
        Automations: ment_automations, after ment_arch_adv, 2w
    section Projetos        
        Chat-v1: prj_chat_v1, after ment_coding, 3w
        Chat-v2: prj_chat_v2, after ment_data_structure, 2w
        CRUD: prj_crud, after prj_chat_v2, 3w
        Chat-v3: prj_chat_v3, after ment_apis, 3w
        OOP-Biblioteca: prj_lib, after prj_chat_v3, 4w
        TCC: prj_tcc, after prj_lib, 4w
    section Equipe Plataforma
        Entrevista: behave_eval_final, after prj_tcc, 2w
    section DevMatch
        Teste final: team_eval, after prj_tcc, 2w
    section Equipe Plataforma
        Feedback: team_feedback, after behave_eval_final, 2w
```

