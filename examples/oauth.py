import tweepy

# == OAuth Authentication ==
#
# This mode of authentication is the new preferred way
# of authenticating with Twitter.

# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
consumer_key="6d2aoD5ptPg94kaxI5VuNwFf7"
consumer_secret="8YVHd0xZruGPuqX3JZEMLTRXdc2VE391GAt2YrBTyKRVKMEbI2"

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located
# under "Your access token")
access_token="1231276706998235136-oUAPoZW4NbcY2EnoKlUfROaP7a0xN0"
access_token_secret="H3icYpCxPNXty1s9NhUb47STlXUvRqvoCS1MvRPkE35ok"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# If the authentication was successful, you should
# see the name of the account print out
print(api.me().name)

# If the application settings are set for "Read and Write" then
# this line should tweet out the message to your account's
# timeline. The "Read and Write" setting is on https://dev.twitter.com/apps
api.update_status(status='Updating using OAuth authentication via Tweepy!')
