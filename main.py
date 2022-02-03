# CODE IS NOT FUNCTIONAL YET !

import os, re

# find type of OS and return default user directory
def default_path(platform):

    if platform=="nt":
        return os.environ['USERPROFILE']

    else:
        return os.environ['HOME']
        

# fetch path from user for input and output files' location
def getpath(prompt):
    
    # set default path incase user skips path
    default = default_path(os.name)

    #if path entered by user exists, return the path; if input is empty or invalid, return default path
    try:
        path=input(f'''{prompt}''')
        if not os.path.exists(path):
            raise Exception
        return path
    except:
        print(f'''Input skipped or entered path is invalid! 
        Choosing {default} as the path...''')
        return default

''' Read files and generate md file in the format

'1. <first comment in file> as title 
The rest as code block'

and do for all code files in that directory
'''
def generate_md():

    default = default_path(os.name)

    input_prompt=(f'''Enter directory path where files exist
    Skipping would choose {default}
    Enter here >  ''')

    input_path=getpath(input_prompt)

    ext=input('''Enter file extension to be considered (.c or .py)
    Enter here >  ''')
    files=[]
    for i in os.listdir(input_path):
        if i.endswith(ext):
            files.append(i)
    
    output_prompt=(f'''Enter folder path to save md file
        Skip to choose the default path as {default}
        Enter here > ''')
    output_filename=input('''Enter filename to be saved (e.g. programs.md) 
    Enter here > ''')
    output_path=getpath(output_prompt)

    # while True:
    #     list_choice=input('''Do you want the list to be ordered or bulleted or ordered?
    #     1. ordered
    #     2. bulleted
    #     input here > ''')

        
    #     if list_choice.lower() in ["ordered","order","1","o"]:
    #         list_choice=1; break
    #     elif list_choice.lower() in ["bulleted","bullet","2","b"]:
    #         list_choice="- "; break
    #     else:
    #         print("Invalid input: please try again!")
    #         continue

    

    #create md file
    md_file=open(os.path.join(output_path,output_filename), "a+"); sno=1
    for i in files:
        path=os.path.join(input_path, i)
        file=open(path, 'r')
        data= file.readlines(); j=0
        title=f"### {data[j]}"; line_1=f"### {sno}. {data[j]}"
        try:
            if ext=='.py':
                flag=False; flag1=1
                while True:
                    if data[0][0]=='#' and flag1==1:
                        md_file.write(line_1); j+=1; sno+=1; flag1=0
                    elif data[0][0:3] in ['"""', "'''" ] and flag1==1:
                        md_file.write(line_1); j+=1; sno+=1; flag=True; flag1=0
                    elif data[j][0]=='#':
                        md_file.write(title); j+=1
                    elif flag==True:
                        if data[j][-4:-1] in ['"""', "'''" ]:
                            md_file.write(title); j+=1
                        else: md_file.write(title); j+=1
                    else:
                        md_file.write(date[j])
            elif ext=='.c':
                flag=False; flag1=1
                while True:
                    if data[0][0:2]=='//' and flag1==1:
                        md_file.write(line_1);j+=1; sno+=1; flag1=0
                    elif data[0][0:2]=="/*" and flag1==1:
                        md_file.write(line_1);j+=1; sno+=1; flag=True; flag1=0
                    elif data[j][0:2]=='//':
                        md_file.write(title); j+=1
                    elif flag==True:
                        if data[j][-3:-1]=="*/":
                            md_file.write(title); j+=1
                        else: md_file.write(title); j+=1
                    else: 
                        md_file.write(date[j])
        except:
            continue
    return True


    
stats=generate_md()


