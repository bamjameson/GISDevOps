![Image of Yaktocat](media/logo.png)

Replacements will proccess string replacements for all files of desired type.

# Parameters
`<replacementsFile>`: Path to the file that stores all your desired environment replacements.

`<directory>`: Target directory that will be processed.

`<environment>`: Root environment elements defined in ReplacementsTemplate.json

### Example format:
`python makeReplacements.py <replacementsFile> <directory> <environment>`

# Example Usage:

The following comand will process replacements on a directory based on the TEST environment configuration stored in "ReplacementsTemplate.json"

### Command
```
python3 makeReplacements.py "ReplacementsTemplate.json" "testData/" "TEST"
```
### Response
```
     ___          _                           _      
    | _ \___ _ __| |__ _ __ ___ _ __  ___ _ _| |_ ___
    |   / -_) '_ \ / _` / _/ -_) '  \/ -_) ' \  _(_-<
    |_|_\___| .__/_\__,_\__\___|_|_|_\___|_||_\__/__/
            |_|                                                    
    

Making replacements for TEST environment.
-------------------------------------------------------------
Changing dev.mydomain.com to test.mydomain.com in testData/file2.json
Changing dev.mydomain.com to test.mydomain.com in testData/file1.xml
Changing Replace02 to Replace03 in testData/file2.json
Changing Replace02 to Replace03 in testData/file1.xml

---------------------------
  Replacements complete.   
---------------------------

```
