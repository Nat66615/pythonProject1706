class Book:
    def __init__(self,
                 title,
                 year,
                 publisher,
                 genre,
                 author,
                 price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price


    def display(self):
        print(
            'Автор: ', self.author, '\n'
            'Название: ', self.title, '\n'
            'Цена: ', self.price
        )


    def get_title(self):
        return self.title

book = Book('Python23', # поля можно заменить на инпуты
            2023,
            'Академия ТОП г.Челябинск',
            'Драма',
            'Комаров А.Н.',
            9500)

book.display()
book.get_title()

# while True:
#     choice = input(
#         '1 - показать каталог\n'
#         '2 - название'
#     )
#     if choice == '1':
#         book.display()
#     if choice == '2':
#         print(book.get_title())
