import os

def main(asset, directory):
    
    # read output.ses
    ses_path = os.path.join(asset,"output.ses")
    
    # instead {0} of 'directory'
    with open(ses_path, 'r') as file:
        filedata = file.read()

    newdata = filedata.replace('{0}', directory)

    # new output.ses in 'directory'
    new_file_path = os.path.join(directory,'output.ses')

    with open(new_file_path, 'w') as file:
        file.write(newdata)

