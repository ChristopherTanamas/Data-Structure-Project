class Node:
    def __init__(self):
        self.data = None
        self.prev = None
        self.next = None
        self.priority = None

class DobubleLinkedListQueue:
    def __init__(self):
        self.head = None
        # to get O(1) for deque
        self.tail = None


##### FUNCTIONS #####


def deque(_queue: DobubleLinkedListQueue):
    current = _queue.head
    _queue.head = _queue.head.next
    _queue.head.prev = None
    current.next = None

    return current.data


def enque(_queue, data):
    new_node = Node()
    new_node.data = data
    if _queue.head == None:
        _queue.head = new_node
        _queue.tail = new_node
    else:
        _queue.tail.next = new_node
        new_node.prev = _queue.tail
        _queue.tail = new_node
    new_node = None
    return _queue


def queue_to_list(_queue):
    temp_list = []
    current = _queue.head
    while current != None:
        temp_list.append(current.data)
        current = current.next
    return temp_list


##### TEST CASE #####


def should_return_list_1_2_3():
    q = DobubleLinkedListQueue()
    q_10 = enque(q, 10)
    q_10_20 = enque(q_10, 20)
    q_10_20_30 = enque(q_10_20, 30)

    assert [10, 20, 30] == queue_to_list(q_10_20_30)


def should_return_queue_consist_10():
    q = DobubleLinkedListQueue()
    queue_10 = enque(q, 10)

    assert [10] == queue_to_list(queue_10)


def should_return_10():
    q = DobubleLinkedListQueue()
    queue_10 = enque(q,10)
    queue_10_20 = enque(queue_10,20)

    assert 10 == deque(queue_10_20)


def tests():
    print("start tests")
    should_return_list_1_2_3()
    should_return_queue_consist_10()
    should_return_10()
    print("end tests")


def main():
    pass


if __name__ == '__main__':
    tests()
    main()
