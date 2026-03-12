"""Utility functions for processing uploaded character images."""

import io
import os

from PIL import Image
from django.core.files.base import ContentFile

# Maximum dimensions for character images.
# The largest display in the UI is w-24 h-24 (96×96 CSS pixels).
# We use 512×512 to keep enough quality for retina displays. # noqa: E800
MAX_IMAGE_SIZE = (512, 512)
WEBP_QUALITY = 80


def compress_character_image(uploaded_file):
    """Compress and resize an uploaded image to save storage and bandwidth.

    - Resizes to at most 512×512 pixels (preserving aspect ratio)
    - Converts to WebP format for optimal compression
    - Returns a Django ``ContentFile`` ready for assignment to an ``ImageField``
    """
    img = Image.open(uploaded_file)

    # Handle RGBA / palette images – WebP supports alpha, but we convert
    # palette-based images with transparency to RGBA, and opaque ones to RGB.
    if img.mode in ("P", "PA"):
        img = img.convert("RGBA" if "transparency" in img.info else "RGB")
    elif img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGB")

    # Resize only if the image exceeds the maximum dimensions.
    img.thumbnail(MAX_IMAGE_SIZE, Image.LANCZOS)

    buffer = io.BytesIO()
    img.save(buffer, format="WEBP", quality=WEBP_QUALITY)
    buffer.seek(0)

    # Build a new filename with the .webp extension.
    original_name = getattr(uploaded_file, "name", "image.png")
    new_name = os.path.splitext(original_name)[0] + ".webp"

    return ContentFile(buffer.read(), name=new_name)
