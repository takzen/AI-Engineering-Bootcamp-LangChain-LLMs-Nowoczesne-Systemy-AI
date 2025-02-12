import os  # Importuje moduł 'os', który dostarcza funkcje do interakcji z systemem operacyjnym, np. do odczytywania zmiennych środowiskowych.
from dotenv import load_dotenv  # Importuje funkcję 'load_dotenv' z biblioteki 'dotenv', która pozwala na załadowanie zmiennych środowiskowych z pliku .env.
import google.generativeai as genai  # Importuje bibliotekę 'google.generativeai' jako 'genai'. Ta biblioteka służy do interakcji z modelami generatywnymi Google, takimi jak Gemini.

# Załaduj zmienne środowiskowe z pliku .env
load_dotenv()  # Wywołuje funkcję 'load_dotenv()', która odczytuje zmienne z pliku .env (jeśli istnieje) i ustawia je jako zmienne środowiskowe.

# Pobierz klucz API Google z zmiennej środowiskowej
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Używa 'os.getenv()' do pobrania wartości zmiennej środowiskowej o nazwie "GOOGLE_API_KEY". Wartość ta jest Twoim kluczem API do Google AI.

# Sprawdź czy klucz API Google został pobrany
if GOOGLE_API_KEY is None:  # Sprawdza, czy zmienna 'GOOGLE_API_KEY' ma wartość 'None', co oznacza, że klucz API nie został znaleziony.
    raise ValueError("Nie znaleziono klucza API Google. Upewnij się, że ustawiłeś zmienną środowiskową GOOGLE_API_KEY.")  # Jeśli klucz API nie został znaleziony, podnosi wyjątek 'ValueError' z odpowiednim komunikatem.

# Konfiguracja klucza API Google
genai.configure(api_key=GOOGLE_API_KEY)  # Konfiguruje bibliotekę 'genai' (Google AI), ustawiając klucz API na wartość pobraną z zmiennej środowiskowej. To jest konieczne, aby uwierzytelnić Twoje żądania do Google AI.

def generate_text(prompt):  # Definiuje funkcję o nazwie 'generate_text', która przyjmuje jeden argument - 'prompt' (tekstowe zapytanie do modelu).
    try:  # Otwiera blok 'try', który pozwala na przechwytywanie potencjalnych błędów podczas wykonywania kodu wewnątrz bloku.
        model = genai.GenerativeModel('gemini-1.5-pro')  # Tworzy instancję modelu generatywnego Gemini o nazwie 'gemini-1.5-pro'. To określa, którego modelu językowego chcesz użyć.
        chat = model.start_chat()  # Rozpoczyna sesję czatu z modelem. Sesja czatu pozwala na prowadzenie wieloetapowych konwersacji z modelem.

        response = chat.send_message(prompt)  # Wysyła 'prompt' (zapytanie) do modelu czatu i zapisuje odpowiedź w zmiennej 'response'.
        return response.text.strip()  # Wyodrębnia tekst z odpowiedzi ('response.text') i usuwa białe znaki z początku i końca tekstu ('strip()'). Następnie zwraca ten tekst jako wynik funkcji.
    except Exception as e:  # Przechwytuje wszelkie wyjątki, które mogą wystąpić w bloku 'try'. Zmienna 'e' przechowuje informacje o wyjątku.
        print(f"Błąd podczas generowania tekstu: {e}")  # Wyświetla komunikat o błędzie, zawierający informacje o wyjątku.
        return None  # Zwraca 'None', aby zasygnalizować, że generowanie tekstu nie powiodło się.

prompt = 'Jakie są główne zalety uczenia maszynowego?'  # Definiuje zmienną 'prompt', która zawiera tekstowe zapytanie, które zostanie wysłane do modelu.
response = generate_text(prompt)  # Wywołuje funkcję 'generate_text' z zdefiniowanym 'prompt' i zapisuje wynik w zmiennej 'response'.

if response:  # Sprawdza, czy zmienna 'response' ma wartość różną od 'None' (czyli czy generowanie tekstu powiodło się).
    print('Model odpowiedział:', response)  # Jeśli generowanie tekstu się powiodło, wyświetla komunikat zawierający odpowiedź modelu.
else:  # Jeśli generowanie tekstu się nie powiodło (zwrócono 'None').
    print("Nie udało się wygenerować odpowiedzi.")  # Wyświetla komunikat informujący o niepowodzeniu generowania odpowiedzi.