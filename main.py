import os,shutil
src=os.path.join(os.path.dirname(__file__),'entry.png'); dst=os.path.join(os.environ.get('MAKEFUN_OUTPUT_DIR','out'),'entry.png'); os.makedirs(os.path.dirname(dst),exist_ok=True); shutil.copyfile(src,dst)
