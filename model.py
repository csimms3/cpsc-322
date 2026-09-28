

# to add onto once we need more node metadata, for now str is fine
class Node:
    def __init__(self, name=""):
        self.name = name

class Arc:
    def __init__(self, from_node, to_node, cost=0):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost

    def __repr__(self):
        return f"({self.from_node} -> {self.to_node})"

def main():
    A = Node("A")
    B = Node("B")
    C = Node()

    Arc1 = Arc(A,B)
    Arc2 = Arc(A,C)

    print(Arc1)
    print(Arc2)
    print(A)



if __name__ == "__main__":
    main()