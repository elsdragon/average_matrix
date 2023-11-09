
import pytest
from average_matrix import * 

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
    