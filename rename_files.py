#!/.venv/bin/python3
# -*- coding: utf-8 -*-


""""""

import os
import argparse


# --------------------------------------------------
def get_args() -> argparse.Namespace:
    """"""

    parser = argparse.ArgumentParser(description="Change Files name")

    parser.add_argument("-d", "--directory", default="./", help="Directory File")
    parser.add_argument("-s", "--start_prefix", default="01", help="Start Prefix File")
    parser.add_argument("-p", "--end_prefix", default="", help="End Prefix File")
    parser.add_argument("-e", "--extension", default=".png", help="Extension File")
    parser.add_argument("-i", "--include", default="", help="Word in File name")
    parser.add_argument(
        "--is_test", default=False, type=lambda x: (str(x).lower() == "true"), help="Is test mode"
    )

    return parser.parse_args()


# --------------------------------------------------
def change_name(
    directory: str,
    start_prefix: str,
    end_prefix: str,
    extension: str,
    include: str,
    is_test: bool,
) -> None:
    """"""
    if not extension.startswith('.'):
        raise Exception("Extensions must start with dot")
    
    end_prefix = '_' + end_prefix if len(end_prefix)>0 else end_prefix
    start_prefix =  start_prefix + '_' if len(start_prefix)>0 else start_prefix

    idx: int = 1
    for filename in os.listdir(directory):
        if filename.endswith(extension) and (include.lower() in filename.lower()):
            filerename = f"{start_prefix}{idx:02}{end_prefix}{extension}"
            if is_test:
                print(filename, '>>', filerename)
            else:
                os.rename(f"{directory}/{filename}", f"{directory}/{filerename}")
            # Count only files filtered
            idx+=1

# --------------------------------------------------
def main() -> None:
    """"""

    args: argparse.Namespace = get_args()
    change_name(
        args.directory,
        args.start_prefix,
        args.end_prefix,
        args.extension,
        args.include,
        args.is_test,
    )


# --------------------------------------------------
if __name__ == "__main__":
    main()
