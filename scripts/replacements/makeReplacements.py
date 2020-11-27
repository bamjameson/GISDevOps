# coding: utf-8

import argparse
import json
import os


def main():

  #source variables:
  replacementsFile = args.replacementsFile
  directory = args.directory
  environment = args.environment
  
  #load replacements file as data
  with open(replacementsFile) as f:
    data = json.load(f)


  print("")
  print(f'Making replacements for {environment} environment.')
  print("-------------------------------------------------------------")

  #Loop through environment replacements within JSON data file.
  for replacement in data[environment]:

    #Loop through all files in directory parameter.
    for subdir, dirs, files in os.walk(directory):
      for file in files:
        if file.endswith((".xml",".xaml",".json.js",".json",".rpx",".css")):
          filePath = os.path.join(subdir, file)
          inplace_change(filePath, replacement['from'], replacement['to'])


  print ("")
  print ("---------------------------")
  print ("  Replacements complete.   ")
  print ("---------------------------")


# replace string in a file.
def inplace_change(filename, old_string, new_string):
    # Safely read the input filename using 'with'
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            return

    # Safely write the changed content, if found in the file
    with open(filename, 'w') as f:
        print (f'Changing {old_string} to {new_string} in {filename}')
        s = s.replace(old_string, new_string)
        f.write(s)



def parseArguments():

  parser = argparse.ArgumentParser()
  parser.add_argument('replacementsFile', help=('File with replacement descriptors.'))
  parser.add_argument('directory', help=('Directory you want replacements done on'))
  parser.add_argument('environment', help=('The environment you want to make replacements for. (ie: DEV, TEST, PROD)'))

  # Read the command line arguments.
  return parser.parse_args()


if __name__ == '__main__':

    print(r'''
        .__       .                     ,    
        [__) _ ._ | _. _. _ ._ _  _ ._ -+- __
        |  \(/,[_)|(_](_.(/,[ | )(/,[ ) | _) 
               |                             
    ''')

    args = parseArguments()

    main()  