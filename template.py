import os
from pathlib import Path
import logging

file_path_str = "C:/Users/Krishna.Arjun/Desktop/mdlprc"

package_name = "SignLanguageDetection"


list_of_file = [

   
    
    "data/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/components/data_ingestion.py",
    f"src/{package_name}/components/data_validation.py",
    f"src/{package_name}/components/model_trainer.py",
    f"src/{package_name}/components/model_pusher.py",
    f"src/{package_name}/configuration/__init__.py",
    f"src/{package_name}/configuration/s3_operations.py",
    f"src/{package_name}/constant/__init__.py",
    f"src/{package_name}/constant/training_pipeline.py/__init__.py",
    f"src/{package_name}/constant/application.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/entity/artifacts_entity.py",
    f"src/{package_name}/entity/config_entity.py",
    f"src/{package_name}/logger/__init__.py",
    f"src/{package_name}/exception/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/pipeline/training_pipeline.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/utils/main_utils.py",
    "template/index.html",
    "dockerignore",
    "requirements.txt",
    "Dockerfile"
    "app.py",
    "setup.py"


    ]
for filepath in list_of_file:
    file_path = Path(filepath)
    filedir,filename=os.path.split(file_path)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
    else:
        print("file already exists")



print("Filename:", file_path.name)
print("Directory:", file_path.parent)








'''Path(


     dir_name = "reference"

root = 'C:/Users/Krishna.Arjun/Desktop/mdlprc'

path = os.path.join(root,dir_name)


os.mkdir(path) 
print("Directory '%s' created" %dir_name)
'''
