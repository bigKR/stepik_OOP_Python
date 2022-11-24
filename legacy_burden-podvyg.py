class Vertex:
    def __init__(self):
        self._links = []

    @property
    def links(self):
        return self._links

    @links.setter
    def links(self, value):
        if isinstance(value, Link):
            self._links.append(value)


class Link:
    def __init__(self, v1, v2):
        self._v1, self._v2 = v1, v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1

    @property
    def v2(self):
        return self._v2

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        if isinstance(value, (int, float)):
            self._dist = value

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return sorted((id(self.v1), id(self.v2))) == sorted((id(other.v1), id(other.v2)))


class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

            for i in v.links:
                if i not in self._links:
                    self._links.append(i)

    def add_link(self, link):
        if link not in self._links:
            self._links.append(link)

            for i in (link.v1, link.v2):
                if i not in self._vertex:
                    self._vertex.append(i)

    def find_path(self, start_v, stop_v):
        pass

    def create_matrix(self):
        pass


map_graph = LinkedGraph()

v1 = Vertex()
v2 = Vertex()
v3 = Vertex()
v4 = Vertex()
v5 = Vertex()
v6 = Vertex()
v7 = Vertex()

map_graph.add_link(Link(v1, v2))
map_graph.add_link(Link(v2, v3))
map_graph.add_link(Link(v1, v3))

map_graph.add_link(Link(v4, v5))
map_graph.add_link(Link(v6, v7))

map_graph.add_link(Link(v2, v7))
map_graph.add_link(Link(v3, v4))
map_graph.add_link(Link(v5, v6))

print(len(map_graph._links))   # 8 связей
print(len(map_graph._vertex))