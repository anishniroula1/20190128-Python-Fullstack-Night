// event-example.js

const btn = document.querySelector('#harass')
const greeting = document.querySelector('#social')
const pointer = document.querySelector('#pointer')
const message = document.querySelector('#message')
const inputField = document.querySelector('#input-field')

btn.addEventListener('click', (evt) => {
  const ssn = prompt('whats your ssn')
  greeting.innerHTML = `<h1>Greetings Human #${ssn}</h1>`
  greeting.innerHTML += 'You just got pwned'
})

btn.addEventListener('mouseover', (evt) => {
  pointer.innerHTML = `Human is touching ${evt.clientX}, ${evt.clientY}`
})

window.addEventListener('keypress', (evt) => {
  // console.log(evt)
  message.innerHTML = `Human is typing "${evt.key}"`
})

inputField.addEventListener('change', (evt) => {
  // console.log(reverseCase(evt.target.value))
  message.innerText = reverseCase(evt.target.value)
})

function reverseCase(text) {
  return text.split('')
             .map(char => (char === char.toUpperCase() 
                                 ? char.toLowerCase() 
                                 : char.toUpperCase()))
             .join('')
}