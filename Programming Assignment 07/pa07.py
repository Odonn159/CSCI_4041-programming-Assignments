#Folder and File classes
#Do not edit the __init__ method for either class
#Feel free to add your own methods, though
class Folder:
    def __init__(self, name, files, subfolders):
        self.name = name
        self.files = files
        self.subfolders = subfolders

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def total_memory(root):
    totmem = 0;
    for folder in root.subfolders:
        totmem+=total_memory(folder)
    for file in root.files:
        totmem +=file.size
    return totmem

def search(root, target):
    for file in root.files:
        if file.name==target:
            return root.name +"/"+target
    for folder in root.subfolders:
            if search(folder,target)!=False:
                return root.name+"/"+search(folder, target)
    return False



if __name__ == '__main__':
    root1 = Folder('courses',[File('CSCI_1133', 205),
                              File('CSCI_3041', 7)], [])

    root2 = Folder('empty',[], [])

    root3 = Folder('root', [File('resume.txt',607),
                File('cat.jpg',607)],
               [Folder('hws', [], []),
                Folder('plans',
                       [File('vacation.txt', 636)],
                       [Folder('evil',
                               [File('world_domination.txt',766)], [])]
                      ),
                Folder('labs',[File('lab1.txt',223),
                               File('lab2.txt',251),
                               File('lab3.txt',317)], [])])
    

