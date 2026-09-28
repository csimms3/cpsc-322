from model import Node, Arc
import queue


def BFS(start, arcs, goal):
    print("BFS________")
    q = queue.Queue()
    pathq = queue.Queue()
    q.put(start)
    pathq.put(start)
    iter = 1
    while True:
        if q.empty(): break

        next = q.get()
        nextpath = pathq.get()
        arcs_out = [i for i in arcs if i.from_node == next]

        print(f"{iter=}, {next=}, {arcs_out=}")
        print(f"path = {nextpath}")

        if next == goal:
            print(f"goal found: {next}, {nextpath}")
            return next

        for arc in arcs_out:
            q.put(arc.to_node)
            pathq.put(nextpath + "->" + arc.to_node)
        iter += 1

def DFS(start, arcs, goal):
    print("DFS_______")
    s = []
    path_s = []
    s.append(start)
    path_s.append(start)
    iter = 1
    while True:
        if len(s) == 0: break

        next = s.pop()
        nextpath = path_s.pop()
        arcs_out = [i for i in arcs if i.from_node == next]

        print(f"{iter=}, {next=}, {arcs_out=}")
        print(f"path = {nextpath}")

        if next == goal:
            print(f"goal found: {next}, {nextpath}")
            return next

        for arc in arcs_out:
            s.append(arc.to_node)
            path_s.append(nextpath + "->" + arc.to_node)
        iter += 1

def main():
    nodes = ["a", "b", "c", "d", "e"]
    arcs = [
        Arc("a","b"),
        Arc("a","c"),
        Arc("b","e"),
        Arc("c","d"),
        Arc("d", "e")
    ]

    BFS("a", arcs, "e")
    DFS("a", arcs, "e")


if __name__ == "__main__":
    main()