import os
import sys

# Author: Sierra Schwellenbach
# Written for UCSB INT 5

from shutil import copyfile
def flatten(input_dir, output_dir):
    ## if output directory doesnt exist then create it
    if(not os.path.exists(output_dir)):
        os.mkdir(output_dir)
    if(not os.path.exists(output_dir+"_temp")):
        os.mkdir(output_dir+"_temp")
    for student_dir in os.listdir(input_dir):
        temp_dir = output_dir + "_temp"
        ## Check if the student_dir is a directory
        if(os.path.isdir(input_dir+'/'+student_dir)):
            for submission_dir in os.listdir(input_dir+'/'+student_dir):
                ## check if the submission_dir is a directory
                if (os.path.isdir(input_dir + '/' + student_dir+'/'+submission_dir)):
                    for file in os.listdir(input_dir+'/'+student_dir+'/'+submission_dir):
                        ## Check for only ipynb
                        if(file.endswith(".ipynb")):
                            copyfile(input_dir+'/'+student_dir+'/'+submission_dir+'/'+file,temp_dir+'/'+student_dir+'_'+file)
                            oldF = open(temp_dir+'/'+student_dir+'_'+file, 'r')
                            newF = open(output_dir+'/'+student_dir+'_'+file, 'w')
                            for line in oldF:
                                newF.write(line.replace('_ = ok.auth(inline=True)', '#_ = ok.auth(inline=True)').replace("_ = ok.submit()", "#_ = ok.submit()"))
                            oldF.close()
                            newF.close()
                            os.remove(temp_dir+'/'+student_dir+'_'+file)
                            # print(student_dir+'_'+file)
    os.rmdir(output_dir + "_temp")
    # pass

if __name__ == "__main__":
    # flatten('./ucsb-int5-fa18-hw01','./ucsb-int5-fa18-hw01_flatten')
    flatten(sys.argv[1],sys.argv[2])
