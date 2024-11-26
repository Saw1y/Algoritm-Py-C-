# Реализуйте структуру данных "дек".  Напишите программу, содержащую описание дека и моделирующую работу дека, реализовав все указанные здесь методы. Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести одну строчку. Возможные команды для программы:

# push_front
# Добавить (положить) в начало дека новый элемент. Программа должна вывести ok.

# push_back
# Добавить (положить) в конец дека новый элемент. Программа должна вывести ok.

# pop_front
# Извлечь из дека первый элемент. Программа должна вывести его значение.

# pop_back
# Извлечь из дека последний элемент. Программа должна вывести его значение.

# front
# Узнать значение первого элемента (не удаляя его). Программа должна вывести его значение.

# back
# Узнать значение последнего элемента (не удаляя его). Программа должна вывести его значение.

# size
# Вывести количество элементов в деке.

# clear
# Очистить дек (удалить из него все элементы) и вывести ok.

# exit
# Программа должна вывести bye и завершить работу.
# Гарантируется, что количество элементов в деке в любой момент не превосходит 100. Перед исполнением операций pop_front, pop_back, front, back программа должна проверять, содержится ли в деке хотя бы один элемент. Если во входных данных встречается операция pop_front, pop_back, front, back, и при этом дек пуст, то программа должна вместо числового значения вывести строку error.

# Входные данные
# Вводятся команды управления деком, по одной на строке.

# Выходные данные
# Требуется вывести протокол работы дека, по одному сообщению на строке

class Deque:
    def __init__(self):
        self.items = []

    def push_back(self, n):
        self.items.append(n)
        return "ok"

    def push_front(self, n):
        self.items = [n] + self.items
        return "ok"

    def pop_back(self):
        if self.is_empty():
            return "error"
        else:
            return self.items.pop()

    def pop_front(self):
        if self.is_empty():
            return "error"
        else:
            return self.items.pop(0)

    def back(self):
        if self.is_empty():
            return "error"
        else:
            return self.items[-1]

    def front(self):
        if self.is_empty():
            return "error"
        else:
            return self.items[0]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items = []
        return "ok"

    def is_empty(self):
        return self.items == []


deque = Deque()
command = input()
while command != "exit":
    if command == "pop_front":
        print(deque.pop_front())
    elif command == "pop_back":
        print(deque.pop_back())
    elif command == "front":
        print(deque.front())
    elif command == "back":
        print(deque.back())
    elif command == "size":
        print(deque.size())
    elif command == "clear":
        print(deque.clear())
    elif command[:9:] == "push_back":
        n = int(command[9::])
        print(deque.push_back(n))
    elif command[:10:] == "push_front":
        n = int(command[10::])
        print(deque.push_front(n))
    command = input()
print("bye")
