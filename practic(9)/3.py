def merge_sort(array):
    length = len(array)

    def merge(left, right):
        result = []
        
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[i]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result += right[j:]
        result += left[i:]

        return result    

    if length <= 1:
        return array

    middle = (length) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])
    return merge(left, right)

array = [9, 8, 7, 6, 0, 4, 3, 2, 1]
array = merge_sort(array)
print(array)