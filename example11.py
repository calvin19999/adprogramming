print("Anagram Test")
ana=input("Enter two space separated words: ")
ana=ana.strip()
word1=(ana.split(" "))[0]
word2=(ana.split(" "))[1]

word1=sorted(word1)
word2=sorted(word2)

if(word1==word2):
 print("the word are anagram")
else:
 print("the word are not anagram")


