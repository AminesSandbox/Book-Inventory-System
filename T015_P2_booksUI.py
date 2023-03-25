#Amine Hammoud 101220672, Emory Shantz, 101221942, Quentin Weir 101234808 & MacKenzie Snow 101146941
#Version 1.0 2021/12/10

#Importing statements
import csv
from T015_P2_search_modify_dataset import *
from P5_T015_load_dataset import *
from T015_P3_sorting import *

#Constants
COMMANDS = ['Q', 'L', 'R', 'F', 'NC', 'CA', 'CB', 'G', 'S','A']
MENU = '1- Command Line L)oad file \n2- Command Line A)dd book \n3- Command Line R)emove book \n4- Command Line F)ind book by title \n5- Command Line NC) Number of books in a category \n6- Command Line CA) Categories for an author \n7- Command Line CB) Categories for a book title \n8- Command Line G)et book \n    R)ate   A)uthor   P)ublisher   C)ategory\n    CT) Category and Title    CR) Category and Rate \n9- Command Line S)ort book \n    T)itle    R)ate    P)ublisher    C)ategory    PA)ageCount \n10- Command line Q)uit \n'

#Amine Hamoud Consts
FUNCDIC1 = {"R":get_books_by_rate,"A":get_books_by_author,"P":get_books_by_publisher,"C": get_books_by_category}
FUNCDIC2 = {"CT":check_category_and_title, "CR":get_books_by_category_and_rate}

def caseG(library)->None:
    """SubMenu for case 3 which finds books using filters"""
    inp = 0

    argList = []
    print(MENU)
    getMethod = 0

    getMethod = input("<GetBooksBy?>: ").upper()
    
    if getMethod == 'Q':
        return
    
    func = FUNCDIC1.get(getMethod) 
    args = 1
    
    if func == None:
        args = 2
        func = FUNCDIC2.get(getMethod) 
    
    if func == None:
        args = 0
        print("No such command")
    
    if func == get_books_by_category_and_rate:
        argList+= [input("Category: ".format(1))]
        argList+= [float(input("Rating: ".format(1)))]
        func(argList[0],argList[1],library)
        
    elif func == check_category_and_title:
        argList+= [input("Title: ".format(1))]
        argList+= [input("Category: ".format(1))]
        func(argList[0],argList[1],library)
        
    elif args == 1:
        if func == get_books_by_rate:
            argList+= [func(float(input("Rating: ".format(1))), library)]
            print(argList)
        else:
            argList+= func(input("argument {0} for parameter: ".format(1)), library)    
 
def caseS(library)->None:
    """SubMenu for case 4 which sorts books using filters"""
    
    callsub = input("Please enter how it will be sorted: ").upper()
    if callsub == "T":
        title = sort_books_title(library)
        print(title)
    elif callsub == "R":
        rate = input("Please enter A)scending or D)escending: ").upper()
        if rate == "A":
            arate = sort_books_ascending_rate(library)
        elif rate == "D":
            drate = sort_books_descending_rate(library)
        elif rate != "Q":
            print("No such command")
    elif callsub == "P":
        publish = sort_books_publisher(library)
    elif callsub == "C":
        category = sort_books_category(library)
    elif callsub == "PA":
        pagecount = sort_books_pageCount(library)          
    elif callsub != 'Q':
        print("No such command")
        callsub = input("Please enter how it will be sorted: ").upper()
    elif callsub == 'Q':
        return        

def mainMenu():
    """Grabs User input and redericts the user to the according function"""
    
    #Orginial Identfiction of variables
    userinput = True
    file_loaded = ''
    isFileLoaded = False    
    print(MENU)
    
    while userinput != 'Q':#Creates a while loop that runs as long as the users input is not Q
        
        userinput = input("Please enter a string (Q to quit): ").upper()
        print(userinput)
        print('')     
        
        if userinput not in COMMANDS:
            print('No such command')
            print('')
            print(MENU)
        
        if userinput == 'L':
            file_loaded = input('Please enter a file: ')
            library = load_dataset(file_loaded)
            print(library)
            isFileLoaded = True  
                    
        elif isFileLoaded:
            if userinput == 'A':    
                lst_info_book = input('Input the book info as a list in the order: title,author,language,publisher,genre,rating,page_count: ').split(",")
                library = add_book(library, tuple(lst_info_book))
                
            elif userinput == 'R':
                title = input('Please enter the title of the book you want to remove: ')
                category = input('Please enter the catergory of the book you want to remove: ')
        
                library = remove_book(title, category, library)
                
            elif userinput == 'F':
                title = input('Please input the title of the book you want to find: ')
                find_books_by_title(title, library)
        
            elif userinput == 'NC':
                cat = input("Please enter a category: ")
                if cat not in library: #if the category exists
                    print(cat, "does not exist, no books in the dataset")
                else:
                    print("The number of books in", cat, "is", print_dictionary_category(cat, library))
                
            elif userinput == 'CA':
                auth = input("Please enter an author: ")
                if get_author_categories(auth, library) == []: #if the author has no categories
                    print(auth, "has no categories")
                else:
                    print("Categories by", auth, "are", ', '.join([str(elem) for elem in get_author_categories(auth, library)]))
                
            elif userinput == 'CB':
                title = input("Please enter a title: ")
                bookList = all_categories_for_book_title(title, library)
                if bookList == []: #if the author has no categories
                    print(title, "has no categories")
                else:
                    print("Categories associated with", title ,"include:", ', '.join([str(elem) for elem in bookList]))
        
            elif userinput == 'G':
                caseG(library)
                            
            elif userinput == 'S':
                caseS(library)
            
        else:
            print('No file loaded ')
            print('')
            print(MENU)    
    

#Main Script           
mainMenu()