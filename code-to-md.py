#!/usr/bin/python3

# os for paths, sys for command line args
import os, sys

# find type of OS and return default user directory
# def default_path(platform):

#     if platform=="nt":
#         return os.environ['USERPROFILE']

#     else:
#         return os.environ['HOME']
        

# fetch path from user for input and output files' location
def getpath(prompt, arg):
    
    # set default path incase user skips path
    default = os.getcwd()

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
        if arg==1:
            default=os.path.join(default, "programs")
        print(f'''Input skipped or entered path is invalid! 
        Choosing {default} as the path...''')
        return default

''' Read files and generate md file in the format

'1. <first comment in file> as title 
The rest as code block'

and do for all code files in that directory
'''
def generate_md():

    default = os.getcwd()

    input_prompt=(f'''Enter directory path where files exist
    Skipping would choose {os.path.join(default, "programs")}
    Enter here >  ''')

    input_path=getpath(input_prompt, 1)

    try:
        ext=sys.argv[2]
    except:
        default_extension=".py"
        ext=input(f'''Enter file extension to be considered (.c or .py)
        Default is {default_extension}
        Enter here >  ''')
        if ext=="": ext=default_extension

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
        default_filename="programs.md"
        output_filename=input(f'''Enter filename to be saved (e.g. programs.md) 
        Skip to choose the default filename as {default_filename}
        Enter here > ''')
        if output_filename=="": output_filename=default_filename
        
    output_path=getpath(output_prompt, 3)

    #create md file
    md_file=open(os.path.join(output_path,output_filename), "w"); sno=1
    for i in files:
        path=os.path.join(input_path, i)
        file=open(path, 'r')
        data= file.readlines();j=0; flag=False; first=True;
        try:
            if ext=='.py':
                while True:
                    title=f"### {data[j]}"
                    if data[0][0]=='#' and j==0:
                        line_1=f"### {sno}. {data[j][1:]}"
                        md_file.write(line_1)
                        sno+=1
                    elif data[0][0:3] in ['"""', "'''" ] and j==0:
                        
################################### Check for ending quotes here too, also in C's case
                        
                        line_1=f"### {sno}. {data[j][3:]}"
                        md_file.write(line_1)
                        flag=True
                        sno+=1
                    # if there is no comment in the first line, use the file name as the title
                    elif j==0:
                        md_file.write(f"### {sno}. {i}\n")
                        sno+=1
                    elif flag==True:
                        if data[j][-4:-1] in ['"""', "'''" ]:
                            flag=False
                        md_file.write(title)
                    else:
                        if (first!=True) and (j!=(len(data)-1)): md_file.write(f"{data[j]}")
                        elif first==True:
                            md_file.write(f"```python\n{data[j]}")
                            first=False
                        else:
                            md_file.write(f"{data[j]}\n```")
                    j+=1
            elif ext=='.c':
                while True:
                    title=f"### {data[j]}"; line_1=f"### {sno}. {data[j][2:]}"
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
                            flag=False
                        md_file.write(title)
                    else:
                        if (first!=True) and (j!=(len(data)-1)): md_file.write(f"{data[j]}")
                        elif first==True:
                            md_file.write(f"```c\n{data[j]}")
                            first=False
                        else:
                            md_file.write(f"{data[j]}\n```")      
                    j+=1
        except:
            md_file.write("\n\n")
            continue
    return f"{output_filename} saved successfully at {output_path} !"
    
stats=generate_md()

print(stats)
