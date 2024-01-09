"""Constructs Pascal's Triangle."""


def pascal_triangle(n):
    """Generates a list of lists representing Pascal's Triangle of size n.

    Args:
        n (int): The desired size of the triangle.

    Returns:
        list: A nested list representing Pascal's Triangle.
    """

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) < n:
        previous_row = triangles[-1]
        new_row = [1]
        for i in range(len(previous_row) - 1):
            new_row.append(previous_row[i] + previous_row[i + 1])
        new_row.append(1)
        triangles.append(new_row)
    return triangles
