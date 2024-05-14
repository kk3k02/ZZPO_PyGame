# Instalacja projektu

W projekcie wykorzystano *Poetry* do zarządzania bibliotekami pythonowymi. Zanim uruchomisz projekt upewnij się że masz zainstalowane [poetry](https://python-poetry.org/docs/).

```bash
curl -sSL https://install.python-poetry.org | python3 -  # instaluje najnowszą wersję poetry - Linux, macOS, Windows (WSL)

(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -  # Windows (Powershell)
```

## Kopiowanie plików i instalacja bibliotek

```bash
git clone https://github.com/kk3k02/ZZPO_PyGame.git
cd ZZPO_PyGame
poetry install --no-root
poetry shell
```

## Uruchomienie projektu

```bash
python -m src.main
```
