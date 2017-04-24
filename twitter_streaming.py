#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = "819236308224770048-OXlMIBMQuz83yitBfdjchFx19inuFCQ"
access_token_secret = "7XrLl6TC2s7moBZIqxJgtp7VVARapM8KIn1QuX60aT3gq"
consumer_key = "hmZLTSjkfA7SXSbw7PtJQjrno"
consumer_secret = "obydPLpDNmTCG3W1HlnKbmdqbb8X2VQMkhSTyjm6w3m2macqqR"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    #stream.filter(track=['flu', 'sick', 'ill', 'unwell', 'miserable', 'illness', 'sickness', 'doctor', 'hospital', 'virus', 'disease', 'medicine', 'influenza'])
    #stream.filter(track=['I' and 'have' and 'the' and 'flu'])
    stream.filter(track=['I have the flu'])

    print(stream)