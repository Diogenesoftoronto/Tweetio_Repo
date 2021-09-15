import os
from searchtweets import ResultStream, gen_request_parameters, load_credentials, collect_results
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    #note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
    #from vaderSentiment import SentimentIntensityAnalyzer

search_args = load_credentials(os.environ['PATH'],
                                       yaml_key="search_tweets_v2",
                                       env_overwrite=False)
query = gen_request_parameters("snow", results_per_call=100, granularity=None)
print(query)

tweets = collect_results(query,
                         max_tweets=100,
                         result_stream_args=search_args)   # change this if you need to
[print(tweet, end='\n\n') for tweet in tweets[0:10]]

print(tweets[0]["data"][0]['text'])
twitter_list = [tweet for tweet in tweets[0]["data"]]
print(twitter_list[1]['text'])
analyzer = SentimentIntensityAnalyzer()

for item in range(len(twitter_list)):
    vs = analyzer.polarity_scores(twitter_list[item]['text'])
    print(vs)
