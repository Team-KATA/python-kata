from transformers import pipeline
pipe_translation_ko_en = pipeline("translation", model="circulus/kobart-trans-ko-en-v2")
pipe_senti = pipeline("sentiment-analysis")

def sentiment_analysing(text):
  dic = pipe_translation_ko_en(text ,max_length=1000)
  translated = dic[0]["translation_text"]
  return pipe_senti(translated)
