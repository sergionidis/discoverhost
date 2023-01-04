# discoverhost

```
Tool para realizar consultas dns sobre un dominio base para descubrir posibles subdominios mediante fuerza bruta.
Brute force dns tool
Dominio base:
google.com
Posibles subdoinios:
www.google.com
support.google.com
etc 

```

## Instalación


```
git clone https://github.com/sergionidis/discoverhost.git
cd discoverhost
pip install -r requirements.txt
```

## Uso

```
python discoverhost.py -t nmap.org -l https://raw.githubusercontent.com/sergionidis/discoverhost/master/subdominios.txt

```
