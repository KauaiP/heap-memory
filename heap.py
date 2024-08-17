from linkedlist import LinkedList

lastAlocation = -1
assign = []
var_assign = []

def adjust(heap, lista):
    cont = 0

    for i in range(len(heap)):
        if (heap[i] == '.'):
            cont = cont + 1
            if (i == 19):
                end = i - cont + 1
                size = cont
                lista.append(end, size)
                cont = 0
        else:
            if (cont > 0):
                end = i - cont
                size = cont
                lista.append(end, size)
                cont = 0

def there_is_space(lista, size):
    pointer = lista.head

    while (pointer):
        if (pointer.quantity >= size):
            return True
        pointer = pointer.next
        
    return False

def best_fit(lista, heap, tag, size):
    pointer = lista.head
    best_register = pointer

    while (pointer):
        dist1 = pointer.quantity - size
        dist2 = best_register.quantity - size
        if (dist2 < 0):
            best_register = pointer
        elif (dist1 >= 0 and dist1 < dist2):
            best_register = pointer
        pointer = pointer.next

    start_value = best_register.address
    end_value = best_register.address + size

    for i in range(start_value, end_value):
        heap[i] = tag
    

def first_fit(lista, heap, tag, size):
    pointer = lista.head

    while (pointer):
        if (pointer.quantity >= size):
            break
        pointer = pointer.next
    
    start_value = pointer.address
    end_value = pointer.address + size

    for i in range(start_value, end_value):
        heap[i] = tag
    

def worst_fit(lista, heap, tag, size):
    pointer = lista.head
    bigger = pointer

    while (pointer):
        if(pointer.quantity > bigger.quantity):
            bigger = pointer
        pointer = pointer. next

    start_value = bigger.address
    end_value = bigger.address + size

    for i in range(start_value, end_value):
        heap[i] = tag
    

def next_fit(lista, heap, tag, size, last_alocation):
    pointer = lista.head
    ja = False
    
    while (pointer):
        if(pointer.quantity >= size and ja == False):
            possible_regist = pointer
            ja = True
        if(pointer.address > last_alocation and pointer.quantity >= size):
            break
        pointer = pointer.next
    
    if(pointer != None):
        for i in range(pointer.address, pointer.address + size):
            heap[i] = tag       
    else:
        for i in range(possible_regist.address, possible_regist.address + size):
            heap[i] = tag

def exibe(heap):
    print('--------------------------------------------------------')
    print('+', end='')
    for i in range(20):
        print('---+', end='')
    
    print('')
    print('|', end='')
    for i in range(20):
        print('', heap[i], '|', end='')
    
    print('')
    print('+', end='')
    for i in range(20):
        print('---+', end='')

    print('')
    for i in range(20):
        if (i < 10):
            print(' ', i, '', end='')
        else:
            print('', i, '', end='')
    print('')
    if (assign):
        for i in range(len(assign)):
            print(assign[i], end='')
    print('')
    print('--------------------------------------------------------')    

def delete(heap, tag):
    for i in range(20):
        if (heap[i] == tag):
            heap[i] = '.'
    
    if (any(tag in par for par in assign)):
        for i in range(len(assign)):
            if (any(tag in par for par in assign[i])):
                assign.pop(i)
                break

def delete_assing(var):
    for i in range(len(assign)):
        if (any(var in par for par in assign[i])):
            assign.pop(i)
            break

def functions(instruct, heap):
    global lastAlocation
    global assign

    operation = str(input())

    while(operation[0] != 'h'):

        if operation == 'sair':
            break

        lista = LinkedList()
        adjust(heap, lista)

        if(operation[0] == 'n' and operation[1] == 'e' and operation[2] == 'w'):
            tag = operation[4]
            size = int(operation[6:])

            if not there_is_space(lista, size):
                print('Não há espaço suficiente para alocar esta quantidade de dados')
                operation = str(input())
                continue

            if (instruct == "heap best"):
               best_fit(lista, heap, tag, size)
            elif (instruct == 'heap worst'):
                worst_fit(lista, heap, tag, size)
            elif (instruct == 'heap first'):
                first_fit(lista, heap, tag, size)
            elif (instruct == 'heap next'):
                next_fit(lista, heap, tag, size, lastAlocation)

            for i in range(20):
                if (heap[i] == tag):
                    lastAlocation = (i + size) - 1
                    break

        elif (operation[0] == 'd' and operation[1] == 'e' and operation[2] == 'l'):
            tag = operation[4]

            if (tag in var_assign):
                delete_assing(tag)
            else:
                delete(heap, tag)

        elif (operation[0] == 'e'):
            exibe(heap)

        elif(operation[2] == '='):
            var_assign.append((operation[0], operation[4]))
            assign.append(f'{operation[0]} = {operation[4]}')
            
        else:
            print('comando inválido')

        operation = str(input())
    
    lista.free()
    return operation


heap = ['.'] * 20
instruct = str(input())

while(instruct != 'sair'):
    if instruct == 'heap best':
        instruct = functions(instruct, heap)
    
    elif instruct == 'heap worst':
        instruct = functions(instruct, heap)
    
    elif instruct == 'heap first':
        instruct = functions(instruct, heap)

    elif instruct == 'heap next':
        instruct = functions(instruct, heap)

    else:
        print('comando invalido')
        instruct = str(input())
