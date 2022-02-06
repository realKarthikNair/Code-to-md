#!/usr/bin/python3
import os, sys

# find type of OS and return default user directory
def default_path(platform):

    if platform=="nt":
        return os.environ['USERPROFILE']

    else:
        return os.environ['HOME']
        

# fetch path from user for input and output files' location
def getpath(prompt, arg):
    
    # set default path incase user skips path
    default = default_path(os.name)

    #if path entered by user exists, return the path; if input is empty or invalid, return default path
    try:
        try:
            path=sys.argv[arg]
        except:
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

    input_path=getpath(input_prompt, 1)

    try:
        ext=sys.argv[2]
    except:
        ext=input('''Enter file extension to be considered (.c or .py)
        Enter here >  ''')

    files=[]
    for i in sorted(os.listdir(input_path)):
        if i.endswith(ext):
            files.append(i)
    

    output_prompt=(f'''Enter folder path to save md file
        Skip to choose the default path as {default}
        Enter here > ''')

    try:
        output_filename=sys.argv[4]
    except:
        output_filename=input('''Enter filename to be saved (e.g. programs.md) 
        Enter here > ''')
        
    output_path=getpath(output_prompt, 3)

    #create md file
    md_file=open(os.path.join(output_path,output_filename), "w"); sno=1
    for i in files:
        path=os.path.join(input_path, i)
        file=open(path, 'r')
        data= file.readlines(); j=0
        try:
            if ext=='.py':
                flag=False
                while True:
                    title=f"### {data[j]}"; line_1=f"### {sno}. {data[j]}"
                    if data[0][0]=='#' and j==0:
                        md_file.write(line_1)
                        sno+=1
                    elif data[0][0:3] in ['"""', "'''" ] and j==0:
                        md_file.write(line_1)
                        flag=True
                        sno+=1
                    # if there is no comment in the first line, use the file name as the title
                    elif j==0:
                        md_file.write(f"### {sno}. {i}\n")
                        sno+=1
                    elif flag==True:
                        if data[j][-4:-1] in ['"""', "'''" ]:
                            md_file.write(title)
                            flag=False
                        else:
                            md_file.write(title)
                    else:
                        md_file.write(f"\t{data[j]}")
                    j+=1
            elif ext=='.c':
                flag=False
                while True:
                    title=f"### {data[j]}"; line_1=f"### {sno}. {data[j]}"
                    if data[0][0:2]=='//' and j==0:
                        md_file.write(line_1); sno+=1
                    elif data[0][0:2]=="/*" and j==0:
                        md_file.write(line_1)
                        flag=True
                        sno+=1
                    # if there is no comment in the first line, use the file name as the title
                    elif j==0:
                        md_file.write(f"### {sno}. {i}\n")
                        sno+=1
                    elif flag==True:
                        if data[j][-3:-1]=="*/":
                            md_file.write(title)
                            flag=False
                        else:
                            md_file.write(title)
                    else:
                        md_file.write(f"\t{data[j]}")
                    j+=1
        except:
            md_file.write("\n\n")
            continue
    return f"{output_filename} saved successfully at {output_path} !"
    
stats=generate_md()

print(stats)