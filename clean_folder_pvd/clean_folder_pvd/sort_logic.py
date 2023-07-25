import sys
from pathlib import Path

# lists (folders-to-be):
archives = []
video = []
audio = []
documents = []
images = []
books =[]
my_other = []

known_extentions = {
    'jpeg': images,
    'jpg': images,
    'png': images,
    'svg': images,
    'avi': video,
    'mp4': video,
    'mov': video,
    'mkv': video,
    'doc': documents,
    'docx': documents,
    'txt': documents,
    'pdf': documents,
    'xlsx': documents,
    'pptx': documents,
    'mp3': audio,
    'ogg': audio,
    'wav': audio,
    'amr': audio,
    'zip': archives,
    'gz': archives,
    'tar': archives,
    'epub': books,
}

folders = []
unknown = set()
extention_s = set()


def get_extension(filename: str) -> str:
    return Path(filename).suffix[1:].lower()

def scan(folder: Path) -> None:
    for obj in folder.iterdir():
        if obj.is_dir():
            # check if the needed folder already exists
            if obj.name not in ('archives', 'video', 'audio', 'documents', 'images', 'books', 'my_other'):
                folders.append(obj)
                scan(obj)
            continue
        extention = get_extension(obj.name) # .name - це фінальне імʼя файлу, без повного шляху до нього (без /dir/subdir/subsubdir...)
        fullname = folder / obj.name
        if not extention:
            my_other.append(fullname)
        else:
            try:
                container = known_extentions[extention] # не розумію, що робить цей блок, тупо скопіював. Допоможіть, пліз
                extention_s.add(extention)
                container.append(fullname)
            except KeyError:
                unknown.add(extention)
                my_other.append(fullname)


if __name__ == "__main__":
    # test if the path received as a command line argument exists
    folder_to_scan = sys.argv[1]
    exist_test = Path(folder_to_scan).exists()
    print(f"The folder you indicated exists: {exist_test}")
   
    print(f'Start in folder {folder_to_scan}')
    scan(Path(folder_to_scan))
    print(f'Archives: {archives}')
    print(f'Video: {video}')
    print(f'Audio: {audio}')
    print(f'Documents: {documents}')
    print(f'Images: {images}')
    print(f'Books: {books}')
    print(f'Other folders: {folders}')
    print(f'Other types of files in {folder_to_scan}: {extention_s}')
    print(f'Unknown file types: {unknown}')
    print(f'Other stuff: {my_other}')

   