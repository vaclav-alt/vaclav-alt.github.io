# Jupyter

> JupyterLab is the latest web-based interactive development environment for notebooks, code, and data. Its flexible interface allows users to configure and arrange workflows in data science, scientific computing, computational journalism, and machine learning. A modular design invites extensions to expand and enrich functionality.

Projekt Jupyter přináší dva produkty Jupyter Notebook a Jupyter Lab. Základem je koncept Notebooku - sešitu, který se skládá z buněk dvou typů: python a markdown[^markdown]. Je to formát, který je populární pro výukové materiály, prezentaci výsledků či jednoduché interaktivní aplikace. Jupyter Lab k tomu přidává i poněkud bohatší prostředí, přinášející i několik prvků klasických IDE.

[^markdown]: Markdown je relativně standardizovaný značkovací jazyk určený pro jednoduchou sazbu strukturovaného textu

Celé to má podobu webové aplikace. Spustit Jupyter Notebook/Lab tedy typicky znamená spustit lokální webový server, který vše obsluhuje.

Ukázky, návody apod. naleznete na domovské stránce projektu: [Jupyter](https://jupyter.org/). Zde si pouze ukážeme, jak se Jupyter instaluje.


## Jupyter a první program

Budu zde vycházet z pracovního prostředí, tak jak je popsáno [zde](sec-work-environment). Níže je celý postup pro Windows a pro Linux/MacOS, včetně přípravy virtuálního prostředí. Můžete samozřejmě využít již existující virtuální prostředí.

```{important}
Stejně jako ostatní balíčky, i Jupyter instalujeme **zásadně** do virtuálního prostředí.
```

### Windows

```console
> cd
C:\Users\vaclav\python
# vytvoreni virt. prostredi se standardnim nazvem venv
> virtualenv venv
# muzeme overit vypsanim slozek, venv bude mezi nimi
> dir
# aktivace prostredi
> venv\Scripts\activate
# aktivni prostredi je uvede v zavorce na zacatku promptu
(venv) >
# instalace Jupyteru
(venv) > pip install notebook
# spusteni prostredi jupyter notebook
(venv) C:\python>jupyter-notebook
```

### Linux/MacOS

```console
$ pwd
/home/vaclav/python
# vytvoreni virt. prostredi se standardnim nazvem venv
$ virtualenv venv
# aktivace prostredi
$ source venv/env01/bin/activate
(venv) $ 
# instalace Jupyteru (pokud jeste nemame)
(venv) $ pip3 install notebook
# spusteni prostredi
(venv) $ jupyter-notebook
```

```{note}
Prostředí Jupyter Lab se instaluje pod názvem `jupyter-lab`, ale spouští se pod názvem `jupyterlab`. Ty pomlček v průběhu let přicházely a odcházely. Nebude-li vám to fungovat, vyzkoušejte více kombinací.
```

## První program v Jupyteru

V prostředí Jupyter-notebook tak uvidíte všechny soubory a složky, které se nachází v naší kořenové složce `python`, ze které jsme Jupyter spustili.

Vyvořte si v prostředí novou buňku, ujistěte se, že je typu `Code` a vepiště do ní
```python
print("Hello world")
```
Klepnutím na tlačíko "play" či stiskem kláves `Ctrl+Enter` buňku spustíte.
