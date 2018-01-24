
import re

# f = open('melon.html', 'rt')
# source = f.read()
# f.close()

PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')

source = open('melon.html', 'rt').read()


for match_div_rank01 in re.finditer(PATTERN_DIV_RANK01, source):
    div_rank01_content = match_div_rank01.group()
    title = re.search(PATTERN_A_CONTENT, div_rank01_content).group(1)
    print(title)


# result = re.findall(pattern_div_rank01, source)
# for index, item in enumerate(result):
#     print(index, item)
