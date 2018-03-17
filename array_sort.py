l = [4,5,6,7,1,3,11,15,30,29,17]
# l = [3,1,2]

def quick_sort(arr, left, right):
    if left >=  right:
        return
    povit = left
    val = arr[povit]
    low = left
    high = right

    while (left < right):
        while val < arr[right] and left < right:
            right = right -1
        arr[left] = arr[right]
        while val > arr[left] and left < right:
            left = left +1
        arr[right] = arr[left]
    arr[left] = val
    quick_sort(arr, low, left -1)
    quick_sort(arr, left+1, high)
    return arr

def merge_sort(arr, left, right):
    if left >= right:
        return [arr[left]]
    mid = (left+right)//2
    left_list = merge_sort(arr, left, mid)
    right_list = merge_sort(arr, mid+1, right)
    #合并
    left_index = 0
    right_index = 0
    result = []
    while left_index < len(left_list) and right_index < len(right_list):
        val_left = left_list[left_index]
        val_right = right_list[right_index]
        if val_left < val_right:
            result.append(val_left)
            left_index += 1
        else:
            result.append(val_right)
            right_index += 1
    if left_index < len(left_list):
        result = result + left_list[left_index:]

    if right_index < len(right_list) :
        result = result + right_list[right_index:]
    return result

def buble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

    return arr



if __name__ =="__main__":
    print('hello world')
    # print(quick_sort(l , 0, len(l)-1))
    # print(merge_sort(l, 0 , len(l)-1))
    print (buble_sort(l))