import sys
# PRASHANT MURALI, ID: 29625564
# FIT2004 Assignment 1

# Task 1

def preprocess(filename):
    """
    This is the preprocess function that will preprocess the words given in the file.
    The worst case time and space complexity of this function is o(nm).
    :param filename: The name of the file that will be input.
    :return: A list of the preprocessed words.
    """
    # Handle the errors if no or incorrect filename is given.
    bflag=False
    while bflag==False:
        try:
            open(filename, "r")
            bflag=True
        except NameError:
            print("Invalid file name was entered, please enter a file name.")
            filename = input("Enter filename : ")
        except TypeError:
            print("Invalid file name was entered, please enter a file name.")
            filename = input("Enter filename : ")
        except FileNotFoundError:
            print("The file could not be found, please enter a file name again.")
            filename = input("Enter filename : ")

    # Open to test the file.
    openTestfile = open(filename, "r")
    # Check the first item in the file to see if its empty.
    testfile = openTestfile.read(1)
    # If the file is empty, the appropriate output is printed, and the function is exited.
    if testfile=="":
        print("Unable to continue:\n1. Writing.txt is empty or\n2. There is no word remaining after preprocessing.")
        sys.exit()
    # Else, continue to read the entire file.
    else:
        file=open(filename, "r")
        file=file.read()

    # Create lists to hold punctuations, newline, tab, auxiliary and article words.
    # Space complexity of the first three lists below are constant as they're of fixed size.
    punctuations=[',','.','?','!',':',';','"']
    spaces=["\t","\n"]
    aux_article_words=["am", "is", "are","was", "were", "has", "have", "had", "been", "will", "shall", "may","can", "would", "should", "might", "could", "a", "an", "the"]
    list = []
    list2 = []

    # Put ALL items in a list.
    # Below would hold time complexity O(nm) as it iterates through each word in the file
    # and through each character in the word.
    for word in file:
        for character in word:
            list.append(character)

    # Remove all punctuations.
    # Complexity would be O(nm) as the outer loop holds complexity of
    # O(nm), while the inner loop has a constant time complexity as
    # it is based on a list of pre-defined punctuations as seen above.
    for character in range(len(list)):
        # Counter to hold number of punctuations there are.
        counter=len(punctuations)
        for i in punctuations:
            if list[character]!=i:
                counter-=1
        # Only append the characters to a list when it has checked
        # through all the punctuations.
        if counter == 0:
            list2.append(list[character])

    # At this point, the list is checked if its empty after removing the punctuations.
    if list2==[]:
        print("Unable to continue:\n1. Writing.txt is empty or\n2. There is no word remaining after preprocessing.")
        sys.exit()

    # Replace tab and newline spaces.
    # This would hold time complexity O(nm) as the outer loop loops
    # through N words of m characters, while the inner loop loops
    # through a constant  number of times as the "spaces" list has
    # been predefined as seen from above.
    for character in range(len(list2)):
        for i in spaces:
            if list2[character] == i:
                list2[character]=" "

    # Clear the first list for next operation.
    list=[]

    # Concatenate everything back together.
    # Now that the punctuations, tab and space have been removed,
    # the characters can be concatenated back together.
    i=0
    j=0
    str=""
    # The loop below loops through the list of characters and concatenates
    # them before a space is found, indicating the ned of each word.
    # The loop below holds O(nm) time complexity as it loops through
    # N words of m characters, and having O(1) operations in the loop.
    while i<len(list2):
        if list2[i]!=" ":
            str+=list2[i]
            i+=1
            if i==len(list2):
                list.append(str)
                break
        else:
            list.append(str)
            str=""
            i+=1

    # Clear the second list for next operation.
    list2=[]

    # Removing aux words.
    # Complexity would be O(N) as the outer loop holds complexity of
    # O(N) from looping through every loop, while the inner loop has
    # a constant time complexity as it is based on a list of pre-defined
    # words as seen above.
    for j in range(len(list)):
        counter=len(aux_article_words)
        for i in aux_article_words:
            if list[j]!=i:
                counter-=1
        # Only append the words to a list when it has checked
        # through all the auxiliary and article words.
        if counter==0:
            list2.append(list[j])

    # At this point, the list is checked if its empty after removing the aux and article words.
    if list2 == []:
        print("Unable to continue:\n1. Writing.txt is empty or\n2. There is no word remaining after preprocessing.")
        sys.exit()

    if len(list2)>10000:
        print("Essay exceeds 10000 words!")
        sys.exit()

    # Set list back to the list with the final result.
    list=list2

    # Return th list.
    return list

# ENF OF PREPROCESS FUNCTION #
# OPTION TO DISPLAY WORDS ARE DONE IN THE
# MAIN BLOCK.







# TASK 2

def wordSort(list):
    """
    This function sorts the preprocessed words in alphabetical order.
    :param list: List of words which are preprocessed in Task 1.
    :return: Sorted list of words which are remained after preprocessing.
    """

    # Check if the list is empty.
    if list == []:
        print("Unable to continue:\n1. Writing.txt is empty or\n2. There is no word remaining after preprocessing.")
        sys.exit()

    list2=[]

    # Set the initial max to the first item in the list.
    maxVal = len(list[0])

    # Find the character with maximum length in the list.
    # This holds time complexity O(N) as the outer loop iterates through the
    # list with N words. Operations inside the loop have constant time
    # complexity, therefore time complexity here is O(N).
    for i in range(0, len(list)):
        if maxVal < len(list[i]):
            maxVal = len(list[i])

    # Adding null zero values to the back of words that are not as long
    # as the longest word in the list.
    # The outer loop holds time complexity O(N) as the outer loop iterates
    # through the list with N words. The inner loop has a complexity lesser
    # than O(m) because it is unlikely to have a word with no characters for the
    # inner loop to loop through m times, so it would be less than O(m), which
    # therefore still holds an overall time complexity of O(nm).
    i = 0
    while i < len(list):
        j = 0
        wordLen = len(list[i])
        while j < (maxVal - wordLen):
            # Adding null zero value to the back of the string.
            list[i] += '\0'
            j += 1
        list2.append(list[i])
        i += 1

    # Set list to list2.
    list=list2

    # The entire loop below sorts the words.
    # The worst-case time complexity of the loop is O(nm).
    # Detailed explanation of complexity is in the documentation.
    k=-1
    while k>=-maxVal:
        indexList=[]
        characterList=[]
        WORD=[]

        # Append one character from each word into characterList,
        # and the word itself into the WORD list.
        for word in list:
             characterList.append((word[k]))
             WORD.append(word)

        # Getting the index of each character.
        for i in range(len(characterList)):
            if characterList[i]=='\0':
                indexList.append(0)
            else:
                indexList.append(ord(characterList[i])-96)

        countList=[0]*27

        wordListCount=[0]*26

        # Creating table.
        for i in range(len(wordListCount)):
            wordListCount[i]=[0]

        # Adding to count and the word's list count.
        j = 0
        for i in indexList:
            countList[i]+=1
            wordListCount[i].append(WORD[j])
            j+=1

        # Clear lists 2.
        list2=[]
        list3=[]

        # Get all the lists from the table.
        for i in range(len(wordListCount)):
            if wordListCount[i] != 0:
                list3+=wordListCount[i]

        # Get all items in the list.
        for i in list3:
            if i!=0:
                list2.append(i)

        list=list2
        k-=1

    list=list2

    # Removing the null characters from the word.
    # Time complexity would be O(nm).
    outputList = []

    # Loops through entire list so O(n).
    for item in list:
        string = ""
        # Loops through every character in the word, so O(m).
        for j in item:
            if j != "\0":
                string += j
        outputList.append(string)


    # Set the list as the outputList.
    list = outputList


    # Return the list.
    return list

# END OF TASK 2 #
# OPTION TO DISPLAY SORTED WORDS ARE
# IN THE MAIN BLOCK.




# TASK 3
def wordCount(list):
    """
    This function finds the words and its frequency in the sorted list.
    :param list: Sorted list of words.
    :return: Array with total number of words and a list of words with their frequency.
    """

    # Check at this point if the list is empty. If so, then the the program is exited.
    if list == []:
        print("Unable to continue:\n1. Writing.txt is empty or\n2. There is no word remaining after preprocessing.")
        sys.exit()

    # Create an outputList with extra length to make sure all items can fit in it.
    # The two lists below holds space complexity of O(N).
    outputList=[0]*(len(list)+1)
    outputList[0]=(len(list))

    # Create a list at every index except for the first index inside the outputList.
    for i in range(1,len(list)+1):
        outputList[i]=[]

    i=0
    j=1
    frequency=1
    # Below gets the frequency of each word and places it into the outputList.
    # It holds complexity of O(N) as it loops through every word in the list.
    while i<len(list):

        # Check if theres only one item in the list to immediately append it in.
        if len(list)==1:
            outputList[j].append(list[i])
            outputList[j].append(1)
            break

        # Compare the words next to each other in the list - this can be done since they're sorted.
        # Increment their frequency if they're the same, else move to the next index in the list
        # and the outputList.
        try:
            if list[i]==list[i+1]:
                frequency+=1
                i+=1
            else:
                outputList[j].append(list[i])
                outputList[j].append(frequency)
                frequency=1
                j+=1
                i+=1

        # It will face an IndexError when the loop reaches the last word, so the last word is
        # checked if was equal to the previous, else the last word and its frequency is added
        # to the next index in the outputList.
        except IndexError:
             if list[i] == list[i - 1]:
                 outputList[j].append(list[i])
                 outputList[j].append(frequency)
             else:
                 outputList[j].append(list[i])
                 outputList[j].append(frequency)
             break
    # The output list would have some empty spaces a the back if there are non-unique words,
    # so those spaces are removed using the loop below.
    # It holds time complexity O(N) as it may loop through N words if all the words are unique.
    list=[]
    for item in outputList:
        if item!=[]:
            list.append(item)

    # As required in the spec sheet, no word can repeat more then 50 times.
    for i in range(1,len(list)):
        if list[i][1]>50:
            print("A word has repeated more than 50 times. Unable to continue.")
            sys.exit()


    return(list)

# ENF OF TASK 3
# ITEMS ARE DISPLAYED FROM THE MAIN BLOCK







# TASK 4
def kTopWords(k,list):
    """
    This function displays the k top most frequent words in the writing. Worst-case time complexity
    would be O(k) and space complexity is O(k).
    :param k: k value for top k words.
    :param list: list of sorted words with their frequencies.
    :return: k number of top most frequent words with their frequencies.
    """
    # Check at this point if the list is empty. If so, then the the program is exited.
    if list == []:
        print("Unable to continue:\n1. Writing.txt is empty or\n2. There is no word remaining after preprocessing.")
        sys.exit()

    # Make sure the list parameter given starts with the first word in the list, otherwise
    # pop the first item in the list as it may be holding the value of total number of words
    # that were in the writing.
    try:
        list[0][1]
    except TypeError:
        list.pop(0)
    except IndexError:
        list.pop(0)

    # Also check if the input is an integer, otherwise prompt the user to re-input the k value.
    while type(k) is not int:
        try:
            k = int(input("How many top-most frequent words do I display: "))
        except ValueError:
            pass
        except TypeError:
            pass

    # If the user asks for 0 top most frequent words, it would be nothing so the function is
    # exited.
    if k==0:
        sys.exit()
    # If the value of k is greater or equal to than the length of the list, then all the words
    # and its frequencies will be displayed.
    if k>=len(list):
        # Goes to the TopK function to get the top k words.
        # Time complexity of the function TopK is O(k).
        k=len(list)
        outputList=TopK(k,list)

        # outputList contains k elements only, so the loop below would have a complexity
        # of O(k).


    # Else if the value of k is less than the length of the list, the top k words
    # will be printed.
    else:
        # Goes to the TopK function to get the top k words.
        # Time complexity of the function TopK is O(k).
        outputList=TopK(k, list)
        # outputList contains k elements only, so the loop below would have a complexity
        # of O(k).



    list=outputList
    return list

def TopK(k,list):
    """
    This function gets the top k words. The overall worst-case time complexity
    of this function is O(k), and space complexity O(k).
    :param k: k value for top k words.
    :param list: list of sorted words with their frequencies.
    :return: k number of top most frequent words with their frequencies.
    """

    # Add the first k items into the list.
    # Below holds a complexity of O(k).
    arr=(list[:k])

    # Set the list to contain only the remaining items.
    # Below holds a complexity of O(n-k).
    list=list[k:]

    # n holds the length of the list.
    n = len(arr)

    # Initialize a list of size 50. The assignment spec sheet has mentioned that no word
    # will repeat more than 50, hence there can be frequencies of up to 50 at most. Also, it is
    # made sure in task 3 that no word is repeated more than 50 times.
    # Space complexity here would be constant as a fixed size of 50 is initialized.
    array = [0] * 50

    # Initialize list of lists for the array.
    # Below would hold constant time complexity because the length
    # of the array is fixed at 50.
    # The space complexity would also be constant as a list of list
    # is being created at every index of the fixed list.
    for i in range(len(array)):
        array[i] = []
    # Append the k items accordingly to the list. The frequency of the word
    # acts as the index.
    # The loop below loops through k elements with constant operations,
    # so its time complexity is O(k).
    for i in range(len(arr)-1,-1,-1):
        array[arr[i][1]].append(arr[i])

    # Get back all the items from the table.
    # The loop below would have constant time complexity because it loops through
    # an array of fixed size 50.
    arr = []
    for i in range(len(array)-1,-1,-1):
        if array[i] != [0]:
            arr += array[i]


    # Now the first k items are in sorted order. If any item is more than the
    # minimum item in the list - which is the item at the last index, that item
    # will be added to the front of the list.
    # The time complexity of the loop below would be O(n-k) because it loops through
    # the remaining of the list, while doing operations that run in constant time.
    # The space complexity is also maintained at O(k) because the last element is popped
    # first before adding the new element into the list.
    for j in range(len(list)):
         if list[j][1]>arr[k-1][1]:
             # Remove last element.
             arr.pop()
             # Add the new element to the front of the list.
             arr[0:0]=[(list[j])]

    # Now, the top k elements are in the list, but they are not in sorted order.
    # So the sorting happens again. The sorting done here is essentially a version
    # counting sort.

    # Sort.

    # Below would hold time constant time complexity because the length
    # of the array is fixed at 50.
    # The space complexity would also be constant as a list of list
    # is being created at every index of the fixed list.
    newarray=[0]*50
    for i in range(len(newarray)):
        newarray[i]=[]

    # Append the k items accordingly to the list. The frequency of the word
    # acts as the index.
    # The loop below loops through k elements with constant operations,
    # so its time complexity is O(k).
    for i in range(len(arr)-1,-1,-1):
        newarray[arr[i][1]].append(arr[i])

    # Retrieve elements from the table.
    # The loop below would have constant time complexity because it loops through
    # an array of fixed size 50.
    arr=[]
    for i in range(len(newarray)-1,-1,-1):
        if newarray[i] != [0]:
            arr+=newarray[i]

    list=arr

    # Return the list.
    return list



# MAIN

if __name__ == "__main__":

    # TASK 1

    # Errors for the preprocess function are handled inside the function.
    list=preprocess("Writing.txt")

    print("Words are preprocessed..")
    userInput = input("Do I need to display the remaining words: ")
    # If user inputs an upper or lower case Y, it is taken as a yes,
    # while any other character would be taken as a no.
    if userInput == "Y":
        for words in list:
            print(words)
    print("\n")

    # TASK 2
    list=wordSort(list)

    # Ask if the sorted words needs to be printed.
    print("The remaining words are sorted in alphabetical order")
    # If user inputs an upper or lower case Y, it is taken as a yes,
    # while any other character would be taken as a no.
    userInput = input("Do you want to see: ")
    if userInput == "Y":
        for item in list:
            print(item)
    print("\n")

    # TASK 3
    # The output of task 3 is printed within the function.
    list=wordCount(list)

    # Print the result.
    print("The total number of words in the writing: " + str(list[0]))
    print("The frequencies of each word:")
    for i in range(1, len(list), 1):
        print(str(list[i][0]) + " : " + str(list[i][1]))
    print("\n")

    # TASK 4
    # The input needs to be an integer, so the programme will repeatedly ask the user
    # to enter a k value until it is found to be an integer. The output of the function is
    # displayed from inside the function.
    k=None
    while type(k) is not int:
        try:
            k = int(input("How many top-most frequent words do I display: "))
        except ValueError:
            pass
        except TypeError:
            pass
    list=kTopWords(k,list)

    print(str(k) + " top most words appear in the writing are:")
    for i in range(len(list)):
        print(str(list[i][0]) + " : " + str(list[i][1]))

