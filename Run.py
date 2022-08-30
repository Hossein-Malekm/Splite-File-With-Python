from fileinput import filename
import os
import shutil
for i in range(1,17):
    target_path = f'{i}'
    os.mkdir(target_path)
    if i < 10:
        for j in range(1,66):
            if j < 10 :
                filename = f'0{j}-000{i}.dcm'
                shutil.move(filename, target_path)
            if j >=10 :
                filename = f'{j}-000{i}.dcm'
                shutil.move(filename, target_path)
    else :
        for j in range(1,66):
            if j < 10 :
                filename = f'0{j}-00{i}.dcm'
                shutil.move(filename, target_path)
            if j >=10 :
                filename = f'{j}-00{i}.dcm'
                shutil.move(filename, target_path)