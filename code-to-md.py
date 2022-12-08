#!/usr/bin/python3

# os for paths, sys for command line args
import os, sys, argparse

''' Read files and generate md file in the format

'1. <first comment in file> as title 
The rest as code block'

and do for all code files in that directory
'''
def return_path(arg, default, prompt):
    if arg and os.path.exists(arg):
        return arg
    else:
        path=input(f'''{prompt} {default}
        Enter here >  ''')
        if not os.path.exists(path):
            print(f'''Input skipped or entered path is invalid! 
            Choosing {default} as the path...''')
            return default
        else: return path    

def generate_md():

    default = os.getcwd()

    input_prompt=('''Enter directory path where files exist
    Skipping would choose ''')

    input_path=return_path(args.input_dir, os.path.join(default, "programs"), input_prompt) # hope this works :D

    ext=args.extension
    if not ext or ext not in ['.py', '.c', '.cpp']:
        default_extension=".py"
        ext=input(f'''Enter file extension to be considered (.c .cpp or .py)
        Default is {default_extension}
        Enter here >  ''')
        if ext=="":
            print(f'''Input skipped!
            Choosing {default_extension} as the extension...''')
            ext=default_extension

    files=[]
    for i in sorted(os.listdir(input_path)):
        if i.endswith(ext):
            files.append(i)

    output_prompt=('''Enter folder path to save md file
        Skip to choose the default path as ''')

    output_path=return_path(args.output, default, output_prompt)

    if args.filename:
        output_filename=args.filename
    else:
        print("yes")
        default_filename="programs.md"
        output_filename=input(f'''Enter filename to be saved (e.g. programs.md) 
        Skip to choose the default filename as {default_filename}
        Enter here > ''')
        if output_filename=="":
            print(f'''Input skipped!
            Choosing {default_filename} as the filename...''')
            output_filename=default_filename
        print(output_path)
    

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
            elif ext=='.c' or ext=='.cpp':
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
    
parser=argparse.ArgumentParser(description="Create a single md file from a directory full of code files!")
parser.add_argument("-idir","--input_dir", help="Directory path where the code files exist")
parser.add_argument("-e","--extension", help="File extension to be considered (.c .cpp or .py)")
parser.add_argument("-odir","--output", help="Directory path to save the md file")
parser.add_argument("-o","--filename", help="Filename to be saved (e.g. programs.md)")
args=parser.parse_args()

stats=generate_md()

print(stats)
