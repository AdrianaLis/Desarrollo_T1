def sumaN(lst,n):

    if n == 0 or len(lst) == 0:
     return 0 
    
    ultimo=lst[-1]
    lista_ultimo=lst[:-1]
    return ultimo + sumaN(lista_ultimo,n-1)


lista=[2,4,6,3]
num=2
print(sumaN(lista,num))

