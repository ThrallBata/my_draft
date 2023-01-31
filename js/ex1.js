"use strict";

const PI = 3.1415;

let message = "hi",
    age = 21,
    email = "groot@mail.ru";

let c = -Infinity;
let x = 'str'/2;
message = 12;

let msg3 = `str = ${age}`;//позволяет вставлять переменные в строки
let cl = "class=\"my\\class\""


let iswin = true, ischeckedField = false;
let isGreater= 4 > 1;

let id = Symbol();
let id2 = Symbol('id');
let idProcess = null;

/*console.log(id === id2)

console.log(isGreater)
console.log(idProcess)
console.log(msg3);

console.log(cl)
*/

let a = '123';
let b = Number(a);
console.log(b);
console.log(typeof b);
console.log(Boolean('2'/'2'), Boolean("" + ""));

let a1, b1 = 1;
let c1 = 3 - (a1 = b1 + 1);

console.log(a1, b1, c1);

//let age1 = prompt('Сколько вам лет?', 18);
//console.log(age1);
//alert('Hello')

//let isCar = confirm('У вас есть машина?');
//console.log(isCar);

//operazii

let a2 = '1.1', b2 = 8.7;
let arg = -a2;
console.log(arg, typeof arg);


let counter = 2, cnt = 5;
counter++; // counter = counter + 1 инкремент
cnt--; //cnt = cnt-1 декремент
console.log( counter, cnt );

let a3, b3, c3 = 10, d3 = 10;
a3 = c3++;
b3 = ++d3;

console.log(a3, b3, c3, d3)

let a4 = 5;
console.log(2**a4++, a4)

a4 /= 2
console.log(a4)

//operators

let x2 = 5;
if(x2 < 0) x2 = -x2;
console.log('|x| = ' + x2)

console.log('Ана' > 'Аяяя')

console.log(null == undefined)//true
console.log(null <= undefined)// false 0<=Nan

console.log(true === 1) // строгое сравнение сравнивается по изначальным типам данных

if(x2 < 0) console.log('x отрицательное число');
else if(x2 > 0) console.log('x положительное число');//78
else console.log('x = 0');

let x3 = -10, sgn = 0;
if(x3 < 0) {
    sgn = -1;
    console.log('x отрицательное число', sgn);
}
else if (x3 > 0) {
    sgn = 1;
    console.log('x положительное число', sgn);
}
else console.log('x = 0', sgn);

let age2 = 14;
let accessAllowed = (age2 > 18) ? 'Hi' : 'Poshel ot suda';
console.log(accessAllowed);

//x4 [2;7], x>=2 x<=7
let x4 = 4;// && - and;
if (x4 >= 2 && x4<=7) console.log('x4 попадает в промежуток [2;7]');
else console.log("Не попадает в промежуток [2;7]");

let x5 = 4;// || - or;
if (x5 < 2 || x5 > 7) console.log('x5 не попадает в промежуток [2;7]');
else console.log("х5 попадает в промежуток [2;7]");

let x6 = 4, y = -2 //
if (x6 >= 2 && x6 <= 7 && (y < 0 || y > 5))
    console.log("х6 попадает в промежуток [2;7], Y не попадает в [0; 5]");

let item = 3;
switch(item) {
    case 1: console.log('item = 1');break;
    case 2: console.log('item = 2');break;
    case 3: console.log('item = 3');break;
    case 4: console.log('item = 4');break;
    default: console.log('item другое значение');
}
/*
let S=0, i=1;
while(i <= 1000 && S < 5) {
    S += 1/i;
    ++i;
}
console.log(S)*/
let f, k = 0.5, b5 = 2;
/*for(let x7=0; x7 <= 1; x7 += 0.1) {
    f = k*x7+b5;
    console.log(f)
}*/

/*
const PSW = "password";
let psw = null;
do {
    psw = prompt('Введите пароль', "");
}
while(psw != PSW);
console.log('Вы вошли в систему!');*/

let S=0, M=10, N=5;
for(let i=1;i <= N; ++i)
    for(let j=1; j <= M; ++j)
        S += i*j;

console.log("S = ", + S);


function out_log(msg) {
    console.log(msg);
}

out_log('Вызов функции');

function showMessage(from, text) {
    V += 1
    let msg = from + " " + V + ':' + text;
    console.log(msg)
}

let V = 3;
showMessage('Python', "Top");
showMessage('Python', "Top");

function abs(x) {
    return (x < 0) ? -x : x;
}

let res = abs(-5);
console.log(res);

let showMsg = function() {
    console.log('Hello!');
};

showMsg();

function agreeCookies(question, yes, no) {
    if (confirm(question)) yes();
    else no();
}

function agreeYes() {
    console.log('Yes cookies')
}

function agreeNO() {
    console.log('No cookies')
}

//agreeCookies('Согашаетесь ли вы, что мы будем использовать куки?', agreeYes, agreeNO)

let anonym = function() {
    console.log('I am anonimus')
};
anonym();

(function() {
    console.log('I amn\'t anonimus')})();//функциональное выражение

/*setTimeout(function() {
    console.log('I amn\'t anonimus - 1 sec')}, 1000);
    */
/* let anonym = function() {
    console.log('Strelochnay func');
    }; */

let anonym_1 = () => 'Strelochnay func';// вернет без ретёрна

console.log(anonym_1());

let anonym_10 = () => {return 228+355};

console.log(anonym_10());

let anonym_2 = () => {
    let a = 228, b =355
    return a+b
};

console.log(anonym_2());

let anonym_3 = (a, b) => a+b;

console.log(anonym_3(355,355));


let book = {
    title: 'Название',
    author: 'Автор',
    nPages: 0,
    price: 0,
    "size book": {height: 100, width: 10}
};

book.isSelled = false;
book.isSelled = true;
delete book.nPages;

console.log(book.isSelled);
console.log('nPages' in book);
if(book.nPages === undefined)
    console.log('nPages не существует')

book['size book'] = {height: 10, width: 50}
console.log(book['size book'])

let keyName = 'size book';
console.log(book[keyName])

let newKey = 'color';

let car = {
    model: 'toyota',
    [newKey]: "black"
};

console.log(car[newKey]);
console.log(car.color);

let book_1 = {
    title: 'Муму',
    author: 'Тургенев',
    nPages: 228,
    price: 100
};

for(let key in book_1) {
    console.log(key+ ': ' + book_1[key]);
}

let car1 = {
    model: "toyota",
    color: "black",
    go: function(driverName) {
        console.log('Водитель ' + driverName + ': машина едет');
    },
    stop() {
        console.log('Машина остановилась');
    },
    getModel() {
        return this.model;
    }
};

car1.go('Антон');
car1.stop();
console.log(car1.getModel());

let book2 = {
    title: 'Название',
    author: 'Автор',
    nPages: 0,
    price: 0,
    size: {height: 22, width: 88}
};
let lib = {};

/*for  (let key in book2) {
    lib[key] = book2[key];
    console.log(key + ": " + lib[key]);
};*/

function cloneDeepObj(dest, obj) {
    for (let key in obj){
        if((typeof obj[key]) == 'object') {
            dest[key] = cloneDeepObj({}, obj[key]);
        }
        else {
            dest[key] = obj[key];
            //console.log(key+ ': ' + dest[key]);
        }
    }
    return dest;
};

console.log(cloneDeepObj(book2, lib));

function Book_4(title, author, price) {
    this.title = title;
    this.author = author;
    this.price = price;
}

let book5 = new Book_4('Mumu', 'Turgenev', 70);
console.log(book5)

let ar = [1, 2, 3, 4];
ar[0] = 'Груша';
console.log(ar[0]);


for (let i=0; i < ar.length; i++)
    console.log(ar[i]);

for(let value of ar)
    console.log(value);


let fruits = ['Apple', 'Sliva'];
fruits.push('Grusha');
console.log(fruits.pop());
console.log(fruits);

let delElem = fruits.shift();
fruits.unshift('Grusha');
console.log(fruits);

let matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
matrix[1][1] = 0;
console.log(matrix);

for(let row of matrix) {
    let cols = '';
    for( let val of row)
        cols += val + ' ';

    console.log(cols);
};

let ar_1 = ['I', 'go', 'to', 'very', 'big', 'dacha']

let delBig = ar_1.splice(3, 2);
console.log(ar_1)//['I', 'go', 'to', 'dacha']
console.log(delBig)//['very', 'big']

ar_1.splice(3, 1, 'rich','hotel');//['I', 'go', 'to', 'rich', 'hotel']
console.log(ar_1)

ar_1.splice(2, 0, 'very')
console.log(ar_1)//['I', 'go', 'very', 'to', 'rich', 'hotel']

console.log(ar_1.slice(4,6))//'rich', 'hotel'

let ar_1_copy = ar_1.slice()
console.log(ar_1_copy)

let ar_1_x2 = ar_1_copy.concat(ar_1)
console.log(ar_1_x2)

//перебор элементов массива
let ar_2 = ['I', 'go', 'to', 'very', 'big', 'dacha']
/*ar_2.forEach(function(item){
    console.log(item);
});*/

ar_2.forEach((item) => console.log(item));

let dig = [17, 2, 13, 4, 55, 16, 7, 98, 9];

dig.forEach((item, index) => {
    if(item % 2 == 1) console.log(`${item} с индексом ${index}`)
});

let res1 = ar_2.indexOf('big', 0);
console.log(res1)

console.log(dig.sort( (a,b) => a-b ));

let res2 = dig.filter(item => dig[item] <= 19);
console.log(res2)

console.log(dig.reverse());

let word = ar_2.join(' ')
console.log(word)

console.log(word.split(' '))

let sum = dig.reduce((sum, current) => sum+current, 0);
console.log(sum);

//система счисления

let num = 255;
console.log( num.toString(16));
console.log( num.toString(2));
console.log( 228..toString(16));

let dik = 1.5;
let rez = Math.floor(dik);
console.log( rez );
console.log( Math.ceil(dik) );
console.log( Math.round(1.4) );
console.log( Math.round(1.5) );

let dic = 1.23756;
let reb = Math.round(dic*100)/100;
console.log(reb)

let reb1 = dic.toFixed(3)
console.log(reb1)

/*let num1 = prompt('Enter a number', '');
if(num1.length > 0 && isFinite(num1) ) console.log('Molodec number')
else console.log('Emelay no number');*/

let arg1 = '12pt';
console.log(parseInt(arg1))

let arg2 = '12.4 pt';
console.log(parseFloat(arg2))

for(let i=0; i<10;++i)
    console.log(Math.random() );

console.log(Math.max(10, 5))

console.log(Math.pow(10, 5))

let str1 = 'hi heLlo bItcH';

for(let ch of 'helelo')
    console.log(ch)

console.log(str1.toUpperCase());
console.log(str1.toLowerCase());
console.log(str1.indexOf('bItcH'));

let str_22 = '    ssgg s sgs wege eg e    1           ';
console.log(str_22.trim());

let str_5 = 'Hi';
console.log(str_5.repeat(25));


let guests = new Set();

let alex = {name: 'Alexey', old:22};
let aleg = {name: 'Aleg', old:27};
let olga = {name: 'olga', old:21};

guests.add(alex);
guests.add(aleg);
guests.add(alex);
guests.add(olga);

for (let guest of guests) {
    console.log(guest.name);
}

let cars = ["yaguar", 'porshe', 'mersedes'];

let [car11, car22, car33] = cars;
console.log(car11, car22, car33)


let book_228 = {
    title: 'Муму',
    author: 'Тургенев',
    nPages: 228,
    price: 100
};

let {title, author: a24, price: p=0} = book_228;
console.log(title, a24, p);


let items = [1,5,7,9,2,10000];
let diggs = [228355,58,-4634,-596];
console.log(Math.max(...items, 100, 54454, ...diggs))

//Hi notebook
let grind = [ 1,4,5];

function showMessage1(msg) {
    console.log(msg);
}

console.log( showMessage1.name)

console.log( showMessage1.length)

function func1(a, b, r) {
    console.log(a, b, r);
}

console.log( func1.length);

function funcCount() {
    console.log("вызов функции: " + ++funcCount.counter);
}

funcCount.counter = 0;

funcCount();
funcCount();


function createCounter() {
    function counter() {
        return counter.count++;
    }

    counter.count = 0;
    return counter;
}

let counter1 = createCounter();
console.log( counter1());
console.log( counter1());
console.log( counter1());

let myMath = {
    nameObj: "myMath",

    sum(...args) {
        return this.nameObj+': '+args.reduce((val, prevVal) => prevVal += val, 0);
    }
};

let sum1 = myMath.sum;
console.log( sum1.apply(myMath, [1,7,8,9,6]) );

let sum2 = myMath.sum.bind(myMath, 100);
console.log( sum2(1,7,8,9,6));


let getName = function Name(name) {
    if(name) return name;
    else return Name("no name");
};

console.log( getName("Ivan") );

let get = getName;
getName = null;
console.log( get() );


let sumTwo = new Function('a', 'b', 'return a+b;');
console.log( sumTwo(1, 5));


setTimeout(funcCount, 2000); 


