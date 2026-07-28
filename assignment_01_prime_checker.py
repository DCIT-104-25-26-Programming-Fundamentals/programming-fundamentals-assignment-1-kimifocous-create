# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================
#
# TASK: Prime Number Checker
#
# Write a Python program that checks whether a given number is prime.
#
# A prime number is a whole number greater than 1 that has no divisors
# other than 1 and itself (e.g., 2, 3, 5, 7, 11, 13 ...).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLES
# -----------------------------------------------------------------------------
#
#   Enter a number: 7
#   7 is a prime number.
#
#   Enter a number: 10
#   10 is NOT a prime number.
#
#   Enter a number: 1
#   1 is NOT a prime number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement the logic inside a function (see scaffold below).
# - Numbers less than 2 are NOT prime — handle this inside the function.
# - The main block must call the function and print the result.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def is_prime(number):
    """
    Return True if 'number' is a prime number, otherwise return False.
 
    A prime number is a whole number greater than 1 that has no
    divisors other than 1 and itself.
    """
 
    # Numbers less than 2 are never prime (this covers 0, 1, and
    # negative numbers).
    if number < 2:
        return False
 
    # 2 is the only even prime number. Handle it directly, then we
    # can skip all other even numbers below.
    if number == 2:
        return True
 
    # Any other even number cannot be prime.
    if number % 2 == 0:
        return False
 
    # Check odd divisors from 3 up to the square root of 'number'.
    # If 'number' is divisible by anything in this range, it is
    # not prime. We only need to check up to sqrt(number) because
    # a larger factor would have to be paired with a smaller one
    # that we would already have found.
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
 
    # No divisors found — the number is prime.
    return True
 
 
def main():
    # Get input from the user and convert it to an integer.
    user_input = input("Enter a number: ")
    number = int(user_input)
 
    # Call the function and print the appropriate message.
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is NOT a prime number.")
 
 
if __name__ == "__main__":
    main()