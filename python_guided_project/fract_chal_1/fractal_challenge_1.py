'''
Longest Even Length Word

Consider a string, sentence, of space-separated words where each word is a substring consisting of English alphabetic letters only.

We want to find the first word in sentence having a length which is both an even number and greater than or
equal to the length of any other word of even length in the sentence. 
For example, if sentence is `Time to write great code` , then the word we're looking for is Time .
While code and Time are of maximal length, Time occurs first. 
If sentence is `Write code for a great time` , then the word we're looking for is code.  
'''

data1 = 'One great way to make predictions about an unfamiliar nonfiction text is to take a walk through the book before reading.'
data2 = 'photographs or other images, readers can start to get a sense about the topic. This scanning and skimming helps set the expectation for the reading.'
data3 = ' testing very9 important'

def q01_longest_even_word(sentence):
    even_list = [x for x in sentence.split() if len(x) % 2 == 0]
    if len(even_list) > 0:
        word = max(even_list, key=len)
    else:
        word = 0
   
    return word
    
print(q01_longest_even_word(data3))
