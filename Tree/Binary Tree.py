class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        self.right_height = -1
        self.left_height = -1

class BinaryTree:
    def __init__(self):
        self.root = None


def loop_add(current, new_node):
    if current.data >= new_node.data and current.left == None:
        current.left = new_node
    elif current.data < new_node.data and current.right == None:
        current.right = new_node
    else:
        if current.data >= new_node.data:
            current = current.left
            current.left_height = current.left_height+1
            return loop_add(current, new_node)
        else:
            current = current.right
            current.right_height = current.right_height+1
            return loop_add(current, new_node)
    return current


def add(b_tree, data_input):
    new_node = Node()
    new_node.data = data_input
    current = b_tree.root
    if b_tree.root == None:
        b_tree.root = new_node
    else:
        loop_add(current, new_node)
    new_node = None
    return current


# def height(node):
#     if node is None:
#         return node
#     h_left = height(node.left_height)
#     h_right = height(node.right_height)
    
#     return max(h_left,h_right)+1


##### TESTS CASE #####


def should_return_20_if_b_tree_root_is_None():
    b_tree = BinaryTree()
    add(b_tree, 20)

    current = b_tree.root.data
    expected = 20

    assert expected == current, f"expect:{expected} but get {current}"


def should_return_30_if_30_is_higher_than_b_tree_root():
    b_tree = BinaryTree()
    add(b_tree, 20)
    add(b_tree, 30)

    current = b_tree.root.right.data
    expected = 30

    assert expected == current, f"expect:{expected} but get {current}"


def should_return_10_if_10_is_lower_than_b_tree_root():
    b_tree = BinaryTree()
    add(b_tree, 20)
    add(b_tree, 30)
    add(b_tree, 10)

    current = b_tree.root.left.data
    expected = 10

    assert expected == current, f"expect:{expected} but get {current}"


def should_return_15_if_15_is_higher_than_10():
    b_tree = BinaryTree()
    add(b_tree, 20)
    add(b_tree, 30)
    add(b_tree, 10)
    add(b_tree, 15)

    current = b_tree.root.left.right.data
    expected = 15

    assert expected == current, f"expect:{expected} but get {current}"


def should_return_40_if_40_is_higher_than_30():
    b_tree = BinaryTree()
    add(b_tree, 20)
    add(b_tree, 30)
    add(b_tree, 10)
    add(b_tree, 15)
    add(b_tree, 40)

    current = b_tree.root.right.right.data
    expected = 40

    assert expected == current, f"expect:{expected} but get {current}"


def tests():
    should_return_20_if_b_tree_root_is_None()
    should_return_30_if_30_is_higher_than_b_tree_root()
    should_return_10_if_10_is_lower_than_b_tree_root()
    should_return_15_if_15_is_higher_than_10()
    should_return_40_if_40_is_higher_than_30()


def main():
    pass


if __name__ == '__main__':
    tests()
    main()
