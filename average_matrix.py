

def add_none_list(long_list):
    ''' 
    Inserte a None in index = 0 and last index in a list. 
    '''
    long_list.insert(0, None)
    long_list.append(None)

    return long_list


def add_none_matrix(matrix):

    ''' 
    Inserte around a matrix a new element None. 
    
    '''

    new_matrix = matrix
    
    for i in range(len(new_matrix)):
        new_matrix[i].insert(0, None)
        new_matrix[i].append(None)
        

    new_list = []
    i = 0
    while i < len(matrix[0]):
        new_list.append(None)
        i += 1
    
    new_matrix.insert(0,new_list)
    new_matrix.append(new_list)
    
    return new_matrix

def add_list_neighbour(matrix):
    ''' create a new list with neighbour elements on matrix'''
    neighbour_matrix = []

    for i in range(1, len(matrix)-1):
        new_matrix= []
        for j in range(1, len(matrix[i])-1):
            new_list = []
            new_list.append(matrix[i][j])
            new_list.append(matrix[i-1][j])
            new_list.append(matrix[i+1][j])
            new_list.append(matrix[i][j-1])
            new_list.append(matrix[i][j+1])
            new_matrix.append(new_list)

        neighbour_matrix.append(new_matrix)    
    
    return neighbour_matrix


def medium_of_list(list):
    ''' 
    Calculate arithmetic average from a list'''
    total = 0
    divisor = len(list)
    for element in list:
        if element != None:
            total += element
        if element == None:
            divisor -= 1
    
    return total/divisor