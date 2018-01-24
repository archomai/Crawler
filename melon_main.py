import re


source = open('melon.html', 'rt').read()


PATTERN_TR = re.compile(r'<tr class="lst.*?>.*?</tr>', re.DOTALL)
PATTERN_TD = re.compile(r'<td.*?>.*?</td>', re.DOTALL)


for tr_list in re.finditer(PATTERN_TR, source):
    td_list = re.findall(PATTERN_TD, tr_list.group())

#    for index, td in enumerate(td_list):
#       td_strip = re.sub(r'[\n\t]+|\s{2,}', '', td)
#       print(f'{index:02}: {td_strip}')


# td_img_cover = td_list[3]d
# PATTERN_IMG = re.compile(r'<img.*?src="(.*?)".*?>', re.DOTALL)
# url_img_cover = re.search(PATTERN_IMG, td_img_cover).group(1)
# print(url_img_cover)

    td_rank = td_list[1]
    PATTERN_RANK = re.compile(r'<span class="rank ">(.*?)</span>', re.DOTALL)
    rank = re.search(PATTERN_RANK, td_rank).group(1)

    td_title_author = td_list[5]
    PATTERN_DIV_RANK01 = re.compile(r'<div class="ellipsis rank01">.*?</div>', re.DOTALL)
    PATTERN_A_CONTENT = re.compile(r'<a.*?>(.*?)</a>')
    div_rank01 = re.search(PATTERN_DIV_RANK01, td_title_author).group()
    title = re.search(PATTERN_A_CONTENT, div_rank01).group(1)

    td_singer = td_list[5]
    PATTERN_SINGER = re.compile(r'<a.*? - 페이지 이동" >(.*?)</a>')
    singer = re.search(PATTERN_SINGER, td_singer).group(1)

    td_album = td_list[6]
    PATTERN_ALBUM = re.compile(r'<a.*? - 페이지 이동">(.*?)</a>')
    album = re.search(PATTERN_ALBUM, td_album).group(1)


    result_dict = {'rank':rank, 'title':title, 'artist':singer, 'album':album}


    print(result_dict)




#    print({f'rank: {rank:>3}, title : {title}, artist : {singer} , album : {album}'})