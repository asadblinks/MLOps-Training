import boto3
import os
s3 = boto3.resource("s3")
bucket = s3.Bucket("mlops-aws-asad")
for each in bucket.objects.all():
    print(each.key)

print(os.environ["AWS_ACCESS_KEY_ID"])
print(os.environ["AWS_SECRET_ACCESS_KEY"])