#Amine Hammoud 101220672, Emory Shantz, 101221942, Quentin Weir 101234808 & MacKenzie Snow 101146941
#Version 1.0 2021/12/10

import csv #import the csv library,

def load_dataset(fileName: str)->dict:
        """
        Returns a dictionary that contains a dictionary sorted by genres that contains a list of the book information as a dictionary. Precondition: files must be a csv file
        >>> load_dataset('Google_Books_Dataset.csv')
        {'Fiction': [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'page_count': '288', 'language': 'English'}, {another element}, ...]}
        >>> load_dataset('Google_Books_Dataset.csv')['Fiction']
        [{'title': "Antiques Roadkill: A Trash 'n' Treasures Mystery", 'author': 'Barbara Allan', 'rating': '3.3', 'publisher': 'Kensington Publishing Corp.', 'page_count': '288', 'language': 'English'}]
        """
        file = open(fileName) #Open the csv file
        csvreader = csv.DictReader(file, delimiter=',')
        
        genres = {} #Creates an empty dictionary
        genres_list = [] #Creates an empty list   
        for line in csvreader: #Printing out all book info
                line.pop('') #Removing empty string
                x = line['generes'] #Indexes the genre
                if line['rating'] == '': #Removes empty string
                        line['rating'] = 0.0
                line['rating'] = float(line['rating']) #changes string to float
                line['page_count'] = int(line['page_count']) #changes string to integer
                line.pop('generes') #removes the genre information
                if x not in genres:
                        genres_list += [x] #Adds book information to the list   
                        if line not in genres_list: #Checks for duplicate books
                                genres.setdefault(x, [line]) #Adds the genre if not already in genres                                         
                else:
                        y = genres[x] #Indexes the list that information needs to be added to
                        y += [line] #Adds the book information to the list
        file.close() #Closes the file
        return genres #Gives the final dictionary

#print(load_dataset('Google_Books_Dataset.csv'))