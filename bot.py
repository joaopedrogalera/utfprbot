import tweepy
import time

twitterTokens = {
                '',
                '',
                '',
                ''
}

searchKeywords = "utfpr"

def getLastRetweet(api):

    #Pega os últimos 20 tweets e retorna o ID do RT mais recente. Se nenhum dos 20 for RT, pega o ID do último tweet
    tweets = api.user_timeline()
    sinceId = ''

    for tweet in tweets:
        if sinceId == '':
            try:
                sinceId = tweet.retweeted_status.id_str
            except:
                pass

    if sinceId == '':
        sinceId = tweets[0].id_str

    return(sinceId)

def main():
    #autentica no twitter e inicia a API
    auth = tweepy.OAuthHandler(twitterTokens['consumerKey'],twitterTokens['consumerSecret'])
    auth.set_access_token(twitterTokens['accessToken'],twitterTokens['accessTokenSecret'])
    api = tweepy.API(auth)

    #Procura o ID do ultimo tweet retuitado
    sinceId = getLastRetweet(api)

    tweets = api.search(searchKeywords,since_id=sinceId)

    for tweet in tweets:
        api.retweet(tweet.id)
        time.sleep(1)

if __name__ == '__main__':
    main()
