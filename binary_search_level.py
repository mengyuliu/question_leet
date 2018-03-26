l = [2, 3, 5, 7, 11, 13, 17]
# test = [-10, -5, 0, 0, 1, 3, 3, 3, 5, 10]
test = [-10, -5, 0, 0, 1, 3, 3, 3, 5, 10]

def binary_search(nums, target):
    left = 0
    right = len(nums)-1
    while (left <=right):
        mid = (left + right)//2
        val = nums[mid]
        if val == target:
            return mid
        elif val > target:
            right = mid -1
        else:
            left = mid + 1

    return None

#以下方法得对最小值判断以下
def binary_search_upBoundary(nums, target):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left + right)//2
        val = nums[mid]
        if val <= target:
            left = mid + 1
        else:
            right = mid

        # print(val, target, mid , left, right)
    return left


def binary_search_lowBoundary(nums, target):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left + right)//2
        # mid = left + (right -left)//2
        val = nums[mid]
        if val >= target:
            right = mid
        else:
            left = mid + 1
        print(val, target, val >= target, mid, left, right)
    return left


if __name__ == "__main__":
    print('binary_search_algorithm')

    # print(binary_search_upBoundary(l , 15))l
    # print(binary_search_upBoundary(l, 7))
    n = 10
    # print(binary_search_upBoundary(test, n))
    print(binary_search_lowBoundary(test,n))
