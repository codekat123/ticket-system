import qrcode
from io import BytesIO
from django.core.files.base import ContentFile


def generate_qr_image(data: str):
    qr = qrcode.make(data)
    buffer = BytesIO()
    qr.save(buffer, format="PNG")
    return ContentFile(buffer.getvalue(), name="ticket_qr.png")
