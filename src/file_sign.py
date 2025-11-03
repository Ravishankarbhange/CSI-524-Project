# file_signature.py
# Reads the first few bytes (magic number) of a file and identifies known file types.

from pathlib import Path

# Dictionary of known magic numbers
MAGIC_SIGNATURES = {
    "89504E470D0A1A0A": "PNG",
    "FFD8FF": "JPEG",
    "25504446": "PDF",
    "504B0304": "ZIP / DOCX / XLSX",
    "4D5A": "EXE (PE)",
}

def read_file_signature(filepath: str, num_bytes: int = 16) -> str:
    """Reads the first few bytes of a file in binary and returns the hex string."""
    with open(filepath, "rb") as file:
        header = file.read(num_bytes)
    # Convert to uppercase hex (e.g., b'\x89PNG' -> '89504E47')
    return header.hex().upper()


def identify_file_type(filepath: str) -> str:
    """Compares the file's signature to known magic numbers."""
    header_hex = read_file_signature(filepath)
    for magic, filetype in MAGIC_SIGNATURES.items():
        if header_hex.startswith(magic):
            return filetype
    return "Unknown type"


if __name__ == "__main__":
    path = input("Enter file path: ").strip()
    if Path(path).exists():
        signature = read_file_signature(path)
        detected = identify_file_type(path)
        print(f"Signature (hex): {signature}")
        print(f"Detected file type: {detected}")
    else:
        print("File not found.")
