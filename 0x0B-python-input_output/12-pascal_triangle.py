#!/usr/bin/python3
"""Defines pascal_triangle"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.
	    
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []
	
    triangle = [[1]]
    
    while len(triangle) != n:
        last_row = triangle[-1]
        new_row = [1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row.append(1)
        triangle.append(new_row)
	    
    return triangle
