#!/usr/bin/env python3
"""QR Code Generator for Biox Systems
Usage:
    python qr_generator.py --url "https://example.com" --out qr.png

This script generates a QR code image from a provided URL or arbitrary text.
It uses the `qrcode` library (with Pillow backend) and exposes a few
customization flags for size, border, and error-correction level.

Author: (Your Name)
"""

from __future__ import annotations

import argparse
from pathlib import Path
import qrcode
from qrcode.constants import ERROR_CORRECT_L, ERROR_CORRECT_M, ERROR_CORRECT_Q, ERROR_CORRECT_H

ERROR_LEVELS = {
    "L": ERROR_CORRECT_L,  # ~7% error correction
    "M": ERROR_CORRECT_M,  # ~15%
    "Q": ERROR_CORRECT_Q,  # ~25%
    "H": ERROR_CORRECT_H,  # ~30%
}

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="qr_generator",
        description="Generate a QR code PNG from a URL or text."
    )
    parser.add_argument(
        "--url",
        required=True,
        help="The URL (or any text) to encode in the QR code.",
    )
    parser.add_argument(
        "--out",
        default="qr_output.png",
        help="Output image filename (PNG). Default: qr_output.png",
    )
    parser.add_argument(
        "--box-size",
        type=int,
        default=10,
        help="Size of each QR box/pixel. Larger = bigger image. Default: 10",
    )
    parser.add_argument(
        "--border",
        type=int,
        default=4,
        help="Border (quiet zone) width in boxes. Default: 4",
    )
    parser.add_argument(
        "--error",
        choices=list(ERROR_LEVELS.keys()),
        default="M",
        help="Error correction level (L, M, Q, H). Default: M",
    )
    return parser

def generate_qr(data: str, out_path: Path, box_size: int = 10, border: int = 4, error_level: str = "M") -> Path:
    """Generate a QR code PNG.

    Args:
        data: The text/URL to encode.
        out_path: Path to write PNG output.
        box_size: Size of each QR module.
        border: Border (quiet zone) width.
        error_level: One of 'L','M','Q','H'.

    Returns:
        Path to the written PNG file.
    """
    qr = qrcode.QRCode(
        version=None,  # let library pick best size
        error_correction=ERROR_LEVELS[error_level],
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    out_path = Path(out_path)
    img.save(out_path)
    return out_path

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    out_file = generate_qr(
        data=args.url,
        out_path=Path(args.out),
        box_size=args.box_size,
        border=args.border,
        error_level=args.error,
    )
    print(f"✅ QR code saved to: {out_file.resolve()}" )

if __name__ == "__main__":
    main()
