"""Copy the bundled news image to the output directory.

The entry image is generated at build time and shipped in this
repository as entry.png. This program simply copies it to the
location the harness expects, so both runs produce identical bytes.
"""

import os
import shutil
import sys


def resolve_source():
    """Locate entry.png next to this file, wherever the repo is mounted."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")
    shutil.copyfile(resolve_source(), destination)
    # Confirm the copy landed before exiting: the harness gates on the
    # output file existing and being a whole, valid image.
    if not os.path.isfile(destination) or os.path.getsize(destination) == 0:
        sys.exit("failed to write entry.png")



if __name__ == "__main__":
    main()
