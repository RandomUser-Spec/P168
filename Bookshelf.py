class Bookshelf:
    def __init__(self, name,author,price,published):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_published = published
    
    def add_Book(self):
        print("Book Name : " + self.book_name)
        print("Book Author : " + self.book_author)
        print("Book Price : "+ str(self.book_price))
        print("Book Published : " + str(self.book_published))
        print("Book Added.")
        
    def years_of_published(self):
        years_of_publishing = 2022 - self.book_published
        print("This book was publish " + str(years_of_publishing) + " years ago")
        
book1 = Bookshelf("One Piece", "Eiichiro Oda", 14.99 , 1997)
book1.add_Book()
book1.years_of_published()

book2 = Bookshelf("Tokyo Ghoul", "Sui Ishida", 12.99, 2011)
book2.add_Book()
book2.years_of_published()

book3 = Bookshelf("The Outsiders", "S.E Hinton", 5.89, 1983)
book3.add_Book()
book3.years_of_published()