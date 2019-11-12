import os
import errno

# You might need to adjust this path depending on your locale
dir = os.path.expanduser('~') + "\Documents\Rockstar Games\Red Dead Redemption 2\Profiles"

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def convert(name, path):
    with open(path + "/" + name, 'rb') as in_file:
        with open("Images/" +name + '.jpg', 'wb') as out_file:
            out_file.write(in_file.read()[300:])

mkdir_p( "Images" )

for folderName in os.listdir(dir):
        folder = dir + "\\" + folderName
        for filename in os.listdir(folder):
                if(filename.startswith( 'PRDR' )):
                        convert(filename, folder)