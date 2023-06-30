num1=int(input())
num2=int(input())
score=''
if num1 not in [3,4,5]:
    score="Error"
elif num1-num2>=0:
    if num1-num2==1:
        score='Birdie'
    elif num1-num2==0:
        score='Par'
    elif num1-num2==2:
        score='Eagle'
elif num1-num2==-1:
    score='Bogey'
else:
    score="Error"
print(score)