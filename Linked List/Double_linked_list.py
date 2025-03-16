##### FUNCTIONS #####

class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


def append(linked_list, data_input):            
    new_node = Node()
    new_node.data = data_input
    if linked_list.head == None:
        linked_list.head = new_node
        new_node = None
    else:
        current = linked_list.head
        while current.next != None:
            current = current.next
        current.next = new_node
        new_node.prev = current
        new_node = None
    linked_list.size = linked_list.size + 1
    return linked_list


def loop_size(linked_list):
    count = 0
    if linked_list == None:
        return count
    elif linked_list.head == None:
        return count
    else:
        count = 1
        current = linked_list.head
        while current.next != None:
            current = current.next
            count = count + 1
        return count


def size(linked_list):
    return linked_list.size


def get_node(linked_list, index):
    count = 0
    current = linked_list.head
    while count != index:
        current = current.next
        count = count + 1
    return current


def next(node):
    return node.next


def prev(node):
    return node.prev


def insert(linked_list, data_input, index):
    new_node = Node()
    new_node.data = data_input
    count = 0
    current = linked_list.head
    while count != (index-1):
        current = current.next
        count = count + 1
    next_current = current.next
    new_node.next = current.next
    current.next = new_node
    new_node.prev = current
    next_current.prev = new_node
    linked_list.size = linked_list.size + 1
    new_node = None
    return linked_list


def delete(linked_list, data_input):
    if linked_list.head.data == data_input:
        removed_node = linked_list.head
        linked_list.head = linked_list.head.next
        removed_node = None
    else:
        before = linked_list.head
        removed_node = linked_list.head.next
        while removed_node.data != data_input:
            before = before.next
            removed_node = removed_node.next
        before.next = before.next.next
        removed_node = None
    linked_list.size = linked_list.size - 1
    return linked_list


def double_linked_list_to_list(linked_list):
    array = [None]*linked_list.size
    current = linked_list.head
    count = 0
    array[count] = current.data
    while current.next != None:
        current = current.next
        count = count + 1
        array[count] = current.data
    return array


##### TESTS CASE #####


def should_return_append_with_node_in_head():
    linked_list = LinkedList()
    data_1 = 15
    append_1 = append(linked_list, data_1)

    current = append_1.head.data
    expected = data_1

    assert expected == current, f"expect:{expected} but get {current}"


def should_return_append_node_with_enter_try_at_least_once_exit_loop():
    linked_list = LinkedList()
    data_1 = 15
    data_2 = 30
    append_1 = append(linked_list, data_1)
    append_2 = append(append_1, data_2)

    current = append_2.head.next.data
    expected = data_2

    assert expected == current, f"expect:{expected} but get {current}"


def should_return_0_if_linked_list_is_None():
    linked_list = None

    current = loop_size(linked_list)
    expected = 0

    assert expected == current, f"expect:{expected} but get {current}"


def should_return_0_if_linked_list_head_is_None():
    linked_list = LinkedList()

    current = loop_size(linked_list)
    expected = 0

    assert expected == current, f"expect:{expected} but get {current}"


def should_return_size_with_enter_try_at_least_once_exit_loop():
    linked_list = LinkedList()
    data_1 = 15
    data_2 = 30
    append_1 = append(linked_list, data_1)
    append_2 = append(append_1, data_2)

    current = loop_size(append_2)
    expected = 2

    assert expected == current, f"expect:{expected} but get {current}"


def should_return_insert_with_enter_try_at_least_once_exit_loop():
    linked_list = LinkedList()
    data_1 = 5
    data_2 = 10
    data_3 = 15
    append_1 = append(linked_list, data_1)
    append_2 = append(append_1, data_2)
    append_3 = append(append_2, data_3)
    insert_data = 100
    index = 2
    insert_1 = insert(append_3, insert_data, index)

    current = insert_1.head.next.next.data
    expected = 100

    assert expected == current, f"expect:{expected} but get {current}"


def should_return_delete_first_node():
    linked_list = LinkedList()
    data_1 = 5
    data_2 = 10
    data_3 = 15
    append_1 = append(linked_list, data_1)
    append_2 = append(append_1, data_2)
    append_3 = append(append_2, data_3)

    delete_1 = delete(linked_list, data_1)

    current = delete_1.head.data
    expected = 10
    assert expected == current, f"expect:{expected} but get {current}"


def should_return_delete_not_in_first_node_with_enter_try_at_least_once_exit_loop():
    linked_list = LinkedList()
    data_1 = 5
    data_2 = 10
    data_3 = 15
    append_1 = append(linked_list, data_1)
    append_2 = append(append_1, data_2)
    append_3 = append(append_2, data_3)

    delete_1 = delete(linked_list, data_2)

    current = delete_1.head.next.data
    expected = 15
    assert expected == current, f"expect:{expected} but get {current}"


def should_return_linked_list_size():
    linked_list = LinkedList()
    append(linked_list,100)
    append(linked_list,200)
    append(linked_list,300)
    insert(linked_list,500,1)
    delete(linked_list,200)
    delete(linked_list,100)

    current = size(linked_list)
    expected = 2

    assert expected == current, f"expect:{expected} but get {current}"


def should_return_node_with_enter_try_at_least_once_exit_loop():
    linked_list = LinkedList()
    append(linked_list,100)
    append(linked_list,200)
    append(linked_list,300)


    current = get_node(linked_list,1)
    expected = linked_list.head.next

    assert expected == current, f"expect:{expected} but get {current}"    


def should_return_prev_node_from_get_node():
    linked_list = LinkedList()
    append(linked_list,100)
    append(linked_list,200)
    append(linked_list,300)
    node_1 = get_node(linked_list,1)

    current = prev(node_1)
    expected = linked_list.head

    assert expected == current, f"expect:{expected} but get {current}"    


def should_return_next_node_from_get_node():
    linked_list = LinkedList()
    append(linked_list,100)
    append(linked_list,200)
    append(linked_list,300)
    node_1 = get_node(linked_list,1)

    current = next(node_1)
    expected = linked_list.head.next.next

    assert expected == current, f"expect:{expected} but get {current}"    


def should_return_double_linked_list_to_list_with_enter_try_at_least_once_exit_loop():
    linked_list = LinkedList()
    append(linked_list,100)
    append(linked_list,200)
    append(linked_list,300)
    my_list = double_linked_list_to_list(linked_list)

    current = my_list
    expected = [100,200,300]

    assert expected == current, f"expect:{expected} but get {current}"    


def tests():
    print("start tests")
    should_return_append_with_node_in_head()
    should_return_append_node_with_enter_try_at_least_once_exit_loop()
    should_return_0_if_linked_list_is_None()
    should_return_0_if_linked_list_head_is_None()
    should_return_size_with_enter_try_at_least_once_exit_loop()
    should_return_insert_with_enter_try_at_least_once_exit_loop()
    should_return_delete_first_node()
    should_return_delete_not_in_first_node_with_enter_try_at_least_once_exit_loop()
    should_return_linked_list_size()
    should_return_node_with_enter_try_at_least_once_exit_loop()
    should_return_prev_node_from_get_node()
    should_return_next_node_from_get_node()
    should_return_double_linked_list_to_list_with_enter_try_at_least_once_exit_loop()
    print("end tests")


def main():
    pass


if __name__ == '__main__':
    tests()
    main()