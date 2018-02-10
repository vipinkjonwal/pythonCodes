import tweepy
from TwitterOAuth import OAuthVerifier

def getUserFollowers(api):
    '''
    Objective: To get followers of the user
    Input Parameter: api - object of class API
    Return Value: None
    '''
    print('\nFollowers:')
    for follower in api.followers():
        print(follower.screen_name)
    
def getUserFriends(api):
    '''
    Objective: To get friends of the user
    Input Parameter: api - object of class API
    Return Value: None
    '''
    print('\nFriends:')
    for friend in api.friends():
        print(friend.screen_name)
        
def getUserTweets(api):
    '''
    Objective: To get tweets of the user
    Input Parameter: api - object of class API
    Return Value: None
    '''
    print('\nTweets: ')
    for tweet in api.user_timeline():
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
