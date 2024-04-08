# V čem psát Python

## Textový editor

Na jednoduché skripty nám obvykle stačí obyčejný textový editor. Program napsaný v Pythonu je stejně textový soubor, který spouštíme tak, že jej předhodíme interpretovi.

## Konzole

Obdobou k systémové konzoli jsou konzole zaměřené na konkrétní jazyk. Samotný Pythoní interpret. Tedy například:
```console
$ python3
Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
Konzole je vhodná na drobné úkony, nebo testy, či jako schopnější kalkulačka. Na jakékoliv programování je spíše nevhodná.

Existuje i několik variací pokročilejších konzolí, uveďme příkladem nástroj `ipython`. Oproti výchozí pythoní konzoli `ipython` nabízí například automatické doplňování, nápovědu atd. Snadno ho nainstalujeme pomocí
```console
# linux/mac
$ pip3 install ipython
# windows
> pip install ipython
```

Součástí instalace Pythonu (na Windows pravděpodobně, na Linux někdy, na MacOS nevím) je i jednoduché Pythoní skoro-IDE s názvem _Idle_ (po Ericu Idleovi ze skupiny Monty Pyton's Flying Circus). 

```{admonition} Osobní názor
:class: important

Osobně jsem nikdy nepochopil, k čemu Idle je. Ovládá se špatně, nic moc neumí a navíc je ohyzdný.
```

## IDE

Na trhu je v současné době několik IDE (integrated development environment).

- **Spyder** solidní OpenSource IDE.
- **PyCharm** z dílny firmy JetBrains je plnohodnotné IDE se spoustou integrovaných funkcí (linting, code inspection, refactoring tools, napojení na VCS, solidní debugger atd.). Community edition je zdarma (na většinu běžné práce stačí), jako studenti máte nárok na plnou licenci (alespoň myslím).
- **VS Code** čím dál populárnější nástroj od Microsoftu. Spousta funkcionality stojí na pluginech. To znamená, že může VS Code použít takřka na cokoliv, ale rizikem je, že pluginy budou nějakým způsobem nekompatibilní.
- **Visual Studio** prý to je použitelné. Nesetkal jsem se s funkčním pokusem.

## Hybrid

Kombinace živé konzole s prvky IDE a možností ukládání session. Na tomto poli dominují nástroje ze sady Jupyter, které se vyvinuly z původního `ipython`. Nástroj, který je skvělý na seznámení s jazykem, prototypování a či některá odvětví aplikované data science.

```{admonition} Osobní názor
:class: important

Na rozsáhlejší projekty je to prostředí krajně nevhodné. Nepořádek, který vzniká v globálním scope vytváří velmi nezdravé programovací návyky.
```

Jupyter-notebook, či jeho bohatší alternativu Jupyter-lab budeme používat na hodinách. Nástroj není povinný, ale formou jupyter notebook budu sdílet většinu poznámek z hodin.