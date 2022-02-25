# Разработайте стек, который поддерживает push, pop, top и извлечение минимального элемента за постоянное время.
class MyStack:

    def __init__(self):
        self.my_stack = []
        self.min_of_stack = []

    def push(self, el: int):
        self.my_stack.append(el)
        if not self.min_of_stack:
            self.min_of_stack.append(el)
        else:
            if el < self.min_of_stack[-1]:
                self.min_of_stack.append(el)
            else:
                self.min_of_stack.append(self.min_of_stack[-1])

    def pop(self):
        if len(self.my_stack) != 0:
            self.min_of_stack.pop()
            return self.my_stack.pop()

    def top(self):
        if len(self.my_stack) != 0:
            return self.my_stack[-1]

    def get_min(self):
        return self.min_of_stack[-1]


test = MyStack()
test.push(-2)                          # Добавление в стэк
test.push(2)
test.push(4)
print(test.my_stack)
print(test.get_min())                  # Вывод минимального значения
print('<*************>')
print(test.top())                      # Вывод последнего добавленного значения
print('<*************>')
test.pop()                              # Удаление last элемента
print(test.my_stack)
print('<*************>')
print(test.get_min())
print(test.my_stack)
test.pop()
test.pop()
print(test.my_stack)










