#coding: latin-1 

def imprime(lista_adjacencia, etapa, lista_visitado, pilha, contador):
	#Imprime etapa
	print('Etapa atual: ', etapa)
	#Imprime vertice atual
	print('Vertice atual: ', pos)
	#Imprime v�rtices visitados
	print('V�rtices visitados: ',lista_visitado)
	#Imprime pilha: 
	print('Pilha: ', pilha)
	#Imprime na tela contador atual
	print('Contador: ', contador)
	
	input('\ENTER para continuar: ')
	print()



#Uma lista est�tica de exemplo � configurada como na busca em largura 
lista_adjacencia = [[1],[3,2],[4],[0,4],[1]]
#A lista de contador � inicializada com todos os campos iguais a 0
contador = [0,0,0,0,0]
#Embora n�o seja necess�rio, a fim da melhor visualiza��, utiliza-se um vetor de suporte para guardar os v�rtices j� visitados 
lista_visitado = []
#Para facilitar o backtracking utiliza-se uma estrutura de pilha para armazenar os v�rtices que est�o sendo visitados
pilha = []
#Posi��o ou v�rtice atual  
pos = 0
#N�mero da etapa a ser colocado no contador
etapa = 1

#Adiciona na posi��o referente ao v�rtice em quest�o o n�mero da etapa
contador[pos] = etapa


#V�rtice visitado � gravado para consulta futura
lista_visitado.append(pos)
#Acrescenta o v�rtice na pilha 
pilha.append(pos)

imprime(lista_adjacencia, etapa, lista_visitado, pilha, contador)

#Etapa � incrementada
etapa+=1

while 0 in contador:  #Enquanto contador n�o tiver sido preenchido 
	#Verifica se os v�rtices adjacentes do v�rtice atual j� foram visitados
	#Caso sim, significa que n�o est� acess�veis, s�o removidos, pois, da lista de adjac�ncia 
	#Caso contr�rio, o algoritmo passa para o primeiro v�rtice dispon�vel encontrado
	for v in lista_adjacencia[pos]:
		if v in lista_visitado:
			lista_adjacencia[pos].remove(v)
		else: 
			break
	#Caso o item da lista de adjac�ncia (v�rtices adjacentes dispon�veis) n�o seja vazio, ou seja, h� v�rtices dispon�veis, fa�a:
	if lista_adjacencia[pos] != []:
		lista_visitado.append(lista_adjacencia[pos][0]) #Adiciona v�rtice seguinte dispon�vel aos visitados
		pilha.append(lista_adjacencia[pos][0]) #V�rtice � adicionado a pilha
		pos = lista_adjacencia[pos][0] #V�rtice atual passa a ser o pr�ximo vertice dispon�vel
		contador[pos] = etapa # A etapa atual � gravada na posi��o atual do v�rtice no contador
	
		imprime(lista_adjacencia, etapa, lista_visitado, pilha, contador)

		#Etapa � incrementada
		etapa+=1
		
	else:
		#Se o v�rtice n�o tiver adjacentes mais dispon�veis, ou seja, se seu item na lista de adjacencia foi vazio fa�a:
		pilha.pop() #Retireo da pilha
		
		imprime(lista_adjacencia, etapa, lista_visitado, pilha, contador)	

		etapa-=1 #Decremente a etapa (processo de backtracking startado)
		while True: #Por itera��es indefinidas fa�a:
			pos = pilha[-1] #Pegue o �ltimo elemento da pilha
			for v in lista_adjacencia[pos]: #Verifique se h� v�rtices adjacentes j� visitados 
				if v in lista_visitado:
					lista_adjacencia[pos].remove(v) #Se houver, remova-os
				else:  
					 break # Interrompa o processo se n�o houver ou se a lista de v�rtices adjacentes j� for vazia
			
			if lista_adjacencia[pos] == []: #Se n�o houver mais v�rtices dispon�veis (todos foram visitados) elimine o v�rtice da pilha e passe para seu pai 
				pilha.pop()
				
				imprime(lista_adjacencia, etapa, lista_visitado, pilha, contador)	
				
				#Decremente uma etapa pois subimos de n�vel. 
				etapa-=1
			
			else: #Se n�o, caso haja um v�rtice dispon�vel, fa�a:
				lista_visitado.append(lista_adjacencia[pos][0]) #Identifique-o como visitado
				pilha.append(lista_adjacencia[pos][0]) #Acrescente-o na pilha
				pos = lista_adjacencia[pos][0] #Referencia a posi��o atual para esse v�rtice 
				contador[pos] = etapa #Marque no contador a etapa desse v�rtice
				
				imprime(lista_adjacencia, etapa, lista_visitado, pilha, contador)
					
				#Incremente a etapa
				etapa+=1
				#Como foi encontrado o v�rtice disponivel, quebre o ciclo de procura
				break


print('\n\nCONTADOR FINAL: ', contador)
input('\ENTER para continuar: ')

