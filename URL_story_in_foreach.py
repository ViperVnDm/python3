from urllib.request import urlopen

story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []

#For loop goes through story
for line in story:
    line_words = line.decode('utf8').split()
    for word in line_words:
        story_words.append(word)

story.close()
story_words