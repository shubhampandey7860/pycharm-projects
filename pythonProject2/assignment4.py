class book:
    def __init__(self):
        self.title=None
        self.author=None
        self.publiser=None
        self.price=None
        self.royalty=None
    def set(self):
        self.title=input('enter title')
        self.price=input('enter price')
        self.royalty=input('enter royalty:')
        self.publiser=input('enter publisher name:')
        self.author=input('enter author:')

    def get(self):
        print(f''' title of book:{self.title}
                   price of book:{self.price}
                   publisher:{self.publiser}
                   author of book:{self.author}
                   royalty:{self.royalty}''')
def main():
    book1=book()
    book1.set()
    book1.get()
main()







# ebook class
class ebook(book):
    def __init__(self):
        self.EPUB=None
        self.PDF=None
        self.MOBl=None
        super().__init__()
    def ebook_format(self):
        pass

