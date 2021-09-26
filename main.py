import entryprogram
import exitprogram
import boto3
status=[0,0,0,0,0,0]
names=6*["unassigned"]
rek_client=boto3.client('rekognition',
                        aws_access_key_id='<AWS KEY ID HERE>',       aws_secret_access_key='<AWS SECRET ACCESS KEY HERE>'
                            ,region_name='ap-south-1')
s3=boto3.client('s3',aws_access_key_id='<AWS KEY ID HERE>',    aws_secret_access_key='<AWS SECRET ACCESS KEY HERE>'
                    ,region_name='ap-south-1')
while True:
    choice=input()    #using RPi.GPIO's GPIO.INPUT() we can take input from switch
    if choice=="entry":
        entryprogram.run(status,names,s3,rek_client)
    
    elif choice=="exit":
        exitprogram.run(status,names,s3,rek_client)

'''
import entryprogram
import exitprogram
import RPI.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.IN)
GPIO.setup(7,GPIO.IN)
status=[0,0,0,0,0,0]
names=6*["unassigned"]
while True:
    #using RPi.GPIO's GPIO.INPUT() we can take input from switch
    if GPIO.input(5):
        entryprogram.run(status,names)
    
    elif GPIO.input(7):
        exitprogram.run(status,names)
'''