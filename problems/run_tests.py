def run_tests(test_cases, solution_func):
    """
    Runs tests on a given solution function with provided test cases.

    Parameters:
    - test_cases: A list of tuples, where each tuple contains the arguments to the solution function and the expected result.
    - solution_func: The solution function to test.

    Each test case tuple should be in the format:
    (*args, expected_result), where *args are the arguments to pass to the solution function.
    """
    for i, test_case in enumerate(test_cases, 1):
        *args, expected = test_case
        result = solution_func(*args)
        assert result == expected, f"Test case {i}: Expected {expected}, got {result}"
        print(f"Test case {i} passed successfully!")

