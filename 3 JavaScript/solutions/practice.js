// practice.js

// // List 6
// Write a function to move all the elements of a list with value less than 10 to a new list and return it.
// Hint: This is a *filter* problem.

// // Using Array.filter()
// Arrow functions
const extract_less_than_ten = (nums) => nums.filter(x => x<10)

// // Equivalent to above

// const extract_less_than_ten = (nums) => {
//     return nums.filter(x => x<10)
// }

// // Anon function
// const extract_less_than_ten = function(nums) {
//     return nums.filter(x => x<10)
// }

// // Named function
// function extract_less_than_ten(nums) {
//     return nums.filter(x => x<10)
// }


// // Using loops
// looping over indices
function extract_less_than_ten_using_loop(nums) {
    let less_than_ten = []
    for (let i=0; i<nums.length; i++) {
        if (nums[i] < 10) {
            less_than_ten.push(nums[i])
        }
    }
    return less_than_ten
}

// looping directly over elements (like Python's for..in syntax)
function extract_less_than_ten_using_loop(nums) {
    let less_than_ten = []
    for (let num of nums) {
        if (num < 10) {
            less_than_ten.push(num)
        }
    }
    return less_than_ten
}

extract_less_than_ten_named_function([1,3,5,7,11,13,15]) // [1, 3, 5, 7, 9]