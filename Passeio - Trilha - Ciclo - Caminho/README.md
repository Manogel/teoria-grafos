Este software foi desenvolvido para uma atividade de Teoria dos Grafos!
O objetivo do software visa saber se uma determinada sequencia de vertices [k, .., k-1],
esta encaixado na categoria de PASSEIO, TRILHA, CAMINHO e CICLO de acordo com suas regras.

======= Execução ======= \n
Para executar o arquivo de maneira correta, tenha instalado o python3 em seu computador.
Também tenha intalado o pip e numpy e Tkinter, caso não tenha, digite os seguintes comandos:

UBUNTU:
==> pip e Tkinter
        sudo apt-get install python-pip
        sudo apt-get install python-tk
WINDOWS
==> numpy
        pip3 install numpy
senão, para qualquer plataforma com o pip ja intalado, execute dentro do diretorio:
        pip3 freeze install -r requerimens.txt

Após ter esses requisitos instalados execute:
    python3 Main.py

======= OBSERVAÇÃO =======\n
O grafo ainda é declarado em linha de codigo(estaticamente) nas primeiras linhas do arquivo "checkGraphs.py"
A E(G) atual é um grafo direcionado:
E(G): {(1,3), (3,2), (2,4), (4,3), (3,2), (2,1)}
