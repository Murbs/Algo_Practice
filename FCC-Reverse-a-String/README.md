# FCC-Reverse-a-String
## Take an input, and reverse it.

Here is a step-by-step guide to the 'Reverse a String' bonfire, broken down and explained.

---

First, write out or use the function provided by FCC.
```javascript
function reverseString(){};
```
---

Next we add a parameter, for the string being reversed.
```javascript
function reverseString(str){};
```
---

Create a variable that will store the parameter, which we will later return.
```javascript
function reverseString(str){
  var reversed = str;
};
```
---

We can then split our string using the split method, turning our string into several substrings.
The .split method takes a separator and limit, we only need to provide a separator for this exercise.
Since we want to return the entire string regardless of white space, our separator can be defined as ' '.
```javascript
function reverseString(str){
  var reversed = str.split('');
};
```
---

Now that our string has been split, we can reverse the order with the .reverse method.
```javascript
function reverseString(str){
  var reversed = str.split('').reverse();
};
```
---

All that is left to do, is use the .join method to put our substrings back into one singular string.
```javascript
function reverseString(str){
  var reversed = str.split('').reverse().join('');
};
```
---

Return the variable you have stored, and call the function.
```javascript
function reverseString(str){
  var reversed = str.split('').reverse().join('');
  return reversed;
};

reverseString("Here I am, doing the splits");

// Returns "stilps eht gniod ,ma I ereH"
```
