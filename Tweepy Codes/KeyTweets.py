import tweepy
from TwitterOAuth import OAuthVerifier

class MyStreamListener(tweepy.StreamListener):
    # Class inheriting StreamListener of tweepy module

    def on_status(self, status):
        '''
        Objective: To print text stream of tweets
        Input Parameters:
            self (implicit parameter) - object of type
            MyStreamListener
            status - string value representing tweet
        Return Value: None
        '''
        print(status.text)
    
    def on_error(self, status):
        '''
        Objective: To disconnect the stream by returning False
        if error 420 occurs
        Input Parameters:
            self (implicit parameter) - object of type
            MyStreamListener
            status - int value representing error code
        Return Value: result - int
        '''
        if status==420:
            return False

def main():
    '''
    Objective: To print streaming data containing given keywords
    Input Parameter: None
    Return Value: None
    '''
    api = OAuthVerifier()
    # Creates a stream listener object listenerOb
    listenerOb = MyStreamListener()
    # Create a Stream object
    myStream = tweepy.Stream(api.auth, listenerOb)
    # Starts streaming by specifying search keywords
    searchList = eval(input('Enter search keywords list: '))
    myStream.filter(track = searchList)

if __name__ == '__main__':
    main()
