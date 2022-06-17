inp = '010111111111100100101000100110111000101111001001011011000011000'
flip_map = {'0': '1', '1': '0', '.': '.'}


def dig(state):
    if state.count('.') == 0 and state.count('1') % 2 == 0:
        return False

    if all(i == '.' for i in state):
        return True

    for face_up in [idx for idx, i in enumerate(state) if i == '1']:
        temp_state = [flip_map[i] if abs(idx - face_up) == 1 else '.' if idx == face_up else i for idx, i in
                      enumerate(state)]
        winning_moves = dig(temp_state)

        if winning_moves == True:
            return [face_up]

        elif winning_moves:
            return [face_up] + winning_moves


ans = dig(list(inp))

if not ans:
    print('no solution')
else:
    print(' '.join(map(str, ans)))