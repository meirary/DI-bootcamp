class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = items if items else []
        self.page_size = int(pageSize)
        self.total_pages = (len(self.items) + self.page_size - 1) // self.page_size
        self.current_page = 1 if self.total_pages > 0 else 0

    def getVisibleItems(self):
        start_idx = (self.current_page - 1) * self.page_size
        end_idx = start_idx + self.page_size
        return self.items[start_idx:end_idx]

    def prevPage(self):
        self.current_page = max(1, self.current_page - 1)
        return self

    def nextPage(self):
        self.current_page = min(self.total_pages, self.current_page + 1)
        return self

    def firstPage(self):
        self.current_page = 1
        return self

    def lastPage(self):
        self.current_page = self.total_pages
        return self

    def goToPage(self, pageNum):
        pageNum = int(pageNum)
        self.current_page = max(1, min(self.total_pages, pageNum))
        return self


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.getVisibleItems())  # ["a", "b", "c", "d"]

p.nextPage()
print(p.getVisibleItems())  # ["e", "f", "g", "h"]

p.lastPage()
print(p.getVisibleItems())  # ["y", "z"]

p.goToPage(10)
print(p.getVisibleItems())  # ["y", "z"]

p.goToPage(-2)
print(p.getVisibleItems())  # ["a", "b", "c", "d"]
