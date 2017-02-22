# coding: utf-8

import os
import sys
import site
import shutil
import subprocess
import settings


def buildup(buildup_dir):
    """
    """
    print 'start buildup...'
    buildup_dir = os.path.realpath(buildup_dir)
    base_dir = os.path.dirname(os.path.realpath(__file__))

    temp_dir = os.path.join(buildup_dir, 'temp')
    print 'mkdir %s' % temp_dir
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    src_dir = os.path.join(base_dir, '..')
    tempsrc_dir = os.path.join(temp_dir, 'src')
    print 'copy src code from %s ==> %s' % (src_dir, tempsrc_dir)
    if os.path.exists(tempsrc_dir):
        shutil.rmtree(tempsrc_dir)

    def ignore(src, names):
        return [name for name in names if name.startswith('.')]
    shutil.copytree(src_dir, tempsrc_dir, ignore=ignore)

    scripts = []
    for dirpath, _, filenames in os.walk(tempsrc_dir):
        for filename in filenames:
            if not filename.endswith('.py'):
                continue
            filepath = os.path.join(dirpath, filename)
            if filename == 'run.py':
                scripts.insert(0, filepath)
            else:
                scripts.append(filepath)

    script_names = ' '.join(scripts)
    pathsep = ';' if os.name == 'nt' else ':'
    sitepathes = pathsep.join(site.getsitepackages())
    exefilename = '%s.exe' % settings.PROJECT_NAME
    cmd = 'pyinstaller -F %s -p %s -n %s' % (script_names, sitepathes, exefilename)
    print 'buildup ready, start cmd: %s' % cmd

    p = subprocess.Popen(cmd, shell=True)
    p.wait()

    exepath = os.path.join(buildup_dir, 'dist', exefilename)
    if not os.path.isfile(exepath):
        print 'buildup error'
        return

    print 'buildup path: %s' % exepath
    print 'success'


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'python -m scripts.buildup [buildup_dir]'
        sys.exit()
    buildup_dir = sys.argv[1]
    buildup(buildup_dir)
