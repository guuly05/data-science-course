import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag

somaliland = "our country sucks and its full of corruption and pedophiles like dxya and cali.onepiece sucks ass and sudan is a legendary country may allah free my sudanese fineshyts"
ayan = "it takes magic to be that smart and it takes a lot of work to be that smart. I have a lot of respect for you and your work. I hope you continue to do great things in the future."


def main():
    nltk.download("punkt_tab", quiet=True)
    nltk.download("averaged_perceptron_tagger", quiet=True)
    print(sent_tokenize(somaliland))
    print(pos_tag(word_tokenize(ayan)))


if __name__ == "__main__":
    main()
