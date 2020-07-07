# cython-flask-example
Exemplo de compilacao em Cython "C" usando um exemplo de servidor web em flask.

Para executar o script em python: python hello.py, isso abrira um webserver na porta 5000.

Agora para compilar com base em C usando Cython:

sudo apt-get install cython ou  cython3 para python3

cython --embed -o hello.c hello.py

** Se der erro avisando sobre o language_level no cython, adcione a seguinte linha no inicio do arquivo.py 

#cython: language_level=2

Depois que gerou o arquivo em c, vem para compilacao usando o gcc

gcc -Os -I /usr/include/python2.7 hello.c -lpython2.7 -o hello

Executando: ./hello

ou compilando com algumas opcoes:

gcc -Os -I /usr/include/python2.7 example.c -lpython2.7 -lpthread -lm -lutil -ldl -o example

Pra executar e a mesma coisa: ./hello
