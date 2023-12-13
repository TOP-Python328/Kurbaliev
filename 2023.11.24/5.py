from random import randrange as rr, sample
from string import ascii_lowercase as letters


class TestCase:
    """
    Адресат.
    """
    def __init__(self):
        self.messages = [
            "".join(sample(letters, k=rr(3, 7)))
            for _ in range(1000)
        ]
        self.numbers = [
            (rr(10, 100) for _ in range(rr(4, 6))) 
            for _ in range(1000)
        ]
    
    def print_msg(self):
        msg = self.messages.pop()
        print(msg)
    
    def print_nums(self):
        nums = self.numbers.pop()
        print(*nums)
    

class Command:
    def __init__(self, test_case):
        self.test_case = test_case
        self.undo_stack = []
        self.redo_stack = []

    def execute(self, method, *args):
        try:
            result = getattr(self.test_case, method)(*args)
            self.undo_stack.append((method, args))
            self.redo_stack.clear()
            return result
        except Exception as e:
            print(f"Exception occurred: {e}")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo")
            return
        method, args = self.undo_stack.pop()
        self.redo_stack.append((method, args))

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo")
            return
        method, args = self.redo_stack.pop()
        self.execute(method, *args)


test_case = TestCase()
manager = Command(test_case)

manager.execute("print_msg")
manager.execute("print_nums")

manager.undo()
manager.redo()