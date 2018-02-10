import tweepy

def OAuthVerifier():
    '''
    Objective: To authorize the application to access Twitter
    Input Parameter: None
    Return Value: API object
    '''
    consumerKey = 'iym0XRG0SOgyPOjmlPQgB4XrC'
    consumerSecret = 'I6gBj8RpcXJvN6xaKUUGeTkPEDpHziRXBmT9d9yG8k5Ik0H0bF'
    authorization = tweepy.OAuthHandler(consumerKey, consumerSecret)
    accessToken = '727494459118653446-XWf9MmBJmCUOM7Ic9xvoHlZCBQAWWA1'
    accessSecret = 'jl4UJPXYSC8ygV8EsyNz6fMOW2NEs9NFvJc2InyfXNvve'
    authorization.set_access_token(accessToken, accessSecret)
    api = tweepy.API(authorization)
    return api

def main():
    '''
    Objective: To provide open authentication of application
    Input Parameter: None
    Return Value: None
    '''
    api = OAuthVerifier()
    print('Application authorized')

if __name__ == '__main__':
    main()
