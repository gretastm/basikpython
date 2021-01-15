#Bubble Sort (n*n)-կիսով չափ սորտավորված
data=[5,1,4,3,2,10,8]
def bubble_sort(data):
    swapped=True
    while swapped:
        swapped=False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped=True
    print(data)
bubble_sort(data)