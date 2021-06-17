import tweepy
import time

twitterTokens = {
                'consumerKey':'',
                'consumerSecret':'',
                'accessToken':'',
                'accessTokenSecret':''
}

searchKeywords = "utfpr -from:utfpr_ -from:ContadorUTFPR"

def main():
    #autentica no twitter e inicia a API
    auth = tweepy.OAuthHandler(twitterTokens['consumerKey'],twitterTokens['consumerSecret'])
    auth.set_access_token(twitterTokens['accessToken'],twitterTokens['accessTokenSecret'])
    api = tweepy.API(auth)

    #Procura o ID do ultimo tweet retuitado
    sinceFile = open('since.txt','r+')
    sinceId = sinceFile.read()
    if sinceId[-1] == '\n':
        sinceId = sinceId[0:(len(sinceId)-1)]

    tweets = api.search(searchKeywords,since_id=sinceId)

    for tweet in tweets:
        api.retweet(tweet.id)
        time.sleep(5)

    if tweets:
        sinceFile.seek(0)
        sinceFile.truncate()
        sinceFile.write(tweets[0].id_str)
    sinceFile.close()

if __name__ == '__main__':
    main()
