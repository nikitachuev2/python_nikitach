
class TreeNode:
    def __init__(self, value):
        # Инициализация узла дерева
        self.value = value  # Значение узла
        self.left = None    # Левый дочерний узел
        self.right = None   # Правый дочерний узел
        self.parent = None  # Родительский узел


class BinarySearchTree:
    def __init__(self):
        # Инициализация бинарного дерева поиска
        self.root = None  # Корень дерева

    def _insert_node(self, node, new_node):
        # Вставка нового узла в дерево
        if new_node.value < node.value:
            if node.left is None:
                node.left = new_node  # Устанавливаем новый узел как левый дочерний
                new_node.parent = node  # Устанавливаем родителя
            else:
                self._insert_node(node.left, new_node)  # Рекурсивный вызов для левого поддерева
        else:
            if node.right is None:
                node.right = new_node  # Устанавливаем новый узел как правый дочерний
                new_node.parent = node  # Устанавливаем родителя
            else:
                self._insert_node(node.right, new_node)  # Рекурсивный вызов для правого поддерева

    def add(self, value):
        # Метод для добавления нового значения в дерево
        new_node = TreeNode(value)  # Создаем новый узел
        if self.root is None:
            self.root = new_node  # Если дерево пустое, устанавливаем корень
        else:
            self._insert_node(self.root, new_node)  # Вставляем новый узел

    def _find_node(self, node, value):
        # Поиск узла с заданным значением
        if node is None or node.value == value:
            return node  # Если узел найден или достигнут конец дерева
        if value < node.value:
            return self._find_node(node.left, value)  # Рекурсивный вызов для левого поддерева
        return self._find_node(node.right, value)  # Рекурсивный вызов для правого поддерева

    def find(self, value):
        # Метод для поиска значения в дереве
        return self._find_node(self.root, value)  # Запускаем поиск от корня

    def _delete_node(self, node, value):
        # Удаление узла с заданным значением
        if node is None:
            return node  # Если узел не найден, возвращаем None

        if value < node.value:
            node.left = self._delete_node(node.left, value)  # Рекурсивный вызов для левого поддерева
        elif value > node.value:
            node.right = self._delete_node(node.right, value)  # Рекурсивный вызов для правого поддерева
        else:
            if node.left is None:
                return node.right  # Если нет левого поддерева, возвращаем правое
            elif node.right is None:
                return node.left  # Если нет правого поддерева, возвращаем левое

            min_larger_node = self._get_min(node.right)  # Находим минимальный узел в правом поддереве
            node.value = min_larger_node.value  # Копируем значение минимального узла
            node.right = self._delete_node(node.right, min_larger_node.value)  # Удаляем минимальный узел

        return node

    def delete(self, value):
        # Метод для удаления значения из дерева
        self.root = self._delete_node(self.root, value)  # Запускаем удаление от корня

    def _get_min(self, node):
        # Поиск минимального узла в поддереве
        while node.left is not None:
            node = node.left  # Переход к левому дочернему узлу
        return node  # Возвращаем минимальный узел

    def _print_tree(self, node, level=0):
        # Вывод дерева в консоль
        if node is not None:
            self._print_tree(node.right, level + 1)  # Сначала выводим правое поддерево
            print(' ' * 4 * level + '->', node.value)  # Выводим текущий узел с отступом по уровню
            self._print_tree(node.left, level + 1)  # Затем выводим левое поддерево

    def print_tree(self):
        # Метод для печати дерева
        self._print_tree(self.root)  # Запускаем вывод от корня


def cli():
    bst = BinarySearchTree()  # Создаем экземпляр бинарного дерева поиска
    while True:
        command = input("Введите команду (add, delete, find, print, exit): ").strip().lower()  # Получаем команду от пользователя
        if command == "add":
            value = int(input("Введите значение для добавления: "))  # Запрашиваем значение для добавления
            bst.add(value)  # Добавляем значение в дерево
        elif command == "delete":
            value = int(input("Введите значение для удаления: "))  # Запрашиваем значение для удаления
            bst.delete(value)  # Удаляем значение из дерева
        elif command == "find":
            value = int(input("Введите значение для поиска: "))  # Запрашиваем значение для поиска
            result = bst.find(value)  # Ищем значение в дереве
            print(f"Найден: {result.value}" if result else "Не найден")  # Выводим результат поиска
        elif command == "print":
            bst.print_tree()  # Печатаем дерево
        elif command == "exit":
            break  # Выход из цикла и завершение программы
        else:
            print("Неизвестная команда. Попробуйте снова.")  # Обработка неизвестной команды


if __name__ == "__main__":  # Исправлено условие запуска основной программы
    cli()  # Запуск CLI интерфейса

