#Projet 7 : Création d'un trieur de fichiers


from pathlib import Path

dirs = {".mp3": "Musique",
        ".wav": "Musique",
        ".flac": "Musique",
        ".avi": "Videos",
        ".mp4": "Videos",
        ".gif": "Videos",
        ".bmp": "Images",
        ".png": "Images",
        ".jpg": "Images",
        ".txt": "Documents",
        ".pptx": "Documents",
        ".csv": "Documents",
        ".xls": "Documents",
        ".odp": "Documents",
        ".pages": "Documents"
}

tri_dir = Path.home() / "Desktop" / "data"
files = [f for f in tri_dir.iterdir() if f.is_file()]
for f in files:
    output_dir = tri_dir / dirs.get(f.suffix, "Divers")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)