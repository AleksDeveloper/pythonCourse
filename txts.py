"""n = 1
finalFile = "que soy"
while n < 4:
    f = open("files/file"+str(n)+".txt", "r")
    print(f.readlines())
    #finalFile = str(f.readlines())
    n += 1
print("FINAL: "+finalFile)

while n < 4:
    with open("files/file"+str(n)+".txt", "r") as lista:
        finalFile = lista.readlines()
    print("IMPRIMO TODAS LAS LINEAS DEL ARCHIVO: \n",finalFile)
    n += 1
print(finalFile)"""

my_files = ["files/file1.txt","files/file2.txt","files/file3.txt"]
with open('file4.txt', 'w') as outfile:
    for i in my_files:
        with open(i) as infile:
            outfile.write(infile.read())
        outfile.write("\n")
        