def main():

    extension= input("File Name: ")

    if extension.endswith(".gif"):
        print("image/gif")

    elif extension.endswith(".jpeg") or extension.endswith(".jpg"):
        print("Image/jpeg")
    else:
        print("application/octet-stream")
    
main()

