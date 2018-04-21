output = []
out_str = []
lines = sum(1 for line in open('../../../qiz3/data/bio_pubtator/bio_pubtator.tokens.txt'))
import random
pick = random.sample(range(0, lines), 100000)
with open('../../../qiz3/data/bio_pubtator/bio_pubtator.tokens.txt') as fp:
    out_str = fp.read().split('\n')
for i in pick:
    output.append(out_str[i])
output = '\n'.join(output)

text_file = open("tmp/Sample_bio_pubtator.txt", "w")
text_file.write(output)
text_file.close()

output = []
out_str = []
lines = sum(1 for line in open('../../../qiz3/data/wiki/sampled_wiki.tokens.txt'))
import random
pick = random.sample(range(0, lines), 100000)
with open('../../../qiz3/data/wiki/sampled_wiki.tokens.txt') as fp:
    out_str = fp.read().split('\n')
for i in pick:
    output.append(out_str[i])
output = '\n'.join(output)

text_file = open("tmp/Sample_wiki.txt", "w")
text_file.write(output)
text_file.close()




