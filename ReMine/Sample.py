import random
pick = random.sample(range(0, 3000000), 100000)

output = []
out_str = []
with open('../../../qiz3/data/bio_pubtator/bio_pubtator.tokens.txt') as fp:
    out_str = fp.read().split('\n')
for i in pick:
    output.append(out_str[i])
output = '\n'.join(output)
text_file = open("tmp/Sample_bio_pubtator.token.txt", "w")
text_file.write(output)
text_file.close()

output = []
out_str = []
with open('../../../qiz3/data/bio_pubtator/bio_pubtator.pos.txt') as fp:
    out_str = fp.read().split('\n')
for i in pick:
    output.append(out_str[i])
output = '\n'.join(output)
text_file = open("tmp/Sample_bio_pubtator.pos.txt", "w")
text_file.write(output)
text_file.close()


import random
pick = random.sample(range(0, 3000000), 100000)

output = []
out_str = []
with open('../../../qiz3/data/wiki/sampled_wiki.tokens.txt') as fp:
    out_str = fp.read().split('\n')
for i in pick:
    output.append(out_str[i])
output = '\n'.join(output)
text_file = open("tmp/Sample_wiki.token.txt", "w")
text_file.write(output)
text_file.close()
output = []
out_str = []
with open('../../../qiz3/data/wiki/sampled_wiki.pos.txt') as fp:
    out_str = fp.read().split('\n')
for i in pick:
    output.append(out_str[i])
output = '\n'.join(output)
text_file = open("tmp/Sample_wiki.pos.txt", "w")
text_file.write(output)
text_file.close()




