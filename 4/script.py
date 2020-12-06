import re


def proc_int(cb=None):
    def inner(x):
        try:
            x = int(x)
        except ValueError:
            return False

        if cb is not None:
            return cb(x)
        return True

    return inner


def proc_substring(cb, start=None, end=None):
    def inner(x):
        return cb(x[(start if start is not None else 0):(end if end is not None else 10000000)])

    return inner


def require_range(lower, upper, cb=None):
    def inner(x):
        if x not in range(lower, upper + 1):
            return False
        elif cb is not None:
            return cb(x)
        return True

    return proc_int(inner)


def require_startswith(suffix):
    def inner(x):
        return x.startswith(suffix)

    return inner


def require_endswith(suffix):
    def inner(x):
        return x.endswith(suffix)

    return inner


def require_length(length):
    def inner(x):
        return len(x) == length

    return inner


def require_match(value):
    def inner(x):
        return x == value

    return inner


def require_regex(pattern):
    def inner(x):
        return bool(re.match(pattern, x))

    return inner


def require_contains(values):
    def inner(x):
        return x in values

    return inner


def cond_or(tests):
    def inner(x):
        for test in tests:
            if test(x):
                return True
        return False

    return inner


def cond_and(tests):
    def inner(x):
        for test in tests:
            if not test(x):
                return False
        return True

    return inner


validators = {
    'byr': cond_and([require_length(4), require_range(1920, 2002)]),
    'iyr': cond_and([require_length(4), require_range(2010, 2020)]),
    'eyr': cond_and([require_length(4), require_range(2020, 2030)]),
    'hgt': cond_or([
        cond_and([require_endswith('cm'), proc_substring(
            require_range(150, 193), end=-2)]),
        cond_and([require_endswith('in'), proc_substring(
            require_range(59, 76), end=-2)]),
    ]),
    'hcl': cond_and([proc_substring(require_match('#'), end=1),
                     proc_substring(require_regex(r'[0-9a-f]{6}'), start=1),
                     require_length(7)]),
    'ecl': cond_and([require_length(3),
                     require_contains(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])]),
    'pid': cond_and([require_length(9),
                     require_regex(r'[0-9]{9}')]),
}


def validate(data, debug=False):
    entries = data.split(' ')
    data = {}
    for entry in entries:
        key = entry[:3]
        value = entry[4:]
        data[key] = value

    for key in validators:
        if key not in data:
            debug and print('Failed: missing', key)
            return False

        value = data[key]
        result = validators[key](value)
        if not result:
            debug and print('Failed', key, value)
            return False
        debug and print('Passed', key, value)

    debug and print('Passed')
    return True


if __name__ == '__main__':
    with open('input', 'r') as file:
        input = [line.strip() for line in file]

    valid = 0
    cache = ''
    for line in input:
        if len(line) == 0:
            print('passport:', cache)
            if validate(cache.strip(), debug=True):
                valid += 1
            cache = ''
        else:
            cache += line + ' '
    if validate(cache.strip(), debug=True):
        valid += 1

    print(valid)
