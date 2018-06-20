from format import *
import os

base('base.html')

start_content()

h1('Hadamard Product')

p(
"""
For two matrices $A$ and $B$ whose dimensions are both $m \\times n$, the Hadamard product
(or entrywise product) is given by \
$$A \\odot B = \\left(A\\right)_{i,j}\\left(B\\right)_{i,j}$$
"""
)

end_content()