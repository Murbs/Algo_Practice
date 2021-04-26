# FCC-Return-Largest-Number-in-Array
## Finding the largest number in an array
---

Return an array consisting of the largest number from each provided sub-array. For simplicity, the provided array will contain exactly 4 sub-arrays.
Remember, you can iterate through an array with a simple for loop, and access each member with array syntax arr[i].
```javascript
function largestOfFour(arr){}

largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
```

---

First, create an empty array that will be used to store the largest numbers we are trying to find.
```javascript
function largestOfFour(arr){
  var result = []; // Store the largest values of each array here
}
  
largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
```

---

Next, use a for loop that will cycle through each index of the top-layer array.
```javascript
function largestOfFour(arr){
  var result = []; 
  for (var i = 0; i < arr.length; i++){} // For loop to cycle through top-layer array
}
  
largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
```

---

Create another variable inside our loop, this will stay outside of our next loop so that a value is only over-written by a larger value within each array.
```javascript
function largestOfFour(arr){
  var result = []; 
  for (var i = 0; i < arr.length; i++){
    var largest = 0; // Variable for storing largest values of each inner array
  }
}
  
largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
```

---

We need to make a second loop, this will cycle the inner arrays.
```javascript
function largestOfFour(arr){
  var result = []; 
  for (var i = 0; i < arr.length; i++){
    var largest = 0;
    for (var n = 0; n < arr[i].length; n++){} // 2nd loop for cycling inner arrays
  }
}
  
largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
```

---

Inside the 2nd loop, an if statement can be used to check an index against our variable 'largest', and replace the value if it's larger. 
```javascript
function largestOfFour(arr){
  var result = []; 
  for (var i = 0; i < arr.length; i++){
    var largest = 0;
    for (var n = 0; n < arr[i].length; n++){
      if (arr[i][n] > largest) {
        largest = arr[i][n]; // if value of current index is greater than current value of 'largest', set largest to that value
      }
    } 
  }
}
  
largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
```

---

Now that we have the largest values of each inner array, we can store those results in our 'result' variable. Return 'result', and when you call your function the largest numbers of each array will be displayed! 
```javascript
function largestOfFour(arr){
  var result = []; 
  for (var i = 0; i < arr.length; i++){
    var largest = 0;
    for (var n = 0; n < arr[i].length; n++){
      if (arr[i][n] > largest) {
        largest = arr[i][n];
      }
    } 
    result[i] = largest; // stores the array of largest numbers in 'result' variable
  }
  return result; // returns [5, 27, 39, 1001]
}
  
largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]]);
```
