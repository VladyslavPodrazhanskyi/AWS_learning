import boto3

# Get the service resource
sqs = boto3.resource('sqs')


def create_queue(name, delay):
    # Create the queue. This returns an SQS.Queue instance
    queue = sqs.create_queue(QueueName=name, Attributes={'DelaySeconds': delay})
    return queue


if __name__ == '__main__':

    # message_queue = create_queue("test_queue", "5")

    for queue in sqs.queues.all():
        print(queue)
        print(queue.url, queue.attributes.get("DelaySeconds"))

    queue = sqs.get_queue_by_name(QueueName='test_queue')

    # Create a new message
    response = queue.send_message(MessageBody='world')

    # The response is NOT a resource, but gives you a message ID and MD5
    print(response.get('MessageId'))
    print(response.get('MD5OfMessageBody'))
    for k, v in response.items():
        print(k, v)






