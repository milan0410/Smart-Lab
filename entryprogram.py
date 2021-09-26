
import cv2 
import time
import boto3
from datetime import datetime
import node
import turn

def run(status,names,s3,rek_client):
    if node.available(status)==0:
        print("Lab is full")
    else:
        P=cv2.VideoCapture(0)
        collectionId='mycollection' #collection name
        '''rek_client=boto3.client('rekognition',
                        aws_access_key_id='<AWS_KEY_ID>',       aws_secret_access_key='<AWS_SECRET_ACCESS_KEY>'
                            ,region_name='ap-south-1')
        s3=boto3.client('s3',aws_access_key_id='<AWS_KEY_ID>',    aws_secret_access_key='<AWS_SECRET_ACCESS_KEY>'
                    ,region_name='ap-south-1') '''
        while True:
            
            print("Image is getting captured")
            #speaker.announce("Face is getting captured")
            time.sleep(2) #camera warm-up time
            result=True
            while(result):
                ret,image=P.read() #capture an image
                img="/home/pi/Accesser_images/{}.jpg".format(datetime.now())
                cv2.imwrite(img,image)
                s3.upload_file(img,'facesmit',"Z_Sample/sample.jpg")
                result=False
                print("Image captured successfully")
                #speaker.announce("Image captured successfully")
            try: #match the captured imges against the indexed faces
                match_response = rek_client.search_faces_by_image(CollectionId=collectionId, Image={'S3Object': { 'Bucket': 'facesmit','Name': "Z_Sample/sample.jpg"}}, MaxFaces=1, FaceMatchThreshold=95)
                if match_response['FaceMatches']:
                    name=match_response['FaceMatches'][0]['Face']['ExternalImageId']
                    similarity=match_response['FaceMatches'][0]['Similarity']
                    print("Person detected is ",name.split("_")[0])
                    #speaker.announce("Person detected is"+ {}".format(name.split("_")[0]))
                    #print("Similarity : ",similarity)
                    n=node.assign(status,names,name)
                    print(name.split("_")[0]," is assigned node ",n)
                    #speaker.announce("{} go to node {}".format(name.split("_")[0],n))
                    #door open
                    turn.on(n)
                    #door closed
                    f=open("records.txt","a")
                    f.write("{} is assigned node {} at {}\n".format(name,n,datetime.now()))
                    f.close()
                    return
                else:
                    print('You cannot be assigned any node,please register yourself, first ')
                    break
            except:
                print('No face detected')
        P.release()
