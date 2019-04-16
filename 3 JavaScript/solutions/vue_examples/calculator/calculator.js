// calculator.js
// vuejs implementation of old school calculator

let app = new Vue({
  el: '#calc-body',
  data: {
    display: 0,
    total: 0,
    operator: null,
    currentValue: '',
    historyDisplay: '',
    history: [],
    decimal: false,
  },
  mounted: function() {
    document.addEventListener('keydown', this.handleKeydown)
  },
  methods: {
    updateDisplay: function(value) {
      const number = parseFloat(value)
      this.display = (isNaN(number) ? '' : number)
      this.historyDisplay = this.history.join('')
    },
    addDigit: function(digit) {
      this.currentValue += digit
      this.updateDisplay(this.currentValue)
    },
    addDecimal: function() {
      if (!this.decimal) {
        this.currentValue += '.'
        this.decimal = true
        this.updateDisplay(this.currentValue)
      }
    },
    operation: function(operator) {
      if (this.operator) {
        this.calculate()
      } else {
        this.total = (this.currentValue ? this.currentValue : 0)
        this.history.push(this.total)
      }
      this.operator = {
        '+': '+',
        '-': '-',
        '×': '*',
        '*': '*',
        '÷': '/',
        '/': '/',
      }[operator]
      this.currentValue = ''
      this.decimal = false
      this.history.push(operator)
      this.updateDisplay(this.currentValue)
    },
    calculate: function() {
      if (this.currentValue) {
        this.history.push(this.currentValue)
        let left = parseFloat(this.total)
        let right = parseFloat(this.currentValue)

        if (this.operator === '+') {
          this.total = left + right
        } else if (this.operator === '-') {
          this.total = left - right
        } else if (this.operator === '*') {
          this.total = left * right
        } else if (this.operator === '/') {
          this.total = left / right
        } else {
          return
        }
      }        
      this.currentValue = ''
      this.decimal = false
      this.updateDisplay(this.total)
    },
    clearEntry: function() {
      this.decimal = false
      this.currentValue = ''
      this.updateDisplay(this.currentValue)
    },
    clearAll: function() {
      this.total = 0
      this.currentValue = ''
      this.history = []
      this.operator = null
      this.decimal = false
      this.updateDisplay(this.total)
    },
    handleDigitClick: function(evt) {
      this.addDigit(evt.target.innerText)
    },
    handleOpClick: function(evt) {
      this.operation(evt.target.innerText)
    },
    handleKeydown: function(evt) {
      console.log(evt)
      if (!isNaN(evt.key)) { // key is digit
        this.addDigit(evt.key)
      } else if ('+-/*'.includes(evt.key)) { // key is operator
        this.operation(evt.key)
      } else if (evt.key === '.') { // key is decimal
        this.addDecimal()
      } else if (evt.key === "Enter" || evt.key === '=') { // key is equal
        this.calculate()
      } else if (evt.key === "Backspace") {
        this.clearEntry()
      }      
    }
  }
})