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


// function createAccount(initialBalance) {
//     let balance = initialBalance;

//     return {
//         deposit(amount) {
//             balance += amount;
//         },

//         withdraw(amount) {
//             if (amount <= balance) {
//                 balance -= amount;
//             } else {
//                 console.log("Insufficient balance");
//             }
//         },

//         getBalance() {
//             return balance;
//         }
//     };
// }

// const account = createAccount(1000);

// account.deposit(500);
// account.withdraw(200);

// console.log(account.getBalance()); // 1300

// console.log(account.balance); // undefined

function checkBalance(initialAmount) {
    let balance = initialAmount;

    function deposite(amount) {
        if (amount <= 0) {
            console.log("Please enter a valid amount")
            return;
        }
        balance += amount; 
    }

    function widhdraw(amount) {
        if (amount > balance) {
            console.log("Insufficient balance")
            return;
        } else if (amount <= 0) {
            console.log("Enter a valid amount")
            return;
        }
        balance -= amount;
    }

    function getBalance() {
        return balance;
    }

    return {
        deposite,
        widhdraw,
        getBalance
    }
}

const checkBankBalance = checkBalance(1000)

checkBankBalance.deposite(500);
checkBankBalance.widhdraw(2000)
console.log(checkBankBalance.getBalance())


function createMultiplier(multiplier) {
    return function (number) {
        return number * multiplier;
    };
}

const multiplyBy2 = createMultiplier(2);
const multiplyBy5 = createMultiplier(5);

console.log(multiplyBy2(10)); // 20
console.log(multiplyBy5(10)); // 50


function memoize(fn) {
    const cache = {};

    return function (...args) {
        const key = JSON.stringify(args);

        if (key in cache) {
            console.log("Using cached result");
            return cache[key];
        }

        console.log("Calculating result");

        const result = fn(...args);

        cache[key] = result;

        return result;
    };
}


const memoizedAdd = memoize((a, b) => a + b);

console.log(memoizedAdd(2, 3));
// Calculating result
// 5

console.log(memoizedAdd(2, 3));
// Using cached result
// 5

console.log(memoizedAdd(5, 10));
// Calculating result
// 15

// function AuthMiddleware(req, res, next) {
//     // Authentication logic here
//     let isAuth = false;

//     if (req.headers.authorization === "Bearer token") {
        
//         token = req.headers.authorization.split(" ")[1];

//     }

//     next();
// }

const authMiddleware = (req, res, next) => {
    const authHeader = req.headers['authorization'];
    const token = authHeader && authHeader.split(' ')[1]; // Bearer TOKEN

    if (token == null) {
        return res.status(401).json({ message: 'No token provided' });
    }
    
    jwt.verify(token, 'somesupersecretsecret', (err, user) => {
        if (err) {
            if (err.name === 'TokenExpiredError') {
                return res.status(401).json({ message: 'Token expired' });
            }
            return res.status(403).json({ message: 'Invalid token' });
        }

        // Attach user info to the request object
        req.userId = user.userId;
        next(); // Proceed to the next middleware or route handler
    });

    next();
};
