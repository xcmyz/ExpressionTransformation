from module import is_operation


class TNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def PostExpTree(data_or, add_id=False):
    data = data_or.copy()
    cnt = 0
    if not data:
        return
    re = []
    while data:
        cnt += 1
        tmp = data.pop(0)
        if not is_operation(tmp):
            if add_id:
                re.append(TNode(tmp+"_"+str(cnt)))
            else:
                re.append(TNode(tmp))
        else:
            if add_id:
                p = TNode(tmp+"_"+str(cnt))
            else:
                p = TNode(tmp)
            p.right = re.pop()
            p.left = re.pop()
            re.append(p)

    return re.pop()


def front_digui(root):
    if root == None:
        return
    print(root.val, end="")
    front_digui(root.left)
    front_digui(root.right)
