from turtledemo.penrose import inflatedart
from types import new_class


class Floor:
    def __init__(self):
        self.color = "White"
        self.d = 50000000
        self.p = None


def bfs_stairs(n: int, x: int, y: int, u: int, d: int) -> str | int:
    elevator = []
    for f in range(1, n + 1):
        elevator.append(Floor())
    Q = []
    elevator[x - 1].d = 0
    elevator[x - 1].color = "Gray"
    Q.append(x)
    while len(Q) > 0:
        next = Q.pop(0)

        # if next == y:
        #     seq = []
        #     p = elevator[y].p
        #     c = y
        #     while p is not None:
        #         if p + u == c:
        #             seq.append("U")
        #         else:
        #             seq.append("D")
        #         c = p
        #         p = elevator[c].p
        #     return seq

        if next + u <= n:
            up = next + u
            if elevator[up - 1].color == "White":
                elevator[up - 1].color = "Gray"
                elevator[up - 1].d = elevator[next - 1].d + 1
                elevator[up - 1].p = next
                Q.append(up)
        if next - d >= 1:
            down = next - d
            if elevator[down - 1].color == "White":
                elevator[down - 1].color = "Gray"
                elevator[down - 1].d = elevator[next - 1].d + 1
                elevator[down - 1].p = next
                Q.append(down)
        elevator[next - 1].color = "Black"

    if elevator[y - 1].d > 5000000:
        return ("TAKE THE STAIRS!")
    else:
        return elevator[y - 1].d

    # return []

a = bfs_stairs(10, 1, 10, 2, 1)
print (a)