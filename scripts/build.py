from __future__ import annotations

from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile

REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIRECTORY = REPOSITORY_ROOT / "custom_components" / "simple_inventory_enhanced"
ARCHIVE_PATH = REPOSITORY_ROOT / "simple_inventory_enhanced.zip"
DESTINATION_DIRECTORY = (
    REPOSITORY_ROOT.parent / "config" / "www" / "community" / "simple-inventory-enhanced"
)


def main() -> None:
    if not SOURCE_DIRECTORY.is_dir():
        raise SystemExit(f"Integration source directory not found: {SOURCE_DIRECTORY}")

    files = sorted(
        path
        for path in SOURCE_DIRECTORY.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc"
    )
    with ZipFile(ARCHIVE_PATH, "w", compression=ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(
                path,
                (Path("simple_inventory_enhanced") / path.relative_to(SOURCE_DIRECTORY)).as_posix(),
            )

    DESTINATION_DIRECTORY.mkdir(parents=True, exist_ok=True)
    with ZipFile(ARCHIVE_PATH) as archive:
        for member in archive.infolist():
            member_path = PurePosixPath(member.filename)
            if member_path.parts[0] != "simple_inventory_enhanced" or len(member_path.parts) == 1:
                continue

            destination = DESTINATION_DIRECTORY.joinpath(*member_path.parts[1:])
            if member.is_dir():
                destination.mkdir(parents=True, exist_ok=True)
                continue

            destination.parent.mkdir(parents=True, exist_ok=True)
            with archive.open(member) as source, destination.open("wb") as target:
                target.write(source.read())

    print(f"Created {ARCHIVE_PATH}")
    print(f"Extracted integration to {DESTINATION_DIRECTORY}")


if __name__ == "__main__":
    main()
