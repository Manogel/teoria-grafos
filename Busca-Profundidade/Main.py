#coding: latin-1 

def imprime(lista_adjacencia, etapa, lista_visitado, pilha, contador):
	#Imprime etapa
	print('Etapa atual: ', etapa)
	#Imprime vertice atual
	print('Vertice atual: ', pos)
	#Imprime vértices visitados
	print('Vértices visitados: ',lista_visitado)
	#Imprime pilha: 
	print('Pilha: ', pilha)
	#Imprime na tela contador atual
	print('Contador: ', contador)
	
	input('\ENTER para continuar: ')
	print()



#Uma lista estática de exemplo é configurada como na busca em largura 
lista_adjacencia = [[1],[3,2],[4],[0,4],[1]]
#A lista de contador é inicializada com todos os campos iguais a 0
contador = [0,0,0,0,0]
#Embora não seja necessário, a fim da melhor visualizaçã, utiliza-se um vetor de suporte para guardar os vértices já visitados 
lista_visitado = []
#Para facilitar o backtracking utiliza-se uma estrutura de pilha para armazenar os vértices que estão sendo visitados
pilha = []
#Posição ou vértice atual  
pos = 0
#Número da etapa a ser colocado no contador
etapa = 1

#Adiciona na posição referente ao vértice em questão o número da etapa
contador[pos] = etapa


#Vértice visitado é gravado para consulta futura
lista_visitado.append(pos)
#Acrescenta o vértice na pilha 
pilha.append(pos)

imprime(lista_adjacencia, etapa, lista_visitado, pilha, contador)

#Etapa é incrementada
etapa+=1

while 0 in contador:  #Enquanto contador não tiver sido preenchido 
	#Verifica se os vértices adjacentes do vértice atual já foram visitados
	#Caso sim, significa que não está acessíveis, são removidos, pois, da lista de adjacência 
	#Caso contrário, o algoritmo passa para o primeiro vértice disponível encontrado
	for v in lista_adjacencia[pos]:
		if v in lista_visitado:
			lista_adjacencia[pos].remove(v)
		else: 
			break
	#Caso o item da lista de adjacência (vértices adjacentes disponíveis) não seja vazio, ou seja, há vértices disponíveis, faça:
	if lista_adjacencia[pos] != []:
		lista_visitado.append(lista_adjacencia[pos][0]) #Adiciona vértice seguinte disponível aos visitados
		pilha.append(lista_adjacencia[pos][0]) #Vértice é adicionado a pilha
		pos = lista_adjacencia[pos][0] #Vértice atual passa a ser o próximo vertice disponível
		contador[pos] = etapa # A etapa atual é gravada na posição atual do vértice no contador
	
		imprime(lista_adjacencia, etapa, lista_visitado, pilha, contador)

		#Etapa é incrementada
		etapa+=1
		
	else:
		#Se o vértice não tiver adjacentes mais disponíveis, ou seja, se seu item na lista de adjacencia foi vazio faça:
		pilha.pop() #Retireo da pilha
		
		imprime(lista_adjacencia, etapa, lista_visitado, pilha, contador)	

		etapa-=1 #Decremente a etapa (processo de backtracking startado)
		while True: #Por iterações indefinidas faça:
			pos = pilha[-1] #Pegue o último elemento da pilha
			for v in lista_adjacencia[pos]: #Verifique se há vértices adjacentes já visitados 
				if v in lista_visitado:
					lista_adjacencia[pos].remove(v) #Se houver, remova-os
				else:  
					 break # Interrompa o processo se não houver ou se a lista de vértices adjacentes já for vazia
			
			if lista_adjacencia[pos] == []: #Se não houver mais vértices disponíveis (todos foram visitados) elimine o vértice da pilha e passe para seu pai 
				pilha.pop()
				
				imprime(lista_adjacencia, etapa, lista_visitado, pilha, contador)	
				
				#Decremente uma etapa pois subimos de nível. 
				etapa-=1
			
			else: #Se não, caso haja um vértice disponível, faça:
				lista_visitado.append(lista_adjacencia[pos][0]) #Identifique-o como visitado
				pilha.append(lista_adjacencia[pos][0]) #Acrescente-o na pilha
				pos = lista_adjacencia[pos][0] #Referencia a posição atual para esse vértice 
				contador[pos] = etapa #Marque no contador a etapa desse vértice
				
				imprime(lista_adjacencia, etapa, lista_visitado, pilha, contador)
					
				#Incremente a etapa
				etapa+=1
				#Como foi encontrado o vértice disponivel, quebre o ciclo de procura
				break


print('\n\nCONTADOR FINAL: ', contador)
input('\ENTER para continuar: ')

