import tweepy
from TwitterOAuth import OAuthVerifier

def getUserFollowers(api):
    '''
    Objective: To get followers of the user
    Input Parameter: api - object of class API
    Return Value: None
    '''
    print('\nFollowers:')
    for follower in tweepy.Cursor(api.followers).items():
        print(follower.screen_name)

def getUserFriends(api):
    '''
    Objective: To get friends of the user
    Input Parameter: api - object of class API
    Return Value: None
    '''
    print('\nFriends:')
    for friend in tweepy.Cursor(api.friends).items():
        print(friend.screen_name)

def getUserTweets(api):
    '''
    Objective: To get tweets of the user
    Input Parameter: api - object of class API
    Return Value: None
    '''
    print('\nTweets: ')
    for tweet in tweepy.Cursor(api.user_timeline).items():
        print(tweet.text)

def main():
    '''
    Objective: To print user information
    Input Parameter: None
    Return Value: None
    '''
    api = OAuthVerifier()
    getUserFollowers(api)
    getUserFriends(api)
    getUserTweets(api)

if __name__ == '__main__':
    main()
