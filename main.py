from heap import heap_rearrange, heap_frequence_sort
from radix import radix_demostration


def main():
    arr = input('Insira as palavras separadas por um " ": ')
    arr = arr.split(' ')

    print('\nOrdenando alfabeticamente atraves do radix sort ->')
    radix_demostration(arr)

    heap_frequence_sort(arr)

    heap_rearrange(arr)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('Interruption')