Leitor de arquivos CNAB para sistemas Bancários


Tenha certeza de ter o Python 3 e o pip instalado em seu computador...

1. Crie seu ambiente virtual:
```bash
python -m venv venv
```

2. Ative seu venv:
```bash
# linux:
source venv/bin/activate

# windows:
.\venv\Scripts\activate
```
3. Use o comando abaixo para instalar os pacotes e dependências do projeto pelo arquivo requirements.txt;
```bash
pip install -r /path/to/requirements.txt
```

4. para executar o servidor, utilize o comando:
```bash
python manage.py runserver
```

5. Para enviar um arquivo, acesse a seguinte url:
   http://127.0.0.1:8000/api/save_file_content

   Para ver o saldo das lojas, acesse esta url:
   http://127.0.0.1:8000/api/saldo_store

obs: É a primeira vez que faço um readme, se puder me dar umas dicas no feedback eu agradeço.#boraCodar

