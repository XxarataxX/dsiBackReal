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
    
    

    p.drawString(50, 760, f"Fecha de Creación: {tarea.fecha_creacion}")
    p.drawString(50, 745, f"Fecha de Vencimiento: {tarea.fecha_vencimiento}")

    

    image_path_on_server = "./media/dsi.jpg"
    p.drawImage(image_path_on_server, 450, 735, width=100, height=50)

    p.line(50, 730, 550, 730)
    tamaño_fuente_predeterminado = 12
    p.setFont("Helvetica-Bold", 18)
    
    # Agrega la información de la tarea
    p.drawString(50, 710, f"Proyecto: {tarea.titulo}")

    p.setFont("Helvetica", tamaño_fuente_predeterminado)

    p.drawString(75, 690, f"{tarea.description}")
    
    p.drawString(450, 715, f"Status: {dict(tarea.opciones)[tarea.status]}")
    p.drawString(50, 660, f"Recibió: {tarea.recibio}")
    
    p.drawString(50, 645, f"Técnico: {tarea.tecnico.username}")

    p.drawString(50, 565, f"{tarea.notas}")

    p.setFont("Helvetica-Bold", 18)

    p.drawString(50, 600, f"Notas:")
    p.drawString(50, 295, f"Firma:")
    p.drawString(50, 520, f"Evidencia:")






    p.setFont("Helvetica", tamaño_fuente_predeterminado)

    if tarea.firma:
        image3_path = tarea.firma.path

        p.setStrokeColor(colors.black)
        p.setLineWidth(1)
        p.rect(225, 195, 150, 75)

        p.drawImage(image3_path, 225, 195, width=150, height=75, mask='auto')
    
    # Si hay una firma, la agrega al PDF
    # if tarea.firma:
    #     firma_path = tarea.firma.path
    #     p.drawImage(firma_path, 100, 590, width=200, height=50)

    # Si hay imágenes adicionales, agrégalas al PDF
    if tarea.image_1:
        image1_path = tarea.image_1.path
        p.drawImage(image1_path, 120, 425, width=150, height=75)

    if tarea.image_2:
        image2_path = tarea.image_2.path
        p.drawImage(image2_path, 345, 425, width=150, height=75)

    if tarea.image_3:
        image3_path = tarea.image_3.path
        p.drawImage(image3_path, 120, 340, width=150, height=75)

    if tarea.image_4:
        image3_path = tarea.image_4.path
        p.drawImage(image3_path, 345, 340, width=150, height=75)

    if tarea.fotos:
        image3_path = tarea.fotos.path
        p.drawImage(image3_path, 225, 100, width=150, height=75)

    

    p.showPage()
    p.save()

    # Guarda el PDF en el modelo Factura
    factura = PDFGenerado(name=f"factura_{numero}.pdf")
    factura.archivo.save(factura.name, ContentFile(buffer.getvalue()))


@receiver(post_save, sender=Tarea)
def generar_pdf_al_modificar(sender, instance, **kwargs):
    # Aquí llama a tu función para generar el PDF
    
    generar_pdf(instance.pk, instance)


  