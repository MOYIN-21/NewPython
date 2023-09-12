lists = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']


def split(p, letter):
    you = []
    step = 3
    for a in range(step):
        you.append(p[a::3])
    return you


print(split(lists, 3))
