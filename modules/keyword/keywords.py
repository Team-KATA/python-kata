from keybert import KeyBERT
from kiwipiepy import Kiwi
from transformers import BertModel
from collections import Counter
from konlpy.tag import Okt

model = BertModel.from_pretrained('skt/kobert-base-v1')
kiwi = Kiwi()
kw_model = KeyBERT(model)


def __noun_extractor(text):
    results = []
    result = kiwi.analyze(text)
    for token, pos, _, _ in result[0][0]:
        if len(token) != 1 and pos.startswith('N') or pos.startswith('SL'):
            results.append(token)
    return results


def keyword_extractor(article_text: str) -> list:
    kiwi.analyze(article_text)
    nouns = __noun_extractor(article_text)
    text = ' '.join(nouns)
    return kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 1), stop_words=None, top_n=30)
