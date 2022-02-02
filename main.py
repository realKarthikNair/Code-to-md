import os

# find type of OS
def default_path(platform):
    if platform=="nt":
        return os.environ['USERPROFILE']
    else:
        return os.environ['HOME']
        

# fetch path from user for input and output files' location
def getpath(prompt):
    # set default path incase user skips path
    default = default_path(os.name)
    try:
        path=input(f'''{prompt}''')
        if not os.path.exists(path):
            raise Exception
        return path
    except:
        print(f'''Input skipped or entered path is invalid! 
        Choosing {default} as the path...''')
        return default

# read files and save as md file
def generate_md(input_path, output_path, language):
    input_prompt=f'''Enter folder path to save file
        Skip to choose the default path as {default}
        Enter here > '''
    input_path=getpath("")

    files=[]
    for i in os.listdir(input_path):
        if i.endswith(".txt"):
            files.append(i)

    output_prompt=f'''dfd'''

