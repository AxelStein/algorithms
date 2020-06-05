def create_phone_number(arr):
    out = ['(']
    for i in range(len(arr)):
        out.append(str(arr[i]))
        if i == 2:
            out.append(') ')
        elif i == 5:
            out.append('-')
    return ''.join(out)


def create_phone_number_2(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


def create_phone_number_3(n):
    n = ''.join(map(str, n))
    return '(%s) %s-%s' % (n[:3], n[3:6], n[6:])


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(create_phone_number(arr))
print(create_phone_number_2(arr))
print(create_phone_number_3(arr))
