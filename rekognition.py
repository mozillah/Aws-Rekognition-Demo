import csv
import boto3
with open('credentials.csv','r' ) as input:
	next(input)
	reader = csv.reader(input)
	for line in reader:
		access_key_id  = line[0]
		secret_access_key = line[1]
print(access_key_id)
print(secret_access_key)
session = boto3.Session(profile_name='ubuntu',aws_access_key_id=access_key_id,aws_secret_access_key=secret_access_key)

print(session)
photo='test.jpg'

client =session.client('rekognition',region_name='us-east-2')
# client =boto3.client('rekognition',aws_access_key=access_key_id,aws_secret_access_key=secret_access_key)

with open(photo,'rb') as source_image:
    source_bytes = source_image.read()

response = client.detect_labels(Image={'Bytes':source_bytes},MaxLabels=10)
rekognition_response = client.detect_faces(Image={'Bytes': source_bytes}, Attributes=['ALL'])
                           
print(rekognition_response)
# print(response)


