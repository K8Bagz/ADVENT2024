
file = open('INPUT_DAY2.txt','r')
safe_count = 0


def Distance(x,y):
    return x-y
    

def Trend(x,y):
    if x>y : return 'Inc'
    if y>x : return 'Dec'
    return 'Non'
    
def Score(report):
    score = 0 
    distance = 0
    trend ='Start'
    temp_trend =''
    for i in range(len(report)):
        distance = Distance(report[i],report[i-1])
        temp_trend = Trend(report[i],report[i-1])
        if distance <=3 and trend !='Start' and temp_trend == trend : score +=1
        trend =temp_trend
    return score
    
for line in file.readlines():
    
    report = list(map(int, line.split()))
    for i in range(len(report)):
        subreport_safe_count = 0
        subreport = report[:i] + report[i+1:]
        score = Score(subreport)
        if score >= len(subreport) - 2 : subreport_safe_count+=1
    if subreport_safe_count>=1 : safe_count+=1
print(safe_count)        

    #SCORE FOR SUBSETS QND IF ONE IS OK THEN SAFE