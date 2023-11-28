from function_tools import *


def matriz_promedio(matrix):

    ''' 
    Change all elements of a matrix by aritmetic average itself and its neighbours. 
    '''
    if is_matrix(matrix):

        matrix_none = add_none_matrix(matrix)
        neighbour_matrix = add_list_neighbour(matrix_none)
        average_matrix = []
        for i in range(len(neighbour_matrix)):
            average_list = []
            for lista in neighbour_matrix[i]:
                average_list.append(medium_of_list(lista))
            average_matrix.append(average_list)
    
    else:
        raise ValueError("It's not a MATRIX.")

    
    return average_matrix