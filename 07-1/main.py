class DirectoryNode(object):
    def __init__(self, name):
        self.name = name
        self.dirs = []
        self.files = []

    def add_dir(self, name):
        if not any(x.name == name for x in self.dirs):
            self.dirs.append(DirectoryNode(name))

    def add_file(self, name, size):
        if not any(x.name == name for x in self.files):
            self.files.append(FileNode(name, size))

    def size(self):
        file_size = 0
        [file_size := file_size + x.size for x in self.files]

        for dir_node in self.dirs:
            file_size += dir_node.size()

        return file_size

    def get_dir(self, path):
        if len(path) == 0:
            return self
        matching_dirs = list(x for x in self.dirs if x.name == path[0])
        if not len(matching_dirs):
            return None
        next_dir = matching_dirs[0]
        path.pop(0)
        return next_dir.get_dir(path)

    def __str__(self):
        return self.get_dir_string(0)

    def __indent(self, num):
        indent = ''
        for _ in range(0, num):
            indent += ' '
        return indent

    def get_dir_string(self, indent):
        dirstr = self.__indent(indent) + f'{self.name}\n'
        dirstr += self.__indent(indent) + 'Directories:\n'
        for dir_node in self.dirs:
            dirstr += dir_node.get_dir_string(indent + 2)
        dirstr += self.__indent(indent) + 'Files:\n'
        for file_node in self.files:
            dirstr += self.__indent(indent + 2) + f'{file_node.name} {file_node.size}\n'
        return dirstr

class FileNode(object):
    def __init__(self, name, size):
        self.name = name
        self.size = size

def get_flat_dir_sizes(dir_node):
    dir_sizes = [dir_node.size()]
    for child in dir_node.dirs:
        dir_sizes += get_flat_dir_sizes(child)
    return dir_sizes

with open("input.txt") as f:
    lines = f.readlines()

line_index = 0
dirs = DirectoryNode('')

current_dir = ['']

browsing_dir = False
while line_index < len(lines):
    line = lines[line_index].strip()
    if line == '':
        continue

    if browsing_dir and line.startswith('$'):
        browsing_dir = False
    elif browsing_dir:
        content = line.split(' ')
        dir_to_add_to = dirs.get_dir(current_dir[1:])
        if content[0].startswith('dir'):
            dir_to_add_to.add_dir(content[1])
        else:
            dir_to_add_to.add_file(content[1], int(content[0]))

    if line.startswith('$ cd'):
        dirname = line.split(' ')[2]
        if dirname == '/':
            current_dir = ['']
        elif dirname == '..':
            current_dir.pop()
        else:
            current_dir.append(dirname)
    elif line.startswith('$ ls'):
        browsing_dir = True

    line_index += 1

print(sum(x for x in get_flat_dir_sizes(dirs) if x <= 100000))
