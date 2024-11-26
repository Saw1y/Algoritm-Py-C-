# Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. Программа дожна определить, является ли данная скобочная последовательность правильной.

# Пустая последовательность явлется правильной. Если A – правильная, то последовательности (A), [A], {A} – правильные. Если A и B – правильные последовательности, то последовательность AB – правильная.

# Входные данные
# В единственной строке записана скобочная последовательность, содержащая не более 100000 скобок.

# Выходные данные
# Если данная последовательность правильная, то программа должна вывести строку yes, иначе строку no.

stack = []
s = input()
n = len(s)
push_stack = ["(", "{", "["]
for i in range(n):
    if s[i] in push_stack:
        stack.append(s[i])
    else:
        if len(stack) == 0:
            print("no")
            exit()
        top = stack[-1]
        if top == "(" and s[i] == ")":
            stack.pop()
        elif top == "[" and s[i] == "]":
            stack.pop()
        elif top == "{" and s[i] == "}":
            stack.pop()
        else:
            print("no")
            exit()
if len(stack) == 0:
    print("yes")
else:
    print("no")
