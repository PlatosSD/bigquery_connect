# BigQuery Connect Example

## Pré-requisitos:

1. Tenha o Python instalado no seu computador.
2. Instale o VSCode.
3. Tenha uma conta Google Cloud Platform (GCP) com um projeto configurado e acesso ao BigQuery.


# Passos

## 01. Variaveis de ambiente

Crie um arquivo chamado `.env` na raiz desse projeto e lá insira:

```
BIGQUERY_KEY = '{"type":"service_account","project_id": "..."}' # sua account key no formato minify
NAME_PROJECT = 'NAME_PROJECT_ID'

```

## 02. Criando ambiente virtual para o projeto

`virtualenv venv`

## 03. Ativando ambeite virtual

`source venv/bin/activate`

## 04. Instalando pacotes

`pip install -r requirements.txt`

## 05. Executando código (via terminal bash ou powershell)

`python main.py` 

