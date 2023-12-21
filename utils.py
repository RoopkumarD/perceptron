import math


def range_to_color(num: float):
    if num > 30 or num < -30:
        raise Exception("Range is between -20 to 20")
    dx = 255 / 60
    val = math.floor((num + 30) * dx)

    return (0, 255 - val, val)


if __name__ == "__main__":
    # n = 1
    # r, g, b = range_to_color(n)
    # print(f"\033[38;2;{r};{g};{b}m{n}\033[0m", end=" ")
    pass
