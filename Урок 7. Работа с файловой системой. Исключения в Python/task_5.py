import os

size = {}


def scan_mem(pth):
    with os.scandir(pth) as files:
        for node in files:
            if os.path.isfile(node):
                mem = 10 ** len(str(os.stat(node).st_size))
                file_extend = os.path.splitext(node)[-1]
                count, extends = size.get(mem, (0, set()))
                extends.add(file_extend)
                count += 1
                size[mem] = (count, extends)
            elif os.path.isdir(node):
                scan_mem(os.path.join(pth, node))


if __name__ == "__main__":
    pth = os.getcwd()
    scan_mem(pth)
    print(size)
