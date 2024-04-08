# CLI

Pro práci s Pythonem se hodí umět ovládat _příkazovou řádkou_ (command prompt, terminal). Do příkazové řádky zadáváme příkazy, kterými můžeme manipulovat se systémem, souboru atd. Nějakou formu příkazové řádky najdeme v každém běžném systému. Ačkoliv každý systém a každá příkazová řádka má svá specifika, za kládní princip a manipulace jsou stejné nebo jen mírně odlišné. Následující odstavce shrnují to nejnutnější, co budeme potřebovat, jak pro systém Windows, tak pro Linux a MacOS (u nich je vše praktické stejné).

Ve Windows ji najdeme jako program s názvem _Command Prompt_, a snadno jej spustít např. pomocí `Win+R`, což otevře konzoli "Run", kam zadáte `cmd` a potvrdíte.

Na MacOS stačí vyhledat aplikaci `Terminal`.

Pokud používáte linux, příkazovou řádku otevřít umíte.

Rozhraní příkazové řádky je jednoduché. Typicky zobrazuje, v jaké složce uživatel nachází, což po startu bývá jeho domovský adresář, a očekává od něho vstup - příkaz (command prompt). Na Windows to vypadá takto

```console
C:\Users\Vaclav> 
```

Na Linux a na MacOS nějak takto:

```console
vaclav@mypc:~$ 
```
kde vlnovka `~` je zkratka právě pro domovský aresář `/home/vaclav`.

Následující tabulka shrnuje základní příkazy.


||Windows|mac/linux|
|---|---|---|
| aktuální složka | `cd` | `pwd` |
| vypsat soubory a složky | `dir` | `ls`|
| přejít do složky s cestou `path` | `cd path` | `cd path` |
| vytvořit složku `newdir` | `mkdir newdir` | `mkdir newdir` |
| odstranit soubor `file` | `del file` | `rm file` |
| odstranit slozku `dir` | `rmdir dir` | `rmdir dir` |

## Příkazy, programy a `PATH`

Některé příkazy umít vykonávat přímo program reprezentovaný příkazovou řádkou (konkrétní command processor). Většina příkazů jsou ve skutečnosti samostatné programy, které ten či onen command processor umí "najít". Systém (případně konkrétní command processor - na linux třeba bash)  si udržuje seznam míst, kde se nachází programy, které mají být dostupné jako příkazy. Tento seznam míst se nachází právě v proměnné prostředí `PATH`.  

Jedním z takových příkazů-programů je například pythoní interpret, tedy program s názvem `python` (na Linuxu a často na MacOS `python3`), díky kterému můžeme spouštět programy napsané v Pythonu

```console
C:\User\vaclav\programovani> python hello.py
Hello World!
```

```{warning}
Abychom nemuseli na Windows ručně upravovat proměnnou `PATH`, je třeba při instalaci Pythonu zaškrtnout možnost "Add Python to PATH". Systém by jinak nevěděl, kde se interpret Pythonu nachází a neuměl by program spustit.
```

(sec-work-environment)=
## Pracovní prostředí

Doporučuji si pro potřeby tohoto kurzy založit složku, do které si budete vkládat vše, co zde budeme dělat. Je jedno, kde to bude. V knize budu v pracovat ve složce `python` umístěné v domovském adresáři, tedy pro linux/mac:
```console
vaclav@mypc:~/python$ 
```
nebo pro Windows
```console
C:\Users\vaclav\python> 
```

A protože ta samotná složka většinu času nebude příliš důležitá, a většina pro nás důležitých příkazů je stejná či podobná na Windows/Linux/Mac, budu většinu konzolových vstupů redukovat na toto
```console
$ 
```
Bude-li nutné zvlášť vyčlenit příklad pro Windows, uvedu
```console
>
```

## Python console

Občas budu v textu ukazovat příkazy v Pythoní konzoli (o ní ještě bude řeč) a budu ji značit `>>>`, tj.

```console
>>> 
```