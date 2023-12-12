colors = {
    'RED': 31, 'GREEN': 32, 'YELLOW': 33, 'BLUE': 34, 'NORMAL': 0
}


def c_print(stringi: str = '\n', color: str = 'NORMAL', end: str = ''):
    """
    COLORS: 'RED', 'GREEN', 'YELLOW', 'BLUE', 'NORMAL'
    """
    if type(stringi) == str:
        print(f"\033[{colors[color]}m{stringi}\033[0m", end=end)
    elif type(stringi) == list:
        for i in range(len(stringi)):
            print(f"\033[{colors[color[i]]}m{stringi[i]}\033[0m", end="")
