'''
# Fractal Hackerrank Hiring Challenge 3

Sam loves chocolates and starts buying them on the 1st day of the year. Each day of the year, x, is numbered from 1 to Y. On days when x is odd, Sam will buy x chocolates; on days when x is even, Sam will not purchase any chocolates.

input_list = [3, 4, 5, 8, 9, 10]

1st day 3 chocolates, divisible by 2 == append it to the list
2nd day 4, not divisible, append 3 to list
3rd day 5, divisible, add it to 3 and append 8 to list
..

'''
# input_list = [2, 5, 8, 11, 4]
input_list = [3, 4, 5, 8, 9, 10]

def q01_chocolates(input_list):
    result = []
    values = 0
    for data in input_list:
        if data % 2 != 0:
            values += data
            
        result.append(values)
    return result

print(q01_chocolates(input_list))