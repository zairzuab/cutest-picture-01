# Cutest picture entry: a tiny cream kitten with big blue eyes and a
# daisy crown gently hugging a fluffy yellow chick, both on a knitted
# blanket. The picture is stored as base64 in cute.b64 (one line); the
# program decodes it and writes it to /output/entry.png (deterministic).
import base64
import os

def main():
    output_dir = os.getenv('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(output_dir, exist_ok=True)
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, 'cute.b64')
    dst = os.path.join(output_dir, 'entry.png')
    with open(src, 'r', encoding='ascii') as f:
        data = base64.b64decode(f.read().strip())
    with open(dst, 'wb') as f:
        f.write(data)

if __name__ == '__main__':
    main()
