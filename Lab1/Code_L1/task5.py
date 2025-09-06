import random

def quick_sort(nums, low, high):
    if low < high:
        pi = partition(nums, low, high)
        quick_sort(nums, low, pi - 1)
        quick_sort(nums, pi + 1, high)
    return nums

def partition(nums, low, high):
    pi = low
    nums[pi], nums[high] = nums[high], nums[pi]

    pi = high
    p = nums[pi]

    i = low
    for j in range(i, high):
        if nums[j] < p:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[pi], nums[i] = nums[i], nums[pi]
    return i

if __name__ == '__main__':    
    arr = [random.randint(-100, 100) for _ in range(10)]
    print('Исходный список: ', arr)
    print('Отсортированный список: ', quick_sort(arr, 0, len(arr) - 1))