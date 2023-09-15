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


from django.conf import settings
from django.core.mail import send_mail, EmailMessage


from django.core.files.base import ContentFile

def generar_pdf(numero, tarea):
    pdf_existente = PDFGenerado.objects.filter(tarea=tarea).first()
    # Genera el PDF utilizando ReportLab
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    #p.drawString(100, 750, f"Factura Número: {numero}")
    
    

    p.drawString(400, 760, f"Numero: {tarea.fecha_creacion}")
    p.drawString(400, 745, f"Estatus: {dict(tarea.opciones)[tarea.status]}")

    

    image_path_on_server = "./media/dsi.jpg"
    p.drawImage(image_path_on_server, 50, 735, width=100, height=50)

    p.line(50, 730, 550, 730)
    tamaño_fuente_predeterminado = 12
    # p.setFont("Helvetica-Bold", 18)
    
    # Agrega la información de la tarea
    p.drawString(50, 710, f"Cliente: {tarea.cliente}")

    # p.setFont("Helvetica", tamaño_fuente_predeterminado)

    # p.drawString(75, 690, f"{tarea.description}")
    
    # p.drawString(450, 715, f"Status: {dict(tarea.opciones)[tarea.status]}")
    p.drawString(50, 370, f"Recibió: {tarea.recibio}")
    
    p.drawString(50, 100, f"Técnico: {tarea.tecnico.username}")

    p.drawString(50, 635, f"{tarea.notas}")

    p.setFont("Helvetica-Bold", 18)

    p.drawString(50, 660, f"Servicio:")
    p.drawString(50, 295, f"Firma:")
    p.drawString(50, 590, f"Fotos:")






    p.setFont("Helvetica", tamaño_fuente_predeterminado)

    if tarea.firma:
        image3_path = tarea.firma.path

        p.setStrokeColor(colors.black)
        p.setLineWidth(1)
        p.rect(120, 195, 150, 75)

        p.drawImage(image3_path, 120, 195, width=150, height=75, mask='auto')
    
    # Si hay una firma, la agrega al PDF
    # if tarea.firma:
    #     firma_path = tarea.firma.path
    #     p.drawImage(firma_path, 100, 590, width=200, height=50)

    # Si hay imágenes adicionales, agrégalas al PDF
    if tarea.image_1:
        image1_path = tarea.image_1.path
        p.drawImage(image1_path, 120, 495, width=150, height=75)

    if tarea.image_2:
        image2_path = tarea.image_2.path
        p.drawImage(image2_path, 345, 495, width=150, height=75)

    if tarea.image_3:
        image3_path = tarea.image_3.path
        p.drawImage(image3_path, 120, 410, width=150, height=75)

    if tarea.image_4:
        image3_path = tarea.image_4.path
        p.drawImage(image3_path, 345, 410, width=150, height=75)

    if tarea.fotos:
        image3_path = tarea.fotos.path
        p.drawImage(image3_path, 345, 195, width=150, height=75)

    

    p.showPage()
    p.save()

    # Guarda el PDF en el modelo Factura
    # factura = PDFGenerado(name=f"factura_{numero}.pdf")
    # # factura.archivo.save(factura.name, ContentFile(buffer.getvalue()))
    # factura.archivo.save(factura.name, tarea=tarea)
    if pdf_existente:
        # Sobrescribe el archivo del PDF existente con el nuevo contenido
        pdf_existente.archivo.delete()  # Elimina el archivo existente
        pdf_existente.archivo.save(f"factura_{numero}.pdf", ContentFile(buffer.getvalue()))
        pdf_existente.save()  # Guarda la instancia de PDFGenerado actualizada


        subject = 'Prueba de envío de PDF'
        message = 'Este es un correo con un archivo PDF adjunto.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['arata.sama.fake@gmail.com']

        email = EmailMessage(subject, message, from_email, recipient_list)

        # Adjunta el archivo PDF al correo
        pdf_path = pdf_existente.archivo.path  # Ruta al archivo PDF
        pdf_filename = pdf_existente.archivo.name  # Nombre del archivo PDF
        email.attach_file(pdf_path, pdf_filename)  # Adjunta el archivo PDF al correo

        # Envía el correo electrónico
        email.send()


    else:
        # Crea una nueva instancia de PDFGenerado si no existe una para la tarea
        factura = PDFGenerado(name=f"factura_{numero}.pdf", tarea=tarea)
        factura.archivo.save(factura.name, ContentFile(buffer.getvalue()))
        factura.save()  # Guarda la instancia de PDFGenerado en la base de datos

        ruta_archivo_pdf = factura.archivo.path

        subject = 'Prueba de envío de PDF'
        message = 'Este es un correo con un archivo PDF adjunto.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = ['arata.sama.fake@gmail.com']
        email = EmailMessage(subject, message, from_email, recipient_list)

        # Adjuntar el archivo PDF al correo
        with open(ruta_archivo_pdf, 'rb') as pdf_file:
            email.attach(factura.name, pdf_file.read(), 'application/pdf')


        email.send()


@receiver(post_save, sender=Tarea)
def generar_pdf_al_modificar(sender, instance, created, **kwargs):
    

    # Check if the instance already exists (update)
    if not created:

        generar_pdf(instance.pk, instance)
    pass


  