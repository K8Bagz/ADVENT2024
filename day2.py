
from collections import Counter


file = open('INPUT_DAY2.txt','r')
safe_count = 0


# part 1 Receives a list of distances and checks if all are max 3
# part 2 Receives a list of distances minus one element
def DistanceLimit(distances):
    return all(x <=3 for x in distances)
    
    
# part 1 Receives a list of trends (True : positive, False : negative) and checks if all are the same.
# part 2 Receives a list of trends minus one element
def IncOrDec(trends):
    return all(x == trends[0] for x in trends)



for report in file.readlines():
    
    original_list = list(map(int, report.split()))
    print(original_list)
    # PART 2 : Iterate through the list and remove one item at a time
    for i in range(len(original_list)):
        values = original_list[:i] + original_list[i+1:]
      
        print(values)

    # 1st column : distance. An absolute value since we don't know if the report is increasing or decreasing.
    # 2nd column : trend. It has to be n+1 - n = positive for increase(True), 0 for stagnant(None) and negative for decrease(False)
    
        result = [[abs(j-i),True if j - i > 0 else (False if j - i < 0 else None)]  for i, j in zip(values[:-1], values[1:])]
    
        result_distance = DistanceLimit([row[0] for row in result])
        result_trend = IncOrDec([row[1] for row in result])
        
        if result_distance and result_trend:
            safe_count+=1
            break

        
print(safe_count)
