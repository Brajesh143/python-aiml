// Q1. Counter using closure

// function createCounter() {
//     let count = 0;

//     function inner() {
//         return count += 1;
//     }

//     return inner; 
// }

// const counter = createCounter();
// console.log(counter());
// console.log(counter());
// console.log(counter());

// function outer() {
//     let x = 10;

//     function inner() {
//         console.log(x);
//     }

//     return inner;
// }

// const fn = outer();

// fn();

// function test() {
//     for (var i = 0; i < 3; i++) {
//         setTimeout(() => console.log(i), 0);
//     }
// }

// test();

// function test() {
//     for(let i=0; i<3; i++) {
//         setTimeout(() => console.log(i), 0);
//     }
// }

// test();

// let x = 10;

// function outer() {
//     let x = 20;

//     return function inner() {
//         console.log(x);
//     };
// }

// const fn = outer();

// fn();


// function privateBank(initialBalance) {
//     let balance = initialBalance;

//     function deposite(amount) {
//         return balance += amount;
//     }

//     function withdraw(amount) {
//         return 
//     }
// }


