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


// Strings 1
//  returns string of each letter in text doubled

// >>> double_letters('hello')
// 'hheelllloo'

// using loops
function double_letters_using_loops(text){
    let double_string = ''
    for (let i=0; i<text.length; i++) {
        double_string += text[i] + text[i]
    }
    return double_string
}

// equivalent to above
function double_letters_using_loops(text){
    let double_string = ''
    for (let letter of text) {
        double_string += letter + letter
    }
    return double_string
}

// using map
const double_letters_using_map = (text) => (text.split('')
                                                .map(letter => letter + letter)
                                                .join(''))


// List 6 common elements
// using filter
const common_elements = (arr1, arr2) => arr1.filter(x => arr2.includes(x))

// equivalent to above
function common_elements(arr1, arr2) {
    return arr1.filter(x => arr2.includes(x))
}

// using sets
const common_elements_using_sets = (arr1, arr2) => {
    const setA = new Set(arr1)
    const setB = new Set(arr2)
    const intersection = [...setA].filter(elem => setB.has(elem))
    return intersection
}

// Fundamentals 4
// Write a function that returns the maximum of 3 parameters.
// (Hint: use Array.reduce() )
// function maximum_of_three(a, b, c) {...}
//     ...
// maximum_of_three(5,6,2) → 6
// maximum_of_three(-4,3,10) → 10

let max_of_three = (a, b, c) => [a, b, c].reduce((acc, cur) => (acc > cur ? acc : cur))
max_of_three = (a, b, c) => Math.max(a, b, c)
max_of_three = (a, b, c) => {
    let running_max = -Infinity
    for (let num of [a, b, c]) {
        if (num > running_max) running_max = num
    }
    return running_max
}


// Lists 12
// Write a function that takes n as a parameter, and returns a list containing the first n Fibonacci Numbers.

// fibonacciList(8) → [0, 1, 1, 2, 3, 5, 8, 13, 21]
const fibonacci = (n) => (n <= 1 ? n : fibonacci(n-1) + fibonacci(n-2))
const fibonacciList = (n) => [...Array(n+1).keys()].map(i => fibonacci(i))

// // equivalent to above
// const fibonacciList = function(n) {
//     let fibList = []
//     for (let i=0; i<=n; i++) {
//         fibList.push(fibonacci(i))
//     }
//     return fibList
// }

// optimized fibonacci (w memoization)
const fib_cache = [0, 1]
const optimized_fibonacci = (n) => {
    if (n < fib_cache.length) { // we've computed fib(n) before
        return fib_cache[n]
    } else { // recursively compute fib(n)
        fibn = optimized_fibonacci(n-1) + optimized_fibonacci(n-2)
        fib_cache.push(fibn)
        return fibn
    }   
}

const optimized_fiblist = (n) => {
    optimized_fibonacci(n)
    return fib_cache.filter((elem, key) => key <= n)
}
