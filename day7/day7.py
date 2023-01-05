import re
from functools import reduce
from typing import List

with open("./data.txt") as f:
    lines = f.readlines()


class File:
    def __init__(self, size: int, name: str):
        self.size = size
        self.name = name


class Directory:
    def __init__(self, name: str):
        self.children: List[Directory] = []
        self.parent: Directory = None
        self.files: List[File] = []
        self.own_size: int = 0
        self.name: str = name
        self.size: int = 0

    def add_children_directory(self, directory: 'Directory'):
        self.children.append(directory)

    def add_file(self, file: File):
        self.files.append(file)

    def add_parent(self, directory: 'Directory'):
        self.parent = directory

    def __calculate_own_size(self):
        self.own_size = reduce(lambda a, b: a + b.size, self.files, 0)

    def calculate_size(self):
        if self.own_size == 0:
            self.__calculate_own_size()
        if self.size == 0:
            self.size = reduce(lambda a, b: a + b.calculate_size(), self.children, 0)
        return self.size + self.own_size

    def traverse(self, fn):
        result = []
        for directory in self.children:
            result.extend(directory.traverse(fn))
        result.append(fn(self))
        return result


class DirectoryTree:
    def __init__(self, console_output: List[str]):
        self.root = None
        self.console_output = console_output
        self.pointer = None

    def process_file(self):
        for output in self.console_output:
            output = output.strip('\n')
            if output.startswith('$ ls'):
                continue
            elif output.startswith('$ cd'):
                self.__change_directory(output)
            elif output.startswith('dir'):
                continue
            else:
                self.__process_file_output(output)
        self.pointer = self.root

    def __change_directory(self, command: str):
        name = command.replace('$ cd ', '')
        if name == '/':
            self.root = Directory(name)
            self.pointer = self.root
            return
        elif name == '..':
            self.pointer = self.pointer.parent
            return
        child = Directory(name)
        child.add_parent(self.pointer)
        self.pointer.add_children_directory(child)
        self.pointer = child

    def __process_file_output(self, command: str):
        file_info = command.split(' ')
        file = File(int(file_info[0]), file_info[1])
        self.pointer.add_file(file)


def get_size(dir: Directory):
    if dir.parent:
        return dir.calculate_size()
    else:
        return 0

tree = DirectoryTree(lines)
tree.process_file()
sum = 0
for size in tree.root.traverse(get_size):
    if size < 100000:
        sum += size
print(sum)

max_size = 70000000
min_free_size = 30000000
current_size = tree.root.calculate_size()
size_to_delete = min_free_size
for size in tree.root.traverse(get_size):
    if max_size - current_size + size > min_free_size and size_to_delete > size:
        size_to_delete = size
print(size_to_delete)
