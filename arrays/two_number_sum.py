"""Two Number Sum

Write a function that takes in a non-empy array of distinct integers and 
an integer representing a target sum. If any two numbers in the input
array sum up to the target sum, the function should return them in an array,
in any order. If no two numbers sum up to the target sum, the function should
return an empty array.
Note that the target sum has to be obtained by summing two different integers
in the array; you can't add a single integer to itself in order to obtain the 
target sum.
You can assume that there will be at most one pair of numbers summing up to the
target sum.

Sample Input:
    array = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10

Sample Output:
    [-1, 11] // the numbers could be in reversed order

"""


def twoNumberSum(array : list, targetSum : int) -> list:
    """Finds the two numbers in the array needed to get targetSum
    This solution has O(n) time complexity | O(n) space complexity

    Args:
        array: A list containing all the candidate numbers
        targetSum: The target number we want to get by adding two numbers from the array

    Returns:
        A list containing the two numbers that added give targetSum as a result
    """
    sum = []
    diff = []
    for e in array:
        if e in diff:
            sum.append(e)
            sum.append(array[diff.index(e)])
            break
        else:
            diff.append(targetSum - e)
    return sum
