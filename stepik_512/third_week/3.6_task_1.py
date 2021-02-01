from xml.etree import ElementTree


tree = ElementTree.fromstring(input())
result = {"red": 0, "green": 0, "blue": 0}
result[tree.attrib['color']] += 1


def dfs(node, cost):
    result[node.attrib['color']] += cost
    cost += 1
    for el in node:
        dfs(el, cost)
    cost -= 1


for el in tree:
    dfs(el, 2)

print(" ".join(map(lambda x: str(x), result.values())))
