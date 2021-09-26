import boto3
import time
import cv2
bucket = 'facesmit'

cam=cv2.VideoCapture(0)
count=0
name=input("Enter the name of person:")
idno=input("Enter the id no:")
s3=boto3.client('s3',aws_access_key_id='<AWS_ACCESS_ID>',aws_secret_access_key='<AWS_SECRET_ACCESS_KEY>',
                region_name='ap-south-1')
while count<60:
    _,image=cam.read()
    count=count+1
    cv2.imwrite("new22.jpg",image)
    s3.upload_file("new22.jpg",bucket,'{}_{}/{}.jpg'.format(name,idno,count))
    print("Uploaded image {} of {}".format(count,name))
print("{} added sucessfully to database".format(name))
cam.release()
print("Succesfully added {}".format(name))