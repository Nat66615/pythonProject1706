class Book:
    def __init__(self, title, author):
        self.a = title
        self.b = author

    def get_title(self):
        return self.a

    def display(self):
        print('Название: ', self.a)
        print('Автор: ', self.b)



class Biblio:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print('Добавлен')

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print('удалил')
        else:
            print('нету')

    def find_book_by_title(self, title):
        for book in self.books:
            if book.a == title:
                return book
        return None


    def display_books(self):
        if self.books:
            for book in self.books:
                print('Название: ', book.a)
        else:
            print('=====')


book = Book('Питон', 'Комаров')
library = Biblio('Академия', 'Челябинск')
library.add_book(book)

library.display_books()

book = library.find_book_by_title('Ихняя учеба да')
if book:
    print(book.get_title())
else:
    print('Евоная книга нет')