from os.path import isdir
from glob import iglob

def remove_empty_args(args: dict):
    """
    Removes empty arguments from a dictionary (of arguments).

    """
    return {k: v for k, v in args.items() if v != None}

def recurse_directory(root_dir: str):
    """
    
    """
    try:
        if (isdir(root_dir)):
            for filename in iglob(root_dir + "**/**", recursive=True):
                print(filename)
    except Exception as e:
        raise e
