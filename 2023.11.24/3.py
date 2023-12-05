from html import HTMLBuilder


class HTMLProfile:
    def __init__(self, name, age, job, email):
        self.name = name
        self.age = age
        self.job = job
        self.email = email
        self.education = []
        self.projects = []
        self.contacts = {}


class CVProfiler(HTMLProfile):
    def __init__(self, name, age, job, email):
        super().__init__(name, age, job, email)

    def add_education(self, place, degree, year):
        super().add_education(place, degree, year)
        return self

    def add_project(self, description):
        super().add_project(description)
        return self

    def add_contact(self, **contacts):
        super().add_contact(contacts)
        return self


class CVProfilerBuilder:
    def __init__(self, name, age, job, email):
        self.builder = HTMLBuilder('html').nested('body')
        self.builder.nested('head').sibling('title', f'{name}: портфолио')
        self.builder.nested('div').sibling('h2', 'Обо мне').sibling('p',\
            f'{name}, {age} лет, {job}, {email}')

    def add_education(self, place, degree, year):
        self.builder.nested('div').sibling('h2', 'Образование')\
        .sibling('p', f'{place}, {degree}, {year}')
        return self

    def add_project(self, title):
        self.builder.nested('div').sibling('h2', 'Проекты').sibling('p', title)
        return self

    def add_contact(self, devianart, telegram):
        self.builder.nested('div').sibling('h2', 'Контакты').sibling("p",\
            f"devianart: {devianart}").sibling("p", f"telegram: {telegram}") 
        return self

    def build(self):
        return self.builder.build()


cv1 = CVProfilerBuilder('Иванов Иван Иванович', 26, 'художник-фрилансер',
        'ivv@abc.de')\
   .add_education('Архитектурная Академия', 'Компьютерный дизайн', 2019)\
   .add_project('Разработка логотипа для компании по производству снеков')\
   .add_contact('ivovuvan_in_art', '@ivovuvan')\
   .build()
print(cv1)