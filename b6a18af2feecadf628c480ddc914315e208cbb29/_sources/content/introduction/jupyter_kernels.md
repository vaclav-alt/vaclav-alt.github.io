# Virtual environment jako Jupyter kernel

__Situace 1__: Chceme virtuální prostředí, v němž je nainstalovaný Jupyter, nazvěme ho `jupyter-env`. V tomto prostředí chceme mít v Jupyter notebook k dispozici jiné prostředí jako kernel, nazvěme ho `myenv`.

1) V prostředí `myenv` musí být nainstalován modul `ipykernel`.
```bash
source /path/to/my/virtualenvs/myenv/bin/activate
pip3 install ipykernel
deactivate
```

2) Přidáme prostředí `myenv` do Jupyter kernels v prostředí `jupyter-env`
```bash
/path/to/myenv/bin/python3 -m ipykernel --prefix=/path/to/jupyter-env \
--name myenv-name --display-name "My virtual environment"
```
 Tento příkaz vytvoří v `/path/to/jupyter-env/share/jupyter/kernels` složku `myenv-name`, ve které se nachází soubor `kernel.json` obsahující informace pro Jupyter, kde a jak spustit kernel `myenv`, neboli jak zpracovat skript v Jupyter notebook v rámci prostředí `myenv`. Obsah `kernel.json` je následující
```json
{
 "argv": [
  "/path/to/myenv/bin/python3",
  "-m",
  "ipykernel_launcher",
  "-f",
  "{connection_file}"
 ],
 "display_name": "My virtual environment",
 "name": "myenv-name"
}
```
 Parametr `display_name` je název, pod kterým bude prostředí/kernel `myenv` k dispozici v Jupyter notebook, `name` je jméno pro interní potřeby Jupyteru. `argv` jsou command line argumenty, kterými Jupyter kernel přímo spouští, tedy volá příkaz
```bash
/path/to/myenv/bin/python3 -m ipykernel_launcher -f {connection_file}
```
Odsud je vidět, proč musí být modul `ipykernel` nainstalovaný i v prostředí `myenv`.

__Situace 2__: Máme globálně nainstalovaný Jupyter a chtěli bychom v něm mít k dispozici virtuální prostředí `myenv` jakožto kernel.

1) V prostředí `myenv` musí být nainstalován modul `ipykernel`
```bash
source /path/to/my/virtualenvs/myenv/bin/activate
pip3 install ipykernel
deactivate
```
2) Přidáme prostředí `myenv` do Jupyter kernels
```bash
/path/to/myenv/bin/python3 -m ipykernel --user \
--name myenv-name --display-name "My virtual environment"
```
Tento příkaz vytvoří složku `myenv-name` v `.local/share/jupyter/kernels`, která opět obsahuje soubor `kernel.json`. Volba `--user` zde zajišťuje zápis do `~/.local/...`, tedy per-user nikoli system-wide instalaci kernelu. Bez volby `--user` se kernel nainstaluje do `/usr/share/jupyter/kernels`. Pak bude kernel přístupný pro každého uživatele, ale instalace bude vyžadovat root oprávnění.

*Poznámka*: Můžeme nainstalovat kernel i zevnitř aktivního prostředí `myenv`. Pro situaci 1:
```bash
source /path/to/my/virtualenvs/myenv/bin/activate
pip3 install ipykernel
python3 -m ipykernel --prefix=/path/to/jupyter-env \
--name myenv-name --display-name "My virtual environment"
```
A pro situaci 2:
```bash
source /path/to/my/virtualenvs/myenv/bin/activate
pip3 install ipykernel
python3 -m ipykernel --user --name myenv-name --display-name "My virtual environment"
```

## Užitečné odkazy
* <https://ipython.readthedocs.io/en/stable/install/kernel_install.html>
* <https://towardsdatascience.com/create-virtual-environment-using-virtualenv-and-add-it-to-jupyter-notebook-6e1bf4e03415>