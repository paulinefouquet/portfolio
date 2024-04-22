import requests
import os
import fitz  # Module pour manipuler les fichiers PDF


# Fonction pour extraire le texte à partir d'un fichier PDF
def extract_text_from_pdf(pdf_url):
    # Télécharger le fichier PDF
    response = requests.get(pdf_url)
    if response.status_code != 200:
        print(f"Failed to download PDF from {pdf_url}")
        return ""

    with open("temp_cv.pdf", "wb") as f:
        f.write(response.content)

    # Vérifier si le fichier a été correctement téléchargé
    if not os.path.exists("temp_cv.pdf"):
        print("Failed to save the PDF file.")
        return ""

    # Ouvrir le fichier PDF
    try:
        doc = fitz.open("temp_cv.pdf")
    except Exception as e:
        print(f"Failed to open PDF file: {e}")
        return ""

    # Extraire le texte de chaque page
    text = ""
    for page in doc:
        text += page.get_text()

    # Fermer le document PDF et supprimer le fichier temporaire
    doc.close()
    return text
