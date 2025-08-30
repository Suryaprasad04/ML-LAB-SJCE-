def step(x):
    return 1 if x >= 0 else 0

def perceptron(x1,x2,w1,w2,bias):
    total=x1*w1 + x2*w2 + bias
    return step(total)

gate=input("Enter the gate (AND, OR): ").strip().upper()
x1=int(input("Enter first input (0 or 1): "))
x2=int(input("Enter second input (0 or 1): "))

if gate == "AND":
    print("Output:", perceptron(x1, x2, 1, 1, -1.5))
elif gate == "OR":
    print("Output:", perceptron(x1, x2, 1, 1, -0.5))
else:
    print("Invalid gate")
    
