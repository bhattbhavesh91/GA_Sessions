'''
# Fractal Hackerrank Hiring Challenge 2

We define a square number to be an integer whose square root is another integer. 
For example, 1, 4, 9, and 16 are all square numbers as they are the respective squares of 1, 2, 3, and 4. 

Emma has two integers, a and b, and wants to count the number of square numbers in the inclusive interval [a, b]. For example, if a = 4 and b =10,
Emma's count would be 2 because the only square numbers in {4, 5, 6, 7, 8, 9} are 4 and 9. 

 
Complete the getMinimumUniqueSum function in the editor below. 
It has 1 parameter: an array of n strings, arr. Each string i in arr contains two space-separated integers describing 
the respective values of ai and bi. 
It must return an array of n integers where each element i contains the number of square numbers in the inclusive range between ai and bi (parsed 
from arri). 

'''
def q01_get_minimum_unique_square(x,y):
    'write your solution here'
    perfect_squares = [x for x in range(x,y+1) if x ** 0.5 ==int(x ** 0.5)]
    return len(perfect_squares)

print(q01_get_minimum_unique_square(3,9))