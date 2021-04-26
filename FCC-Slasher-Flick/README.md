# FCC-Slasher-Flick
## Return the remaining elements of an array after chopping off n elements from the head. The head means the beginning of the array, or the zeroth index.
```javascript
function slasher(arr, howMany) {
  // it doesn't always pay to be first
  return arr;
}

slasher([1, 2, 3], 2);
```
---

This one is pretty simple, if you know how to use the splice method. We want to remove from the beginning of our array, the amount specified
by our 'howMany' parameter. We can do this in one step.

```javascript
function slasher(arr, howMany) {
  arr.splice(0, howMany); // starting from index 0 of 'arr', remove 'howMany' (in this example, 2)
  return arr; // returns [3]
}

slasher([1, 2, 3], 2);
```
