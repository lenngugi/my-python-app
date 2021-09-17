try:
   file= open("king,docx","w")
   file.write("hello there, here is your info")
   print("file created succefully")
except IOError:
    print("sorry, we dont manage creating your file")
    