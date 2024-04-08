# Instalace

Instalací jazyka Python máme na mysli instalaci interpreta. V zásadě jsou na výběr dvě možnosti:

1. standardní Python, [python.org](https://www.python.org)
1. Anaconda distribution, [anaconda.com](https://www.anaconda.com)

Anaconda je distribuce Python, která sdružuje balíčky relevantní pro "data science" a součástí je i manažer balíčku (alternativa k `pip`). Na Windows a MacOS funguje příjemně, na Linux je třeba postupovat trochu opatrněji kvůli případným kolizím se systémovou instalací.

Celé materiály budou psané s ohledem na standardní Python, jehož instalace je popsána v knize k předmětu - [zde](https://uuapp.plus4u.net/uu-bookkit-maing01/53a20e3ea54944218d769347a3cad1c1/book/page?code=47568968).


Instalaci ověříme tak, že zkusíme z příkazové řádky (konzole, terminálu, *command line* atp.) interpreta spustit.

``` console
> python   # win
$ python3  # linux/macos
```

```{tip}
Pokud uvidíte nějakou zprávu o tom, že příkaz python je neznámý, znamená to, že instalace selhala, nebo že python nebyl přidán do proměnné `PATH`. Zkuste interpreta přeinstalovat nebo si vyhledejte, jak se `PATH` aktualizuje manuálně.
```