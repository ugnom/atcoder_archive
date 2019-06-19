import array
import time

class UnionFind :
    def __init__(self, n):
        self.par = array.array('i', range(n))
        self.sizes = array.array('i', [1]*n)
        self.rank = array.array('i', [0]*n)


    def root(self, i):
        if i == self.par[i]:
            return i
        else:
            r = self.root(self.par[i])
            self.par[i] = r
            return r

    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        srx = self.sized(x)
        sry = self.sized(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.par[rx] = ry
            else:
                self.par[ry] = rx
                if self.rank[rx] == self.rank[ry]:
                    self.rank[rx] = self.rank[rx] + 1
            self.sizes[self.root(rx)] = srx + sry

    def same(self, x, y) :
        return self.root(x) == self.root(y)

    def sized(self, x):
        return self.sizes[self.root(x)]

    def debug(self):
        print(self.par)
        print(self.sizes)
