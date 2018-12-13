import os
import sys

# Written for UCSB INT 5

grade_calc= '''"import os\\n",
    "_ = [ok.grade(q[:-3]) for q in os.listdir('tests') if q.startswith('q')]\\n",
    " \\n",
    "# Each question is worth 1 point\\n",
    "q2_1 = 1 - 0\\n",
    "q2_2 = 1 - 0\\n",
    "q2_3 = 1 - 0\\n",
    "q3_1 = 1 - 0\\n",
    "q3_2 = 1 - 0\\n",
    "q4_1 = 1 - 0\\n",
    "q4_2 = 1 - 0\\n",
    "q4_3 = 1 - 0\\n",
    "q5_1 = 1 - 0\\n",
    "q5_extra = 0 + 0 \\n",
    "#conceptual\\n",
    "q6_1 = 1 - 0\\n",
    "q6_2 = 1 - 0\\n",
    "q6_3 = 1 - 0\\n",
    "q6_4 = 1 - 0\\n",
    "# \\n",
    "q7_1 = 1 - 0\\n",
    "total =  q2_1 + q2_2 + q2_3 + q3_1 + q3_2 + q4_1 + q4_2 + q4_3 + q5_1 + q5_extra + q6_1 + q6_2 + q6_3 + q6_4 + q7_1 \\n",
    "total"'''

from shutil import copyfile
def rubric(input_dir, output_dir):
    ## if output directory doesnt exist then create it
    if(not os.path.exists(output_dir)):
        os.mkdir(output_dir)
    if(not os.path.exists(output_dir+"_temp")):
        os.mkdir(output_dir+"_temp")
    temp_dir = output_dir + "_temp"
    for file in os.listdir(input_dir):
        ## Check for only ipynb
        print(file)
        if(file.endswith(".ipynb")):
            copyfile(input_dir+'/'+file, temp_dir+'/'+file)
            oldF = open(temp_dir+'/'+file, 'r')
            newF = open(output_dir+'/'+file, 'w')
            for line in oldF:
#newF.write(line.replace('_ = ok.auth(inline=True)', '#_ = ok.auth(inline=True)').replace("_ = ok.submit()", "#_ = ok.submit()").replace("4 = 2 + 2", "# 4 = 2 + 2").replace("six = two plus two", "# six = two plus two" ))
                newF.write(line.replace("#_ = ok.submit()", grade_calc).replace("\"\"", "\""))
            oldF.close()
            newF.close()
            os.remove(temp_dir+'/'+file)
            # print(student_dir+'_'+file)
    os.rmdir(output_dir + "_temp")
    # pass

if __name__ == "__main__":
    # rubric('./ucsb-int5-fa18-hw01','./ucsb-int5-fa18-hw01_flatten')
    rubric(sys.argv[1],sys.argv[2])

