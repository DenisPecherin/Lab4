# Напишите процедуру вычисления арифметического выражения в дереве, используя постфиксный обход
class Node:
    def __init__(self , key): 
        self.Key = key 
        self.Left = None
        self.Right = None
  
def ExampleTree(t):
    if t is not None: 
        if t.Left != None:
            print("(", end='')
        ExampleTree(t.Left)
        print(t.Key, end="") 
        ExampleTree(t.Right)
        if t.Left != None:
            print(")", end='')

def Solve(t): 
    if t.Key == "+":
        return Solve(t.Left) + Solve(t.Right)
    elif t.Key == "-":
        return Solve(t.Left) - Solve(t.Right)
    elif t.Key == "*":
        return Solve(t.Left) * Solve(t.Right)
    elif t.Key == "/":
        return Solve(t.Left) // Solve(t.Right)
    else:
        return int(t.Key)
  
def BuildTree(input): 
    tree = []   
    for elem in input : 
        if not (elem == '+' or elem == '-' or elem == '*' or elem == '/'):
            t = Node(elem) 
            tree.append(t) 
        else: 
            new_node = Node(elem)
            sub_node0 = tree.pop()
            sub_node1 = tree.pop()
            new_node.Right = sub_node0
            new_node.Left = sub_node1
            tree.append(new_node)
    t = tree.pop()      
    return t   

expression = "10 2 3 + * 5 +"
tree = BuildTree(expression.split())
print("Выражение: ", end='')
ExampleTree(tree)
print("\nОтвет: " + str(Solve(tree)))
