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
def generate_md(input_path, output_path, language):

    default = default_path(os.name)

    input_prompt=f'''Enter directory path where files exist
    Skipping would choose {default}'''
    input_path=getpath(input_prompt)

    ext=input('''Enter file extension to be considered (.c or .py)
    Enter here >  ''')
    files=[]
    for i in os.listdir(input_path):
        if i.endswith(ext):
            files.append(i)
    
    output_prompt=f'''Enter folder path to save md file
        Skip to choose the default path as {default}
        Enter here > '''
    output_filename=input('''Enter filename to be saved (e.g. programs.md) 
    Enter here > ''')
    output_path=getpath(output_prompt)

    while True:
        list_choice=input('''Do you want the list to be ordered or bulleted or ordered?
        1. ordered
        2. bulleted
        input here > ''')

        
        if list_choice.lower() in ["ordered","order","1","o"]:
            list_choice=1; break
        elif list_choice.lower() in ["bulleted","bullet","2","b"]:
            list_choice="- "; break
        else:
            print("Invalid input: please try again!")
            continue

    #create md file
    md_file=open(os.path,join(output_path,output_filename), "w")

    for i in files:
        path=os.path.join(input_path, i)
        open(path, 'r')
        data= path.readlines(path)
        title=[]; j=0
        try:
            if ext=='.py':
                    while True:
                        if data[j][0]=='#':
                            title+=f"### {data[j]}"
                            j+=1
                        elif data[j][0:3] in ['"""', "'''", ]



