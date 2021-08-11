def countdown(n):
    while n > 0:
        yield n
        n -= 1

#Generators simulate multi-threading and achieve same purpose

# c1 = countdown(10)
# c2 = countdown(20)
# print(next(c1))
# print(next(c2))
# print(next(c1))
# print(next(c2))
# print(next(c1))
# print(next(c2))


tasks = [countdown(10), countdown(5), countdown(20)]

while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        tasks.append(task)
    except StopIteration:
        print('Task Finished')