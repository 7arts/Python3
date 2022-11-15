import os
import shutil

ROOT = os.path.dirname(__file__)
root_dir = os.path.join(ROOT, 'my_project')
dst_dir = os.path.join(ROOT, 'my_project', 'templates')

if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

for root, dirs, files in os.walk(root_dir):
    if root.count('templates'):
        for dir in dirs:
            if not os.path.exists(os.path.join(dst_dir, dir)):
                os.makedirs(os.path.join(dst_dir, dir))
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dst_dir, os.path.basename(root))
            if not os.path.dirname(src_file) == dst_file:
                shutil.copy(src_file, dst_file)
