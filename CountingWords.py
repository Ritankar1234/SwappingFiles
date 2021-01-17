string=input('Enter your string')
print(string)
wordCount=1
charecterCount=0
for i in string:
    charecterCount=charecterCount+1
    
    if(i==' '):
        wordCount=wordCount+1
        charecterCount=charecterCount-1

print(charecterCount)
print(wordCount)