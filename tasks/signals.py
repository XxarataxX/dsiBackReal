from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Tarea, PDFGenerado
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from django.core.files import File
from reportlab.pdfgen import canvas
from io import BytesIO

from django.core.files.base import ContentFile

def generar_pdf(instance):

    try:
        # Intenta obtener un registro existente con la misma tarea
        factura = PDFGenerado.objects.get(tarea=instance)
    except PDFGenerado.DoesNotExist:
        # Si no existe, crea uno nuevo
        factura = PDFGenerado(tarea=instance)

     # Genera el PDF utilizando ReportLab
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(100, 750, "Factura Número: {}".format(instance))
    # p.drawString(100, 730, "Fecha: {}".format(fecha))
    # Puedes agregar más contenido a tu PDF aquí
    p.showPage()
    p.save()

    # Guarda el PDF en el registro existente o en el nuevo
    factura.archivo.save('factura.pdf', ContentFile(buffer.getvalue()))
    factura.save()

@receiver(post_save, sender=Tarea)
def generar_pdf_al_modificar(sender, instance, **kwargs):
    # Aquí llama a tu función para generar el PDF
    
    generar_pdf(instance)


  