
nums = [1, 2, 1, 2, 3]

def function(arr):

    output = float("-inf")
    distincts = set()

    n = len(arr) - 1

    if n <= 1:

        return n
    print("Poo")
    distincts.add(arr[0])
    distincts.add(arr[1])

    i = 0
    j = 1
    
    curr = 0

    while i < j and j < n:

        distincts.add(arr[j])

        if len(distincts) <= 2:

            curr = j - i
            print(curr)
            output = max(output, curr)

        else:

            distincts.remove(arr[i])
            i += 1
            j = i + 1

    return output

print(function(nums))