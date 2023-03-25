#Amine Hammoud 101220672, Emory Shantz, 101221942, Quentin Weir 101234808 & MacKenzie Snow 101146941
#Version 1.0 2021/12/10

from P5_T015_load_dataset import load_dataset

def refactoring(dictlist: dict) ->list:
    """Returns list containg the rearranged argument dictionary
    >>> refactoring(load_dataset('Google_Books_Dataset.csv'))
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288, 'language': 'English', 'genre': 'Fiction'}, {another element}, ...]
    """
    lBook = list(dictlist.items())
    newList = []
    for tup in lBook: #Creates a list of all the dictionnaries
        genre = tup[0]
        for dic in tup[1]:
            dic["generes"]=genre
            x = dic["rating"]
            if x == '':
                x = '0.0'
            else:
                dic["rating"] = str(x)
            x = dic["page_count"]
            dic["page_count"] = int(x)
            newList.append(dic)
    return newList


#function 
def sort_books_title(nDic:dict)->list:
    """Given a dictionnary, return a list of the dictionnary with the titles sorted in alphabetical order
    
    >>>sort_books_title(load_dataset("3books.csv"))
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288, 'language': 'English', 'genre': 'Fiction'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'page_count': 226, 'language': 'English', 'genre': 'Horror'}, {'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 544, 'language': 'English', 'genre': 'Horror'}]

    >>>sort_books_title(load_dataset("10books.csv"))
    [{'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 4544, 'language': 'English', 'genre': 'Adventure'}, {'title': 'A Trace of Crime (a Keri Locke Mystery--Book #4)', 'author': 'Blake Pierce', 'rating': 4.7, 'publisher': 'Blake Pierce', 'page_count': 250, 'language': 'English', 'genre': 'Mystery'}, {'title': 'A Trace of Crime (a Keri Locke Mystery--Book #4)', 'author': 'Blake Pierce', 'rating': 4.7, 'publisher': 'Blake Pierce', 'page_count': 250, 'language': 'English', 'genre': 'Detective'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': 4.6, 'publisher': 'HarperCollins UK', 'page_count': 224, 'language': 'English', 'genre': 'Mystery'}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'rating': 4.6, 'publisher': 'Crown Business', 'page_count': 464, 'language': 'English', 'genre': 'Biography'}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'rating': 4.3, 'publisher': 'Minotaur Books', 'page_count': 60, 'language': 'English', 'genre': 'Fiction'}, {'title': 'Permanent Record', 'author': 'Edward Snowden', 'rating': 4.6, 'publisher': 'Metropolitan Books', 'page_count': 352, 'language': 'English', 'genre': 'Biography'}, {'title': 'Personal Success (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': '', 'publisher': 'AMACOM', 'page_count': 112, 'language': 'English', 'genre': 'Economics'}, {'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': '', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'page_count': 14, 'language': 'English', 'genre': 'Business'}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel, continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'rating': 4.1, 'publisher': 'Vintage Crime/Black Lizard', 'page_count': 416, 'language': 'English', 'genre': 'Mystery'}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'rating': 4.3, 'publisher': 'Pan', 'page_count': 226, 'language': 'English', 'genre': 'Fantasy'}]


    >>>sort_books_title(load_dataset("15books.csv"))
    [{'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'page_count': 416, 'language': 'English', 'genre': 'Fiction'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288, 'language': 'English', 'genre': 'Fiction'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'page_count': 368, 'language': 'English', 'genre': 'Fiction'}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'page_count': 96, 'language': 'English', 'genre': 'Comics'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'page_count': 226, 'language': 'English', 'genre': 'Fiction'}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'page_count': 320, 'language': 'English', 'genre': 'Economics'}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'page_count': 320, 'language': 'English', 'genre': 'Psychology'}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'page_count': 176, 'language': 'English', 'genre': 'Business'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'page_count': 336, 'language': 'English', 'genre': 'Fiction'}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': '', 'publisher': 'AMACOM', 'page_count': 112, 'language': 'English', 'genre': 'Economics'}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'page_count': 224, 'language': 'English', 'genre': 'Business'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'page_count': 400, 'language': 'English', 'genre': 'Fiction'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': '', 'publisher': 'Hachette UK', 'page_count': 384, 'language': 'English', 'genre': 'Fiction'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'page_count': 320, 'language': 'English', 'genre': 'Detective'}, {'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 544, 'language': 'English', 'genre': 'Fiction'}]

    """
    newList = refactoring(nDic)
    for i in range(len(newList)-1):#bubble sort algorithm
        for j in range(len(newList)-i-1):
            if newList[j].get("title") > newList[j+1].get("title"):
                newList[j], newList[j+1] = newList[j+1], newList[j]    
    return newList

#Function Sort books by ascending rate

def sort_books_ascending_rate(dictionary: dict) -> list:
    """Returns a list that contains the books in descending order based on rating
    >>> sort_books_ascending_rate(load_dataset('Google_Books_Dataset.csv'))
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 0.0, 'publisher': 'Kensington Publishing Corp.', 'genres': 'Fiction', 'page_count': 288}, {another element}, ...
    >>> sort_books_ascending_rate(load_dataset('Unsorted_Data_Set.csv'))
    [{'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'language': 'English', 'rating': 0.0, 'publisher': 'Hachette UK', 'genres': 'Thrillers', 'page_count': 416}, {another element}, ...
    >>> sort_books_ascending_rate(load_dataset('10books.csv'))
    [{'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': 0.0, 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'page_count': 14, 'generes': 'Business', 'language': 'English'},, {another element}, ...
    """
    booklist = refactoring(dictionary)
    n = len(booklist)
    for i in range(n):
        for j in range(0, n-i-1):
            if booklist[j]['rating'] > booklist[j+1]['rating']:
                booklist[j], booklist[j+1]= booklist[j+1], booklist[j]
    for index in range(n):
        print(booklist[index])
    return booklist

#Function Sort books by descending rate

def sort_books_descending_rate(dictionary: dict) -> list:
    """
    Returns a list that contains the books in descending order based on rating
    >>>sort_book_descending_rate(load_dataset('Google_Books_Dataset.csv'))
    [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'language': 'English', 'rating': 5.0, 'publisher': 'Kensington Publishing Corp.', 'genres': 'Fiction', 'page_count': 288}, {another element}, ...
    >>> sort_books_descending_rate(load_dataset('Unsorted_Data_Set.csv'))
    [[{'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'page_count': 96, 'generes': 'Fiction', 'language': 'English'}, {another element}, ...
    >>>sort_books_descending_rate(load_dataset(10books.csv))
    [{'title': 'A Trace of Crime (a Keri Locke Mystery--Book #4)', 'author': 'Blake Pierce', 'rating': 4.7, 'publisher': 'Blake Pierce', 'page_count': 250, 'generes': 'Mystery', 'language': 'English'}, ...
    """
    booklist = refactoring(dictionary)
    n = len(booklist)
    for i in range(n):
        for j in range(0, n-i-1):
            if booklist[j]['rating'] < booklist[j+1]['rating']:
                booklist[j], booklist[j+1] = booklist[j+1], booklist[j]
    for index in range(n):
        print(booklist[index])
    return booklist

#function 6
def sort_books_category(bookcollect: dict) ->list:
    """Returns a list with each book sorted ALPHABETically by generes from the argument dictionary
    >>> sort_books_category(load_dataset('Unsorted_Data_Set.csv'))
    [{'title': 'Antiques Con', 'author': 'Barbara Allan', 'rating': '4.8', 'publisher': 'Kensington Books', 'page_count': '288', 'language': 'English', 'generes': 'Detective'}, {'title': 'Homecoming (A Chloe Fine Psychological Suspense Mystery—Book 5)', 'author': 'Blake Pierce', 'rating': '4.6', 'publisher': 'Blake Pierce', 'page_count': '250', 'language': 'English', 'generes': 'Detective'}, {'title': 'Platform: Get Noticed in a Noisy World', 'author': 'Michael Hyatt', 'rating': '4.6', 'publisher': 'HarperCollins Leadership', 'page_count': '288', 'language': 'English', 'generes': 'Economics'}, {'title': "Chronicle of the Unhewn Throne: (The Emperor's Blades, The Providence of Fire, The Last Mortal Bond)", 'author': 'Brian Staveley', 'rating': '4.3', 'publisher': 'Macmillan', 'page_count': '1728', 'language': 'English', 'generes': 'Fantasy'}, {'title': 'The Malady and Other Stories: An Andrzej Sapkowski Sampler', 'author': 'Andrzej Sapkowski', 'rating': '4.8', 'publisher': 'Hachette UK', 'page_count': '96', 'language': 'English', 'generes': 'Fiction'}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'rating': '4.3', 'publisher': 'Pan', 'page_count': '226', 'language': 'English', 'generes': 'Fiction'}, {'title': 'Twas The Nightshift Before Christmas: Festive hospital diaries from the author of million-copy hit This is Going to Hurt', 'author': 'Adam Kay', 'rating': '4.7', 'publisher': 'Pan Macmillan', 'page_count': '112', 'language': 'English', 'generes': 'Humor'}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'rating': '4.6', 'publisher': 'Crown Business', 'page_count': '464', 'language': 'English', 'generes': 'Information Technology'}, {'title': 'The Secrets of Saving and Investing with Alvin Hall: Simple Strategies to Make Your Money Go Further', 'author': 'Alvin Hall', 'rating': '3.7', 'publisher': 'Hachette UK', 'page_count': '30', 'language': 'English', 'generes': 'Investing'}, {'title': 'Antiques Chop', 'author': 'Barbara Allan', 'rating': '4.5', 'publisher': 'Kensington Books', 'page_count': '240', 'language': 'English', 'generes': 'Mystery'}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'rating': '4.3', 'publisher': 'Minotaur Books', 'page_count': '60', 'language': 'English', 'generes': 'Thrillers'}, {'title': 'No Mercy: The brand new novel from the Queen of Crime', 'author': 'Martina Cole', 'rating': '0', 'publisher': 'Hachette UK', 'page_count': '416', 'language': 'English', 'generes': 'Thrillers'}, {'title': 'Riley Paige Mystery Bundle: Once Gone (#1) and Once Taken (#2)', 'author': 'Blake Pierce', 'rating': '4.5', 'publisher': 'Blake Pierce', 'page_count': '250', 'language': 'English', 'generes': 'Thrillers'}]
    
    >>> sort_books_category(load_dataset('10books.csv'))
    [{'title': 'A Game of Thrones: The Story Continues Books 1-5: A Game of Thrones, A Clash of Kings, A Storm of Swords, A Feast for Crows, A Dance with Dragons (A Song of Ice and Fire)', 'author': 'George R.R. Martin', 'rating': '4.5', 'publisher': 'HarperCollins UK', 'page_count': '4544', 'language': 'English', 'generes': 'Adventure'}, {'title': 'Becoming Steve Jobs: The Evolution of a Reckless Upstart into a Visionary Leader', 'author': 'Brent Schlender', 'rating': '4.6', 'publisher': 'Crown Business', 'page_count': '464', 'language': 'English', 'generes': 'Biography'}, {'title': 'Permanent Record', 'author': 'Edward Snowden', 'rating': '4.6', 'publisher': 'Metropolitan Books', 'page_count': '352', 'language': 'English', 'generes': 'Biography'}, {'title': 'Summary: Think and Grow Rich', 'author': 'Nine99 Innovation Lab', 'rating': '', 'publisher': 'Nine99 Innovation Lab (OPC) Pvt Ltd', 'page_count': '14', 'language': 'English', 'generes': 'Business'}, {'title': 'A Trace of Crime (a Keri Locke Mystery--Book #4)', 'author': 'Blake Pierce', 'rating': '4.7', 'publisher': 'Blake Pierce', 'page_count': '250', 'language': 'English', 'generes': 'Detective'}, {'title': 'Personal Success (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': '', 'publisher': 'AMACOM', 'page_count': '112', 'language': 'English', 'generes': 'Economics'}, {'title': 'We', 'author': 'Yevgeny Zamyatin', 'rating': '4.3', 'publisher': 'Pan', 'page_count': '226', 'language': 'English', 'generes': 'Fantasy'}, {'title': 'In Dark Company: A Kate Burkholder Short Story', 'author': 'Linda Castillo', 'rating': '4.3', 'publisher': 'Minotaur Books', 'page_count': '60', 'language': 'English', 'generes': 'Fiction'}, {'title': 'A Trace of Crime (a Keri Locke Mystery--Book #4)', 'author': 'Blake Pierce', 'rating': '4.7', 'publisher': 'Blake Pierce', 'page_count': '250', 'language': 'English', 'generes': 'Mystery'}, {'title': 'And Then There Were None', 'author': 'Agatha Christie', 'rating': '4.6', 'publisher': 'HarperCollins UK', 'page_count': '224', 'language': 'English', 'generes': 'Mystery'}, {'title': "The Girl in the Spider's Web: A Lisbeth Salander novel, continuing Stieg Larsson's Millennium Series", 'author': 'David Lagercrantz', 'rating': '4.1', 'publisher': 'Vintage Crime/Black Lizard', 'page_count': '416', 'language': 'English', 'generes': 'Mystery'}]
    """
    alphacat = refactoring(bookcollect)
    for books in range(len(alphacat)):
        for j in range(len(alphacat)-1-books):
            if alphacat[j]['generes'] > alphacat[j+1]['generes']:
                alphacat[j], alphacat[j+1] = alphacat[j+1], alphacat[j]
            if alphacat[j]['generes'] == alphacat[j+1]['generes']:
                if alphacat[j]['title'] > alphacat[j+1]['title']:
                    alphacat[j], alphacat[j+1] = alphacat[j+1], alphacat[j]                
    print(alphacat)
    return alphacat

#Quentin Weir 101234808

ALPHABET = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26, 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26} 
#makes the alphabet with corresponding numbers


#Function 4 sort_books_publisher 
def sort_books_publisher(dataset: dict) -> list: #definition
    """
    Returns a list with the book data stored as a dictionary where the books are sorted ALPHABETically by publisher. The function will also print the data.
    >>>sort_books_publisher(load_dataset('rand_dataset_1.csv'))
    [{'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': '', 'publisher': 'AMACOM', 'page_count': 112, 'language': 'English', 'generes': 'Economics'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'page_count': 400, 'language': 'English', 'generes': 'Fiction'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': '', 'publisher': 'Hachette UK', 'page_count': 384, 'language': 'English', 'generes': 'Fiction'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'page_count': 336, 'language': 'English', 'generes': 'Fiction'}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'page_count': 224, 'language': 'English', 'generes': 'Business'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'page_count': 416, 'language': 'English', 'generes': 'Fiction'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'page_count': 368, 'language': 'English', 'generes': 'Fiction'}, {'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 544, 'language': 'English', 'generes': 'Fiction'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288, 'language': 'English', 'generes': 'Fiction'}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'page_count': 176, 'language': 'English', 'generes': 'Business'}, {'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'page_count': 96, 'language': 'English', 'generes': 'Comics'}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'page_count': 320, 'language': 'English', 'generes': 'Economics'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'page_count': 320, 'language': 'English', 'generes': 'Detective'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'page_count': 226, 'language': 'English', 'generes': 'Fiction'}] (---------------------- OR ----------------------) book_list_dictionary('pub_sort_dataset_1.csv')
    
    >>>sort_books_publisher(load_dataset('rand_dataset_2.csv'))
    [{'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'rating': 3.9, 'publisher': 'Ballantine Books', 'page_count': 208, 'language': 'English', 'generes': 'Fiction'}, {'title': 'Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible, Edition 2', 'author': 'Brian Tracy', 'rating': 4.3, 'publisher': 'Berrett-Koehler Publishers', 'page_count': 288, 'language': 'English', 'generes': 'Economics'}, {'title': 'A Trace of Vice (a Keri Locke Mystery--Book #3)', 'author': 'Blake Pierce', 'rating': 4.8, 'publisher': 'Blake Pierce', 'page_count': 250, 'language': 'English', 'generes': 'Fiction'}, {'title': 'Watching (The Making of Riley Paigeâ€”Book 1)', 'author': 'Blake Pierce', 'rating': 4.6, 'publisher': 'Blake Pierce', 'page_count': 250, 'language': 'English', 'generes': 'Mystery'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'page_count': 400, 'language': 'English', 'generes': 'Adventure'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'page_count': 336, 'language': 'English', 'generes': 'Mystery'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'page_count': 208, 'language': 'English', 'generes': 'Thrillers'}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'rating': 4.0, 'publisher': 'Kensington Books', 'page_count': 288, 'language': 'English', 'generes': 'Detective'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 240, 'language': 'English', 'generes': 'Detective'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'page_count': 624, 'language': 'English', 'generes': 'Mystery'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'page_count': 624, 'language': 'English', 'generes': 'Fiction'}, {'title': 'The Infinite Game', 'author': 'Simon Sinek', 'rating': 3.8, 'publisher': 'Penguin', 'page_count': 272, 'language': 'English', 'generes': 'Business'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'page_count': 320, 'language': 'English', 'generes': 'Classics'}] (---------------------- OR ----------------------) book_list_dictionary('pub_sort_dataset_2.csv')
    """
    list_of_books = refactoring(dataset)
    for q in range(len(list_of_books)+1):
        for e in range(len(list_of_books)):
            if e != len(list_of_books)-1: #makes sure that e isn't greater than the book list
                
                
                #sort publishers
                first_book = list_of_books[e] #sets first_book to list_of_books at e
                second_book = list_of_books[e+1] #sets second_book to list_of_books at e + 1
                
                
                first_pub = [] #creates an empty list
                for abc in first_book['publisher']: #loops through each letter
                    if abc in ALPHABET: #checks to see if abc is in the ALPHABET list
                        first_pub.append(abc) #adds the letter to the empty list
                second_pub = [] #creates an empty list
                for abc in second_book['publisher']: #loops through each letter
                    if abc in ALPHABET: #checks to see if abc is in the ALPHABET list
                        second_pub.append(abc)  #adds the letter to the empty list
                      
                if first_pub != second_pub: #make sure that both publishers aren't the same
                    
                    if len(first_pub) < len(second_pub): #compares the length of each publisher
                        wrd_len = len(first_pub) #sets the varible wrd_len to the lesser length
                        if first_pub[0:wrd_len] != second_pub[0:wrd_len]: #makes sure the two publishers aren't the same up until wrd_len
                    
                            for letter in range(wrd_len): #loop through each letter
                                first_letter = first_pub[letter] #individual letter for the first publisher
                                second_letter = second_pub[letter] #individual letter for the second publisher
                                
                                if ALPHABET[first_letter] > ALPHABET[second_letter]: #compares the two wrd_len
                                    list_of_books[e] = second_book #switch the publishers
                                    list_of_books[e+1] = first_book #switch the publishers
                                    break 
                                elif ALPHABET[first_letter] < ALPHABET[second_letter]: #if the first letter is smaller
                                    break                         
                    else:
                        wrd_len  = len(second_pub) #wrd_len is the lesser length of the two publishers
                        if first_pub[0:wrd_len] != second_pub[0:wrd_len]: #makes sure the two publishers aren't the same up until wrd_len
                            for letter in range(wrd_len): #loops through the range of wrd_len
                                first_letter = first_pub[letter] #individual letter for the first publisher
                                second_letter = second_pub[letter] #individual letter for the second publisher
                                
                                if ALPHABET[first_letter] > ALPHABET[second_letter]: #compares the two wrd_len
                                    list_of_books[e] = second_book #switch
                                    list_of_books[e+1] = first_book #switch
                                    break
                                elif ALPHABET[first_letter] < ALPHABET[second_letter]: #if the first letter is smaller
                                    break   
                        else:
                            list_of_books[e] = second_book #switches 
                            list_of_books[e+1] = first_book #switches 
                        
                else:
                    
                    #sort titles
                    first_title = [] #creates an empty list
                    for abc in first_book['title']: #loops through each letter  
                        if abc in ALPHABET: #checks to see if abc is in the ALPHABET list
                            first_title.append(abc) #adds the letter to the empty list
                    second_title = [] #creates an empty list
                    for abc in second_book['title']: #loops through each letter 
                        if abc in ALPHABET: #checks to see if abc is in the ALPHABET list
                            second_title.append(abc) #adds the letter to the empty list
                    
                    if first_title != second_title: #make sure that both titles aren't the same
                        if len(first_title) < len(second_title): #compares the length of each publisher
                            wrd_len = len(first_title) #wrd_len is the lesser length of the two publishers
                            if first_title[0:wrd_len] != second_title[0:wrd_len]: #makes sure the two publishers aren't the same up until wrd_len
                                for letter in range(wrd_len): #loop through each letter
                                    first_letter = first_title[letter] #individual letter for the first title
                                    second_letter = second_title[letter] #individual letter for the second title
                                    
                                    if ALPHABET[first_letter] > ALPHABET[second_letter]: #compares the two wrd_len
                                        list_of_books[e] = second_book #switch
                                        list_of_books[e+1] = first_book #switch
                                        break
                                    elif ALPHABET[first_letter] < ALPHABET[second_letter]: #if the first letter is smaller
                                        break
                        else:
                            wrd_len = len(second_title) #wrd_len is the lesser length of the two titles
                            if first_title[0:wrd_len] != second_title[0:wrd_len]: #makes sure the two publishers aren't the same up until wrd_len
                                for letter in range(wrd_len): #loops through all the wrd_len
                                    first_letter = first_title[letter] #individual letter for the first title
                                    second_letter = second_title[letter] #indiviual letter for the second title
                                    
                                    if ALPHABET[first_letter] > ALPHABET[second_letter]: #compares the two wrd_len
                                        list_of_books[e] = second_book #switch
                                        list_of_books[e+1] = first_book #switch
                                        break
                                    elif ALPHABET[first_letter] < ALPHABET[second_letter]: #if the first letter is smaller
                                        break
                            else:
                                list_of_books[e] = second_book #switch
                                list_of_books[e+1] = first_book #switch   
    max_len = 0 
    for book in list_of_books:
        if max_len < len(book['publisher']):
            max_len = len(book['publisher'])
    for book in list_of_books:
        print(book['publisher'] + ' ' * (max_len - len(book['publisher'])), '  ' ,book['title'])  
    #prints the data
    return list_of_books #returns the book list

def sort_books_pageCount(dataset: dict) -> list: #definition
    """
    Returns a list with the book data stored as a dictionary where the books are sorted by page count.
    >>>sort_books_pageCount(load_dataset('rand_dataset_1.csv'))
    [{'title': 'Deadpool Kills the Marvel Universe', 'author': 'Cullen Bunn', 'rating': 4.2, 'publisher': 'Marvel Entertainment', 'page_count': 96, 'language': 'English', 'generes': 'Comics'}, {'title': 'Marketing (The Brian Tracy Success Library)', 'author': 'Brian Tracy', 'rating': '', 'publisher': 'AMACOM', 'page_count': 112, 'language': 'English', 'generes': 'Economics'}, {'title': 'How to Understand Business Finance: Edition 2', 'author': 'Bob Cinnamon', 'rating': 3.5, 'publisher': 'Kogan Page Publishers', 'page_count': 176, 'language': 'English', 'generes': 'Business'}, {'title': 'Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth', 'author': 'T. Harv Eker', 'rating': 4.6, 'publisher': 'Harper Collins', 'page_count': 224, 'language': 'English', 'generes': 'Business'}, {'title': 'Edgedancer: From the Stormlight Archive', 'author': 'Brandon Sanderson', 'rating': 4.8, 'publisher': 'Tor Books', 'page_count': 226, 'language': 'English', 'generes': 'Fiction'}, {'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': 3.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 288, 'language': 'English', 'generes': 'Fiction'}, {'title': 'How To Win Friends and Influence People', 'author': 'Dale Carnegie', 'rating': 4.3, 'publisher': 'Simon and Schuster', 'page_count': 320, 'language': 'English', 'generes': 'Economics'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'page_count': 320, 'language': 'English', 'generes': 'Detective'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'page_count': 336, 'language': 'English', 'generes': 'Fiction'}, {'title': 'Bring Me Back', 'author': 'B A Paris', 'rating': 3.8, 'publisher': 'HarperCollins UK', 'page_count': 368, 'language': 'English', 'generes': 'Fiction'}, {'title': 'The Guardians: The explosive new thriller from international bestseller John Grisham', 'author': 'John Grisham', 'rating': '', 'publisher': 'Hachette UK', 'page_count': 384, 'language': 'English', 'generes': 'Fiction'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'page_count': 400, 'language': 'English', 'generes': 'Fiction'}, {'title': 'After Anna', 'author': 'Alex Lake', 'rating': 4.1, 'publisher': 'HarperCollins UK', 'page_count': 416, 'language': 'English', 'generes': 'Fiction'}, {'title': 'The Painted Man (The Demon Cycle, Book 1)', 'author': 'Peter V. Brett', 'rating': 4.5, 'publisher': 'HarperCollins UK', 'page_count': 544, 'language': 'English', 'generes': 'Fiction'}]
    >>>sort_books_pageCount(load_dataset('rand_dataset_2.csv')) (---------------------- OR ----------------------) book_list_dictionary('pgcount_sort_dataset_1.csv')
    
    [{'title': 'Mrs. Pollifax Unveiled', 'author': 'Dorothy Gilman', 'rating': 3.9, 'publisher': 'Ballantine Books', 'page_count': 208, 'language': 'English', 'generes': 'Fiction'}, {'title': 'The Mysterious Affair at Styles', 'author': 'Agatha Christie', 'rating': 4.4, 'publisher': 'HarperCollins UK', 'page_count': 208, 'language': 'English', 'generes': 'Thrillers'}, {'title': 'Antiques Knock-Off', 'author': 'Barbara Allan', 'rating': 4.3, 'publisher': 'Kensington Publishing Corp.', 'page_count': 240, 'language': 'English', 'generes': 'Detective'}, {'title': 'A Trace of Vice (a Keri Locke Mystery--Book #3)', 'author': 'Blake Pierce', 'rating': 4.8, 'publisher': 'Blake Pierce', 'page_count': 250, 'language': 'English', 'generes': 'Fiction'}, {'title': 'Watching (The Making of Riley Paigeâ€”Book 1)', 'author': 'Blake Pierce', 'rating': 4.6, 'publisher': 'Blake Pierce', 'page_count': 250, 'language': 'English', 'generes': 'Mystery'}, {'title': 'The Infinite Game', 'author': 'Simon Sinek', 'rating': 3.8, 'publisher': 'Penguin', 'page_count': 272, 'language': 'English', 'generes': 'Business'}, {'title': 'Goals!: How to Get Everything You Want -- Faster Than You Ever Thought Possible, Edition 2', 'author': 'Brian Tracy', 'rating': 4.3, 'publisher': 'Berrett-Koehler Publishers', 'page_count': 288, 'language': 'English', 'generes': 'Economics'}, {'title': 'Killer Blonde', 'author': 'Laura Levine', 'rating': 4.0, 'publisher': 'Kensington Books', 'page_count': 288, 'language': 'English', 'generes': 'Detective'}, {'title': 'The Memoirs of Sherlock Holmes', 'author': 'Arthur Conan Doyle', 'rating': 4.2, 'publisher': 'Simon and Schuster', 'page_count': 320, 'language': 'English', 'generes': 'Classics'}, {'title': 'Little Girl Lost: A Lucy Black Thriller', 'author': 'Brian McGilloway', 'rating': 4.0, 'publisher': 'Harper Collins', 'page_count': 336, 'language': 'English', 'generes': 'Mystery'}, {'title': 'Sword of Destiny: Witcher 2: Tales of the Witcher', 'author': 'Andrzej Sapkowski', 'rating': 4.8, 'publisher': 'Hachette UK', 'page_count': 400, 'language': 'English', 'generes': 'Adventure'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'page_count': 624, 'language': 'English', 'generes': 'Mystery'}, {'title': 'Total Control', 'author': 'David Baldacci', 'rating': 4.0, 'publisher': 'Pan Macmillan', 'page_count': 624, 'language': 'English', 'generes': 'Fiction'}] (---------------------- OR ----------------------) book_list_dictionary('pgcount_sort_dataset_2.csv')
    """
    list_of_books = refactoring(dataset)
            
    for q in range(len(list_of_books)+1):
        for e in range(len(list_of_books)):
            if e != len(list_of_books)-1: #makes sure that e isn't greater than the book list
                #sort page count
                first_book = list_of_books[e] #sets first_book to list_of_books at e
                second_book = list_of_books[e+1] #sets second_book to list_of_books at e + 1
                
                first_page_count = int(first_book['page_count']) #sets first_page_count to the page count as type int
                second_page_count = int(second_book['page_count']) #sets second_page_count to the page count as type int
                
                      
                if first_page_count != second_page_count: #makes sure that the page counts aren't the same
                    
                    
                                
                    if first_page_count > second_page_count: #compares the page counts
                        list_of_books[e] = second_book #switch
                        list_of_books[e+1] = first_book #switch
                        
                    
                        
                else:
                    #sort titles
                    first_title = [] #creates an empty list
                    for abc in first_book['title']: #loops through each letter  
                        if abc in ALPHABET: #checks to see if abc is in the ALPHABET list
                            first_title.append(abc) #adds the letter to the empty list
                    second_title = [] #creates an empty list
                    for abc in second_book['title']: #loops through each letter 
                        if abc in ALPHABET: #checks to see if abc is in the ALPHABET list
                            second_title.append(abc) #adds the letter to the empty list
                    
                    if first_title != second_title: #make sure that both titles aren't the same
                        if len(first_title) < len(second_title): #compares the length of each publisher
                            wrd_len = len(first_title) #wrd_len is the lesser length of the two publishers
                            if first_title[0:wrd_len] != second_title[0:wrd_len]: #makes sure the two publishers aren't the same up until wrd_len
                                for letter in range(wrd_len): #loop through each letter
                                    first_letter = first_title[letter] #individual letter for the first title
                                    second_letter = second_title[letter] #individual letter for the second title
                                    
                                    if ALPHABET[first_letter] > ALPHABET[second_letter]: #compares the two wrd_len
                                        list_of_books[e] = second_book #switch
                                        list_of_books[e+1] = first_book #switch
                                        break
                                    elif ALPHABET[first_letter] < ALPHABET[second_letter]: #if the first letter is smaller
                                        break
                        else:
                            wrd_len = len(second_title) #wrd_len is the lesser length of the two titles
                            if first_title[0:wrd_len] != second_title[0:wrd_len]: #makes sure the two publishers aren't the same up until wrd_len
                                for letter in range(wrd_len): #loops through all the wrd_len
                                    first_letter = first_title[letter] #individual letter for the first title
                                    second_letter = second_title[letter] #indiviual letter for the second title
                                    
                                    if ALPHABET[first_letter] > ALPHABET[second_letter]: #compares the two wrd_len
                                        list_of_books[e] = second_book #switch
                                        list_of_books[e+1] = first_book #switch
                                        break
                                    elif ALPHABET[first_letter] < ALPHABET[second_letter]: #if the first letter is smaller
                                        break
                            else:
                                list_of_books[e] = second_book #switch
                                list_of_books[e+1] = first_book #switch                     
    for book in list_of_books:
        print(book['page_count'],'          ',book['title']) 
    #prints the data
    return list_of_books #returns the book list

