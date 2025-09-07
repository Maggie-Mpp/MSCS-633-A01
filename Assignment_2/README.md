# Biox Systems — QR Code Generator (Python)

Generate a QR code image from a URL (or any text).

## Prerequisites
- Python 3.9+
- pip

## Install
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

## Usage
```bash
python qr_generator.py --url "https://example.com" --out qr_example.png --box-size 10 --border 4 --error M
```
- `--url` : URL or text to encode (required)
- `--out` : Output file (PNG). Default: `qr_output.png`
- `--box-size` : Size of each QR module (default 10)
- `--border` : Quiet zone size (default 4)
- `--error` : Error correction level in {L, M, Q, H} (default M)

## Notes on Best Practices
- Clear function boundaries (`generate_qr`, `main`) and type hints.
- Command-line interface with explicit, validated flags.
- Constants for error correction mapping; no magic numbers.
- Minimal dependencies (`qrcode` + `Pillow`).
- Descriptive README and requirements pinned.
- Input is treated as plain text; no URL fetching.
