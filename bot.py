import tweepy

consumer_key = 'consumer key'
consumer_secret = 'consumer secrets'
access_token = 'access token'
access_token_secret = 'access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)
print(user.location)

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        # Reply
        print('\nTweet by: @' + tweet.user.screen_name)
        print('ID: @' + str(tweet.user.id))
        tweetId = tweet.user.id
        username = tweet.user.screen_name
        api.update_status("@" + username + " " + phrase, in_reply_to_status_id=tweetId)
        print("Replied with " + phrase)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
