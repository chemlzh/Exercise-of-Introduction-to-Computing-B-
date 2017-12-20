from functools import reduce

def judge(x):
    if 'height' in x:
        return x['height']
    else:
        return 0


people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
height_total = reduce(lambda x, y: x + y, map(judge, people))
height_count = len(list(filter(judge, people)))
if height_count > 0:
    average_height = height_total / height_count