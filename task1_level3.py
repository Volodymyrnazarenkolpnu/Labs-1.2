"""Lab 3 variant 3 level 3"""

class Node():
    """Binary tree class"""
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def find_parent(root, data1, data2):
    """finding a lowest node that contains both gicen nodes"""
    if root is None:
        return None
    if root.value == data1 or root.value == data2:
        return root
    left_find = find_parent(root.left, data1, data2)
    right_find = find_parent(root.right, data1, data2)
    if left_find and right_find:
        return root
    if left_find:
        return left_find
    else:
        return right_find

def find_max_distance(root):
    ends = []
    def inOrder(root):
        ans = []
        stack = []
        curr = root
        depth = 0
        maxes = []
        counter = 0

        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
                if curr is not None:
                    for el in ends:
                        el[0] += 1
            curr = stack.pop()
            if curr.left is not None:
                for el in ends:
                    if el[1] <= 0:
                        el[0] += 1
                    else:
                        el[0] -= 1
            if curr.left is None and curr.right is None:
                ends.append([0, 0])
                widths = []
                for el in ends:
                    width, _turns = el[0], el[1]
                    widths.append(width)
                maxes.append(max(widths))

            ans.append(curr.value)
            curr = curr.right
            if curr is not None:
                for el in ends:
                    el[1] += 1
                    el[0] += 1
        print(counter)

        return maxes
    maximums = inOrder(root) 
    max_dist = max(maximums)
    return max_dist

root = Node(1)
root.right = Node(3)
root.left = Node(2)
root.left.left = Node(7)
root.left.right = Node(9)
root.right.left = Node(4)
root.right.left.right = Node(5)
root.right.right = Node(6)
root.left.left.left = Node(8)
root.left.right.left = Node(1)
root.left.right.right = Node(8)
root.left.right.right.left = Node(7)
root.left.right.right.right = Node(5)
print(find_max_distance(root))
