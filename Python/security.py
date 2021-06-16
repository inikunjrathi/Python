import cv2
import time
import dropbox
import random

start = time.time()


def take_image():
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    number = random.randint(1, 10000)
    while result:
        ret, frame = videoCaptureObject.read()
        imageName = "pic" + str(number) + ".jpg"
        number = number + 1
        cv2.imwrite(imageName, frame)
        start = time.time()
        result = False

    return imageName
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_image(image):
    access_token = "*******************************************************************"
    file_from = image
    file_to = "/security" + (image)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded successfully...")


def main():
    print("Starting Upload...")
    while True:
        if (time.time() - start) >= 10:
            print("say cheese!!!")
            image = take_image()
            upload_image(image)


main()
