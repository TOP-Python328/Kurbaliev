"""
Модель MVC приложения.
"""

from pathlib import Path
from re import Pattern, compile, IGNORECASE
from sys import path


Pathlike = str | Path


class Email:
    """Описывает модель взаимодействия и хранения email адресов."""
    pattern: Pattern = compile(r'[a-z0-9][\w\.-]*@[a-z0-9][\w\.-]*\.[a-z]{2,}', IGNORECASE)
    
    def __init__(self, email: str):
        self.email = email
    
    @property
    def email(self) -> str:
        """Возвращает значение поля __email."""
        return self.__email
    
    @email.setter
    def email(self, value: str):
        """Проверяет, является ли переданныя строка корректным email адресом, и устанавливает значение поля __email."""
        if self.pattern.fullmatch(value):
            self.__email = value
        else:
            raise ValueError(f'Invalid email address: {value}')


class FileIO:
    default_emails_path: Pathlike = Path(path[0]) / 'emails.txt'

    @classmethod
    def add_email(cls, email: str, file_path: Pathlike = None) -> None:
        """Добавляет значение поля __email в файл."""
        if file_path is None:
            file_path = cls.default_emails_path
        with open(file_path, 'a', encoding='utf-8') as fileout:
            print(email, file=fileout)

