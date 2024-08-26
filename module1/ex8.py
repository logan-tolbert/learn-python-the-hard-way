formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "thre", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    '"The obstacle in the path becomes the path. Never forget, within \nevery',
    'obstacle is an opprtunity to improve our condition"\n',
    '\t- Ryan Holiday,\n',
    '\tThe Obstacle Is The Way'
))

