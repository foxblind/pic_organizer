import os


def get_files(path: str) -> list:

    types = ["jpg", "png", "jpeg"]

    all_files = []

    for top, dirs, files in os.walk(path):

        for file in files:
            tp = file.split(".")[-1]
            if tp in types:
                all_files.append(f"{file}")

    return all_files


def add_dir(path: str) -> str:

    if not os.path.exists(path):
        os.mkdir(path)

    return path


def move_file(old_path: str, new_path: str, name: str):
    os.rename(f"{old_path}/{name}", f"{new_path}/{name}")


def rename_file(path: str, old_name: str, new_name: str) -> str:
    old_name, ext = os.path.splitext(f"{path}/{old_name}")
    old_name = os.path.basename(old_name)

    os.rename(f"{path}/{old_name}{ext}", f"{path}/{new_name}{ext}")

    return f"{new_name}{ext}"
