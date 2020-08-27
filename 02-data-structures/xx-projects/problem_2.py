"""
Problem 2: File Recursion
"""

import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    if suffix == "" or len(os.listdir(path)) == 0:
        return []

    path_content = os.listdir(path)
    files = [file for file in path_content if file.endswith(f'.{suffix}')]
    folders = [f for f in path_content if os.path.isdir(f'{path}/{f}')]

    for folder in folders:
        files.extend(
            find_files(
                suffix=suffix,
                path=f"{path}/{folder}"
            )
        )
    return files

#%% Testing official
# Testing preparation
path_base = os.getcwd() + '/testdir'

# Normal Cases:
print(find_files(suffix='c', path=path_base))
# ['t1.c', 'a.c', 'a.c', 'b.c']

print(find_files(suffix='h', path=path_base))
# ['t1.h', 'a.h', 'a.h', 'b.h']

print(find_files(suffix='z', path=path_base))
# []

# Edge Cases:
print(find_files(suffix='', path=path_base))
# []