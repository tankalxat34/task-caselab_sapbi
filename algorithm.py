
class Node:
    """
    Узел дерева
    """
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"{self.value} -> ({self.left} ; {self.right})"


class InorderTraversal:
    """
    Обход узлов в отсортированном (симметричном) порядке. Для получения ответа вызвать метод `get`
    """
    def __init__(self) -> None:
        self.value = None

    def _body(self, node: Node, target: int):
        if node.value > target and self.value is None:
            self.value = node.value
            return self.value

    def inorderTraversal(self, node: Node, target: int):
        if node and self.value is None:
            self.inorderTraversal(node.left, target)
            self._body(node, target)
            self.inorderTraversal(node.right, target)

    def get(self, root: Node, target: int) -> int:
        """
        Возвращает ближайшую статью с бОльшим номером

        root: корневой элемент (без предка)
        target: искомое значение
        """
        self.value = None
        self.inorderTraversal(root, target)
        return self.value or -1


def build_bst(numbers: list[int] | set[int]) -> Node:
    """
    Создает бинарное дерево из списка чисел. В списке числа должны быть уникальными

    numbers: список или множество чисел, которые будут в дереве
    """
    def insert_bst(root, value):
        if root is None:
            return Node(value)
        if value < root.value:
            new_node = insert_bst(root.left, value)
            root.left = new_node
            new_node.parent = root
        else:
            new_node = insert_bst(root.right, value)
            root.right = new_node
            new_node.parent = root
        return root
    
    root = None
    for num in numbers:
        root = insert_bst(root, num)
    return root
