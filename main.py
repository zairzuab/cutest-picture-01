# Cutest picture entry: a tiny ginger kitten with big amber eyes, head
# tilted, one paw raised, and a ball of yarn on a knitted blanket.
# The program copies the picture to /output/entry.png (deterministic).
import os
import shutil

def main():
    output_dir = os.getenv('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, 'cute.jpg')
    dst = os.path.join(output_dir, 'entry.png')
    shutil.copyfile(src, dst)

if __name__ == '__main__':
    main()
