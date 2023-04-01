from capitalize import capitalize

if (capitalize('hello')) != 'Hello':
    raise Exception('did not work!')

if (capitalize('')) != '':
    raise Exception('did not work!')

print('All tests are done')
