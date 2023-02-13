
def img2ascii(img_data, black = '#', white = '.') -> str:
    '''
    >>> img = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ])
    >>> img2ascii(img)
    '..........\n..######..\n.##....##.\n.#......#.\n.#......#.\n.#......#.\n.#......#.\n.##....##.\n..######..\n..........'
    >>> print(img2ascii(img))
    ..........
    ..######..
    .##....##.
    .#......#.
    .#......#.
    .#......#.
    .#......#.
    .##....##.
    ..######..
    ..........
    '''

    return '\n'.join([''.join([white if pixel == 0 else black for pixel in line]) for line in img_data])

img = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

ascii = img2ascii(img)
print(repr(ascii))
print(ascii)



'''if __name__ =='__main__':
    import doctest
    doctest.testmod()
    '''
tests = [
    '..........\n..######..\n.##....##.\n.#......#.\n.#......#.\n.#......#.\n.#......#.\n.##....##.\n..######..\n..........',
    '          \n  OOOOOO  \n OO    OO \n O      O \n O      O \n O      O \n O      O \n OO    OO \n  OOOOOO  \n          ',

    ]

if tests[0] == img2ascii(img):
    print('bien !!!')
if tests[1] == img2ascii(img, 'O', ' '):
    print('tout de bien')