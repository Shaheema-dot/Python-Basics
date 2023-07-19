opr, *x = input().split()
x = list(map(int, x))    
def add(x):
    return sum(x)

def mul(x):
    count = 1
    for i in x:
        count = count * i
    return count       

def sub(x):
    return x[0] - x[1]

def div(x):
    return x[0] - x[1]

if opr == "add":
    ans = add(x)
elif opr == "mul":
    ans = mul(x)
elif opr == "sub":
    ans = sub(x)
elif opr == "div":
    ans = div(x)
else:
    ans ="Invalid Operation"

print(ans)      

