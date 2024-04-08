# Balíčky a virtuální prostředí

Správa balíčků v Pythonu prošla divokým vývojem a existuje spousta navzájem špatně kompatibilních možností, jak trefně ilustruje následující příspěvěk z [xkcd](https://www.xkcd.com).
![XKCD: Python environment](https://imgs.xkcd.com/comics/python_environment.png)

V poslední době se situace ustaluje a většinu času v nepříliš specifických projektech vystačíme se standardním manažerem balíčků `pip`, případně s Anacondou.

## Virtuální prostředí

V praxi se může stát, že balíčky/moduly, které potřebujeme pro práci na různých projektech, jsou navzájem nekompatibilní, nebo si prostě chceme nějaký balíček vyzkoušet, aniž by zasahoval do funkčního prostředí.

K tomu slouží modul `virtualenv`, pomocí kterého můžeme vytvářet nezávislá prostředí, do nichž je možné instalovat další balíčky/moduly nezávisle. Modul `virtualenv` je nutné nainstalovat globálně, tedy v příkazové řádce:
```bash
pip install virtualenv   # win
pip3 install virtualenv  # linux/macos
```

Virtuální prostředí vytvoříme příkazem
```bash
virtualenv <my_env_name>
```
nebo
```bash
python -m virtualenv <my_env_name>   # win
python3 -m virtualenv <my_env_name>  # linux/mac
```
který v aktuální složce vytvoří novou složku s názvem `<my_env_name>`.

Virtuální prostředí je nutné aktivovat:
```bash
path\to\my_env\Scripts\activate    # win
source path/to/my_env/bin/activate # linux/macos
```
Po úspěšné aktivace se na začátku každého řádku v konzoli objeví název prostředí v závorce. Je-li prostředí aktivní, veškerá činnost související s pythonem nadále probíhá v tomto prostředí. Včetně instalace nových balíčků.

```{important}
Pokud si nejste jistí, co děláte, raději nikdy neinstalujte balíčky mimo virtuální prostředí.
```
```{warning}
Platnost/aktivita virtuálního prostředí je omezena na konkrétní okno příkazové řádky. Otevřu-li novou instanci příkazové řádky, žádné virtuální prostředí v ní aktivní nebude (bude chybět název v závorce).
```

Práci s virtuálním prostředím mohu ukončit jeho deaktivací příkazem
```bash
deactivate                        # linux/macos (nekdy i win)
path\to\my_env\Scripts\deactivate # win (vetsinou)
```

Pokud se ve virtuálním prostředí něco pokazí, například:
- instalace nového balíčku
- balíčky po aktualizaci přestanou být kompatibilní
- balíček obsahuje závažné chyby působící kolaps interpreta
mohu virtuální prostředí jednoduše smazat (smazaním prostředí obsahující složky) a systémová instalace zůstane nedotčena.