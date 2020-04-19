# Напишите рекурсивную процедуру построения идеально сбалансированного дерева
# для произвольных N узлов, хранящихся в файле
class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None


def buildBalancedTree(values):
    if len(values) == 0:
        return None
    else:
        tmp = Node()
        tmp.left = buildBalancedTree(values[:len(values) // 2])
        tmp.value = values[len(values) // 2]
        tmp.right = buildBalancedTree(values[len(values) // 2 + 1:])
        return tmp


def printBalancedTree(root):
    if root == None:
        return "не существует"
    else:
        print(f"{root.value} → лево - {printBalancedTree(root.left)}; право - {printBalancedTree(root.right)}")
        return root.value


if __name__ == "__main__":
    with open("vtoroe.txt") as f:
        data = [x for x in f.readline().split(" ")]
    root = buildBalancedTree(data)
    printBalancedTree(root)

