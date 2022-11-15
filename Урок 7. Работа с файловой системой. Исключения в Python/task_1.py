import os
import shutil

project_name = {
   "my_project": [{
            "settings": [],
            "mainapp": [],
            "adminapp": [],
            "authapp": []
        }]
}


def project(pth, dic):

    for path, nodes in dic.items():
        test_path = os.path.join(pth, path)
        if not os.path.exists(test_path):
            os.mkdir(test_path)
        #else:
         #   shutil.rmtree(test_path)
    for node in nodes:
        project(test_path, node)


if __name__ == "__main__":
    ROOT = os.path.dirname(__file__)
    project(ROOT, dic=project_name)

