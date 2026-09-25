def square_root_bisection(nums, tolerance=0.01, iterations=50):
    if nums < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")
    elif nums == 0 or nums == 1:
        print(f"The square root of {nums} is {nums}")
        return nums
    
    low = 0
    if nums < 1:
        high = 1 
        low = nums
    else:
        high = max(1, nums)
    root = None
    
    for _ in range(iterations):
        root = (low + high) / 2
        if abs(root**2 - nums) < tolerance:
            break
        elif root**2 < nums:
            low = root
        else:
            high = root
    else:
        print(f"Failed to converge within {iterations} iterations")
        return None

    print(f"The square root of {nums} is approximately {root}")
    return root