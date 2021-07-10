""" 

Taking a string input and splitting it into a string and a list
so as to find if the string can be split into two using elements
already present in the list

"""


def word_split(phrase, list_of_words, output=None):
    #Set a default output, which is overwritten later
    if output is None:
        output = []

    #Loop through the list_of_words
    for word in list_of_words:
    
        #Check if the current word begins with the phrase
        if phrase.startswith(word):
        
            #Add to the output
            output.append(word)
            
            #keep recursively calling the function to get all instances
            word_split(phrase[len(word):], list_of_words, output)

    #Return the output
    return output


#Take the input and split it into the phrase and list
phrase, li = input().split(",", 1)
#Remove quotes in case if they are present
phrase = phrase.strip('\"')
#Conver to a list from strings
list_of_words = list(li.split(","))
l1 = word_split(phrase, list_of_words)
#Take the largest string and remove it from thre list
res = max(l1, key=len)
l1.remove(res)
#Take the second largest and print both
res2 = max(l1, key=len)
print("{0},{1}".format(res,res2))
