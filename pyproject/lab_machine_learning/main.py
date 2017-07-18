import markov
import util

<<<<<<< HEAD
words = util.readLetters('text/spongebob_texas.txt')

chain = markov.Chain(3)
for word in words:
    chain.observe(word)
=======
elems = util.readWords('text/spongebob_texas.txt')
chain = markov.Chain(2)
for x in elems:
    chain.observe(x)
>>>>>>> ee1db3beb01e8b92555d8a65d9929322bda300b8

content = chain.chooseFirst()
for i in range(100):
    next = chain.chooseNext()
    if not next: break
    content.append(next)

content = ' '.join(content)
print(content)
input()