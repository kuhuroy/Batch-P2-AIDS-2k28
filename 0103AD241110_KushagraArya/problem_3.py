# input1 : string : "Fi_er" 
# input2 : string: "Filer:filter:Fiber:Fever:tailor:Fixer"
# Outout: string : "FILER:FIBER:FIXER"
input1 = 'Fi_er'
input2 = 'Filer:filter:Fiber:Fever:tailor:Fixer'
output = ''
input1 =input1.upper()
inputs= [x.upper() for x in input2.split(':')] 
pos = input1.index('_')
for i in inputs:
    temp = input1[0:pos] + i[pos] + input1[pos+1:len(input1)]
    if temp == i:
        if output == '':
            output += temp
        else: 
            output += ':' + temp 
print(output)        
