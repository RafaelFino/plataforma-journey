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
    section Oracle One
        Cadastro: one_cad, 0, 1d
        Trilha básica: 30d
        Trilha básica: 30d
        Trilha básica: 30d
    section Content Bot
        Bot Conteúdo Básico: bot_content_basic, after one_end, 45d
        Exercícios Básicos: bot_content_basic, after one_end, 45d
        Bot Conteúdo Intermediário: bot_content_med, after beheviour_evaluation, 30d
        Exercícios intermediários: bot_content_med, after beheviour_evaluation, 30d
        Bot Conteúdo Avançado: bot_content_adv, after bot_content_med, 30d
        Exercícios avançados: bot_content_adv, after bot_content_med, 30d
    section Avaliações Equipe Plataforma
        Avaliação: beheviour_evaluation, after bot_content_basic, 21d
    section Mentoria
        Mentoria: mentorship, after beheviour_evaluation, 180d
        Intro: ment_intro, after beheviour_evaluation, 21d
        SO: ment_SO, after ment_intro, 7d
        Infra: ment_infra, after ment_SO, 7d        
        Coding: ment_coding, after ment_infra, 7d
        Arch Básica: ment_arch_basic, after ment_coding, 14d
        Data Structures: ment_data_structure, after ment_arch_basic, 14d
        Data base: ment_sql, after ment_data_structure, 21d
        Solution Arch: ment_solution_arch, after ment_sql, 14d
        APIs: ment_apis, after ment_solution_arch, 21d
        OOP: ment_oop, after ment_apis, 30d
        Tests: ment_tests, after ment_oop, 7d
        Arch Avançada: ment_arch_adv, after ment_tests, 14d
    section Projetos        
        Chat-v1: prj_chat_v1, after bot_content_adv, 14d
        Chat-v2: prj_chat_v2, after prj_chat_v1, 14d
        CRUD: prj_crud, after prj_chat_v2, 21d        
        Chat-v3: prj_chat_v3, after prj_crud, 21d
        OOP-Biblioteca: prj_lib, after prj_chat_v3, 21d
        TCC: prj_tcc, after prj_lib, 30d
```

