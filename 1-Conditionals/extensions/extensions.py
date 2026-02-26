file = input("File name: ")

if file.endswith(".jpg"):
    print("image/jpeg")
elif file.endswith(".pdf"):
    print("application/pdf")
else:
    print("application/octet-stream")
