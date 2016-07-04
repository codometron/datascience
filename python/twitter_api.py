# Use Twitter API 

import yaml
import twitter
import json

credentials = yaml.load(open('cred_file.yml'))
twitter_key= credentials['twitter_key']
twitter_secret =credentials['twitter_secret']
token = credentials['twitter_token']
token_secret=credentials['twitter_tokensecret']
auth=twitter.oauth.OAuth(token,token_secret,twitter_key,twitter_secret)
twitter_api =twitter.Twitter(auth=auth)
search_string='#adele'
count =10
search_results = twitter_api.search.tweets(q=search_string,count=count)
search_results['search_metadata']
type(search_results['statuses'])
print json.dumps(search_results['statuses'][0],sort_keys=True,indent=4,separators=(',',':'))
