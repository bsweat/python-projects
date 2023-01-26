import sys


def createIndex():
    index = {}
    return index

def recordBook(index, bookISBN, bookTitle):
    index[bookISBN] = bookTitle
    
def findBook(index, bookISBN):
    if bookISBN in index:
        book = index[bookISBN]
        return book
    else:
        book = ''
        return book
    
def listBooks(index):
    stringList = []
    count = 1
    for ISBN in index:
        stringList.append("{}) {}: {}".format(count,ISBN,index[ISBN]))
        count += 1
    return stringList

def formatMenu():
    menu = ['Command list: ','[r] to record a book','[f] to find a book','[l] to list all books','[q] to quit']
    return menu

def formatMenuPrompt():
    prompt = 'Enter an option: '
    return prompt


def getUserChoice(prompt):
    userInput = ''
    while userInput == '':
        userInput = input(prompt).strip()
    return userInput

def getISBN():
    isbn = getUserChoice('Please input the book ISBN: ')
    return isbn

def getTitle():
    title = getUserChoice('Please input the book title: ')
    return title

def recordBookAction(index):
    bookISBN = getUserChoice('Enter the ISBN: ')
    bookTitle = getUserChoice('Enter the title: ')
    index[bookISBN] = bookTitle

def listBooksAction(index):
    if index == {}:
        print('Dictionary machine broke.')
    else:
        count = 1
        for book in index:
            print("{}) {}: {}".format(count,book,index[book]))
            count += 1

def findBookAction(index):
    isbn = getISBN()
    if isbn in index:
        print(index[isbn])
    else:
        print('ding dong ur fuckin wrong')

def quitAction(index):
    print('lmao im dead :P')
    sys.exit( 0 )
    return

# createIndex , recordBook , findBook , listBooks , formatMenu , formatMenuPrompt
# getUserChoice , getISBN , getTitle , recordBookAction , findBookAction , listBookAction, quitAction
def applyAction(index,userInput):
    if userInput == 'r':
        recordBookAction(index)
    elif userInput == 'f':
        findBookAction(index)
    elif userInput == 'l':
        listBooksAction(index)
    elif userInput == 'q':
        quitAction(index)
    else:
        print('ding dong ur wrong')
    return


def main():
    index = createIndex()
    while True:
        userInput = getUserChoice('Please input an option: R to record, L to list, F to find, or Q to quit.')
        applyAction(index,userInput)
        
        
if __name__ == '__main__':
    main()