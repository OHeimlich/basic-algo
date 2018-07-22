import random
import tkinter as tk
import time


class DrawGraph(object):
    def __init__(self,graph, width=800, height=500, r=30):
        self.root = tk.Tk()
        self.width = width
        self.height = height
        self.radius = r
        self.canvas = tk.Canvas(self.root, width=width, height=height, borderwidth=0, highlightthickness=0, bg='white')
        self.canvas.grid()
        self.graph = graph
        self.items = {}
        self.locations = []
        self.vertex = set()
        self.get_vertices()
        self.set_locations(len(self.vertex))
        self.draw_vertex()
        self.draw_lines()

    def _create_circle(self, x, y, r, **kwargs):
        return self.create_oval(x - r, y - r, x + r, y + r, **kwargs)

    tk.Canvas.create_circle = _create_circle

    def intersection(self, x, y, size, locations):
        for _x, _y in locations:
            if ((x + size > _x - size) and (x + size < _x + size)) or ((_x + size > x - size) and (_x + size < x + size)):
                if ((y + size > _y - size) and (y + size < _y + size)) or (((_y + size > y - size) and (_y + size < y + size))):
                    return 1
        return 0

    def get_vertices(self):
        for v in self.graph.keys():
            self.vertex.add(v)
            for v_next in self.graph[v]:
                self.vertex.add(v_next)

    def set_locations(self, n):
        for i in range(n):
            while True:
                x = random.randint(50, self.width-50)
                y = random.randint(50, self.height-50)
                if self.intersection(x, y, self.radius, self.locations) == 0:
                    break
            self.locations.append((x, y))

    def draw_vertex(self):
        for v in self.vertex:
            x, y = self.locations.pop()
            c = self.canvas.create_circle(x, y, self.radius, fill='white', outline='black', width=1)
            self.canvas.create_text(x, y, text=v, activefill='red')
            self.items[v] = (x, y, c)

    def draw_lines(self):
        for v in self.graph.keys():
            x, y, _ = self.items[v]
            for e in self.graph[v]:
                _x, _y, _ = self.items[e]
                self.canvas.create_line(x, y, _x, _y)

    def show(self, path):
        self.root.after(2000, self.walk, path)
        self.root.wm_title('BFS')
        self.root.mainloop()

    def walk(self, path, delay=2):
        for v in path:
                _, _, c = self.items[v]
                self.canvas.itemconfig(c, fill='blue')
                self.canvas.update()
                time.sleep(delay)
