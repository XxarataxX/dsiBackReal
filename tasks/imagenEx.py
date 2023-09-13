from PIL import Image
import io

# Ruta al archivo SVG de entrada y PNG de salida
input_svg_file = 'firma.svg'
output_png_file = 'salida.png'

# Abre el archivo SVG
with open(input_svg_file, 'rb') as svg_file:
    # Lee el contenido del archivo SVG
    svg_content = svg_file.read()

# Convierte el contenido SVG a imagen PNG
image = Image.open(io.BytesIO(svg_content))
image.save(output_png_file, 'PNG')