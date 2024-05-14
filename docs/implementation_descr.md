# Opis Implementacji Gry

## Struktura Projektu

Projekt jest zorganizowany w modularny sposób, co ułatwia zarządzanie i rozwój kodu. Główne komponenty projektu znajdują się w katalogu `src` i obejmują następujące pliki:

- `main.py`: Punkt wejściowy do gry, zarządza główną pętlą gry oraz inicjalizacją wszystkich zasobów.
- `player.py`: Definiuje klasę `Player`, która reprezentuje statek gracza i zarządza jego ruchem oraz interakcjami.
- `bullet.py`: Zawiera logikę pocisków wystrzeliwanych przez gracza.
- `enemy.py`: Definiuje klasę `Enemy`, reprezentującą przeciwników w grze.
- `enemyBullet.py`: Zawiera logikę pocisków wystrzeliwanych przez przeciwników.
- `cell.py`, `virus.py`, `object.py`: Inne komponenty gry, reprezentujące różne obiekty i ich interakcje.

## Inicjalizacja Gry

Główna klasa gry, `Game`, jest zdefiniowana w pliku `main.py`. Podczas inicjalizacji (konstruktor `__init__`) wykonywane są następujące kroki:

- **Inicjalizacja Pygame**: Inicjalizowana jest biblioteka Pygame, co umożliwia tworzenie okna gry i zarządzanie zasobami multimedialnymi.
- **Ustawienia ekranu**: Określana jest szerokość i wysokość okna gry (1000x600 pikseli). Ustawiany jest tytuł okna gry.
- **Ładowanie zasobów**: Obrazy i dźwięki są ładowane z odpowiednich plików, takich jak tło, statek gracza, przeciwnicy, dźwięki strzałów i eksplozji.
- **Inicjalizacja zmiennych gry**: Inicjalizowane są zmienne kontrolujące stan gry, takie jak liczba żyć gracza, wynik, tryb szybkiego strzelania i inne.
- **Tworzenie obiektów gry**: Tworzony jest obiekt reprezentujący gracza (`Player`) oraz listy przechowujące pociski gracza, przeciwników, pociski przeciwników i inne obiekty gry.

## Główna Pętla Gry

Główna pętla gry znajduje się w metodzie `run` klasy `Game`. Pętla ta wykonuje następujące zadania:

- **Obsługa zdarzeń**: Sprawdzane są zdarzenia generowane przez użytkownika, takie jak zamknięcie okna gry. Reaguje się na naciskanie klawiszy sterujących ruchem gracza.
- **Aktualizacja stanu gry**: Pozycje gracza i innych obiektów są aktualizowane na podstawie bieżących danych wejściowych. Aktualizowane są również stany, takie jak wynik i liczba żyć.
- **Rysowanie na ekranie**: Wszystkie obiekty gry są rysowane na ekranie w odpowiednich pozycjach. Ekran jest aktualizowany, aby odzwierciedlić zmiany wprowadzone w bieżącej klatce.
- **Kontrola FPS**: Ustawiana jest liczba klatek na sekundę (60 FPS), co zapewnia płynność gry.

## Moduły Gry

Każdy moduł zawiera klasy i funkcje odpowiedzialne za specyficzne aspekty gry:

- **Klasa `Player`**: Zarządza ruchem statku gracza, jego strzałami oraz kolizjami z innymi obiektami. Ruch gracza jest kontrolowany za pomocą strzałek na klawiaturze. Konstruktor inicjalizuje gracza, ustawia początkową pozycję, kąt obrotu oraz rysuje gracza na ekranie.
- **Klasa `Bullet`**: Reprezentuje pociski wystrzeliwane przez gracza. Pociski startują z pozycji głowy gracza i poruszają się zgodnie z kątem obrotu gracza. Klasa zarządza pozycją, ruchem i rysowaniem pocisków oraz sprawdzaniem, czy pocisk znajduje się poza ekranem.
- **Klasa `Enemy`**: Reprezentuje przeciwników, którzy pojawiają się na ekranie. Przeciwnicy startują z losowych punktów na krawędziach ekranu i poruszają się w kierunku środka ekranu. Klasa zarządza ruchem, rysowaniem i losowym generowaniem początkowych pozycji przeciwników.
- **Klasa `EnemyBullet`**: Zarządza pociskami wystrzeliwanymi przez przeciwników. Pociski zmierzają w stronę gracza, a ich kierunek jest obliczany na podstawie pozycji gracza. Klasa zawiera metody do rysowania pocisków oraz aktualizacji ich pozycji.

## Inne komponenty gry, reprezentujące różne obiekty i ich interakcje

Pliki `cell.py`, `virus.py` i `object.py` zawierają definicje kluczowych obiektów w grze oraz mechanik ich interakcji:

### Klasa `Cell` (cell.py)

Klasa `Cell` reprezentuje komórki w grze, które są przeszkodami lub celami dla gracza. Główne elementy tej klasy to:

- **Inicjalizacja**: Konstruktor ustawia szerokość i wysokość ekranu, obraz reprezentujący komórkę oraz losową pozycję startową na krawędzi ekranu. Komórka może startować z dowolnego miejsca na górnej, dolnej, lewej lub prawej krawędzi ekranu.
- **Ruch**: Komórka porusza się w kierunku środka ekranu. Kierunek ruchu jest określany na podstawie początkowej pozycji komórki.
- **Rysowanie**: Komórka jest rysowana na ekranie za pomocą obrazu przypisanego do niej w momencie inicjalizacji.

### Klasa `Virus` (virus.py)

Klasa `Virus` reprezentuje wirusy w grze, które mają różne rankingi wpływające na ich wielkość i obraz. Główne elementy tej klasy to:

- **Inicjalizacja**: Konstruktor przyjmuje szerokość i wysokość ekranu, ranking wirusa oraz listę obrazów dla różnych rang wirusów. Na podstawie rankingu wybierany jest odpowiedni obraz i ustawiane są wymiary wirusa. Wirus startuje z losowej pozycji na krawędzi ekranu.
- **Ruch**: Kierunek ruchu wirusa jest ustalany na podstawie jego początkowej pozycji. Wirus porusza się w kierunku środka ekranu z losową prędkością.
- **Rysowanie**: Wirus jest rysowany na ekranie za pomocą obrazu przypisanego do niego w momencie inicjalizacji.

### Klasa `GameObject` (object.py)

Klasa `GameObject` jest bazową klasą dla innych obiektów w grze, takich jak `Player`, `Enemy`, `Cell` i `Virus`. Główne elementy tej klasy to:

- **Inicjalizacja**: Konstruktor przyjmuje szerokość i wysokość ekranu oraz obraz obiektu. Ustawiane są podstawowe właściwości obiektu, takie jak jego pozycja, szerokość, wysokość oraz obraz.
- **Rysowanie**: Metoda `draw` odpowiada za rysowanie obiektu na ekranie. Każda klasa dziedzicząca po `GameObject` może nadpisać tę metodę, aby dostosować sposób rysowania obiektu.
- **Kolizje**: Klasa `GameObject` może również zawierać metody do wykrywania kolizji z innymi obiektami. Metody te mogą być wykorzystywane przez klasy pochodne do implementacji specyficznych interakcji między obiektami.

## Interakcje i Kolizje

Gra zawiera różne typy interakcji i kolizji:

- **Kolizje gracza z przeciwnikami**: Kiedy statek gracza zderzy się z przeciwnikiem, gracz traci życie. Kolizje są wykrywane na podstawie położenia obiektów na ekranie.
- **Kolizje pocisków**: Pociski wystrzeliwane przez gracza mogą niszczyć obiekty takie jak `Virus` lub `Enemy`. Podobnie, pociski wystrzeliwane przez przeciwników (`EnemyBullet`) mogą zniszczyć statek gracza. Wykrywanie kolizji pomiędzy pociskami a obiektami opiera się na sprawdzaniu, czy pozycje tych obiektów pokrywają się.
- **Kolizje z przeszkodami**: Gracz i przeciwnicy mogą zderzać się z różnymi przeszkodami na planszy, co może wpływać na ich ruch lub prowadzić do ich zniszczenia.

## Dźwięk i Grafika

W grze zastosowano różne zasoby multimedialne, które zwiększają jej atrakcyjność i immersję. Przyjrzyjmy się szczegółowo, jakie elementy grafiki są używane i jakie dźwięki towarzyszą poszczególnym akcjom w grze.

### Grafika

Grafika w grze jest używana do reprezentowania różnych obiektów oraz tła. Oto kluczowe elementy graficzne:

- **Tło gry (`background.png`)**: Reprezentuje statyczne tło, na którym toczy się rozgrywka. Jest to obraz przedstawiający przestrzeń kosmiczną, który nadaje grze odpowiedni klimat.
- **Statek gracza (`ship.png`)**: Reprezentuje statek kosmiczny kontrolowany przez gracza. Jest to główny obiekt, którym steruje gracz, unikając przeszkód i strzelając do przeciwników.
- **Przeciwnicy (`virus2.png`)**: Obrazy przeciwników reprezentowane są przez różne wirusy. Przeciwnicy poruszają się po ekranie i stanowią zagrożenie dla gracza.
- **Komórki (`cell.png`)**: Komórki są innymi obiektami w grze, które mogą działać jako przeszkody lub cele. Mają swoje unikalne obrazy, które odróżniają je od innych obiektów.
- **Asteroidy (`virus1.png`, `dust1.png`, `dust2.png`)**: Asteroidy to przeszkody w grze, które mogą zderzać się ze statkiem gracza lub przeciwnikami. Są reprezentowane przez różne obrazy, które różnią się rozmiarami i wyglądem.

### Dźwięk

Dźwięki w grze są używane do podkreślenia różnych akcji i zdarzeń. Oto główne dźwięki używane w grze:

- **Strzał (`shoot.wav`)**: Ten dźwięk odtwarzany jest za każdym razem, gdy gracz wystrzeli pocisk ze swojego statku. Dźwięk strzału dodaje realizmu i pomaga graczowi lepiej zrozumieć, kiedy został oddany strzał.
- **Eksplozje (`bangLarge.wav`, `bangSmall.wav`)**: Dźwięki eksplozji są odtwarzane, gdy dochodzi do kolizji, na przykład gdy pocisk gracza trafia w przeciwnika lub gdy statek gracza zostaje zniszczony. `bangLarge.wav` jest używany dla większych eksplozji, a `bangSmall.wav` dla mniejszych.
- **Muzyka tła (`background.wav`)**: Odtwarzana jest ciągła muzyka tła, która nadaje grze dynamiczny i angażujący klimat. Pomaga utrzymać gracza w stanie skupienia i podkreśla atmosferę gry.
- **Inne dźwięki**: Mogą być używane dodatkowe dźwięki do innych akcji, takich jak zdobywanie punktów, trafianie w przeszkody itp.

### Szczegóły implementacji dźwięków i grafiki

- **Ładowanie zasobów graficznych**: Obrazy są ładowane z plików w momencie inicjalizacji gry. Każdy obraz jest przypisany do odpowiedniego obiektu, na przykład tło jest przypisane do zmiennej `self.background`, a obraz statku gracza do `self.playerShip`.
- **Ładowanie zasobów dźwiękowych**: Dźwięki są ładowane z plików i przypisywane do zmiennych. Na przykład, dźwięk strzału jest przypisany do `self.shoot`, a dźwięk dużej eksplozji do `self.bangLargeSound`. Ustawiana jest także głośność każdego dźwięku, aby zapewnić odpowiedni balans dźwiękowy w grze.
- **Odtwarzanie dźwięków**: Dźwięki są odtwarzane w odpowiednich momentach gry za pomocą funkcji `play`. Na przykład, dźwięk strzału jest odtwarzany w momencie wystrzału pocisku, a dźwięk eksplozji w momencie kolizji.

Dzięki zastosowaniu odpowiednich zasobów dźwiękowych i graficznych, gra staje się bardziej realistyczna i angażująca dla gracza. Grafika pomaga w identyfikacji różnych obiektów i ich stanów, a dźwięki wzmacniają wrażenia płynące z rozgrywki, informując gracza o ważnych wydarzeniach w grze.

## Podsumowanie

Projekt jest dobrze zorganizowany i modularny, co pozwala na łatwe zarządzanie kodem oraz jego rozwijanie. Każdy moduł ma jasno określoną odpowiedzialność, co ułatwia debugowanie i wprowadzanie nowych funkcji. Główne funkcje gry są zaimplementowane w sposób przejrzysty i efektywny, zapewniając płynną i angażującą rozgrywkę.
