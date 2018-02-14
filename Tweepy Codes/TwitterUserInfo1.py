import tweepy
from TwitterOAuth import OAuthVerifier

def getUserStatistics(user):
    '''
    Objective: To get user statistics using various
            variables of the api
    Input Parameter: user - string
    Return Value: None
    '''
    print('\nName: ', user.name)
    print('Screen Name: ', user.screen_name)
    print('ID: ', user.id)
    print('Account creation date and time: ', user.created_at)
    print('Location: ', user.location)
    print('Description: ', user.description)
    print('No. of followers: ', user.followers_count)
    print('No. of friends: ', user.friends_count)
    print('No. of favourite tweets: ', user.favourites_count)
    print('No. of posted tweets: ', user.statuses_count)
    print('Associated URL: ', user.url)

def main():
    '''
    Objective: To collect user information
    Input Parameter: None
    Return Value: None
    '''
    # To print user's information
    api = OAuthVerifier()
    # Authenticated User
    user = api.me()
    getUserStatistics(user)
    # Different User
    name = input('\n\nEnter the user identification: ')
    user = api.get_user(name)
    getUserStatistics(user)

if __name__ == '__main__':
    main()
