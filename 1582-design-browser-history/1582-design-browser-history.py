class Node:
    def __init__(self,val):
        self.url = val
        self.back = None
        self.forward = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)

    def visit(self, url: str) -> None:
        node = Node(url)
        node.back = self.curr
        self.curr.forward = node
        self.curr = node

    def back(self, steps: int) -> str:
        while steps and self.curr.back:
            self.curr = self.curr.back
            steps -= 1
        return self.curr.url
        

    def forward(self, steps: int) -> str:
        while steps and self.curr.forward:
            self.curr = self.curr.forward
            steps-=1
        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)