import os
import sys

from shutil import copyfile
def flatten(input_dir, output_dir):
    ## if output directory doesnt exist then create it
    if(not os.path.exists(output_dir)):
        os.mkdir(output_dir)
    for student_dir in os.listdir(input_dir):
        ## Check if the student_dir is a directory
        if(os.path.isdir(input_dir+'/'+student_dir)):
            for submission_dir in os.listdir(input_dir+'/'+student_dir):
                ## check if the submission_dir is a directory
                if (os.path.isdir(input_dir + '/' + student_dir+'/'+submission_dir)):
                    for file in os.listdir(input_dir+'/'+student_dir+'/'+submission_dir):
                        ## Check for only ipynb
                        if(file.endswith(".ipynb")):
                            copyfile(input_dir+'/'+student_dir+'/'+submission_dir+'/'+file,output_dir+'/'+student_dir+'_'+file)
                            # print(student_dir+'_'+file)

    # pass

if __name__ == "__main__":
    # flatten('./ucsb-int5-fa18-hw01','./ucsb-int5-fa18-hw0_flatten')
    flatten(sys.argv[1],sys.argv[2])
