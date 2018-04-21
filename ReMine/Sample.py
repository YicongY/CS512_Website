output = []
lines = sum(1 for line in open('../../../qiz3/data/bio_pubtator/bio_pubtator.tokens.txt'))
import random
pick = random.sample(range(0, lines), 100000)
with open('../../../qiz3/data/bio_pubtator/bio_pubtator.tokens.txt') as fp:
    line = fp.readline()
    index = 0
    while line:
        if index % 1000 == 0:
            print(index)
        if index in pick:
            output.append(line.strip())
        line = fp.readline()
        index += 1
output = '\n'.join(output)

text_file = open("tmp/Sample.txt", "w")
text_file.write(output)
text_file.close()




