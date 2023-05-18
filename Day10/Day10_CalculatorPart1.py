
def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  if n1>n2:
    return n1-n2
  else:
    return n2-n1


def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,

  
}
not_end=True
num1=int(input("What's the first number?"))

while not_end:
    for symbol in operations:
        print(symbol)
    operation_symbol=input("Pick an operation from the line above: ")
    num2=int(input("What's the next number?"))
    answer=operations[operation_symbol](num1,num2)
    print(f"{num1}{operation_symbol}{num2}={answer}")
    option=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit:")
    num1=answer
    if option=="n":
       not_end=False