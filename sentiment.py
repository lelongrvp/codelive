import time

## Text menu in Python

def print_menu():       ## Your menu design here
    print ('Learning data file name?', input())
    print ('What would you like to do?')
    print (30 * "-" , "MENU" , 30 * "-")
    print ("1. Get the score of a word")
    print ("2. Get the average score of words in a file")
    print ("3. Find the highest/ lowest scoring words in a file")
    print ("4. Sort the words in a file into positive.txt and negative.txt")
    print ("5. Exit")
    print (67 * "-")

loop=True      

while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = int(input("Enter your choice [1-5]: "))

    if choice==1:     
        Start_Time = time.time()
        #to store the words
        sentimentData = {}

        #opening the file for reviews
        fileData = open('training.txt', 'r')

        #Sotring all data into TotalData after converting the data into lowercase
        TotalData = str.lower(fileData.read())
        #file closing
        fileData.close()

        #split the data into lines by using newlinecharacter
        reviewsData = TotalData.split('\n')

        print('Initializing sentiment database')
        #splitin the line into words by using space
        for review in reviewsData:
            words = review.split(' ')

        for word in words:
            if word not in sentimentData:
                sentimentData[word] = [1, int(float(words[0]))]
            else:
                sentimentData[word][0] += 1
                sentimentData[word][1] += int(float(words[0]))
    elif choice==2:
        Start_Time = time.time()
        #to store the words
        sentimentData = {}

        #opening the file for reviews
        fileData = open('training.txt', 'r')

        #Sotring all data into TotalData after converting the data into lowercase
        TotalData = str.lower(fileData.read())
        #file closing
        fileData.close()

        #split the data into lines by using newlinecharacter
        reviewsData = TotalData.split('\n')

        print('Initializing sentiment database')
        #splitin the line into words by using space
        for review in reviewsData:
            words = review.split(' ')

        #doing the analysis on captured data
        ending_time = time.time()

        #time taken to read data
        time = format(ending_time - Start_Time, '.2f')
        #status what we are done
        print('All Sentiment Data is taken from file and setups like a database')
        print('Unique words are :', len(sentimentData))
        print('For analyses taken time to compelte', time)
        print('')

        #asking the user to take phrase to enter phrase and converting to lower case and storing
        phraseData = str.lower(input('Enter a phrase to test: '))
        single_phrase = phraseData.split()

        average = 0
        count = 0

        #count values to figure out the average score for the phrase
        for word in single_phrase:
            if word in sentimentData:
                score = sentimentData[word][1] / sentimentData[word][0]
                print('* \'', word, '\' appears ', sentimentData[word][0], ' times with an average score of ', score, sep = '')
                average += score
                count += 1
            else:
                print('* \'', word, '\' does not appear in any movie reviews', sep = '')

        #if no words appears
        if count == 0:
            print('Not enough words to determine sentiment.')
        else:
            print('Average score for this phrase is:', average / count)
    elif choice==3:
        Start_Time = time.time()
        #to store the words
        sentimentData = {}
        #opening the file for reviews
        fileData = open('training.txt', 'r')

        #Sotring all data into TotalData after converting the data into lowercase
        TotalData = str.lower(fileData.read())
        #file closing
        fileData.close()

        #split the data into lines by using newlinecharacter
        reviewsData = TotalData.split('\n')

        print('Initializing sentiment database')
        #splitin the line into words by using space
        for review in reviewsData:
            words = review.split(' ')
            
    elif choice==4:
        Start_Time = time.time()
        # to store the words
        sentimentData = {}
        # opening the file for reviews
        fileData = open('training.txt', 'r')

        # Sotring all data into TotalData after converting the data into lowercase
        TotalData = str.lower(fileData.read())
        # file closing
        fileData.close()

        # split the data into lines by using newlinecharacter
        reviewsData = TotalData.split('\n')

        print('Initializing sentiment database')
        # splitin the line into words by using space
        for review in reviewsData:
            words = review.split(' ')
        
    elif choice==5:
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        input("Wrong option selection. Enter any key to try again..")