import re

# Check the size of the word with more length
def check_max_word_size(words):
    m_length = 0
    for word in words:
        if len(word) > m_length:
            m_length=len(word)

    return m_length


# Adds '.' characters to the words that have less length than the max, so we can compare the same indexes
def set_same_size(words, max_size):
    new_list=[]
    for word in words:
        new_arr = ['.' * (max_size - len(word))]
        new_list.append(word.lower()+''.join(new_arr))
    return new_list


# Recursive radix_sort (LSD), starting on the least significant, in this case, the last character of each word
def radix_sort(words, max_size, index):
    print(words)
    
    if(index == max_size+1):
        return words
    dic = []
    dict_letters = {}
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_index=0
    tmp_list = []

    # Create dic with the value for each letter of the alphabet, in order to make comparision possible
    for x in range(26):
        dict_letters.update({letters[letter_index]:(x+1)})
        letter_index+=1
        dict_letters.update({'.':1000})

    # Create a dict with key value corresponding to the word and its value
    for word in words:
        if(dict_letters[word[max_size-index].lower()] < 1000 ):
            dic.append([word.lower(), dict_letters[word[max_size-index].lower()] ])

    # Create and sort a list of words for the current index
    for x, y in dic:
        tmp_list.append([x,y])
        tmp_list.sort(key=lambda x: x[1])

    # Create a return list that is populated with the list above
    return_list=[]
    for item in tmp_list:
        return_list.append(item[0])

    # Add the remaining elements that are ordered from previous recursions
    for item in words:
        if item not in return_list:
            return_list.append(item.lower())

    # Recursive call for the next index
    return radix_sort(return_list, max_size, index+1)


def radix_demostration(words):
    max_size = check_max_word_size(words)
    new_list = set_same_size(words, max_size)
    new_list = radix_sort(new_list, max_size-1, 0)
    
    # Remove the dots previously added to the words
    index = 0
    for word in new_list:
        new_list[index]= re.sub('[.]', '', word)
        index+=1
    
    # Print the final ordered list, all lower case
    print(new_list)
