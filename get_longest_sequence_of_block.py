def get_lnogest_sequence_of_block(block_colors, favorite_color):
    '''
    time complexity is O(n)
    '''

    curr_length = max_length = 0

    for color in block_colors:
        if color == favorite_color:
            curr_length += 1
        else:
            curr_length = 0

        max_length = max(max_length, curr_length)

    return max_length


print(get_lnogest_sequence_of_block([6, 5, 2, 1, 2, 2, 3, 4, 5, 2], 4))
