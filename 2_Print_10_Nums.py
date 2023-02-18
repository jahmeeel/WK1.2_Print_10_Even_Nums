"""
Write a Python program that prints the first 10 even numbers.

Expected output: 0, 2, 4, 6, 8, 10, 12, 14, 16, 18.
"""

"""
1. Understand the Problem:
    - What is this problem asking?
        - Print even numbers.
        - Print even numbers in a specific range.
        - By implication, I use use a for loop, the range keyword, and maybe a function.
        
    - What are the inputs?
        - A number to iterate through.
        
    - What is the expected output?
        - Even numbers: Output: 0, 2, 6, etc. 
        
    - Edge Cases:
        - String input
        
2. Plan
    - Use the range()
    - Create a for loop?
    - Define a function to contain the arguments.
    - Iterate through the list and define an argument that skips selects only the even numbers:
        - Use modulus
        - Use an if statement
    - Pseudo:
        - def function(number):
            for even in range(number):
                if even % number == 0:
                    print even
3. Execute

4. Review
    - After refactoring and reminding myself of how the range function work, I realized that I didn't have to rewrite a whole function to do what the range function already does. 

    - And so, I just used the start, stop, and step parameters to set the function as I needed in order to print the expected output. 
"""

# def select_even_numbers(number)
#     for even in range(11):
#         if even % number == 0:
#             return

# print(select_even_numbers(11))

# 

for num in range(0, 19, 2):
    print(num)