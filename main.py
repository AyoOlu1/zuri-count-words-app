# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}


def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename, "r") as file:
         return file.read() 


def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here

    result = dict()
    words = text.split()

    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    print(result)
    return result

count_words()