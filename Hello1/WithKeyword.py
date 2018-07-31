import sys
from urllib.request import urlopen
url=url='http://sixty-north.com/c/t.txt' 
def fetchWords(url):
    with urlopen(url) as story:
        story_words=[]
        for line in story:
            line_words = line.decode('utf-8').split()
            for words in line_words:
                story_words.append(words)
    return story_words
            
def printItems(items):
    for word in items:
        print(word)
        
def main():
 #   url=sys.argv[1]
    items=fetchWords(url)
    printItems(items)
    
 
#fetchwords()
if __name__ == '__main__':
    main()

  