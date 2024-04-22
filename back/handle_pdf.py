import requests
import fitz  # Module pour manipuler les fichiers PDF


# Fonction pour extraire le texte à partir d'un fichier PDF
def extract_text_from_pdf(pdf_url):
    # Télécharger le fichier PDF
    response = requests.get(pdf_url)
    with open("temp_cv.pdf", "wb") as f:
        f.write(response.content)

    # Ouvrir le fichier PDF
    doc = fitz.open("temp_cv.pdf")

    # Extraire le texte de chaque page
    text = ""
    for page in doc:
        text += page.get_text()

    # Fermer le document PDF et supprimer le fichier temporaire
    doc.close()
    return text
