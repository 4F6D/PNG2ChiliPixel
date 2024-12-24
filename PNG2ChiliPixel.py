from PIL import Image

# Bildpfad und Ausgabe-Dateipfad
input_image_path = 'input.png'   
output_text_path = 'output.txt'  # Name der Ausgabedatei

# Bild öffnen
image = Image.open(input_image_path)
pixels = image.load()
width, height = image.size

# Textdatei schreiben
with open(output_text_path, 'w') as file:
    for b in range(height):  
        for a in range(width):  
            r, g, b_color = pixels[a, b][:3]  # RGB-Werte extrahieren (ignoriere Alpha, falls vorhanden)
            file.write(f'gfx.PutPixel(x + {a}, y + {b}, {r}, {g}, {b_color});\n')

print(f"Das Bild wurde erfolgreich in '{output_text_path}' konvertiert.")
