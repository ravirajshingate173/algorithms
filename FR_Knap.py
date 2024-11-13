class item:
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight
        self.value_per_weight=value/weight
    
def fractional_knapsack(capacity,items):
    items.sort(key=lambda item:item.value_per_weight,reverse=True)
    
    total_value=0.0
    for item in items:
        if capacity - item.weight >= 0:
            capacity -= item.weight
            total_value += item.value

        else:
            total_value += (item.value*capacity)/item.weight
            capacity=0
            break
    return total_value

capacity = int(input("Enter the Capacity: "))
n = int(input("Enter the number of items: "))

array=[]

for i in range(0,n):
    value = int(input("Enter the value of item "+str(i+1)+" : "))
    weight = int(input("Enter the weight of item "+str(i+1)+" : "))

    obj=item(value,weight)
    array.append(obj)

max_value=fractional_knapsack(capacity,array)

print("The maximum value in knapsack is: ",max_value)