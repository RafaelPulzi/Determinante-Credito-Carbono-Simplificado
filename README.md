# Carbon Credit Estimator

A command line tool in Python that estimates what a small or medium company would earn and spend by entering the carbon credit market through tree planting. It sizes a planting, measures CO2 absorption from tree diameter and height, and writes the results to Excel.

## What it does

**Earnings from planting trees.** You pick a species (Jatobá-da-Mata, Guapuruvu or Pau-jacaré) and give the area available in square metres. The program returns how many trees fit, what the planting costs, how long absorption takes, total CO2 absorbed and the carbon credits generated. Results are formatted as a table and can be exported to Excel.

**Carbon measurement on planted trees.** You give the number of trees of a species and the minimum and maximum diameter at breast height (DBH) and height. The program samples values within those ranges and calculates avoided carbon in tonnes per hectare, along with the matching carbon credits.

**Reading stored tables.** Opens the existing tables with planted trees, DBH, height, avoided carbon and credits generated.

## Requirements

Python 3.10 or newer.

```sh
pip install -r requirements.txt
```

That installs pandas 1.5.0, openpyxl 3.0.10 and requests 2.28.1. Everything else the program uses (`random`, `time`, `os`, `glob`) ships with Python.

## Running it

```sh
python main.py
```

The menu takes a number for each option. Spreadsheets are read from and written to `./Tabelas`, so run the program from the repository root.

## Project structure

```
main.py                  Menu and program flow
funcoes/
  tabela_criacao.py      Creates and writes Excel tables
  tabela_leitura.py      Reads existing Excel tables
Tabelas/
  BDinfoArvores_1.xlsx   Reference data on tree species
teste/                   Scratch scripts and study data
```

`funcoes` is a package, imported as `from funcoes import tabela_criacao`.

## Notes

The program expects valid numbers at each prompt and does not yet validate input. Generated spreadsheets stay out of version control, except the reference file `BDinfoArvores_1.xlsx`.

## License

MIT. See [LICENSE](LICENSE).
