"""fname = input("File name: ")
name = fname.lower()

if ".gif" in name:
    print("image/gif")

elif ".jpg" in name:
    print("image/jpeg")

elif ".jpeg" in name:
    print("image/jpeg")

elif ".png" in name:
    print("image/png")

elif ".pdf" in name:
    print("application/pdf")

elif ".txt" in name:
    print("text/plain")

elif ".zip" in name:
    print("application/zip")

else:
    print("application/octet-stream")"""



fname = input("File name: ")
name = fname.lower()

new_name, extension = name.split(".")

match extension:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "jpg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")



