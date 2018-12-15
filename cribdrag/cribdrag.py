# -*- coding: utf-8 -*-

from os import urandom


def generate_key(length):
    return urandom(length)


def cipher(msg, k):
    return [m_byte ^ k_byte for (m_byte, k_byte)
                in zip(bytearray(msg), bytearray(k))]


def print_bytearray(barray):
    print "".join([chr(x) for x in barray])


#msg1 = "回顾习近平总书记的从政生涯恰好契合了中国波澜壮阔的年改革开放历程在正定改革开放初潮涌动他带领当地百姓解放生产力脱贫致富在福建他办经济特区为外商投资营造良好环境在浙江改革开放已取得一定成果他开始将目光投向开发较少的蓝色海域在上海他抓党建发展高新技术鼓励上海当好全国改革开放的排头兵梳理习近平总书记在各地主政期间的改革措施不难看出其中的一脉相承与不断丰富发展事"
#msg2 = "为隆重庆祝改革开放周年全方位展示改革开放波澜壮阔的伟大历程由中央宣传部中央改革办中央党史和文献研究院国家发展改革委国家广播电视总局新华社中央广播电视总台中央军委政治工作部联合拍摄的集大型政论专题片必由之路月日起在中央电视台综合频道点档播出该片以改革开放是坚持和发展中国特色社会主义的必由之路为主题全景式回顾改革开放年历程以风云激荡的感人故事激荡的感人故事事"

msg1 = "With that many messages, crib dragging should become easier, not harder... They are more likely to have things like the cropping up, plus once you find a word in one of the texts, you can be confident that you have it right if all the ciphertexts work. At any rate, I am currently working on two ciphertexts with the same key and I wrote a program that speeds it up immensely. A little trick I found useful is that, with a text file of all english words, it isn't actually that difficult to write an algorithm that is pretty good at predicting if a text sample could be a fragment of english words..."
msg2 = "This PEP proposes to introduce a syntax to declare the encoding of a Python source file. The encoding information is then used by the Python parser to interpret the file using the given encoding. Most notably this enhances the interpretation of Unicode literals in the source code and makes it possible to write Unicode literals using e.g. UTF-8 directly in an Unicode aware editor.  In Python 2.1, Unicode literals can only be written using the Latin-1 based encoding unicode-escape.  I propose to make the Python source code encoding both visible and changeable on a per-source file basis by using."
key = generate_key(len(msg1))
print len(msg1), len(msg2)
cipher1 = cipher(msg1, key)
cipher2 = cipher(msg2, key)

print_bytearray(cipher1)
print_bytearray(cipher2)

#cribs = ["的", "了", "是", "不", "在", "有", "个", "这", "着", "就", "你", "我",
#         "他", "和", "说", "上", "人", "地", "也", "里", "来", "到", "都", "大"]

cribs = [
    " the ", "be", "to", "of", "and", "a", "in", "that", "have", "I", "it", "for", "not", "on", "with", "he",
    "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an",
    "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get",
    "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", "people",
    "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only",
    "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", "well",
    "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"
]

msg1_2 = cipher(msg1, msg2)
print_bytearray(msg1_2)

for crib in cribs:
    the_crib = bytearray(crib)
    print "============="
    for i in xrange(len(msg1) - len(the_crib)):
        guess = cipher(the_crib, msg1_2[i:i+len(the_crib)])
        print_bytearray(guess)
