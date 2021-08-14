def isPalin(word):
    if len(word) < 1:
        return True
    else:
        if word[0].lower() == word[-1].lower():
            return isPalin(word[1:-1])
        else:
            return False

myword = ""
myword = input("Enter a word: ")
while(myword.lower() != "done"):
    print(myword, isPalin(myword))
    myword = input("Enter a word: ")
