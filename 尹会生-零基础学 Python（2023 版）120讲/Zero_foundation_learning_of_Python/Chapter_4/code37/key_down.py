from pynput.keyboard import Key, Listener, KeyCode


def on_press(key):
    if key == KeyCode.from_char('w'):
        print('You pressed Key UP.')
    if key == KeyCode.from_char('a'):
        print('You pressed Key A.')
    if key == KeyCode.from_char('d'):
        print('You pressed Key D.')
    if key == KeyCode.from_char('s'):
        print('You pressed Key S.')


with Listener(on_press=on_press) as listener:
    listener.join()
