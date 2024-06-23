state = "00000001"
start = 0
iter = 0
flag = 0
while state != "00000001" or start==0:
    iter += 1
    start = 1

    significant_bit = state[0]
    if(significant_bit != state[4]):
        num1 = '1'
    else:
        num1 = '0' 

    if(significant_bit != state[5]):
        num2 = '1'
    else:
        num2 = '0'

    if(significant_bit != state[6]):
        num3 = '1'
    else:
        num3 = '0'
    state = state[1:4] + num1 + num2 + num3 + state[7] + significant_bit
    #print(f"{iter} : {para}")

    
print(f"There are {iter} different non-zero bit pattern")
if(iter == 255):
    print("x^8 + x^4 + x^3 + x^2 + 1 is a  primitive polynomial")
else:
    print("x^8 + x^4 + x^3 + x^2 + 1 is not a primitive polynomial")