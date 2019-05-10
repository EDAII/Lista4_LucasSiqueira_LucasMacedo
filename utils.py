def order_by_frequency(word_list):
    
    big_word = ''.join(word_list)
    
    letters_list = [[i, big_word.count(i)] for i in set(big_word)]
    
    take = lambda i: i[1]
    sorted_list = sorted(letters_list, key=take, reverse=True)
    
    heap = heapSort([i.copy() for i in sorted_list], len(big_word))
    print(heap)

    big_sorted_word = ''
    for i in sorted_list:
        big_sorted_word += i[0] * i[1]

    return big_sorted_word


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


def heapSort(arr, t): 
    n = len(arr) 

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

    if len(new_str) != t:
        return 'Deu ruim parça!'

    return new_str


print(order_by_frequency(['aaabc']))
print(order_by_frequency(['aaabb']))
print(order_by_frequency(['aa']))
print(order_by_frequency(['aaaabc']))