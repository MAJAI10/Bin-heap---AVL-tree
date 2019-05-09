import csv
import random

class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    def shift_up(self, i):
        while i > 0 and self.values[i] < self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]
            i = (i - 1) // 2

    def shift_down(self, i):
        while 2 * i + 1 < self.size:
            j = i
            if self.values[2 * i + 1] < self.values[i]:
                j = 2 * i + 1
            if 2 * i + 2 < self.size and self.values[2 * i + 2] < self.values[j]:
                j = 2 * i + 2
            if i == j:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j

    def insert(self, x):
        self.values.append(x)
        self.size += 1
        self.shift_up(self.size - 1)

    def extract_min(self):
        if not self.size:
            return None # if list is empty(no tree)
        deleted_element = self.values[0]
        self.values[0] = self.values[-1] # turning the last element into root
        self.values.pop()
        self.size -= 1
        self.shift_down(0)
        return deleted_element

    # Sorting List with HEAP...O (N logN)

    def Heap_sort(self, list, x_obj):
        """Sorting list with heap sort...complexity - O(NlogN)..."""
        self.list = list
        self.x_obj = x_obj
        x_obj = Heap()
        for x in list:
            x_obj.insert(x)  # inserting in Heap every object in list
        list.clear()  # deleting all objects of the list
        for x in range(len(x_obj.values)):  # looping through Heap's values quantity
            list.append(x_obj.extract_min())  # adding every next minimum element
        return list

    # FAST HEAP SORTING ( O(N) ) !!!!

    def heap_sort_fast(self, list, object):
        """Heap sort FAST...Complexity - O(N)..."""
        self.list = list
        self.object = object
        object = Heap()
        object.values = list[:]
        object.size = len(list)
        for i in reversed(range(len(list) // 2)):
            object.shift_down(i)
        list.clear()
        for x in range(object.size):
            list.append(object.extract_min())
        return list

def createData(file_name,key_num):

    #file_name = input("Enter the file name to create >>")
    #key_num = int(input("no of keys to be inserted"))

    #key_num = int(val)
    with open(file_name,'w') as out:
        rand_list = random.sample(xrange(1,10000), key_num)
        for val in rand_list:
            out.write(str(val))
            out.write(",")
            out.write("0")
            
            #out.write(val)
		
        
    out.close() 





TheHeap = Heap()



key_num = input("enter the no.of keys")

createData("input.txt",key_num)

with open("input.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        for item in row:
            TheHeap.insert(int(item))
#TheHeap.insert(6)
#TheHeap.insert(1)
#ch = "yes"
while(1):
    print("1- deletemin")
    print("2 - print")
    print("3 - inset manually")
    choice = input("Enter your choice")
    print(choice)
    
    if(choice == 1):
    
        print(TheHeap.extract_min())
    
    elif(choice == 2):
        print(TheHeap.values)

    elif(choice == 3):
        value = input("Enter the key")
        TheHeap.insert(int(value))

    else:
        print("none")
    #ch = char

    
# Sorting List witxh HEAP... O (N logN)

##list = [46, 15, 3, 4, 21, 79]
#print(TheHeap.Heap_sort(list, TheHeap))

# Fast sorting with Heap .... O (N)

#print(TheHeap.heap_sort_fast(list, TheHeap))