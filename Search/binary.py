# def search(arr: list, search_item: int):
#     arr_middle = len(arr) // 2
#     current_item = arr[arr_middle]
    
#     if current_item > search_item:
#         return search(arr=arr[:arr_middle], search_item=search_item)
#     elif current_item < search_item:
#         return search(arr=arr[arr_middle:], search_item=search_item)
    
#     if current_item == search_item:
#         return current_item
    
# print(search([1, 2, 3], 2))



def recursive(lista: list, soma=0):
    if len(lista) != 0:
        num = lista[0]
        return recursive(lista[1:], soma+num)
    else:
        return soma

print(recursive([1, 2, 3, 4]))

def recur_factorial(n):
    if n == 1:
        return n
    else:
       return n*recur_factorial(n-1)

recur_factorial(5)