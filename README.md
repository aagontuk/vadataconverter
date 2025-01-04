# VADataConverter

To process verbal autopsy data.

## How to Download VADataConverter ##

1. Download the zip file from this link: https://github.com/aagontuk/vadataconverter/releases/download/v2.0.0/vadataconverter.zip
2. Unzip it.
3. Go to vadataconverter folder.
4. Double click on vadataconverter to run the software.

## How to Use ##

1. Click `Add` and add one or more verbal autopsy data CSV file.
2. CSV files must contain "icd10", "age" and "sex" columns.
3. After adding desired files click `Convert`.
4. Software will process each file and create a new xlsx file for each file with processed data.

## Developer Instruction ##

* PyInstaller is used for packaging windows binary
```
pyinstaller.exe --noconsole vadataconverter.py
```

* Using the converter from commandline

The converted takes a csv file and creates a xlsx file.

```
python converter.py --input-file vadataoriginal.csv --output-file vadataconverted.xlsx --sheet-name vadata
```
