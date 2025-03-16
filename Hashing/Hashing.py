##### Functions #####

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


def hash_order(dictionary, input_array):
    name = dictionary['nama_pemesan']
    first_char_of_num = name[0]
    index = convert_to_num(first_char_of_num)
    return (index % len(input_array))


def hash_recipe(dictionary, input_array):
    index = 0
    recipe_name = dictionary['nama_resep']
    for i in range(len(recipe_name)):
        char_to_num = convert_to_num(recipe_name[i])
        index = index + char_to_num
    return (index % len(input_array))


##### Recipe_Functions ######

def insert_recipe(data, input_array):
    index = hash_recipe(data, input_array)
    if input_array[index] is None:
        input_array[index] = data
        return input_array
    elif None in input_array:
        while index < len(input_array):
            if input_array[index] != None:
                index = ((index+1) % len(input_array))
            else:
                input_array[index] = data
                return input_array
    else:
        return "Full"


def search_recipe(data, input_array):
    index = hash_recipe(data, input_array)
    if input_array[index] == data:
        return f"{data} ada di index ke- {index}"
    elif data in input_array:
        while index < len(input_array):
            if input_array[index] != data:
                index = (index+1) % len(input_array)
            else:
                input_array[index] == data
                return f"{data} ada di index ke- {index}"
    else:
        return "Data is not available"


def delete_recipe(data, input_array):
    index = hash_recipe(data, input_array)
    if input_array[index] == data:
        input_array[index] = None
        return input_array
    elif data in input_array:
        while index < len(input_array):
            if input_array[index] != data:
                index = (index+1) % len(input_array)
            else:
                input_array[index] = None
                return input_array
    else:
        return "Data is not available"


##### Order_Functions #####

def resize(index, old_array):
    lenght_new_array = len(old_array[index])*2
    new_array = [None]*lenght_new_array
    a = 0
    while a < len(old_array):
        new_array[a] = old_array[index][a]
        a = a+1
    old_array[index] = new_array
    return old_array


def insert_order(data, input_array):
    index = hash_order(data, input_array)
    if input_array[index][0] == None:
        input_array[index][0] = data
        return input_array
    elif None in input_array[index]:
        for i in range(len(input_array[index])):
            if input_array[index][i] != None:
                i = (i+1) % len(input_array)
            else:
                input_array[index][i] = data
                return input_array
    else:
        resized_array = resize(index, input_array)
        for i in range(len(resized_array[index])):
            if resized_array[index][i] != None:
                i = (i+1) % len(resized_array)
            else:
                resized_array[index][i] = data
                return resized_array


def search_order(data, input_array):
    index = hash_order(data, input_array)
    if data in input_array[index]:
        return f"{data} ada di index ke- {index}"
    else:
        return "tidak ada"


def delete_order(data, input_array):
    index = hash_order(data, input_array)
    if input_array[index][0] == data:
        input_array[index][0] = None
        return input_array
    elif data in input_array[index]:
        for i in range(len(input_array)):
            if input_array[index][i] != data:
                i = (i+1) % len(input_array)
            else:
                input_array[index][i] = None
                return input_array
    else:
        return "Data is not available"

##### End Functions ######


##### Tests ######

def recipe_should_insert_data_in_right_index():
    recipe = {
        'nama_resep': 'Ayam Goreng',
        'bahan_makanan': ['ayam', 'tepung', 'minyak', 'bawang', 'garam'],
        'tahun_dicatat': '12-2-2000'
    }
    array = [None]*100
    expected = [None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, recipe, None, None, None, None, None, None,   # index 33
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None]
    current = insert_recipe(recipe, array)

    assert expected == current, f"expect:{expected} but get {current}"


def recipe_should_insert_data_in_same_index():
    recipe = {
        'nama_resep': 'Ayam Goreng',
        'bahan_makanan': ['ayam', 'tepung', 'minyak', 'bawang', 'garam'],
        'tahun_dicatat': '12-2-2000'
    }
    recipe_2 = {
        'nama_resep': 'Tahu Bulat',
        'bahan_makanan': ['tahu', 'minyak', 'micin'],
        'tahun_dicatat': '18-12-2018'
    }
    array = [None]*100
    array[33] = recipe

    expected = [None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, recipe, recipe_2, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None]

    current = insert_recipe(recipe_2, array)
    assert expected == current, f"expect:{expected} but get {current}"


def recipe_should_delete_data_in_the_index():
    recipe = {
        'nama_resep': 'Ayam Goreng',
        'bahan_makanan': ['ayam', 'tepung', 'minyak', 'bawang', 'garam'],
        'tahun_dicatat': '12-2-2000'
    }
    array = [None, None, None, None, None, None, None, None, None, None,
             None, None, None, None, None, None, None, None, None, None,
             None, None, None, None, None, None, None, None, None, None,
             None, None, None, recipe, None, None, None, None, None, None,
             None, None, None, None, None, None, None, None, None, None,
             None, None, None, None, None, None, None, None, None, None,
             None, None, None, None, None, None, None, None, None, None,
             None, None, None, None, None, None, None, None, None, None,
             None, None, None, None, None, None, None, None, None, None,
             None, None, None, None, None, None, None, None, None, None]
    expected = [None]*100
    current = delete_recipe(recipe, array)

    assert expected == current, f"expect:{expected} but get {current}"


def recipe_should_return_coallision():
    array = [None]*100
    recipe = {
        'nama_resep': 'Ayam Goreng',
        'bahan_makanan': ['ayam', 'tepung', 'minyak', 'bawang', 'garam'],
        'tahun_dicatat': '12-2-2000'
    }
    recipe_2 = {
        'nama_resep': 'Tahu Bulat',
        'bahan_makanan': ['tahu', 'micin', 'minyak'],
        'tahun_dicatat': '18-12-2018'
    }

    expected = 33 == 33
    current = hash_recipe(recipe, array) == hash_recipe(recipe_2, array)

    assert expected == current, f"expect:{expected} but get {current}"


def order_should_insert_data_in_right_index():
    order = {
        'nama_pemesan': 'Anton',
        'nama_resep': 'Ayam Goreng'
    }
    array = [[None, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None]]

    expected = [[None, None, None, None, None],
                [order, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None]]
    current = insert_order(order, array)

    assert expected == current, f"expect:{expected} but get {current}"


def order_should_insert_data_in_same_index():
    order = {
        'nama_pemesan': 'Anton',
        'nama_resep': 'Ayam Goreng'
    }
    order_2 = {
        'nama_pemesan': 'Fanny',
        'nama_resep': 'Iga Bakar'
    }
    array = [[None, None, None, None, None],
             [order, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None]]

    expected = [[None, None, None, None, None],
                [order, order_2, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None]]
    current = insert_order(order_2, array)

    assert expected == current, f"expect:{expected} but get {current}"


def order_shoud_delete_data_in_the_index():
    order = {
        'nama_pemesan': 'Endang',
        'nama_resep': 'Bebek Bakar'
    }
    array = [[order, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None]]

    expected = [[None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None],
                [None, None, None, None, None]]
    current = delete_order(order, array)

    assert expected == current, f"expect:{expected} but get {current}"


def order_should_return_coallision():
    array = [[None, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None],
             [None, None, None, None, None]]
    order = {
        'nama_pemesan': 'Anton',
        'nama_resep': 'Ayam Goreng'
    }
    order_2 = {
        'nama_pemesan': 'Fanny',
        'nama_resep': 'Iga Bakar'
    }

    expected = 1 == 1
    current = hash_order(order, array) == hash_order(order_2, array)

    assert expected == current, f"expect:{expected} but get {current}"


def tests():
    print("start test")
    recipe_should_insert_data_in_right_index()
    recipe_should_insert_data_in_same_index()
    recipe_should_delete_data_in_the_index()
    recipe_should_return_coallision()
    order_should_insert_data_in_right_index()
    order_should_insert_data_in_same_index()
    order_shoud_delete_data_in_the_index()
    order_should_return_coallision()
    print("end tests")

##### End Tests #####


def main():
    pass


if __name__ == '__main__':
    tests()
    main()