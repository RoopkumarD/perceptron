# reference https://bsouthga.dev/posts/color-gradients-with-python

fact_cache = dict()


def factorial(n):
    try:
        return fact_cache[n]
    except KeyError:
        if n == 0 or n == 1:
            result = 1
        else:
            result = n * factorial(n - 1)

        fact_cache[n] = result
        return result


def bernstein(t, n, i):
    binom = factorial(n) / float(factorial(i) * factorial(n - i))
    return binom * ((1 - t) ** (n - i)) * (t**i)


def bezier_gradient(num: float, lowest_num: float, biggest_num: float):
    # purple -> yellow
    colors_stops = [
        [41, 4, 69],
        [28, 97, 130],
        [15, 145, 128],
        [50, 181, 101],
        [246, 226, 16],
    ]

    n = len(colors_stops) - 1

    def bezier_interp(t):
        # List of all summands
        summands = [
            list(map(lambda x: int(bernstein(t, n, i) * x), c))
            for i, c in enumerate(colors_stops)
        ]
        # Output color
        out = [0, 0, 0]
        # Add components of each summand together
        for vector in summands:
            for c in range(3):
                out[c] += vector[c]

        return out

    color = bezier_interp((num - lowest_num) / (biggest_num - lowest_num))
    return color


if __name__ == "__main__":
    # g = bezier_gradient()
    # for color in g:
    #     r, g, b = color
    #     print(f"\033[38;2;{r};{g};{b}m{color}\033[0m")
    pass
