import openapi_client
import time
from openapi_client.rest import ApiException

with openapi_client.ApiClient() as api_client:
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
                print("Working on task %s for %s with tweet \"%s\"" % (task.id, task.topic_name, task.variables["tweet"].value))
                complete_task_body = {
                    "workerId" : "pyworker"
                }

                try:
                    external_tasks_client.complete_external_task_resource(task.id, complete_external_task_dto=complete_task_body)
                except ApiException as e:
                    print("Completing Task failed; %s\n" % e)

                print("Done!")
        else:
            print("Idling...")
            time.sleep(1)
