class SegmentTree:

    def __init__(self, n):
        k = 4 * n + 4
        self.a = [0] * k
        self.ma = [0] * k
        self.su = [0] * k
        self.lazy = [-1] * k

    def left(self, id):
        return id * 2 + 1

    def right(self, id):
        return self.left(id) + 1

    def push_up(self, id):
        lc, rc = self.left(id), self.right(id)
        self.ma[id] = max(self.ma[lc], self.ma[rc])
        self.su[id] = self.su[lc] + self.su[rc]

    def push_down(self, l, r, id):
        lc, rc = self.left(id), self.right(id)
        if l != r and self.lazy[id] != - 1:
            self.lazy[lc] = self.lazy[rc] = self.lazy[id]
            self.lazy[id] = -1
            self.ma[lc] = self.ma[rc] = self.lazy[lc]
            mid = (l + r) // 2
            self.su[lc] = (mid - l + 1) * self.lazy[lc]
            self.su[rc] = (r - mid) * self.lazy[lc]

    def build_tree(self, l, r, id, m):
        if l == r:
            self.ma[id] = m
            self.su[id] = self.a[id] = m
            return
        lc, rc = self.left(id), self.right(id)
        mid = (l + r) // 2
        self.build_tree(l, mid, lc, m)
        self.build_tree(mid + 1, r, rc, m)
        self.push_up(id)

    def update_range(self, l, r, id, ul, ur, v):
        if ul <= l and ur >= r:
            self.lazy[id] = v
            self.ma[id] = v
            self.su[id] = v * (r - l + 1)
            return
        lc, rc = self.left(id), self.right(id)
        mid = (l + r) // 2
        self.push_down(l, r, id)
        if ul <= mid:
            self.update_range(l, mid, lc, ul, ur, v)
        if ur >= mid + 1:
            self.update_range(mid + 1, r, rc, ul, ur, v)
        self.push_up(id)

    def update(self, l, r, id, k, v):
        self.update_range(l, r, id, k, k, v)

    def query(self, l, r, id, ql, qr, flag):
        if ql <= l and qr >= r:
            if flag == "sum":
                return self.su[id]
            else:
                return self.ma[id]
        mid = (l + r) // 2
        lc, rc = self.left(id), self.right(id)
        self.push_down(l, r, id)
        ans = 0 if flag == "sum" else -1 << 31
        if ql <= mid:
            res_l = self.query(l, mid, lc, ql, qr, flag)
            if flag == "sum":
                ans += res_l
            else:
                ans = max(ans, res_l)
        if qr >= mid + 1:
            res_r = self.query(mid + 1, r, rc, ql, qr, flag)
            if flag == "sum":
                ans += res_r
            else:
                ans = max(ans, res_r)
        return ans

    def gather(self, l, r, id, mr, k):
        if l > mr:
            return []
        if self.ma[id] < k:
            return []
        if l == r:
            self.su[id] -= k
            self.ma[id] -= k
            return [l, self.su[id] + k]
        mid = (l + r) // 2
        self.push_down(l, r, id)
        lc, rc = self.left(id), self.right(id)
        ans_l = self.gather(l, mid, lc, mr, k)
        if not ans_l:
            ans_l = self.gather(mid + 1, r, rc, mr, k)
        self.push_up(id)
        return ans_l

    def scatter(self, l, r, id, mr, k):
        if l > mr:
            return 0
        if r <= mr:
            if self.su[id] <= k:
                t = self.su[id]
                self.su[id] = self.lazy[id] = self.ma[id] = 0
                return t
            elif l == r:
                t = self.su[id]
                self.su[id] = t - k
                self.ma[id] = t - k
                return k
        if not k:
            return 0
        mid = (l + r) // 2
        self.push_down(l, r, id)
        lc, rc = self.left(id), self.right(id)
        ans_l = self.scatter(l, mid, lc, mr, k)
        if ans_l >= k:
            self.push_up(id)
            return k
        self.scatter(mid + 1, r, rc, mr, k - ans_l)
        self.push_up(id)
        return k


class BookMyShow:

    def __init__(self, n: int, m: int):
        self.seg = SegmentTree(n)
        self.seg.build_tree(0, n - 1, 0, m)
        self.n = n
        self.m = m

    def gather(self, k: int, maxRow: int) -> List[int]:
        t = self.seg.query(0, self.n - 1, 0, 0, maxRow, "max")
        if t < k:
            return []
        ans = self.seg.gather(0, self.n - 1, 0, maxRow, k)
        return [ans[0], self.m - ans[1]]

    def scatter(self, k: int, maxRow: int) -> bool:
        t = self.seg.query(0, self.n - 1, 0, 0, maxRow, "sum")
        if t < k:
            return False
        self.seg.scatter(0, self.n - 1, 0, maxRow, k)
        return True
