*** Settings ***
Documentation    rm testing
Library          OperatingSystem

*** Test Cases ***
Removing file
    Create File                     file
    Run                             rm file
    File Should Not Exist           file

Removing nonexistent file or directory
    ${output} =                     Run                 rm temp
    Should Be Equal                 ${output}           rm: cannot remove 'temp': No such file or directory

Forced removing nonexistent file
    ${output} =                     Run                 rm -f file
    Should Be Empty                 ${output}

Removing directory
    Create Directory                temp
    ${output} =                     Run                 rm temp
    Should Be Equal                 ${output}           rm: cannot remove 'temp': Is a directory

Recusive removing directory
    Create Directory                temp
    Run                             rm temp -r
    Directory Should Not Exist      temp

Removing empty directory with -d
    Create Directory                temp
    Run                             rm temp -d
    Directory Should Not Exist      temp

Removing not empty directory with -d
    Create File                     temp/file
    ${output} =                     Run                 rm temp -d
    Should Be Equal                 ${output}           rm: cannot remove 'temp': Directory not empty

Recursive removing directories and files
    Create File                     temp/file
    Create File                     temp/temp2/file2
    Run                             rm temp -r
    Directory Should Not Exist      temp

# can be dangerous
Refusing to remove '.' or '..'
    ${output} =                     Run                 rm -r .*
    Should Be Equal                 ${output}           rm: refusing to remove '.' or '..' directory: skipping '.'\nrm: refusing to remove '.' or '..' directory: skipping '..'
