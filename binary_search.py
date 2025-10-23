def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Element found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found

# 🧾 Take sorted input from user
arr = list(map(int, input("Enter sorted list of numbers (space-separated): ").split()))
arr.sort()
target = int(input("Enter the number to search: "))

result = binary_search(arr, target)

print(result)
