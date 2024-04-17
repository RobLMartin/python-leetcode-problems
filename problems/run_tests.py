import time
def run_tests(test_cases, solution_func):
    """
    Runs tests on a given solution function with provided test cases.

    Parameters:
    - test_cases: A list of tuples, where each tuple contains the arguments to the solution function and the expected result.
    - solution_func: The solution function to test.

    Each test case tuple should be in the format:
    (*args, expected_result), where *args are the arguments to pass to the solution function.
    """
    timed_solution_func = time_it(solution_func)
    
    total_time = 0 
    for i, test_case in enumerate(test_cases, 1):
        *args, expected = test_case
        result, exec_time = timed_solution_func(*args)  
        total_time += exec_time  
        assert result == expected, f"Test case {i}: Expected {expected}, got {result}"
        print(f"Test case {i} passed successfully!")

    average_time = total_time / len(test_cases) 
    print(f"Average execution time: {average_time} mil sec")

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        exec_time = (end - start) * 1000  
        return result, exec_time 
    return wrapper