with open("test.txt", "w") as f:
 f.write("Hello TY-D Students!")
with open("test.txt", "r") as f:
 content = f.read()
 print("File content:", content)

 # Copy File Content

with open("demo.txt","r")as f1, open("copy.txt","w") as f2:
    f2.write(f1.read())