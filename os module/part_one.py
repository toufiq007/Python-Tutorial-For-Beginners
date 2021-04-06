import os
import shutil

# os.getcwd()
# os.chdir()
# os.listdir()
# os.path.join(os.getcwd(),files)
# print(os.getcwd())
# os.mkdir('movies')
# print(os.path.exists('movies'))



# if os.path.exists('movies'):
#     print('already exits')

# else:
#     print('not exits')

# os.mkdir('os module/movies')


# open('first.txt','a').close()

# os.chdir() // this method change the current directory

# print(os.listdir())


# for item in os.listdir():
#     path = os.path.join(os.getcwd(),item)
#     print(path)



# os.walk() functions

filelocation = os.walk(r'F:\myfile')

for current_location,folder_name,file_name in filelocation:
    print(f' current location {current_location} ')
    print(f' folder name {folder_name} ')
    print(f' file name {file_name} ')


# os.makedirs('new/another new/index.html')
# os.removedirs('new/another new/index.html')
os.chdir('F:\myfile')
print(os.listdir())

# os.mkdir('new')
# os.rmdir('new')
# os.removedirs('new')



# usign shutill module for deleting a directory which is not empty
# shutil.rmtree('new')
# shutil.copytree('new')

print(os.getcwd())
# os.mkdir('new')
# os.mkdir('document')

# shutil.copytree('new','document/new')
# os.rmdir('new')
print(os.listdir())
# os.mkdir('another_new')

# shutil.move('another_new','document')
print(os.listdir())


