# FCC-Repeat-a-String
## Repeat a given string (first argument) num times (second argument). Return an empty string if num is not a positive number.
---

To solve this I used a simple if statement, and the .repeat method.
```javascript
function repeatStringNumTimes(str, num) {
  // repeat after me
  return str;
}

repeatStringNumTimes("abc", 3);
```
---

Using an if statement, we check if a value is > 0, if so, use the .repeat method multiplied by our num parameter and return the output.
```javascript
function repeatStringNumTimes(str, num) {
  
  if (num > 0) { // if parameter is > 0, do this thing
    return str.repeat(num); // returns 'str' parameter multiplied 'num' amount of times
  }
}

repeatStringNumTimes("abc", 3);
```

---

Add an else statement that returns an empty string if the value isn't positive, call the function and we're done!
```javascript
function repeatStringNumTimes(str, num) {
  
  if (num > 0) { 
    return str.repeat(num); 
  }
  else {
    return ""; // return an empty string when if condition isn't met
  }
}

repeatStringNumTimes("abc", 3); // returns abcabcbac
```

