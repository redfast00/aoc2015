import re
import json


def recursive_count_no_red(node):
    if isinstance(node, dict):
        if any(v == 'red' for v in node.values()):
            return 0
        return sum(recursive_count_no_red(k) + recursive_count_no_red(v) for k, v in node.items())
    elif isinstance(node, list):
        return sum(recursive_count_no_red(k) for k in node)
    elif isinstance(node, int):
        return node
    else:
        return 0


with open('input') as infile:
    content = infile.read()
    print(sum(int(i) for i in re.findall(r'-?\d+', content)))
    print(recursive_count_no_red(json.loads(content)))
