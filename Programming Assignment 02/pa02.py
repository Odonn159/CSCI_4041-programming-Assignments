import random, timeit, math

def mystery1(vals):
    #Computes the largest difference between two elements, opposite of bank function
    #We can make it faster by simply tracking as we iterate through
    maximum1 = vals[0]
    minimum1 = vals[0]
    for i in range(len(vals)):
        if vals[i]>maximum1:
            maximum1 = vals[i]
        if vals[i]<minimum1:
            minimum1 = vals[i]
    return maximum1-minimum1


def mystery2(filename):
    time = {}
    with open(filename) as fp:
        text = fp.read()
        while len(text)>0:
            LTR = text[0]
            time[LTR] = text.count(LTR)
            text = text.replace(LTR, '')
    return time


def merge(array, Lstart, Lend, Rend):
    n1 = Lend - Lstart + 1
    n2 = Rend - Lend
    L = [0] * (n1+1)
    R = [0] * (n2+1)
    for i in range(0, n1):
        L[i] = int(array[Lstart + i])
    for j in range(0, n2):
        R[j] = int(array[Lend + 1 + j])
    L[n1]=(math.inf)
    R[n2]=(math.inf)
    i = 0
    j = 0
    for k in range(Lstart, Rend+1):
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1
def mergeSort(arr, start, end):
    if start < end:
        half = start + (end - start) // 2
        mergeSort(arr, start, half)
        mergeSort(arr, half + 1, end)
        merge(arr, start, half, end)
#This Code I have written was based on pseudocode in class. I modified it to python, but this was given in class.
#This is in the interest of full disclosure, this code was not entirely my own idea. Please don't call me a plagiarist.
# I realize this is more complex than other sort methods, but I figured if optimization was the goal, this was the way to do it.
def mystery3(filename):
    storage = {}
    numlist = []
    with open(filename) as fp:
        for line in fp:
            items = line.split()
            storage[int(items[1])] = items[0]
            numlist.append(int(items[1]))
    mergeSort(numlist,0,(len(numlist)-1))
    output = [0]*len(numlist)
    i=0
    for element in numlist:
        output[i]=(storage[element])
        i+=1
    return output

if __name__ == '__main__':
    lst = [random.randint(0, 9999999) for i in range(1000)]
    time1 = timeit.timeit('mystery1(lst)', globals=globals(), number = 10)
    out = mystery1(lst)
    print("mystery1(lst) output:", out)
    print("mystery1(lst) runtime:", time1, "seconds")
    print('\n------------------\n')
    time2 = timeit.timeit('mystery2("wizard.txt")', globals=globals(), number = 10)
    out = mystery2('wizard.txt')
    print("mystery2('wizard.txt') output:", out)
    print("mystery2('wizard.txt') runtime:", time2, "seconds")
    print('\n------------------\n')
    time3 = timeit.timeit('mystery3("screentime_ms.txt")', globals=globals(), number = 10)
    out = mystery3("screentime_ms.txt")
    print("mystery3('screentime_ms.txt') output:", out)
    print("mystery3('screentime_ms.txt') runtime:", time3, "seconds")
