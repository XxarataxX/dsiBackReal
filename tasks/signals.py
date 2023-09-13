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

def generar_pdf(numero, tarea):
    # Genera el PDF utilizando ReportLab
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    #p.drawString(100, 750, f"Factura Número: {numero}")
    
    

    p.drawString(50, 750, f"Fecha de Creación: {tarea.fecha_creacion}")
    p.drawString(50, 735, f"Fecha de Vencimiento: {tarea.fecha_vencimiento}")

    if tarea.fotos:
        image3_path = tarea.fotos.path
        p.drawImage(image3_path, 450, 735, width=100, height=50)

    p.line(50, 730, 550, 730)
    tamaño_fuente_predeterminado = 12
    p.setFont("Helvetica-Bold", 18)
    
    # Agrega la información de la tarea
    p.drawString(50, 710, f"Proyecto: {tarea.titulo}")

    p.setFont("Helvetica", tamaño_fuente_predeterminado)

    p.drawString(75, 690, f"{tarea.description}")
    
    p.drawString(450, 700, f"Status: {dict(tarea.opciones)[tarea.status]}")
    p.drawString(50, 660, f"Recibió: {tarea.recibio}")
    p.drawString(50, 645, f"Técnico: {tarea.tecnico.username}")

    p.setFont("Helvetica-Bold", 18)

    p.drawString(50, 600, f"Evidencia:")
    p.drawString(50, 425, f"Firma:")





    p.setFont("Helvetica", tamaño_fuente_predeterminado)

    if tarea.image_3:
        image3_path = tarea.image_3.path
        p.drawImage(image3_path, 225, 325, width=150, height=75)
    
    # Si hay una firma, la agrega al PDF
    # if tarea.firma:
    #     firma_path = tarea.firma.path
    #     p.drawImage(firma_path, 100, 590, width=200, height=50)

    # Si hay imágenes adicionales, agrégalas al PDF
    if tarea.image_1:
        image1_path = tarea.image_1.path
        p.drawImage(image1_path, 50, 490, width=150, height=75)

    if tarea.image_2:
        image2_path = tarea.image_2.path
        p.drawImage(image2_path, 225, 490, width=150, height=75)

    if tarea.image_3:
        image3_path = tarea.image_3.path
        p.drawImage(image3_path, 400, 490, width=150, height=75)

    

    p.showPage()
    p.save()

    # Guarda el PDF en el modelo Factura
    factura = PDFGenerado(name=f"factura_{numero}.pdf")
    factura.archivo.save(factura.name, ContentFile(buffer.getvalue()))


@receiver(post_save, sender=Tarea)
def generar_pdf_al_modificar(sender, instance, **kwargs):
    # Aquí llama a tu función para generar el PDF
    
    generar_pdf(instance.pk, instance)


  