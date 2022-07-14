import boto3

s3 = boto3.resource("s3")

for bucket in s3.buckets.all():
    print(bucket.name)


with open("index.jpeg", "rb") as image:
    s3.Bucket("pvv-athena").put_object(Key="cat.jpeg", Body=image)
