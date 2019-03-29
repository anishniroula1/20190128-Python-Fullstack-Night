// sock_sorter.js
const sockTypes = ['ankle', 'crew', 'calf', 'thigh']
const sockColors = ['black', 'white', 'blue']
const sockList = []
const sockCounter = {}

for (let i=0; i<100; i++) {
  // randomly select sock from socktypes
  let type = sockTypes[Math.floor(Math.random() * sockTypes.length)]
  let color = sockColors[Math.floor(Math.random() * sockColors.length)]
  let sock = [type, color]
  sockList.push(sock)

  // setting default values: equivalent to dict.get() in JS 
  sockCounter[sock] =  (sockCounter[sock] || 0) + 1

  // if (sockCounter.hasOwnProperty(sock)) { // sock exists in counter
  //   sockCounter[sock] += 1 // increase count by 1
  // } else {
  //   sockCounter[sock] = 1 // set count as 1
  // }
}

for (let sock in sockCounter) {
  console.log(`(${sock}) has ${sockCounter[sock] % 2} loner(s).`)
}

console.log(sockList)
console.log(sockCounter)