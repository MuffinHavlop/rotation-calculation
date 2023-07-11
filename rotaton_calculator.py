nums = [2, 3, 4, 7, 8, -2, 1, 0]

def rotation_calculation(nums):
    position = 0
    while position <= len(nums):
        if position > 0 and nums[position] == min(nums):
            return f'The list has rotated {position} times'
        position += 1 
    return -1

print(rotation_calculation(nums))