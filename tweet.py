import tweepy

def store_last_id(tweet_id):
    """ Stores a tweet id in text file """
    with open('lastid', 'w') as fp:
        fp.write(str(tweet_id))


def get_last_id():
    """ Retrieve the list of tweets that were
    already retweeted """

    with open('lastid') as fp:
        return fp.read()

if __name__ == '__main__':

    auth = tweepy.OAuthHandler("your_consumer_key", "your_consumer_key_secret")
    auth.set_access_token("your_access_token", "your_access_token_secret")

    api = tweepy.API(auth)

    try:
        last_id = get_last_id()
    except FileNotFoundError:
        print("No retweet yet")
        last_id = None

    for tweet in tweepy.Cursor(api.search, q="fedoramagazine.org", since_id=last_id).items():
        if tweet.user.name  == 'Fedora Project':
            store_last_id(tweet.id)
            #tweet.retweet()
            print(f'"{tweet.text}" was retweeted')
