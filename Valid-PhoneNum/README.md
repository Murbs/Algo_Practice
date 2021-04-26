# Valid-PhoneNum

Leetcode exercise to write a shell script that parses a text document for specific phone number formatting.

### Example:

#### *Assume that file.txt has the following content:* 

```
987-123-4567
123 456 7890
(123) 456-7890

Valid formats are (xxx) xxx-xxxx / xxx-xxx-xxxx
```

Given the examples provided, we only want to see line 1 and 3. Using some RegEx and the 'Select-String' function we can apply some pattern matching.

```Powershell
Select-String -Path '..\file.txt' -Pattern '\(\d\d\d\) \d\d\d-\d\d\d\d|\d\d\d-\d\d\d-\d\d\d\d'

# Returns:

# ..\Path\file.txt:1:987-123-4567
# ..\Path\file.txt:2:(123) 456-7890
```
