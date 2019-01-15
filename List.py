import os
from fnmatch import fnmatch
import face_recognition
from PIL import Image
from shutil import move, copy2

picture_of_me = face_recognition.load_image_file("/Users/nirmal/Downloads/CNN Faces/Test Images/test.png")
my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

root = "/Users/nirmal/Downloads/OneDrive_2_1-7-2019/2018/Japan/Reshma's 10th Birthday"
pattern = "*.png"
pattern2 = "*.PNG"
pattern3 = "*.JPG"
destination = "/Users/nirmal/Downloads/CNN Faces/Temp"
destination2 = "/Users/nirmal/Downloads/CNN Faces/Nirmal"
count = 1

fileList = []
tempFileList = []


for path, subdirs, files in os.walk(root):
    for name in files:
        #print os.path.join(path, name)
        fileList.append(os.path.join(path, name))


for x in fileList:
    if fnmatch(x, pattern) or fnmatch(x, pattern2) or fnmatch(x, pattern3):
        unknown_picture = face_recognition.load_image_file(x)
        face_locations = face_recognition.face_locations(unknown_picture)

        if len(face_locations) != 1:

            for face_location in face_locations:

                # Print the location of each face in this image
                top, right, bottom, left = face_location
                #print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

                # You can access the actual face itself like this:
                face_image = unknown_picture[top:bottom, left:right]
                pil_image = Image.fromarray(face_image)
                #pil_image.show()
                filename = str(count) + ".png"
                pil_image.save(filename)
                move(filename, destination)
                count += 1


            count = 1
            for path, subdirs, files in os.walk(destination):
                for name in files:
                    #print os.path.join(path, name)
                    tempFileList.append(os.path.join(path, name))

            for y in tempFileList:
                if fnmatch(y, pattern) or fnmatch(y, pattern2) or fnmatch(y, pattern3):
                    unknown_picture2 = face_recognition.load_image_file(y)
                    face_locations2 = face_recognition.face_locations(unknown_picture2)

                    unknown_face_encoding = face_recognition.face_encodings(unknown_picture2)[0]
                    results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

                    print(x)

                    if results[0] == True:
                        print(y)
                        print("It's a picture of me!")
                        copy2(x, destination2)
                    else:
                        print(y)
                        print("It's not a picture of me!")


            for the_file in os.listdir(destination):
                file_path = os.path.join(destination, the_file)
                if os.path.isfile(file_path):
                    os.unlink(file_path)

             tempFileList = []

        else:
            unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
            results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)

            if results[0] == True:
                print(x)
                print("It's a picture of me!")
                copy2(x, destination2)
            else:
                print(x)
                print("It's not a picture of me!")
