article = '''When I wrote the following page, or rather the bulk of them, I live alone, in the wood, a mile from any neighbor, in a house which I had built myself, on the shore of Walden pond, in Concord, Massachusetts, and earned my living by the labor of my hands only. I lived there two years and two months. At present I am a sojourner in civilized life again.'''
#瓦尔登湖选段
word = article.split(" ")
print(word)
words = {"and","or","are","is","what","how","in","a"}
#指定词汇未在选段中出现，加了两个词以进行测试
for word in article:
    if word in words:
        words[word] += 1
    else:
        words[word] = 0
print(words)
