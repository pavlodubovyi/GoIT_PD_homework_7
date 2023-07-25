from pathlib import Path
import shutil
import sys
import sort_logic as parser
from normalizer import normalize


def handle_video(filename: Path, video: Path) -> None:
    video.mkdir(exist_ok=True, parents=True)
    filename.replace(video / normalize(filename.name))

def handle_audio(filename: Path, audio: Path) -> None:
    audio.mkdir(exist_ok=True, parents=True)
    filename.replace(audio / normalize(filename.name))

def handle_documents(filename: Path, documents: Path) -> None:
    documents.mkdir(exist_ok=True, parents=True)
    filename.replace(documents / normalize(filename.name))

def handle_images(filename: Path, images: Path) -> None:
    images.mkdir(exist_ok=True, parents=True)
    filename.replace(images / normalize(filename.name))

def handle_my_other(filename: Path, my_other: Path) -> None:
    my_other.mkdir(exist_ok=True, parents=True)
    filename.replace(my_other / normalize(filename.name))

def handle_books(filename: Path, books: Path) -> None:
    books.mkdir(exist_ok=True, parents=True)
    filename.replace(books / normalize(filename.name))

def handle_archives(filename: Path, archives: Path) -> None:
    archives.mkdir(exist_ok=True, parents=True)
    new_folder = archives / normalize(filename.name.replace(filename.suffix, '')) # починаючи з цього моменту і до кінця архівів - не розумію
    new_folder.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(filename, new_folder)
    except shutil.ReadError:
        print('It is not an archive')
        new_folder.rmdir()
    filename.unlink()

def handle_folders(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f"Can't delete folder: {folder}")

def clean(folder: Path):
    parser.scan(folder)
    for file in parser.images:
        handle_images(file, folder / 'images')
    for file in parser.audio:
        handle_audio(file, folder / 'audio')
    for file in parser.documents:
        handle_documents(file, folder / 'documents')
    for file in parser.books:
        handle_books(file, folder / 'books')
    for file in parser.video:
        handle_video(file, folder / 'video')
    for file in parser.my_other:
        handle_my_other(file, folder / 'my_other')
    for file in parser.archives:
        handle_archives(file, folder / 'archives')

    for folder in parser.folders[::-1]:
        handle_folders(folder)

if __name__ == "__main__":
    if sys.argv[1]:
        folder_for_scan = Path(sys.argv[1])
        print(f'Start in folder: {folder_for_scan.resolve()}') # resolve() - convert a relative path to an absolute path
        clean(folder_for_scan.resolve())