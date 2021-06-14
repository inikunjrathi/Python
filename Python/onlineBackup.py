import dropbox


class uploadFiles:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, "rb") as f:
            dbx.files_upload(f.read(), file_to)


def main():
    access_token = "******"
    uploadF = uploadFiles(access_token)

    file_from = input(
        "Enter the full path of file including the file name you want to backup: "
    )
    file_path = file_from.split("/")
    file_name = file_path[len(file_path) - 1]
    file_to = "/" + file_name

    uploadF.upload(file_from, file_to)
    print("Backup created successfully for " + file_name)


main()
