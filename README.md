# LaveIn

### Requisitos para rodar o projeto:

Você deve possuir na sua máquina <code> Python 3.6</code> rodando corretamente.

### Baixando e rodando o projeto:

#### 1. Clone o repositório:

```
$ git clone https://github.com/unb-pandemicos/laveIn.git
```

#### 2. Acesse o diretório do repositório:

```
$ cd laveIn
```

#### 3. Crie um ambiente virtual e logo em seguida o ative:

```
$ python3.6 virtualenv venv
```

```
$ source venv/bin/activate
```

#### 4. O arquivo requirements.txt deve listar todas as bibliotecas Python que você vai precisar, você pode instalar todas elas com o comando:

```
(venv) $ pip install -r requirements.txt
```

#### 5. Em seguida, você deve fazer as migrações do banco de dados:

```
(venv) $ python manage.py makemigrations
```
```
(venv) $ python manage.py migrate
```


#### 7. Então, rode o servidor:

```
(venv) $ python manage.py runserver
```


Pronto! Agora o servidor deve estar rodando em: http://127.0.0.1:8000

