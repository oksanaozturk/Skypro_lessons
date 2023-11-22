"""Создайте класс TodoList, который хранит ваши задачи.
Реализуйте магические методы, которые позволят добиться следующего поведения:"""
#
# >>> tasks = ['task1', 'task2']
#
# >>> list1 = TodoList(tasks)
#
# >>> print(repr(list1))
# TodoList(list[str])
#
# >>> print(list1)
# task1
# task2


class TodoList:
    """Класс для представления списка задач"""

    def __init__(self, tasks: list[str]) -> None:
        self.tasks = tasks

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.tasks})"

    def __str__(self):
        return '\n'.join(self.tasks)

    def __add__(self, other: 'TodoList') -> 'TodoList':
        total_tasks = self.tasks
        total_tasks.extend(other.tasks)
        return TodoList(total_tasks)
        # return TodoList(self.tasks + other.tasks)

    def __len__(self) -> int:
        return len(self.tasks)


if __name__ == '__main__':
    tasks = ['task1', 'task2']
    list1 = TodoList(tasks)

    print(repr(list1))
    # TodoList(list[str]

    print(list1)
    # task1
    # task2

    list2 = TodoList(['task3', 'task4'])
    list3 = list1 + list2

    print(list3)
    # task1
    # task2
    # task3
    # task4

    print(len(list3))
    # 4