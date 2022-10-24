import concurrent.futures
import logging
from pathlib import Path
from shutil import move
import sys
from threading import Thread


file_list = []
folder_list = []


def scan(path: Path):
    for el in path.iterdir():
        if el.is_dir():
            # logging.info(f'Scan folder {el.name}')
            folder_list.append(el)
            thread_ = Thread(target=scan, args=(Path(el),))
            thread_.start()
        else:
            file_list.append(el)


def copy_file(file_path: Path):
    ext = file_path.suffix[1:]
    new_path = scan_folder / ext.upper()
    try:
        new_path.mkdir(parents=True)
        logging.info(f'New folder {ext}')
    except FileExistsError:
        pass
    move(file_path, new_path / file_path.name)


def delete_folders(folder: Path):
    try:
        folder.rmdir()
        # logging.info(f'{folder} deleted')
    except OSError:
        logging.info(f'{folder} not deleted')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(threadName)s %(message)s')
    scan_folder = Path(sys.argv[1])
    thread = Thread(target=scan, args=(Path(scan_folder),))
    thread.start()
    thread.join()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(copy_file, file_list)

    if concurrent.futures.as_completed(file_list):
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            executor.map(delete_folders, folder_list[::-1])

    logging.info('All done')
