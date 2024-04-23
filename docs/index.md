# ZZPO

Celem naszego projektu jest stworzenie gry 2D której logika jest wzorowana na popularnej grze “Asteroids”. W naszej grze gracz wciela się w postać z popularnej kreskówki i walczy ze złymi bakteriami i wirusami.

## Wymagania funkcjonalne

- Gracz może kontrolować swoją postać poprzez ruch przód, tył, obrót w prawo, obrót w lewo oraz strzał.
- Gra generuje losowych przeciwników, którzy poruszają się ruchem jednostajnym prostoliniowym.
- Gracz może niszczyć przeciwników poprzez strzelanie do nich.
- Niektórzy przeciwnicy również posiadają możliwość strzelania.
- Przeciwnik po trafieniu rozpada się na mniejsze części lub ulega całkowitemu zniszczeniu.
- Gracz traci życia w momencie zderzenia lub trafieniu wrogim pociskiem.
- Gracz zwiększa swój wynik poprzez trafianie przeciwników.

## Wymagania niefunkcjonalne

- Gra desktopowa, napisana w języku python z wykorzystaniem biblioteki pygames.

## Pojęcia

- `Gracz`: postać sterowana przez osobę grającą w grę.
- `Przeciwnik`: postać sterowana przez komputer.
- `Trafienie`: kolizja pocisku z graczem lub przeciwnikiem.
- `Zderzenie`: kolizja gracza z przeciwnikiem.
- `Obrażenia`: łączna suma zderzeń i kolizji gracza z przeciwnikiem.
- `Życia`: maksymalna ilość obrażeń możliwa do przyjęcia.
- `Wynik`: suma punktów uzyskanych za trafienia przeciwników.
