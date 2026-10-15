class Publication:
    def __init__(self, title, author):  # in this part we are initializing the title and author of the publication privately with the double underscore]
        self.title = title              
        self.author = author

    def get_title(self):       #thisa is getter for the title of the publication
        return f"Title: {self.__title}"
    
    def get_author(self):           #this is the getter for the author of the publication
        return f"Author: {self.__author}"
    
    def set_title(self, title):       # this is the setter for the title of the publication
        self.__title = title

    def set_author(self, author):       #setter for the author of the publication
        self.__author = author
        
    def display_info(self):         #display info method to display the title and author of the publication
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        
 class Book(Publication):       # this is the book class from the publication class
    def __init__(self, title, author, number_pages):     #defining the ook class that takes the title, author, and number of pages
        Publication.__init__(self, title, author)    
        self.__number_pages = 0
        self.set_number_pages(number_pages)
        
    def get_number_pages(self):        #getter for the number of pages in the book
        return f"Number of Pages: {self.__number_pages}"
    
    def set_number_pages(self, number_pages):      #setter for the number of pages in the book
        if number_pages >= 0:
            self.__number_pages = number_pages      #here we are checking to make sure the number of pages is not negative and if it is not then it will set the number of pages to the value given
        else:
            print("Number of pages must be a non-negative value (positive integer).")
            
    def display_info(self):
        print(f"Title: {self.__title}")    # display info method to display the title, author, and number of pages in the book
        print(f"Author: {self.__author}")
        print(f"Number of Pages: {self.__number_pages}")
        
class Magazine(Publication):     # this is the magazine class from the publication class
    def __init__(self, title, author, issue_number):    #defining the magazine class that takes the title, author, and issue number of  amagazine
        Publication.__init__(self, title, author)    
        self.__issue_number = 0        # initializing the issue number to 0
        self.set_issue_number(issue_number)     # 
        
    def get_issue_number(self):     #getter for the issue number of the magazine
        return f"Issue Number: {self.__issue_number}"
    
    def set_issue_number(self, issue_number):      #setter for the issue number of the magazine
        if issue_number >= 0:
            self.__issue_number = issue_number      #checking to make sure the issue number is not negative and if it is not then it will set the issue number to the value given
        else:
            print("Issue number must be a non-negative value (positive integer).")
            
    def display_info(self):       #display info method to display the title, author, and issue number of the magazine
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Issue Number: {self.__issue_number}")
        
pub1 = Publication("Journey of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")    #creating an object for the publication class with the title and author of the publication
pub2 = Publication("Science Today", "Various Authors")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)       #creating an object for the book class with the title, author, and no. of pages of the book
book2 = Book("Harry Potter", "J.K. Rowling", 350)
mag1 = Magazine("National Geographic", "Various Authors", 202)      #creating an object for the magazine class with the title, author, and issue no. of the magazine
mag2 = Magazine("Science Monthly", "Various Authors", 15)

print("\nPublication Information:")    # displaying information for the publication objects
pub1.display_info()
pub2.display_info()

print("\nBook Information:")    # displaying information for the book objects
book1.display_info()
book2.display_info()

print("\nMagazine Information:")    #displaying information for the magazine objects
mag1.display_info()
mag2.display_info()




