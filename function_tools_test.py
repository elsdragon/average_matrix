import pytest
from function_tools import *

def test_has_equal_lengths():
    assert has_equal_lengths([]) == True
    assert has_equal_lengths([[1, 2], [2, 3, None]]) == False
    assert has_equal_lengths([[8, 6, 9], [2, 3, 4]]) == True

def test_is_matrix():
    assert is_matrix([]) == True
    assert is_matrix([[4, 5, 6], [23, 8, 9.0]]) == True
    assert is_matrix([[3, "hola"], [7, 6.6]]) == False
    assert is_matrix([[4.5, 7.9], [3, 5, 8], []]) == False

def test_add_one_list(): 

    assert add_none_list([1, 2, 3]) == [None, 1, 2, 3, None]
    assert add_none_list([]) == [None, None]

def test_add_none_matrix():

    assert add_none_matrix([[1,2], [1,2]]) == [[None, None, None, None],
                                            [None, 1, 2, None],
                                            [None, 1, 2, None],
                                            [None, None, None, None]]
    
def test_add_list_neighbour():

    assert add_list_neighbour(add_none_matrix([[1,2],[1,2]])) == [[[1, None, 1, None, 2], 
                                                                  [2, None, 2, 1, None]],
                                                                  [[1, 1, None, None, 2], 
                                                                   [2, 2, None, 1, None]]]
    

def test_medium_of_list():

    assert medium_of_list([1, 2, 3]) == 2
