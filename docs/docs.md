# Dokumentacja kodu

W projekcje zdecywowano się wykorzystać nowe standardy Pythona związane z dokumentacją kodu. Poniżej znajduje się opis konwencji oraz wykorzystane narzędzia do automatycznej generacji dokumentacji z kodu.

## Dokumentowanie kodu za pomocą docstringów

Konwencja Pythona [PEP 257](https://peps.python.org/pep-0257/) wyjaśnia sposób dokumentacji kodu.
Zgodnie z tą konwencją każdy moduł, klasa oraz funkcja powinny posiadać komentarz dokumentacyjny - tak zwany docstring.
Jego treść jest umieszczona pomiędzy potrójnymi znakami cudzysłowów `""" """`. W docstringu znajduje się opis działania,
przyjmowanych argumentów oraz zwracanych wartości. Są różne style pisania docstringów. W niniejszym projekcje zdecydowano się
na styl zaproponowany przez Google ze względu na jego przejrzystość.

Na poniższym listingu widnieje przykładowy docstring napisany w stylu Google.

```Python
def fetch_smalltable_rows(
    table_handle: smalltable.Table,
    keys: Sequence[bytes | str],
    require_all_keys: bool = False,
) -> Mapping[bytes, tuple[str, ...]]:
    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
        table_handle: An open smalltable.Table instance.
        keys: A sequence of strings representing the key of each table
          row to fetch.  String keys will be UTF-8 encoded.
        require_all_keys: If True only rows with values set for all keys will be
          returned.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {b'Serak': ('Rigel VII', 'Preparer'),
         b'Zim': ('Irk', 'Invader'),
         b'Lrrr': ('Omicron Persei 8', 'Emperor')}

        Returned keys are always bytes.  If a key from the keys argument is
        missing from the dictionary, then that row was not found in the
        table (and require_all_keys must have been False).

    Raises:
        IOError: An error occurred accessing the smalltable.
    """
```

## Generowanie dokumentacji z kodu

Do tego celu były rozważane 2 powszechne narzędzia - Sphinx oraz MkDocs. Oba narzędzia pozwalają na generowanie dokumentacji z kodu na podstawie wcześniej przygotowanych docstringów. Sphinx zwykle wykorzystywany w dużych projektach ze względu na możliwość większego dostowowania jego opcji do własnych potrzeb, co jednak mocno komplikuje jego konfigurację. Z tego powodu zdecydowano się na MkDocs ze względu na bardziej intuicyjna konfigurację oraz wsparcie dla markdowna.

MkDocs to szybki i prosty generator statycznych stron internetowych, który jest przeznaczony do tworzenia dokumentacji projektu. Pliki źródłowe dokumentacji są pisane w Markdown i konfigurowane za pomocą pojedynczego pliku konfiguracyjnego YAML.

### Struktua plików związanych z MkDocs

```bash
├── docs
│   ├── api_reference
│   │   ├── bullet_reference.md
│   │   ├── cell_reference.md
│   │   ├── enemy_bullet_reference.md
│   │   ├── enemy_reference.md
│   │   ├── player_reference.md
│   │   └── virus_reference.md
│   ├── docs.md
│   └── index.md
├── src
└── mkdocs.yml
```

### Struktura pliku konfiguracyjnego `mkdocs.yml`

MkDocs konfigurowane jest za pomocą jednego pliku. Poniżej przedstawiono plik konfiguracyjny naszego projektu.

```yml
# Nazwa projektu
site_name: ZZPO Project documentation
copyright: ZZPO Team

# Konfiguracja wyglądu strony
theme:
  name: "material"
  palette:
    # Palette toggle for light mode
    - scheme: default
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    # Palette toggle for dark mode
    - scheme: slate
      toggle:
        icon: material/brightness-4
        name: Switch to light mode

# Podlinkowanie plików z treścią srony
nav:
  - Home: 'index.md'
  - API Reference:
    - Player: 'api_reference/player_reference.md'
    - Virus: 'api_reference/virus_reference.md'
    - Cell: 'api_reference/cell_reference.md'
    - Enemy: 'api_reference/enemy_reference.md'
    - Enemy Bullet: 'api_reference/enemy_bullet_reference.md'
    - Bullet: 'api_reference/bullet_reference.md'

# Opcjonalne wtyczki i rozszerzenia
plugins:
  - search
  - mkdocstrings

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - tables
```
