# Solução para o desafio técnico



## Ativando a Venv:


A partir do diretório raiz deste projeto, executar:
```
    source venv/bin/activate
```


## Instalando o pacote:


A partir do diretório onde este documento está localizado, executar:
```
    pip install .
```

## Executando a aplicação:


```
    python -m app
```
A aplicação será executada em http://localhost:5000.
Para que a aplicação seja executada corretamente é importante definir o PYTHONPATH como o diretório onde este README está localizado


## Detalhes do Pacote:


### Models

    Conjunto de modelos de banco de dados. A aplicação inteira faz uso de sqlalchemy ORM
    1. UserSession: Modelagem básica de uma sessão.
    Campos:
        - id(integer): Identificador unico de uma sessão.
        - created(datetime.datetime): Data em que a sessão foi criada.
    2. Action: Modelagem de consultas performadas por dentro de uma sessão
    Campos:
        - id(integer): Identificador unico de uma consulta.
        - session_id(foreign key): Identificador da sessão relacionada a consulta
        - url(string): A url acessada nesta consulta
        - created(datetime.datetime): Data em que a consulta foi executada.

    As tabelas se relacionam a partir do campo UserSession.id

### Views

    Conjunto de views utilizadas pela aplicação
    Index(endpoint: '/'): Pagina inicial da aplicação
    GetQuote(endpoint: '/quotes/{quote_id}'): Retorna a quote identificada por quote_id
    GetQuotes(endpoint: '/quotes'): Retorna todas as quotes disponiveis
    RandomQuote(endpoint: '/quotes/random'): Retorna uma quote aleatória
    GetSession(endpoint: '/sessions/{session_id}'): Retorna JSON com todas as consultas efetuadas por session_id
    GetSessions(endpoint: '/sessions'): Retorna JSON com todas as sessões criadas na aplicação
    GetActions(endpoint: '/actions'): Retorna JSON com todas as consultas efetuadas no sistema

## Detalhes de implementação e uso:


    Bibliotecas utilizadas:
        - pyramid: backend
        - pyramid-chameleon: renderizar templates
        - sqlalchemy: banco de dados
        - requests: Executar chamadas de api
        - waitress: Executar a aplicação


    Banco de dados: sqlite acessado utilizando sqlalchemy.orm
    
    A aplicação foi construída como um pacote python, desta forma podendo ter seus recursos facilmente importados por outras aplicações, assim como permitindo a execução desta aplicação dentro de um docker.
