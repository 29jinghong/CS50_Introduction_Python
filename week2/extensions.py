answer = input("File name: ").strip()
if answer.endswith(".gif"):
    print("image/gif")
elif answer.endswith(".jpg"):
    print("image/jpeg")
elif answer.endswith(".jpeg"): 
    print("image/jpeg")
elif answer.endswith(".png"):
    print("image/png")
elif answer.endswith(".pdf"):
    print("application/pdf")
elif answer.endswith(".txt"):
    print("text/plain")
elif answer.endswith(".zip"):
    print("application/zip")
else:
    print("sorry we cant identify this type of file rn.")
