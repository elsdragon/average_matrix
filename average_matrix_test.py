
import pytest
from average_matrix import * 


def test_matriz_promedio():

    assert matriz_promedio([[1,2, 3],[2,1, 3], [3, 2, 1]]) == [[1.6666666666666667, 1.75, 2.6666666666666665],
                                     [1.75, 2.0, 2.0],
                                     [2.3333333333333335, 1.75, 2.0]]
    
    assert matriz_promedio([]) == []
    