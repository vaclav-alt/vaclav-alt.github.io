filename = "articles.txt"

print_chars = 50
outfmt = """[{0}] {1}
{2}...
"""


def load_articles_from_file(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()

    articles = {}

    for i in range(0, len(lines), 3):
        id    = lines[i].strip()
        title = lines[i+1].strip()
        text  = lines[i+2].strip()

        articles[id] = (title, text)
    
    return articles


def find_first_occurences(text):
    text_lc = text.lower()
    words   = text_lc.split()
    
    occs = {}
    for word in words:
        if word.isnumeric():
            continue
        pos = text_lc.find(word + " ")
        occs[word] = pos
    return occs


def build_index(articles):
    word_index = {}

    for id, (title, text) in articles.items():
        occs = find_first_occurences(text)

        for word, pos in occs.items():
            if word in word_index:
                word_index[word].append((id, pos))
            else:
                word_index[word] = [(id, pos)]
    return word_index


def search(words, articles, index):
    for word in words:
        entries = index.get(word)
        if entries is not None:
            fail = False
            for id, pos in entries:
                title, text = articles[id]
                print(outfmt.format(id, title, text[pos:pos+print_chars]))

        else:
            print(f"no search results for {word}\n")


articles = load_articles_from_file(filename)
word_index = build_index(articles)

while True:
    usrinput = input("Search for: ")
    print()
    if usrinput == "":
        break
    
    words = usrinput.split()
    search(words, articles, word_index)
    print("-"*30)
