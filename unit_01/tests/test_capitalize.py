from unit_01.capitalize import capitalize


if capitalize('hello world!') != 'Hello world!':
    raise Exception('Error!')

if capitalize('') != '':
    raise Exception('Error!')

if capitalize('hello world!') == 'Hello world!':
    print('Ok!')

print('Done')
