import os
import os.path

from shutil import copyfile


def get_class(str):
    return str.split("\\")[0]


import os
from shutil import copyfile
def get_class(str):
      return str.split('\\')[0]
def main():
    by_merge_dir = '/Users/brindakulkarni/Downloads/CV_Proj/by_merge/'
    output_dir = '/Users/brindakulkarni/Downloads/CV_Proj/output/'
    index = 0
    class_index = 0
    counter = 0
    n_copied = 0
    classes = []
    list1=[]
    for subdir, dirs, files in os.walk(by_merge_dir):
        list1.append(dirs)
        break
    for i in list1[0]:
        # print(by_merge_dir+str(i))
        for subdir, dirs, files in os.walk(by_merge_dir+str(i)):
            print(subdir)
            # n_copied+=len(files)
            
            for file in files:
                class_index += 1
                if class_index % 160 == 0:
                    counter+=1
                path=output_dir+i 
                if os.path.exists(path)==False:
                    os.makedirs(path)
                copyfile(os.path.join(subdir, file),os.path.join(path, '{}.png'.format(str(counter))))
            index += 1
            # print(class_index)
            class_index=-1
        
        n_copied+=counter
        counter=0
    print('Total images: '+ str(n_copied))
if __name__ == '__main__':
    main()





