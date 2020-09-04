# cython-flask-example
Exemplo de compilacao em Cython "C" usando um exemplo de servidor web em flask.

Para executar o script em python: python hello.py, isso abrira um webserver na porta 5000.

Agora para compilar com base em C usando Cython:

sudo apt-get install cython ou cython3 para python3

As linhas abaixo devem conter no inicio do arquivo como no exemplo hello.py isso evitar erros de futuros updates como o language level 2 para python2 e 3 para python3, como redirecionamento de URIs pelo flask usando o boundscheck=False, always_allow_keywords=True.

#cython: language_level=2, boundscheck=False, always_allow_keywords=True

Adicionada as linhas execute o comando:

Python2-> cython --embed -o hello.c hello.py
Python3-> cython3 --embed -o hello.c hello.py


Depois que gerou o arquivo em c, vem para compilacao usando o gcc

Python2-> gcc -Os -I /usr/include/python2.7 hello.c -lpython2.7 -o hello
Python3-> gcc -Os -I /usr/include/python3.6m hello.c -lpython3.6m -o hello

Executando: ./hello

ou compilando com algumas opcoes:

Python2-> gcc -Os -I /usr/include/python2.7 example.c -lpython2.7 -lpthread -lm -lutil -ldl -o example
Python3-> gcc -Os -I /usr/include/python3.6m example.c -lpython3.6m -lpthread -lm -lutil -ldl -o example

Pra executar e a mesma coisa: ./hello
