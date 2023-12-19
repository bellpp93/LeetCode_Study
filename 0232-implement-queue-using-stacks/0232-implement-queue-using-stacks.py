class MyQueue:

    def __init__(self):
        self.__push_stack = []
        self.__pop_stack = []

    def push(self, x: int) -> None:
        self.__push_stack.append(x)

    def __transfer_elements(self):
        self.__pop_stack.extend(reversed(self.__push_stack))
        self.__push_stack = []
        
    def pop(self) -> int:
        if not self.__pop_stack:
            self.__transfer_elements()
        return self.__pop_stack.pop()

    def peek(self) -> int:
        if not self.__pop_stack:
            self.__transfer_elements()
        return self.__pop_stack[-1]

    def empty(self) -> bool:
        return not (self.__push_stack or self.__pop_stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()