#Amine Hammoud, Quentin Weir, Mackenzie Snow, Emory Shantz
#All Functions Defined
#Version 1.0 2021/12/10

from P5_T015_load_dataset import load_dataset

#Function 3
def remove_book(title: str, category: str, dictionary: dict) -> dict:
    """
    The function removes the book specified in the argunment and returns the new dictionary and prints a message stating whether the book was removed successfully or if there was an error.
    >>>remove_book("Antiques Roadkill: A Trash 'n' Treasures Mystery", "Fiction", x)
    {'Fiction': [{'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'page_count': '544', 'language': 'English'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': '4.8', 'publisher': 'Tor Books', 'page_count': '226', 'language': 'English'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': '4.8', 'publisher': 'Hachette UK', 'page_count': '400', 'language': 'English'}, {another element}, ...
    """
    index = 0
    book_removed = False
    while index < len(dictionary[category]):
        for val in dictionary[category][index].values():
            if val == title:
                dictionary[category].remove(dictionary[category][index])
                book_removed = True
        index += 1
    if book_removed == False:
        print("There was an error removing the book. Book not found")
    else:
        print("The book has been removed correctly")
        print(dictionary)
    return dictionary

def get_books_by_author(author:str, newDic:dict)->list:
    """Given the name of the author returns the authors books in a list format and prints the books to the console
   
    >>>get_books_by_author("Arthur Conan Doyle",load_dataset("Google_Books_Dataset.csv"))
        The publisher "Kensington Publishing Corp." has published the following books:
           0- The Memoirs of Sherlock Holmes
    >>>get_books_by_author("NoAut",load_dataset("Google_Books_Dataset.csv"))
        The publisher "NoAut" has published the following books:
    """
    listOfBooksByAut = []
    for bookList in newDic.values(): #iterates through lists of dictionnaries
        for identifier in bookList: #iterates through dictionnaries
            if identifier.get("author") == author:
                listOfBooksByAut += [identifier.get("title")]
    uniqueTitles = list(set(listOfBooksByAut)) #remove copies of same book

    print('The author "{}" has published the following books:'.format(author))
    for i in range(len(uniqueTitles)):
        print("   {}- {}".format(i,uniqueTitles[i]))
    
    return uniqueTitles

#Function 7
def get_books_by_publisher(pub_name: str, dictionary: dict) -> list:
    """
    Returns a list of books' title for the given publisher's name. Additionally, the function prints the books information for that publisher.
    >>>get_books_by_publisher('AMACOM', x)
    The publisher AMACOM has published the following books:
        1 - Marketing (The Brian Tracy Success Library)
        2 - Management (The Brian Tracy Success Library)
        3 - Business Strategy (The Brian Tracy Success Library)
        4 - Personal Success (The Brian Tracy Success Library)
        5 - The Essentials of Finance and Accounting for Nonfinancial Managers
    """
    book_list = []
    for key in dictionary.keys():
        for dic in dictionary[key]:
            for val in dic.values():
                if val == pub_name:
                    if dic['title'] not in book_list:
                        book_list.append(dic['title'])
    print("The publisher",pub_name ,"has published the following books:")
    index = 1
    for x in book_list:
        print('    ', index, "-", x)
        index += 1
    return book_list

#Function 11
def get_books_by_category_and_rate(category: str, rating: int, dictionary: dict) -> list:
    """
    Returns a list of book titles for the given category and rating.
    get_books_by_category_and_rate("Fiction", 4, x)
    The category Fiction and rating 4 has the following books:
     1 - The Painted Man (The Demon Cycle, Book 1)
     2 - Edgedancer: From the Stormlight Archive
     3 - Sword of Destiny: Witcher 2: Tales of the Witcher
     4 - After Anna
     5 - Little Girl Lost: A Lucy Black Thriller
     6 - The Name of the Wind: The Kingkiller Chronicle:, Book 1
     7 - Antiques Con
     8 - Antiques Chop
     9 - 'Salem's Lot
     10 - Killer Blonde
     11 - Antiques Knock-Off
     12 - A Trace of Vice (a Keri Locke Mystery--Book #3)
     13 - Total Control
     14 - And Then There Were None
     15 - The Lord of the Rings: The Fellowship of the Ring, The Two Towers, The Return of the King
     16 - A Feast for Crows (A Song of Ice and Fire, Book 4)
     17 - A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
     18 - The Mysterious Affair at Styles
     19 - The Girl in the Spider's Web: A Lisbeth Salander novel, continuing Stieg Larsson's Millennium Series
     20 - Night of the Bold (Kings and Sorcerers--Book 6)
     21 - A Trace of Crime (a Keri Locke Mystery--Book #4)
     22 - Shantaram
     23 - The Black Box
     24 - The Tower of the Swallow: Witcher 6
     25 - Prince of Thorns (The Broken Empire, Book 1)
     26 - The Vagrant (The Vagrant Trilogy)
     27 - The Weight of Honor (Kings and Sorcerers--Book 3)
     28 - The Memoirs of Sherlock Holmes
     29 - We
     30 - In Dark Company: A Kate Burkholder Short Story
     31 - Chronicle of the Unhewn Throne: (The Emperor's Blades, The Providence of Fire, The Last Mortal Bond)
     32 - The Malady and Other Stories: An Andrzej Sapkowski Sampler
    """
    book_list = []
    for dic in dictionary[category]:
        if dic["rating"] != '':
            if rating <= float(dic["rating"]) < (rating + 1):
                book_list.append(dic["title"])
    print("The category", category ,"and rating", rating ,"has the following books:")
    index = 1
    for x in book_list:
        print('    ', index, '-', x)
        index += 1
    return book_list

#Function 2
def add_book(newDic:dict, book:tuple)->dict:
    """Given existing dictionary, adds a new book with 7 identifiers (title,author,language,publisher,category,rating,pageCount) to the dictionnary
    >>>add_book(case1_dict, (0,'a','b','c',"Fiction",'e','f'))
        The book has been added correctly
        newDic = {[... ,(title:0,author:'a',language:'b',publisher:'c',category:"Fiction",rating:'e',pageCount:'f') ] (What the newDictionnary should look like)
    >>>add_book(case1_dict, (0,'a','b','c'))
        There was an error adding the book
        The inputted dictionnary remains the same.
    """
    book = list(book)
    sBook = {}

    if len(book) != 7:
        print("There was an error adding the book")
    else:

        sBook["title"] = book[0] #append title
        sBook["authors"] = book[1] #append authors
        sBook["language"] = book[2] #append Language
        sBook["publisher"] = book[3] #append Language
        sBook["rating"] = book[5] #append rating
        sBook["pageCount"] = book[6] #append pageCount

        if book[4] not in newDic:
                newDic.setdefault(book[4], [sBook])
        else:
                y = newDic[book[4]]
                y += [sBook]

        if sBook in newDic.get(book[4]):
            print ("The book has been added correctly")
        else: 
            print("There was an error adding the book")
    
    return newDic 

case1_dict = load_dataset('Google_Books_Dataset.csv')

#Function 10
def get_books_by_category(category:str, newDic:dict)->list:
    """Given the name of the category, function returns the books in a list format and prints the books to the console
    >>>get_books_by_category("Fiction",load_dataset("Google_Books_Dataset.csv"))
    The category "Fiction" has published the following books:
       0- The Guardians: The explosive new thriller from international bestseller John Grisham
       1- A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)
       2- The Red Signal: An Agatha Christie Short Story
       3- The Vagrant (The Vagrant Trilogy)
       4- Bring Me Back
       5- The Black Box
       6- The Lord of the Rings: The Fellowship of the Ring, The Two Towers, The Return of the King
       7- Antiques Roadkill: A Trash 'n' Treasures Mystery
       8- Total Control
       9- Little Girl Lost: A Lucy Black Thriller
       10- The Girl in the Spider's Web: A Lisbeth Salander novel, continuing Stieg Larsson's Millennium Series
       11- The Malady and Other Stories: An Andrzej Sapkowski Sampler
       12- Killer Blonde
       13- A Trace of Vice (a Keri Locke Mystery--Book #3)
       14- Chronicle of the Unhewn Throne: (The Emperor's Blades, The Providence of Fire, The Last Mortal Bond)
       15- A Trace of Crime (a Keri Locke Mystery--Book #4)
       16- The Memoirs of Sherlock Holmes
       17- Antiques Con
       18- Antiques Knock-Off
       19- Edgedancer: From the Stormlight Archive
       20- No Mercy: The brand new novel from the Queen of Crime
       21- Night of the Bold (Kings and Sorcerers--Book 6)
       22- Antiques Chop
       23- After Anna
       24- A Feast for Crows (A Song of Ice and Fire, Book 4)
       25- The Weight of Honor (Kings and Sorcerers--Book 3)
       26- 'Salem's Lot
       27- Mrs. Pollifax Unveiled
       28- Final Option: 'The best one yet'
       29- The Tower of the Swallow: Witcher 6
       30- In Dark Company: A Kate Burkholder Short Story
       31- Sword of Destiny: Witcher 2: Tales of the Witcher
       32- The Mysterious Affair at Styles
       33- Prince of Thorns (The Broken Empire, Book 1)
       34- We
       35- The Painted Man (The Demon Cycle, Book 1)
       36- The Name of the Wind: The Kingkiller Chronicle:, Book 1
       37- And Then There Were None
       38- Shantaram
    >>>get_books_by_category("NoCat",load_dataset("Google_Books_Dataset.csv"))
        The category "NoCat" has published the following books:
    """
    listOfBooksByCat = []
    if category in newDic.keys(): #if category in dictionnary
        #print(newDic.get(category))
        for i in newDic.get(category): #Iterate through each dic of that category
            listOfBooksByCat += [i.get("title") ]
            
    uniqueTitles = listOfBooksByCat #remove copies of same book
    #uniqueTitles.sort()
    
    print('The category "{}" has published the following books:'.format(category))
    for i in range(len(uniqueTitles)):
        print("   {}- {}".format(i,uniqueTitles[i]))
    
    return uniqueTitles


#Function 4
def get_books_by_rate(rate: int, bookdict: dict) ->dict:
    """Returns dictionary containing all books in argument dictionary with the argument integer rate
    >>> get_books_by_rate(3,load_dataset('Google_Books_Dataset.csv'))
    {title: "Antiques Roadkill: A Trash 'n' Treasures Mystery" 
    author: " Barbara Allan” 
    language: "English" 
    rating: 3.3 
    publisher: "Kensington Publishing Corp."  
    page Count: 288
    category: "Fiction”}
    {another element}...
    {1:{title: "Antiques Roadkill: A Trash 'n' Treasures Mystery" 
    author: " Barbara Allan” 
    language: "English" 
    rating: 3.3 
    publisher: "Kensington Publishing Corp."  
    page Count: 288
    category: "Fiction”},
    {another element}...}
    >>> get_books_by_rate(6,load_dataset('Google_Books_Dataset.csv'))
    {}
    {}
    """
    booknum = 1
    shelf = {}
    for book in bookdict:
        novel = bookdict[book]
        for i in range(len(novel)):
            info = novel[i]
            if info['rating'] != '':
                if float(info['rating']) >= rate and float(info['rating']) < (rate + 1):
                    info['category'] = book
                    shelf[booknum] = info
                    booknum += 1 
    return shelf
    
#Function 8
def check_category_and_title(title: str, category: str, bookdict: dict) ->bool:
    """Returns bool if the arugment title exists in the argument dictionary with the argument category and prints a message depnding on the bool result
    >>>check_category_and_title("Antiques Roadkill: A Trash 'n' Treasures Mystery","Fiction",load_dataset('Google_Books_Dataset.csv'))
    The category Fiction has the book title Antiques Roadkill: A Trash 'n' Treasures Mystery.
    True
    >>>check_category_and_title("A","Fiction",load_dataset('Google_Books_Dataset.csv'))
    The category Fiction doe not have the book title Antiques Roadkill: A Trash 'n' Treasures Mystery.
    False
    """
    correct = False
    novel = bookdict[category]
    for i in range(len(novel)):
        info = novel[i]        
        if info['title'] == title:
                correct = True
    if correct == True:
        print('The category', category, 'has the book title', title, '.')
    else:
        print('The category', category, 'does not have the book title', title, '.')
    return correct

#Function 12
def get_author_categories(authors: str, bookdict: dict) ->list:
    """Returns list of categories the argument author has been found in from the argument dictionary
    >>>get_author_categories("Barbara Allan",load_dataset('Google_Books_Dataset.csv'))
    The author Barbara Allan has published books under the following categories:
    1 - Fiction
    2 - Detective
    3 - Mystery
    ['Fiction', 'Detective', 'Mystery']
    >>>get_author_categories("Blake Pierce",load_dataset('Google_Books_Dataset.csv'))
    The author Blake Pierce has published books under the following categories:
    1 - Fiction 
    2-  Thrillers 
    3-  Mystery 
    4-  Detective 
    ['Fiction', 'Detective', 'Thrillers', 'Mystery']
    """
    categorlist = []
    for book in bookdict:
        novel = bookdict[book]
        for i in range(len(novel)):
            info = novel[i]        
            if info['author'] == authors:
                categor = book
                if categor not in categorlist:
                    categorlist += [categor]
    print('The author', authors, 'has published books under the following categories:')
    for i in range(len(categorlist)):
        print(i+1, '-', categorlist[i])
    return categorlist

#Function 1
def print_dictionary_category(category: str, dictionary: dict)-> int:
    """
    Returns the number of elements associated for that key
    >>> print_dictionary_category("Fiction", load_dataset("Google_Books_Dataset.csv"))
    39
    >>> print_dictionary_category("Mystery", load_dataset("Google_Books_Dataset.csv"))
    18
    >>> print_dictionary_category("Business", load_dataset("Google_Books_Dataset.csv"))
    20
    """
    number_of_books = 0
    book_list = dictionary.get(category)
    for index in book_list:
        number_of_books += 1
    print('The category ' + category + ' has ' + str(number_of_books) + ' books. This is the list of books in the category ' + category)
    for index in range(len(book_list)):
        print(book_list[index])
    return number_of_books

#Function 5
def find_books_by_title(title: str, dictionary: dict) -> bool:
    """
    Returns True if the book is in the dictionary and False if the book is not in the dictionary
    >>> find_books_by_title("Antiques Roadkill: A Trash 'n' Treasures Mystery", load_dataset("Google_Books_Dataset.csv"))
    True
    >>> find_books_by_title("The Very Hungry Catpillar", load_dataset("Google_Books_Dataset.csv"))
    False
    >>> find_books_by_title("Prince of Thorns (The Broken Empire, Book 1)", load_dataset("Google_Books_Dataset.csv"))
    True
    """
    titles = []
    for key in dictionary:
        book_list = []
        book_list = dictionary.get(key)
        for index in range(len(book_list)):
            titles += [book_list[index].get('title')]
            if title in titles:
                print("The book has been found")
                return True
    print("The book has NOT been found")
    return False

#Function 9
def all_categories_for_book_title(title: str, dictionary: dict) -> list:
    """
    Returns a list of genres the book is associated with
    >>> all_categories_for_book_title("The Memoirs of Sherlock Holmes", load_dataset("Google_Books_Dataset.csv"))
    ['Detective', 'Classics']
    >>>all_categories_for_book_title("The Tower of the Swallow: Witcher 6", load_dataset("Google_Books_Dataset.csv"))
    ['Fiction', Fantasy', 'Epic']
    >>> all_categories_for_book_title("Very Hungry Catpillar", load_dataset("Google_Books_Dataset.csv"))
    []
    """
    genre_list = []
    for key in dictionary:
        book_list = []
        book_list = dictionary.get(key)
        for i in range(len(book_list)):
            titles = [book_list[i].get('title')]
            if title in titles:
                genre_list += [key]
    print("The book title " + title + " has the following categories:")
    for index in range(len(genre_list)):
        number = str(index + 1)
        category = genre_list[index]
        print(number + '-' + category)
    return genre_list

