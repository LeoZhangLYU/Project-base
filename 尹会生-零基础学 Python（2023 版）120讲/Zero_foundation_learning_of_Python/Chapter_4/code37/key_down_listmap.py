from pynput.keyboard import Key, Listener, KeyCode

background = [[0, 0, 0], [0, "x", 0], [0, 0, 0]]
print(background)


def on_press(key):
    if key == KeyCode.from_char("w"):
        for i in range(3):
            for j in range(3):
                if background[i][j] == 'x' and i > 0:
                    background[i - 1][j] = 'x'
                    background[i][j] = 0
                    break

    if key == KeyCode.from_char("s"):
        for i in range(3):
            for j in range(3):
                if background[i][j] == 'x' and i < 2:
                    background[i + 1][j] = 'x'
                    background[i][j] = 0
                    break

    if key == KeyCode.from_char("a"):
        for i in range(3):
            for j in range(3):
                if background[i][j] == 'x' and j > 0:
                    background[i][j - 1] = 'x'
                    background[i][j] = 0
                    break

    if key == KeyCode.from_char("d"):
        for i in range(3):
            for j in range(3):
                if background[i][j] == 'x' and j < 2:
                    background[i][j + 1] = 'x'
                    background[i][j] = 0
                    break

    for i in background:
        print(i)


with Listener(on_press=on_press) as listener:
    listener.join()
