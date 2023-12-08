from dataclasses import dataclass
from os import name as os_name
from os import path


if os_name == "nt":
    PATH_SEP = "\\"
else:
    PATH_SEP = "/"


@dataclass
class File:
    """Файл в файловой системе."""
    name: str
    dir: str

    @property
    def extension(self) -> str:
        return "".join(self.name.rsplit(".", 1)[1:])

    def ls(self) -> str:
        return self.dir + PATH_SEP + self.name


class Folder(list):
    """Каталог в файловой системе. Может содержать вложенные каталоги и файлы."""
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add(self, obj):
        self.contents.append(obj)

    def ls(self) -> None:
        print(self.name)
        for obj in self.contents:
            obj.ls()


def ls(*objects: File | Folder) -> None:
    for obj in objects:
        obj.ls()

project_dir = path.abspath(path.dirname(__file__))
file1 = File("file1.txt", project_dir)
folder1 = Folder("folder1")
folder1.add(file1)

with open(file1.ls(), "w") as f:
    f.write(folder1.name)

ls(folder1)