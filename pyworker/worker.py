import openapi_client
import time
import twitter
from openapi_client.rest import ApiException

def connectTwitterApi() :
    twitter

def publishTweet(tweet, twitter_api) :
    twitter_api.PostUpdate(tweet)

def beautifyTweet(tweet, twitter_api) :
    trends = twitter_api.GetTrendsCurrent()
    tweet = tweet + ", #cugdd presents a twitter trend:" + trends[9].name
    return tweet

with openapi_client.ApiClient() as api_client:

    twitter_api = twitter.Api(consumer_key='lRhS80iIXXQtm6LM03awjvrvk',
                      consumer_secret='gabtxwW8lnSL9yQUNdzAfgBOgIMSRqh7MegQs79GlKVWF36qLS',
                      access_token_key='220324559-jet1dkzhSOeDWdaclI48z5txJRFLCnLOK45qStvo',
                      access_token_secret='B28Ze8VDucBdiE38aVQqTxOyPc7eHunxBVv7XgGim4say')

    external_tasks_client = openapi_client.ExternalTaskApi(api_client)
    fetch_and_lock_body = {
        "workerId" : "pyworker",
        "maxTasks" : 1,
        "topics" : [
            {
                "topicName" : "cugdd.tweet.publish",
                "lockDuration" : 3000
            },
            {
                "topicName" : "cugdd.tweet.beautify",
                "lockDuration" : 3000
            }
        ]
    }

    while True:
        try:
            tasks = external_tasks_client.fetch_and_lock(fetch_external_tasks_dto=fetch_and_lock_body)
        except ApiException as e:
            print("Fetch and Lock failed; %s" % e)

        if tasks :
            for task in tasks:
                
                if task.topic_name == "cugdd.tweet.publish" :
                    print("Publishing tweet \"%s\"" % task.variables["tweet"].value)
                    publishTweet(task.variables["tweet"].value, twitter_api)
                    try:
                        complete_task_body = {
                            "workerId" : "pyworker"
                        }
                        external_tasks_client.complete_external_task_resource(task.id, complete_external_task_dto=complete_task_body)
                    except ApiException as e:
                        print("Completing Task failed; %s\n" % e)

                elif task.topic_name == "cugdd.tweet.beautify" :
                    tweet = beautifyTweet(task.variables["tweet"].value, twitter_api)
                    try:
                        complete_task_body = {
                            "workerId" : "pyworker",
                            "variables": {"tweet": {"value": tweet}}
                        }
                        external_tasks_client.complete_external_task_resource(task.id, complete_external_task_dto=complete_task_body)
                    except ApiException as e:
                        print("Completing Task failed; %s\n" % e)

                print("Working on task %s for %s with tweet \"%s\"" % (task.id, task.topic_name, task.variables["tweet"].value))
                
                complete_task_body = {
                    "workerId" : "pyworker"
                }   
        else:
            print("Idling...")
            time.sleep(1)
