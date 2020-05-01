import os
import errno

# You might need to adjust this path depending on your locale
dir = os.path.expanduser('~') + "\Documents\Rockstar Games\Red Dead Redemption 2\Profiles"
print("Opening %s" % dir)

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def convert(name, path):
    in_filename = path + "/" + name
    out_filename = "Images/" + name + '.jpg'
    print("Converting %s " % in_filename)
    with open(in_filename, 'rb') as in_file:
        statinfo = os.stat(in_filename)
        with open(out_filename, 'wb') as out_file:
            out_file.write(in_file.read()[300:])
            os.utime(out_filename, (statinfo.st_atime, statinfo.st_mtime))

mkdir_p( "Images" )

for folderName in os.listdir(dir):
        folder = dir + "\\" + folderName
        for filename in os.listdir(folder):
                if(filename.startswith( 'PRDR' )):
                        convert(filename, folder)
