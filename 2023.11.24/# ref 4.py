from dataclasses import dataclass
from os import name as os_name


if os_name == 'nt':
    PATH_SEP = '\\'
else:
    PATH_SEP = '/'


@dataclass
class File:
    """Файл в файловой системе."""
    name: str
    dir: str
    
    @property
    def extension(self) -> str:
        return ''.join(self.name.rsplit('.', 1)[1:])
    
    def ls(self) -> str:
        return self.dir_path + PATH_SEP + self.name


class Folder(list):
    """Каталог в файловой системе. Может содержать вложенные каталоги и файлы."""


def ls(*objects: File | Folder) -> str:
    for obj in objects:
        print(obj.ls())

