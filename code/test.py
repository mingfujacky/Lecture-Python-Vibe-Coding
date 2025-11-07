# 輸入一個句子，然後計算該句子內的字數，還有最長的字是哪一個
def analyze_sentence(sentence):
    words = sentence.split()
    word_count = len(words)
    longest_word = max(words, key=len) if words else ""
    return word_count, longest_word

input_sentence = input("請輸入一個句子: ")
count, longest = analyze_sentence(input_sentence)
print(f"字數: {count}, 最長的字: {longest}")


def hanio_tower(n, source, target, auxiliary):
    if n == 1:
        print(f"將碟片從 {source} 移動到 {target}")
    else:
        hanio_tower(n-1, source, auxiliary, target)
        print(f"將碟片從 {source} 移動到 {target}")
        hanio_tower(n-1, auxiliary, target, source)

a = 1
b = 2
if a < b:
    print("a 小於 b")
else:
    print("a 不小於 b")        