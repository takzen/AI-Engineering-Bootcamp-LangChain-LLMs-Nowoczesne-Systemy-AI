# Langchain i Gemini - Przykładowe lekcje

Ten projekt zawiera dwa skrypty Pythona, które demonstrują przykładowe lekcje kursu

## Opis Skryptów

*   **`lekcja25.py`**: Ten skrypt demonstruje podstawowe generowanie tekstu za pomocą modelu Gemini. Klucz API jest pobierany z pliku `.env`. Skrypt konfiguruje połączenie z Gemini i generuje odpowiedź na zadane pytanie.
*   **`lekcja31.py`**: Ten skrypt pokazuje, jak używać Langchain do tworzenia łańcucha (sequence) operacji. Łańcuch ten składa się z:
    *   Szablonu promptu (`PromptTemplate`).
    *   Modelu językowego Gemini (`ChatGoogleGenerativeAI`).
    *   Parsera wyjścia (`StrOutputParser`), który konwertuje wynik na tekst.

## Wymagania

*   Python 3.12.8 
*   Biblioteki Python:
    *   `langchain`
    *   `langchain-google-genai`
    *   `python-dotenv`
    *   `google-generativeai`

## Instalacja

1.  Sklonuj repozytorium:

    ```bash
    git clone https://github.com/takzen/AI-Engineering-Bootcamp-LangChain-LLMs-Nowoczesne-Systemy-AI.git
    cd AI-Engineering-Bootcamp-LangChain-LLMs-Nowoczesne-Systemy-AI

2.  Stwórz środowisko wirtualne (opcjonalne, ale zalecane):

    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/macOS
    venv\Scripts\activate.bat  # Windows
    ```

3.  Zainstaluj wymagane biblioteki:

    ```bash
    pip install langchain langchain-google-genai python-dotenv google-generativeai
    ```

## Konfiguracja

1.  Utwórz plik `.env` w głównym katalogu projektu.
2.  Dodaj do pliku `.env` zmienną `GOOGLE_API_KEY` z Twoim kluczem API Google AI:

    ```
    GOOGLE_API_KEY="TWÓJ_KLUCZ_API"
    ```

    **Uwaga:** Nie udostępniaj swojego klucza API publicznie. Upewnij się, że plik `.env` jest dodany do `.gitignore`, aby nie był przechowywany w repozytorium Git.

## Użycie

1.  Upewnij się, że Twoje środowisko wirtualne jest aktywne (jeśli go używasz).
2.  Uruchom dowolny skrypt:

    ```bash
    python lekcja25.py
    ```

    lub

    ```bash
    python lekcja31.py
    ```

    Skrypt wygeneruje odpowiedź na pytanie "Jakie są główne zalety uczenia maszynowego?" (w przypadku `lekcja25.py`) lub "Jak działa LangChain?" (w przypadku `lekcja31.py`) przy użyciu modelu Gemini.

## Wyjaśnienie Kodu

*   **Klucz API:** Oba skrypty pobierają klucz API Google z pliku `.env`. Jest to bezpieczniejszy sposób przechowywania klucza niż umieszczanie go bezpośrednio w kodzie.
*   **Langchain:** Skrypt `lekcja31.py` demonstruje użycie Langchain do tworzenia łańcucha (sequence) operacji. Langchain ułatwia łączenie różnych komponentów (prompty, modele, parsery) w celu tworzenia bardziej złożonych aplikacji.

## Plik requirements.txt
Aby ułatwić instalacje stwórz plik `requirements.txt` z następującą zawartością:

```text
langchain
langchain-google-genai
python-dotenv
google-generativeai