import os  # Importuje moduł 'os', który dostarcza funkcje do interakcji z systemem operacyjnym, np. do odczytywania zmiennych środowiskowych.
from dotenv import load_dotenv  # Importuje funkcję 'load_dotenv' z biblioteki 'dotenv', która pozwala na załadowanie zmiennych środowiskowych z pliku .env.
from langchain_google_genai import ChatGoogleGenerativeAI  # Importuje klasę 'ChatGoogleGenerativeAI' z biblioteki 'langchain_google_genai'. Ta klasa służy do interakcji z modelami Gemini w Langchain.
from langchain.prompts import PromptTemplate  # Importuje klasę 'PromptTemplate' z biblioteki 'langchain.prompts'. Ta klasa służy do tworzenia szablonów promptów.
from langchain.schema import StrOutputParser  # Importuje klasę 'StrOutputParser' z biblioteki 'langchain.schema'. Ta klasa służy do konwersji wyniku modelu na string.

# Załaduj zmienne środowiskowe z pliku .env
load_dotenv()  # Wywołuje funkcję 'load_dotenv()', która odczytuje zmienne z pliku .env (jeśli istnieje) i ustawia je jako zmienne środowiskowe.

# Pobierz klucz API Google z zmiennej środowiskowej
google_api_key = os.getenv("GOOGLE_API_KEY")  # Używa 'os.getenv()' do pobrania wartości zmiennej środowiskowej o nazwie "GOOGLE_API_KEY". Wartość ta jest Twoim kluczem API do Google AI.

# Sprawdź czy klucz API Google został pobrany
if google_api_key is None:  # Sprawdza, czy zmienna 'google_api_key' ma wartość 'None', co oznacza, że klucz API nie został znaleziony.
    raise ValueError("Nie znaleziono klucza API Google. Upewnij się, że ustawiłeś zmienną środowiskową GOOGLE_API_KEY w pliku .env.")  # Jeśli klucz API nie został znaleziony, podnosi wyjątek 'ValueError' z odpowiednim komunikatem.

# Ustaw klucz API i zainicjuj model ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=google_api_key)  # Tworzy instancję modelu językowego Gemini za pomocą klasy 'ChatGoogleGenerativeAI'. Określa model ("gemini-1.5-pro") i przekazuje klucz API. Zmienna 'llm' będzie używana do interakcji z modelem.

# Utwórz prompt template
template = "Jak działa LangChain?"  # Definiuje zmienną 'template', która zawiera tekst promptu.
prompt = PromptTemplate.from_template(template)  # Tworzy instancję 'PromptTemplate' z tekstu promptu. 'PromptTemplate' pozwala na dynamiczne generowanie promptów.

# Stwórz łańcuch
chain = prompt | llm | StrOutputParser()  # Tworzy łańcuch (sequence) operacji. Operator '|' łączy komponenty: najpierw prompt jest formatowany, następnie przekazywany do modelu językowego ('llm'), a na końcu wynik jest konwertowany na string.

# Wykonaj zapytanie i uzyskaj odpowiedź
response = chain.invoke({})  # Uruchamia łańcuch, przekazując pusty słownik '{}' jako argument wejściowy. Słownik jest pusty, ponieważ prompt nie ma żadnych zmiennych. Wynik łańcucha jest zapisywany w zmiennej 'response'.

# Wyświetl odpowiedź
print(response)  # Wyświetla odpowiedź wygenerowaną przez model językowy.