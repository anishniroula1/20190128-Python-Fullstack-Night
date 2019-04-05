// calculator.js

// DOM selectors 
const displayDiv = document.querySelector('#display')
const historyDiv = document.querySelector('#history')
const acDiv = document.querySelector('#AC')
const ceDiv = document.querySelector('#CE')
const eqDiv = document.querySelector('#eq')
const decDiv = document.querySelector('#dec')
const digits = document.querySelectorAll('.num')
const ops = document.querySelectorAll('.op')

// variables
let runningTotal = 0
let currentValue = ''
let decimal = false
let negative = false
let operator = null
let history = []

// functions
const add = (a, b) => a + b
const subtract = (a, b) => a - b
const multiply = (a, b) => a * b
const divide = (a, b) => a / b

const updateDisplay = (value) => {
  displayDiv.innerText = value
  historyDiv.innerText = history.join('')
}

// py: input in list
// js: arr.includes(input)

const calculate = () => {
  if (currentValue) {
    history.push(currentValue)
    let a = parseFloat(runningTotal)
    let b = parseFloat(currentValue)
    if (operator === '+') {
      runningTotal = add(a, b)
    } else if (operator === '-') {
      runningTotal = subtract(a, b)
    } else if (operator === '×' || operator === '*') {
      runningTotal = multiply(a, b)
    } else if (operator === '÷' || operator === '/') {
      runningTotal = divide(a, b)
    }  
    currentValue = ''
  }
  updateDisplay(runningTotal)  
}

const addDigit = (digit) => {
    currentValue += digit
    updateDisplay(currentValue)  
}

const addDecimal = () => {
  if (!decimal) {
    currentValue += '.'
    updateDisplay(currentValue)
    decimal = true  
  }  
}

const addOp = (op) => {
    if (operator === null) { 
      runningTotal = (currentValue ? currentValue : 0)
      history.push(runningTotal)
    } else {
      calculate()
    }
    operator = op
    history.push(op)
    currentValue = ''
    decimal = false
    updateDisplay(operator)
}

const clearEntry = () => {
  currentValue = ''
  decimal = false
  updateDisplay(runningTotal)  
}

// display 0 at first
updateDisplay(runningTotal)

// calculator button event listeners
acDiv.addEventListener('click', () => {
  runningTotal = 0
  currentValue = ''
  operator = null
  decimal = false
  history = []
  updateDisplay(runningTotal)
})

ceDiv.addEventListener('click', () => {
  clearEntry()
})

digits.forEach(elem => {
  let digit = elem.innerText
  elem.addEventListener('click', () => {
    addDigit(digit)
  })
})

decDiv.addEventListener('click', () => {
  addDecimal()
})

ops.forEach(elem => {
  let op = elem.innerText
  elem.addEventListener('click', () => {
    addOp(op)
  })
})

eqDiv.addEventListener('click', () => {
  calculate()
})

// keypress event listener
document.addEventListener('keydown', (evt) => {
  if (!isNaN(evt.key)) { // key is digit
    addDigit(evt.key)
  } else if ('+-/*'.includes(evt.key)) { // key is operator
    addOp(evt.key)
  } else if (evt.key === '.') { // key is decimal
    addDecimal()
  } else if (evt.key === "Enter" || evt.key === '=') { // key is equal
    calculate()
  } else if (evt.key === "Backspace") {
    clearEntry()
  }
})