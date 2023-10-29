import tweepy

# 트위터 개발자 계정에서 얻은 키들을 아래에 입력하세요.
def tweets_crawling(consumer_key, consumer_secret, access_token, access_token_secret, keyword):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    # 특정 키워드가 포함된 트윗을 검색합니다. 
    public_tweets = api.search(q=keyword, lang="ko", count=5)

    for tweet in public_tweets:
        print(tweet.text)
