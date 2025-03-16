from tkinter import *


class Node:
    def __init__(self, data, name, acc_number, status):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
        self.name = name
        self.acc_number = acc_number
        self.status = status


class AVLTree:
    def __init__(self):
        self.root = None


##### FUNCTIONS #####


def convert_to_num(char):
    char_to_num_dictionary = {
        'a': 1, 'A': 1,
        'b': 2, 'B': 2,
        'c': 3, 'C': 3,
        'd': 4, 'D': 4,
        'e': 5, 'E': 5,
        'f': 6, 'F': 6,
        'g': 7, 'G': 7,
        'h': 8, 'H': 8,
        'i': 9, 'I': 9,
        'j': 10, 'J': 10,
        'k': 11, 'K': 11,
        'l': 12, 'L': 12,
        'm': 13, 'M': 13,
        'n': 14, 'N': 14,
        'o': 15, 'O': 15,
        'p': 16, 'P': 16,
        'q': 17, 'Q': 17,
        'r': 18, 'R': 18,
        's': 19, 'S': 19,
        't': 20, 'T': 20,
        'u': 21, 'U': 21,
        'v': 22, 'V': 22,
        'w': 23, 'W': 23,
        'x': 24, 'X': 24,
        'y': 25, 'Y': 25,
        'z': 26, 'Z': 26,
        ' ': 27
    }
    return char_to_num_dictionary[char]


def convert(name):
    array = []
    number = 0
    for i in range(len(name)):
        index = convert_to_num(name[i])
        array.append(index)
    for i in array:
        if i < 10:
            number = number*10 + i
        else:
            number = number*100 + i
    return number


def height(node):
    if node is None:
        return -1
    else:
        return node.height


def balance_factor(node):
    if node is None:
        return -1
    else:
        return height(node.left) - height(node.right)


def rotate_right(root):
    left_child = root.left
    right_child_of_left_child = left_child.right

    left_child.right = root
    root.left = right_child_of_left_child

    root.height = 1+max(height(root.left), height(root.right))
    left_child.height = 1+max(height(left_child.left),
                              height(left_child.right))

    return left_child


def rotate_left(root):
    right_child = root.right
    left_child_of_right_child = right_child.left

    right_child.left = root
    root.right = left_child_of_right_child

    root.height = 1+max(height(root.left), height(root.right))
    right_child.height = 1 + \
        max(height(right_child.left), height(right_child.right))

    return right_child


def rearrange_left_left(root):
    return rotate_right(root)


def rearrange_left_right(root):
    root.left = rotate_left(root.left)
    return rotate_right(root)


def rearrange_right_right(root):
    return rotate_left(root)


def rearrange_right_left(root):
    root.right = rotate_right(root.right)
    return rotate_left(root)


def search_loop(current, name_to_number, iteration_count):
    if current is None:
        return None

    if current.data == name_to_number:
        return current
    else:
        if current.data >= name_to_number:
            current = current.left
            iteration_count[0] += 1
            return search_loop(current, name_to_number, iteration_count)
        else:
            current = current.right
            iteration_count[0] += 1
            return search_loop(current, name_to_number, iteration_count)


def input(avl_tree, name, acc_number, status):
    data = convert(name)
    value = append(avl_tree, data, name, acc_number, status)
    return value


def append(root, data, name, acc_number, status):
    if root is None:
        return Node(data, name, acc_number, status)
    elif data <= root.data:
        root.left = append(root.left, data, name, acc_number, status)
    elif data > root.data:
        root.right = append(root.right, data, name, acc_number, status)

    root.height = 1 + max(height(root.left), height(root.right))
    balance = balance_factor(root)

    if balance > 1 and data < root.left.data:
        return rearrange_left_left(root)

    if balance < -1 and data > root.right.data:
        return rearrange_right_right(root)

    if balance > 1 and data > root.left.data:
        return rearrange_left_right(root)

    if balance < -1 and data < root.right.data:
        return rearrange_right_left(root)

    return root


def search(avl_tree, name, iteration_count):
    name_to_number = convert(name)
    if avl_tree.root.data == name_to_number:
        return avl_tree.root
    else:
        current = avl_tree.root
        result = search_loop(current, name_to_number, iteration_count)
        return result


def search_button_clicked(avl_tree, search_entry, result_name, result_acc_num, result_status, result_iteration):
    # Get the user input from the search entry
    user_input = search_entry.get()
    # Perform AVL tree search
    iteration_count = [0]
    result = search(avl_tree, user_input, iteration_count)
    # Update the labels with the search result
    if result:
        result_name.set(result.name)  # Update with appropriate data
        result_acc_num.set(str(result.acc_number))
        result_status.set(result.status)
    else:
        result_name.set("Not Found")
        result_acc_num.set("Not Found")
        result_status.set("Not Found")
    result_iteration.set(str(iteration_count[0]))


def to_list_bfs(avl_tree):
    if avl_tree.root is None:
        return ''
    queue = [avl_tree.root]
    to_list = [[avl_tree.root.name,
                avl_tree.root.acc_number, avl_tree.root.status]]
    while len(queue) > 0:
        current = queue.pop(0)

        if current.left != None:
            queue.append(current.left)
            to_list.append(
                [current.left.name, current.left.acc_number, current.left.status])
        if current.right != None:
            queue.append(current.right)
            to_list.append(
                [current.right.name, current.right.acc_number, current.right.status])
    return to_list


##### TESTS CASE #####


def test_rebalance_left_right():
    avl_tree = AVLTree()
    avl_tree.root = input(avl_tree.root, 'Samuel', 12345678, 'NONE')    # Samuel    = 1911321512
    avl_tree.root = input(avl_tree.root, 'Grace', 23789132, 'FINED')    # Grace     = 718135
    avl_tree.root = input(avl_tree.root, 'Jemima', 8213854, 'BORROW')   # Jemima    = 105139131

    expected = [['Jemima', 8213854, 'BORROW'], ['Grace', 23789132, 'FINED'], ['Samuel', 12345678, 'NONE']]
    current = to_list_bfs(avl_tree)
    assert expected == current, f"expect:{expected} but get {current}"


def test_rebalance_right_left():
    avl_tree = AVLTree()
    avl_tree.root = input(avl_tree.root, 'Grace', 23789132, 'FINED')    # Grace     = 718135
    avl_tree.root = input(avl_tree.root, 'Samuel', 12345678, 'NONE')    # Samuel    = 1911321512
    avl_tree.root = input(avl_tree.root, 'Nathan', 734963578, 'BORROW') # Nathan    = 141208114

    expected = [['Nathan', 734963578, 'BORROW'], ['Grace', 23789132, 'FINED'], ['Samuel', 12345678, 'NONE']]
    current = to_list_bfs(avl_tree)
    assert expected == current, f"expect:{expected} but get {current}"


def GUI_search():
    avl_tree = AVLTree()
    avl_tree.root = input(avl_tree.root, 'Nathan', 250421218, 'Borrowed')
    avl_tree.root = input(avl_tree.root, 'Minx', 300321416, 'None')
    avl_tree.root = input(avl_tree.root, 'Grace', 800512327, 'Paid')
    avl_tree.root = input(avl_tree.root, 'Jemima', 567834161, 'Borrowed')
    avl_tree.root = input(avl_tree.root, 'Johntor', 458239340, 'Paid')
    avl_tree.root = input(avl_tree.root, 'Ali', 328457239, 'None')
    avl_tree.root = input(avl_tree.root, 'Sanga', 281490812, 'Paid')

    main_window = Tk()
    main_window.title("Membership Record")
    main_window.geometry("270x210")

    first_label = Label(
        main_window, text="Helen-Nathan-Bibliothek \n Karl-Marx-Straβe 66, \n 12043 Berlin,")
    first_label.pack()

    # Entry name
    second_label = Label(main_window, text="   Name                    :    ")
    second_label.place(x=0, y=60)
    result_name = StringVar()
    second_result = Label(main_window, textvariable=result_name)
    second_result.pack(fill="x")
    second_result.place(x=135, y=60)

    # Label account number
    third_label = Label(main_window, text="   Acc number         :     ")
    third_label.place(x=0, y=90)
    result_acc_num = StringVar()
    third_result = Label(main_window, textvariable=result_acc_num)
    third_result.pack(fill="x")
    third_result.place(x=135, y=90)

    # Label status
    fourth_label = Label(main_window, text="   Status                    :  ")
    fourth_label.place(x=0, y=120)
    result_status = StringVar()
    fourth_result = Label(main_window, textvariable=result_status)
    fourth_result.pack(fill="x")
    fourth_result.place(x=135, y=120)

    # iteration
    result_iteration = StringVar()
    iteration_label = Label(main_window, textvariable=result_iteration)
    iteration_label.pack()
    iteration_label.place(x=3, y=180)
    iteration_label.config(width=13)

    # Search Input entry fill
    search_entry = Entry(main_window)
    search_entry.insert(0, "Input")

    def clear_entry(event):
        search_entry.delete(0, END)
    search_entry.bind("<FocusIn>", clear_entry)
    search_entry.pack(fill="x")
    search_entry.place(x=135, y=150)

    # Search Button
    search_button = Button(main_window, text="Search", command=lambda entry=search_entry: search_button_clicked(
        avl_tree, search_entry, result_name, result_acc_num, result_status, result_iteration))
    search_button.pack(fill="x")
    search_button.place(x=5, y=150)
    search_button.config(width=12, height=0)

    main_window.mainloop()


def tests():
    test_rebalance_left_right()
    test_rebalance_right_left()
    GUI_search()


def main():
    pass


if __name__ == '__main__':
    tests()
    main()
