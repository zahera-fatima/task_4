def average_fun(*args):
    average=[]
    for pair in zip(*args):
        average.append(sum(pair)/len(pair))
    return average

# average_fun = lambda *args: [sum(pair)/len(pair) for pair in zip(*args)]

print(average_fun([1,2,3,4] , [5,6,7,8] , [9,10,11,12]))