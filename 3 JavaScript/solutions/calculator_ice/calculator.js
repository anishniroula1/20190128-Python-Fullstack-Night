// calculator.js
const displayDiv = document.querySelector('#display')
const acDiv = document.querySelector('#AC')
const ceDiv = document.querySelector('#CE')
const multDiv = document.querySelector('#mult')
const divideDiv = document.querySelector('#divide')
const addDiv = document.querySelector('#add')
const subDiv = document.querySelector('#sub')
const eqDiv = document.querySelector('#eq')
const decDiv = document.querySelector('#dec')
const oneDiv = document.querySelector('#one')
const twoDiv = document.querySelector('#two')
const threeDiv = document.querySelector('#three')
const fourDiv = document.querySelector('#four')
const fiveDiv = document.querySelector('#five')
const sixDiv = document.querySelector('#six')
const sevenDiv = document.querySelector('#seven')
const eightDiv = document.querySelector('#eight')
const nineDiv = document.querySelector('#nine')
const zeroDiv = document.querySelector('#zero')

const add = (a, b) => a + b
const subtract = (a, b) => a - b
const multiply = (a, b) => a * b
const divide = (a, b) => a / b
const updateDisplay = (value) => {
  displayDiv.innerText = value
}

let running_total = 0
let current_value = 0
updateDisplay(running_total)

acDiv.addEventListener('click', (evt) => {
  console.log(evt)
})