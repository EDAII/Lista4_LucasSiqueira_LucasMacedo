def pre_processing(arr):
    big_word = ''.join(arr)

    print('\nTransformando as palavras ordenadas em uma grande palavra ->')
    print(big_word)
    
    letters_list = [[i, big_word.count(i)] for i in set(big_word)]
    
    take = lambda i: i[1]
    sorted_list = sorted(letters_list, key=take, reverse=True)
    copy = [i.copy() for i in sorted_list]

    return copy, len(big_word)


def heap_frequence_sort(arr):
    sorted_list, trash = pre_processing(arr)

    print('\nOrdenando decrescentemente pela frequencia das letras utilizando heap sort ->')

    big_sorted_word = ''
    for i in sorted_list:
        big_sorted_word += i[0] * i[1]

    print(big_sorted_word)


def heapify(arr, n, i): 
	largest = i  
	l = 2 * i + 1	 
	r = 2 * i + 2	  

	if l < n and arr[i][1] < arr[l][1]: 
		largest = l 

	if r < n and arr[largest][1] < arr[r][1]: 
		largest = r 

	if largest != i: 
		arr[i], arr[largest] = arr[largest], arr[i] 

		heapify(arr, n, largest) 


def heap_rearrange(arr):
    arr, tam = pre_processing(arr) 
    n = len(arr) 

    print('\nRearanjando letras de forma que nao hajam letras iguais lado a lado ->')

    for i in range(n, -1, -1): 
        heapify(arr, n, i)

    new_str = ''
    old_temp = ('#', 0)
    while len(arr) != 0:
        print(arr)
        arr[0][1] -= 1
        new_str += arr[0][0]

        arr[0], arr[len(arr) - 1] = arr[len(arr) - 1], arr[0]

        new_temp = arr.pop()

        heapify(arr, len(arr), 0)

        if(old_temp[1] > 0):
            arr.append(old_temp)

        old_temp = new_temp

        heapify(arr, len(arr), 0)

    if len(new_str) != tam:
        print('Deu ruim parça!')
        return
    
    print(new_str)
