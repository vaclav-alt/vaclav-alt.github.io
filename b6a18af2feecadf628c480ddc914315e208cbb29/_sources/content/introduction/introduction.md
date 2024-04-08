# O jazyku

Podle Wiki je Python:

> ...a **high-level**, **general-purpose** programming language. Its design philosophy emphasizes code readability with the use of significant indentation.
> Python is **dynamically typed** and **garbage-collected**. It supports multiple **programming paradigms**, including structured (particularly **procedural**), **object-oriented** and **functional programming**. It is often described as a "batteries included" language due to its comprehensive standard library.

Na ta zvýrazněná slova se v průběhu semestru podíváme a řekneme se, co to v kontextu jazyka Python vlastně znamená.

Jazyk Python vyvinul v 80. letech holandský programátor Guido van Rossum a první verzi vydal v roce 1991. Python 2 byl vypuštěn roku 2000 a poté roku 2008 Python 3 - významné přepracování. Podpora Pythonu 2 měla být do roku 2015, ale nakonec se protáhla do roku 2020. Aktuální verze Pythonu je 3.12 (únor 2024).

```{note}
V čase psaní tohoto materiálu používám verzi `3.10.12`. Až na pár drobných výjimek by většina příkladů měla fungoval pro verze `>3.8`.
```

Jazyk van Rossum pojmenoval po své oblíbené televizní show Monty Python's flying circus.

![](../../images/pythons.jpeg)



A k čemu se dnes Python vlastně používá? Prakticky ke všemu.

- Data science
- scripting
- scientific computation
- automation
- game dev
- web dev
- ...

Python se v současné době řadí mezi nejpopulárnější jazyky a jeho popularita v posledních cca 12 letech stále roste. Důvodů je celá řada, mezi ty nejvýznamnější patrně patří fakt, že již součástí Python Standard Library je obrovské množství nástrojů ("batteries included" na Wiki) a celá řada dalších je k dispozici ke stažení přes různé správce balíčků (např. pip či Anaconda). Python je poměrně snadný na použití, podporuje řadu programovacích paradigmat (procedurální, OOP, funkcionální) a je poměrně čitelný (do jisté míry síla zvyku, ale pravdou je, že se kód nehemží "zbytečnými" znaky, což je umocněno ještě tím, že Python je dynamicky typovaný). Srovnejme definici obdobné funkce v Pythonu, C a ve Fortranu.

```python
# samozrejme lze napsat jeste usporneji, ale pak se vytraci porovnani
def average(array):
    sum = 0.
    for x in array:
        sum += x
    return sum / len(array)
```

```c
float average(float *array, int n) {
    float sum = 0.0;
    for (int i = 0; i < n; i++) {
        sum += array[i];
    }
    return sum / n;
}
```

```fortran
FUNCTION AVERAGE(ARRAY)
    REAL :: A(*)
    REAL :: AVERAGE
    INTEGER :: I, N

    AVERAGE = 0.0
    DO I=1, N
        AVERAGE = AVERAGE + ARRAY(I)
    END DO
    AVERAGE = AVERAGE / N
    RETURN
END FUNCTION AVERAGE
```

V extrémním případe narazíte na něco takového:

![Python developer, who has to write Java.](../../images/python_java.png)


## Kritika

Kritici nejčástěji uvádějí dva důvody, proč jim Python vadí:

1. Python je pomalý.
2. Python je dynamicky typovaný.

Osobně jsem poněkud alergický na stížnosti na rychlost Pythonu. Ačkoliv existují dobré důvody, proč běžné operace kompilovaný jazyk jako C, C++ nebo Java zvládne rychleji než Python, řada příkladů ilustrujících to, jak je Python pomalý, je poměrně hloupá a plyne z nepochopení toho, jak Python funguje. Ovšem i řada zastánců se dopouští při obhajobě rychlosti Pythonu podivných přešlapů a demostruje to spravení špatně napsaného kódu, který následně v Pythonu trochu opraví způsobem, který je aplikovatelný v každém jazyce (např. cachování při výpočtu Fibonacciho čísel). Zkrátka *bad code is bad*. Během tohoto kurzu se pokusím osvětlit, co stojí za tím, že je Python pomalý a jak se tomu vyhnout jiným způdobem, než úpravou algoritmu.

Druhá výtka nesměřuje ani tak na Python samotný, jako spíš celkově na dynamicky typované jazyky. Mnoho lidí považuje dynamické typování za zdroj veškerého zla ve světě. Má zkušenost ukazuje, že záleží na kontextu. V kratších či jednodušších programech nebo prototypech umožňuje dynamické typování psát rychleji a v jistém smyslu přehledněji. Kód v dynamicky typovaném jazyce může být poměrně univerzální (viz například funkce `average` výše - bude fungovat s celými i necelými čísly). Ale u větších projektů to bývá právě tato nevázanost, která se vymstí. Zhruba od verze 3.6 se tedy v Pythonu začíná objevovat podpora typování, určená ke statické analýze kódu. Je to nenahraditelný pomocník, který pomůže odhalit řadu spících chyb dříve než v provozu. Budeme se tomu věnovat.

## Interpretovaný, nikoliv kompilovaný. Možná trochu obojí.

**Jednoduchá ne tak úplně pravda:** Python je interpretovaný jazyk. Abychom mohli program napsaný v jazyce Python spustit, potřebujeme mít nainstalový program, kterému se říká *interpret*, který napsaný program řádek po řádku prochází a vykonává. Liší se tak od kompilovaných jazyků, jako například C, C++, Fortran. Programy napsané v nich překládá takzvaný *kompilátor* do strojové jazyka, který se už skládá z instrukcí přímo pro procesor.

**Složitější víceméně pravda:** Python ve skutečnosti prochází kompilací a je to až výsledek této kompilace, který je interpretován. Ten zásadní rozdíl oproti kompilovaným jazykům je, že výsledek této _prekompilace_ není strojový kód, ale v případě pythonu tzv. _bytecode_, což je jakási low-level reprezentace jazyka, kterou pak _Python Virtual Machine_ (PVM) přímo vykonává. Právě PVM zde pak hraje roli toho interpreta.

Tento přístup je poměrně běžný (stejně to dělá např. Java). Má to své výhody - kompilátor typicky provede pár věcí navíc, jako např.:

 - řadu kontrol (v této fázi např. hlásí `SyntaxError`, se kterou se v průběhu semestru dobře seznámíte),
 - základní sémantickou analýzu,
 - mírnou optimalizaci (oproti např. jazyku C++ skutečně mírnou),
 - vygeneruje bytecode.
 
 Pokud se zdrojový kód nezměnil, bytecode se znovu nevytvaří a jeho vykonávání bývá typicky rychlejší než přímá interpretace. Prekompilované kódy naleznete ve složce `__pycache__`.

Je dokonce možné Python zcela zkompilovat do jednoho standalone executable souboru, ale v praxi to znamená, že součástí toho executable musí být is celý PVM. Je to relativně obtížné a přináší to minimum výhod. Nebudeme se tím zabývat.

```{note}
Pro rýpaly: ano, správně, jazyk není interpretovaný ani kompilovaný - to jsou vlastnosti jeho implementace (o nich více níže). Když se budete nudit, můžete napsat kompilátor pro Python nebo interpret pro C, ale bude to těžké. Některé implementace jazyka Python (PyPy) zahrnují _just-in-time_ (JIT) kompilaci, která bytecode překládá přímo do strojového.
```

## Co tedy vlastně Python je?

Jenoduše řečeno, Python je programovací jazyk. Jeho sémantiku a syntaxi naleznete popsanou v dokumentaci v sekci [The Python Language Reference](https://docs.python.org/3/reference/index.html) a základní výbavu, tedy moduly a balíčky, kterou jsou součástí, v sekci [The Python Standard Library](https://docs.python.org/3/library/index.htm). V zásadě vám nic nebrání toto vše nějakým způsobem implentovat a výslednému produktu můžete říkat Python. K tomuto datu (únor 2024) si nejsem vědom žádné formálnější specifikace a jsem přesvědčen, že neexistuje. Ale sami autoři přiznávají, že Language Reference není jednoznačně specifikující: 

> ...if you were coming from Mars and tried to re-implement Python from this document alone, you might have to guess things and in fact you would probably end up implementing quite a different language.

Není překvapivé, že existuje několik implementací jazyka Python. Mezi hlavní patří

- **CPython**: nejpopulárnější a nejrozšířenější implementace jazyka, napsaná v jazyce C. Nainstalujete-li si Python naslepo, velmi pravděpodobně si nainstalujete tuto implementace. Projekt je open-source, můžete se na něm klidně podílet. Doporučuji do zdrojových kódů CPython občas nahlédnout, může to být velmi poučné. Vše ke stažení na [GitHubu](https://github.com/python/cpython).
- **Jython**: implementace v Java.
- **PyPy**: pozoruhodná, ale populární implementace - Python implementovaný v jazyce Python.  Mírně rozšiřuje základní výbavu, dodává JIT, čímž v některých případech dosahuje až pětinásobného zrychlení.

V průběhu semestru budu mluvit v podstate výhradně o CPython. Pokud budete používat jinou implementaci, můžete narazit na rozdíly a nemohu garantovat, že vám vše bude fungovat.

### PEP

Vývoj Pythonu je řízen prostřednictvím takzvaných PEPs - [Python Enhancement Proposals](https://peps.python.org/). V nich nalezneme dokumenty popisující širokou škálu záležitostí - postup při návrhu nových funkcí, postup při nakládání s deprecated vlastnostmi nebo třeba samotné návrhy nových vlastností. Vyberme z nich dva nejznámější příspěvky. 

#### PEP 8

Style Guide for Python Code. V průběhu semestru se budeme snažit tímto řídit (ikdyž přímo v PEP 8 se píše, že vynucovat si styl za každou cenu je pošetilé

> "A Foolish Consistency is the Hobgoblin of Little Minds").

#### PEP 20

The Zen of Python. Má jít od seznam 20 principů, jimiž se návrh Pythonu řídí, ale dostalo se jich tam jen 19.

1. Beautiful is better than ugly.
1. Explicit is better than implicit.
1. Simple is better than complex.
1. Complex is better than complicated.
1. Flat is better than nested.
1. Sparse is better than dense.
1. Readability counts.
1. Special cases aren't special enough to break the rules.
1. Although practicality beats purity.
1. Errors should never pass silently.
1. Unless explicitly silenced.
1. In the face of ambiguity, refuse the temptation to guess.
1. There should be one-- and preferably only one --obvious way to do it.
1. Although that way may not be obvious at first unless you're Dutch.
1. Now is better than never.
1. Although never is often better than *right* now.
1. If the implementation is hard to explain, it's a bad idea.
1. If the implementation is easy to explain, it may be a good idea.
1. Namespaces are one honking great idea -- let's do more of those!


## Kde a co studovat?

- studijní opory - BookKit. najdete v odkazech na stránce předmětu.
- Dokumentace k jazyku Python, [docs.python.org/3/](https://docs.python.org/3/)
  - (The Python Language Reference)[https://docs.python.org/3/reference/index.html]
  - (Beginner's guide)[https://wiki.python.org/moin/BeginnersGuide]
  - (The Python Language Reference)[https://docs.python.org/3/reference/index.html]
- Film Python (2000), [csfd.cz/film/30525-python](https://www.csfd.cz/film/30525-python)
- YouTube, kanál [Arjan Codes](https://www.youtube.com/@ArjanCodes)
- [https://knihy.nic.cz/files/edice/python_3.pdf](https://knihy.nic.cz/files/edice/python_3.pdf)
- [https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/)

```{warning}
Buďte opatrní při používání náhodných YT tutoriálů nebo online návodů - často jsou v nich nesmysly. Když si nejste jisti, můžete se mě zeptat.
```
