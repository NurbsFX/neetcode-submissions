class Node:
    def __init__(self, url: str):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node(homepage)

    def visit(self, url: str) -> None:
        newNode = Node(url)

        self.current.next = newNode
        newNode.prev = self.current

        self.current = newNode
        

    def back(self, steps: int) -> str:
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev
        return self.current.url
        

    def forward(self, steps: int) -> str:
        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next
        return self.current.url