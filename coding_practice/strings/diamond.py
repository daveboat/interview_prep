def print_diamond(height):
    assert height % 2 == 1, 'height must be odd'
    assert height >= 1, 'height must be greater than or equal to 1'

    n_stars_max = 2 * (height // 2 + 1) - 1

    for i in range(1, height//2 + 2):
        n_stars = 2 * i - 1
        n_spaces = (n_stars_max - n_stars) // 2
        print(' ' * n_spaces + '*' * n_stars)

    for i in range(height//2 + 2, height + 1):
        n_stars = 2 * (height + 1 - i) - 1
        n_spaces = (n_stars_max - n_stars) // 2
        print(' ' * n_spaces + '*' * n_stars)


if __name__ == '__main__':
    print_diamond(1)
