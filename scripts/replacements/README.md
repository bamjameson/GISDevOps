# Introduction
Replacements will proccess string replacements for all files of desired type.

# Parameters
`<replacementsFile>`: Path to the file that stores all your desired environment replacements.

`<directory>`: Target directory that will be processed.

`<environment>`: Root environment elements defined in ReplacementsTemplate.json

### Example format:
`python makeReplacements.py <replacementsFile> <directory> <environment>`

# Example Usage:

The following comand will process replacements on a directory based on the DEV environment configuration stored in "ReplacementsTemplate.json"

### Process "DEV" replacements.

```
python makeReplacements.py "ReplacementsTemplate.json" "testData/" "DEV"
```
### Process "TEST" replacements.
```
python makeReplacements.py "ReplacementsTemplate.json" "testData/" "TEST"
```
### Process "PROD" replacements.
```
python makeReplacements.py "ReplacementsTemplate.json" "testData/" "PROD"
```


