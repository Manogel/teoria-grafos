# Grafos5
algoritmo de fleury

Atividade avaliativa da disciplina de teoria dos grafos

======= Execução ======= 

Para executar o arquivo de maneira correta, tenha instalado o python3 em seu computador.
Também tenha intalado o pip e numpy, caso não tenha, digite os seguintes comandos:

UBUNTU:
==> pip

        sudo apt-get install python-pip
 
WINDOWS

==> numpy

        pip3 install numpy ou
        pip install numpy
        

Após ter esses requisitos instalados execute:

    python Fleury.py ou
    python3 Fleury.py

======= OBSERVAÇÃO =======

O grafo ainda é declarado em linha de codigo(estaticamente).
A questões que correspondem o algoritmo estao no arquivo pdf no mesmo diretorio;
Ao executar o codigo, o algoritmo pede para que seja informado o numero da questão, 
que estao enumeradas em 1, 2, 3 respectivamente na ordem de cada grafo no pdf.
Por exemplo, se colocamos a entrada 2, será feita a análise no grafo estrela do pdf.

Após isso, será pedido o vertice inicial para iniciar a busca da trilha no grafo selecionado, além disso, será retornado
se o grafo é euleriano ou semi-euleriano. Ao final será mostrado a matriz de incidencia com valores -1, significando
que naquela posição foi feita uma verificação, além disso, a trilha euleriana encontrada.
