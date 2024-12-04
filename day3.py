import re 

total = 0
def mul(x,y):
    return x*y 
    
    
with  open('INPUT_DAY3.txt','r') as file : input_data = file.read()
pattern = r"mul\(\d{1,3},\d{1,3}\)"
 
matches = re.findall(pattern,input_data)
print(matches)

for item in matches :
    total += eval(item)
    
print(total)
