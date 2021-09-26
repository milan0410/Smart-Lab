
import cv2 
import time
import boto3
from datetime import datetime
import node
import turn
def run(status,names,s3,rek_client):
    #door.unlock()
    P=cv2.VideoCapture(0)
    collectionId='mycollection' #collection name
    '''
    rek_client=boto3.client('rekognition',aws_access_key_id='<AWS_SECRET_ID>',aws_secret_access_key='<AWS_SECRET_ACCESS_KEY>'
                            ,region_name='ap-south-1')
    s3=boto3.client('s3',aws_access_key_id='<AWS_SECRET_ID>',            aws_secret_access_key='<AWS_SECRET_ACCESS_KEY>'
                    ,region_name='ap-south-1')'''
    while True:
        #camera warm-up time
        print("Image is getting captured") #speaker.announce()
        time.sleep(2)
        result=True
        while(result):
            ret,image=P.read() #capture an image
            img="/home/pi/Exiter_images/{}.jpg".format(datetime.now())
            cv2.imwrite(img,image)
            s3.upload_file(img,'facesmit',"Z_Sample/sample.jpg")
            result=False
            print("Image captured successfully")  #speaker.announce()
        try:#match the captured imges against the indexed faces
            match_response = rek_client.search_faces_by_image(CollectionId=collectionId, Image={'S3Object': { 'Bucket': 'facesmit','Name': "Z_Sample/sample.jpg"}}, MaxFaces=1, FaceMatchThreshold=95)
            if match_response['FaceMatches']:
                name=match_response['FaceMatches'][0]['Face']['ExternalImageId']
                print("Person detected is ",name.split("_")[0])
                n=node.deassign(status,names,name)
                print(name.split("_")[0]," exited and node {} is deassigned ".format(n)) #speaker.announce()
                turn.off(n)
                f=open("records.txt","a")
                f.write("{} exited lab at {}\n".format(name,datetime.now()))
                f.close()
                #door.lock()
                break
            else:
                print('Please retry exiting ')
                break
        except:
            print('No face detected')
    P.release()
