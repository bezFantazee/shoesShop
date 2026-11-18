import sys
from pathlib import Path


def resource_path(relative_path: str) -> Path:
    if getattr(sys, "frozen", False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).resolve().parent

    return base_path / relative_path


def images_directory() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent / "present" / "images"

    return Path(__file__).resolve().parent / "present" / "images"


def image_path(image_name: str | None) -> Path:
    file_name = Path(image_name).name if image_name else "picture.png"

    writable_path = images_directory() / file_name

    if writable_path.exists():
        return writable_path

    return resource_path(str(Path("present") / "images" / file_name))


def external_config_path() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent / "config.ini"

    return Path(__file__).resolve().parent.parent / "config.ini"
