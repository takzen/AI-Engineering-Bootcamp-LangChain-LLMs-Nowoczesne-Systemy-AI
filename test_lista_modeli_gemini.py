import os
from dotenv import load_dotenv
import google.generativeai as genai

# Załaduj zmienne środowiskowe z pliku .env
load_dotenv()

# Pobierz klucz API Google z zmiennej środowiskowej
google_api_key = os.getenv("GOOGLE_API_KEY")

# Sprawdź czy klucz API Google został pobrany
if google_api_key is None:
    raise ValueError("Nie znaleziono klucza API Google. Upewnij się, że ustawiłeś zmienną środowiskową GOOGLE_API_KEY w pliku .env.")

# Konfiguracja klucza API
genai.configure(api_key=google_api_key)

# Wyświetlenie listy modeli
for model in genai.list_models():
    print(model)