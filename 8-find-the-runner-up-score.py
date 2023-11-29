if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lista = list(arr)
    
    maximo = max(lista)
    lista = [x for x in lista if x != maximo]
    runner_up_score = max(lista)
    print(runner_up_score)