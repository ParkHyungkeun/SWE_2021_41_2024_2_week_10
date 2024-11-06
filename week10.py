# main.py
from typing import List

# Skeleton code for even_list
def even_list(int_list: List[int]) -> List[int]:
    """Returns a list of even integers."""
    # TODO: Implement even_list
    x=[]
    for i in int_list:
        if i%2==0:
            x.append(i)
    return x

# Skeleton code for sum_of_squares_of_even  
def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    """Returns the sum of squares of even integers."""
    # TODO: Implement sum_of_squares_of_even
    sum=0
    for i in even_int_list:
        sum+=i**2
    return sum

# Main function
def main():
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)

if __name__ == "__main__":
    main()