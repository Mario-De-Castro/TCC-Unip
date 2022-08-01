# TCC Unip

### Rodar com o Docker

## **Nome dos container**

    - dj -> Container responsavel pelo Django
    - dbpg -> Container do banco de dados do PostgreSQL
    - ng -> Container responsavel pelo Angular com NGINX


Use o comando abaixo para construir os containers, necessario estar na pagina raiz do projeto:
```sh
docker-compose up --build
```

Para deixar o banco de dados rodando em segundo plano eu executo:

```sh
docker-compose up -d dbpg
```
Use esse comando para rodar os containers: 

```sh
docker-compose up dj ng
```

Use esse comando para rodar as Migrations:

```sh
docker-compose run dj python3 manage.py migrate
```

OBS: Não é necessario ter o POSTGRESQL Server instalado em seu computador para funcionamento, se voce tiver o postgresql instalado deve desabilitar o servidor que esta rodando local.

### Env file .env na raiz do seu projeto

Deve ser adicionado um arquivo .env na raiz do projeto para reconhecer como as variaveis de ambiente, necessario para o funcionamento da Conexão com o Docker e outros parametros do sistema:

```
SECRET_KEY=arandomstring

DEBUG=True

DEFAULT_DB_ENGINE=django.contrib.gis.db.backends.postgis
DEFAULT_DB_NAME=tccunip
DEFAULT_DB_USER=postgres
DEFAULT_DB_PWD=postgres
DEFAULT_DB_HOST=Seu IPVA
DEFAULT_DB_PORT=5432

```
