// console.log("Hello World")

// JavaScript
// let name_first = "Barra"
// for (let i = 0; i <= 5; i=i+2) {
//     console.log(name_first);
// }

// let newArray = [1, 3, 5, 8]
// (...) means it will not give the first value. It will take the whole array
// console.log(Math.max(...newArray))


// Python
// for i in range(0,5, 1):
//     print(name_first)

// Problem 1: "FizzBuzz"
// for (let i = 1; i <= 100; i++){
//     if(i % 3 == 0) 
//         console.log("Fizz");
//     else if(i % 5 == 0) 
//         console.log("Buzz");
//     else(console.log(i));
// }

// Problem 2: Fibonnaci Sequence
// First Print out the first 20 numbers in the Fibonnaci Sequence
const number = parseInt(prompt("Enter a number: "));
let n1 = 0, n2 = 1, nextFibonnaciNumber;

console.log("Fibonacci Series with the first 20 numbers:");

for (let i = 1; i <= number; i++) {
    console.log(n1);
    nextFibonnaciNumber = n1 + n2;
    n1 = n2;
    n2 = nextFibonnaciNumber;
}