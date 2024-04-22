ENVIRONMENT = "dev"

# Saisissez votre Key obtenu sur le site edenai format "Bearer xxxxxxxxxxx...xxxx"
# EDENAI_KEY = passwordkey
AZURE_OPENAI_KEY = passwordkey
PORT = 8000  # port utiliser par uvicorn
FRONT_URL = (
    "http://staging-pauline-portfolio.westeurope.azurecontainer.io"
    if ENVIRONMENT == "dev"
    else "http://pauline-portfolio.westeurope.azurecontainer.io"
)

URL_CV_PDF = (
    "https://drive.google.com/file/d/1n9OPn9PZDrXbHebV9eXkzbEpfKbpzt0-/view?usp=sharing"
)
