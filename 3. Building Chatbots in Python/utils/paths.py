import platform
from pathlib import Path

drive = Path('G:/Mi unidad/944/')
drivel = Path('/mnt/g/mi unidad/944/')
drive_colab = Path("/content/drive/MyDrive/944/")

def mod(modality):
    if modality == 'p':
        return 'projects'
    elif modality == 'c':
        return 'courses'
    elif modality == 'e':
        return 'exercises'
    else:
        return 'test'

def make_dir_line(modality, project_name):

    ''' 
        Esta funcion hace blablabla  \n
        p for projects \n
        c for courses \n
        e for exercises \n
    '''

    modality = mod(modality)

    def dir_dir(*args):

        user_plataform = platform.system()
    
        if user_plataform == 'Windows':
            return drive.joinpath(modality, project_name, *args)
        elif user_plataform == 'Linux':
            return drivel.joinpath(modality, project_name, *args)

    return dir_dir
