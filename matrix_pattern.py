matrix = [[0,0,1,2],
          [0,2,2,2],
          [2,1,0,1]]

m, n = len(matrix), len(matrix[0])



def is_border(i, j):
    return i == 0 or j == 0 or i == m - 1 or j == n - 1

def is_out_of_border(i, j):
    return i < 0 or j <= 0 or i > m - 1 or j > n - 1

def pattern_generator():
    yield 1
    while True:
        yield 2
        yield 0

def pattern_match(target, expected):
    return target == expected


def find_ones():
    ones = [(i, j) for i in range(m) for j in range(n) if matrix[i][j] == 1]
    return ones

def traverse_disgonally(i, j, direction):
    x, y = direction
    gen = pattern_generator()
    
    best_so_far = 1
    next(gen)
    i += x
    j += y
    
    if is_out_of_border(i, j):
        return best_so_far
    
    while not is_border(i, j) and pattern_match(matrix[i][j], next(gen)):
        best_so_far += 1
        i += x
        j += y
    if is_border(i, j):
        return best_so_far + 1
    return 0

def main():
    ones = find_ones()
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    best_res = 0
    for one in ones:
        for dir in directions:
            x, y = one
            best_res = max(traverse_disgonally(x, y, dir), best_res)
    
    return best_res


print(main())
    