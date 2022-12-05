// Dia #1
// Comentarios cortos
/* 
    Comentarios de varias
    lineas de codigo...
    Holaaa!!!
*/

// Variables 

// var x = 10; // Int
// var z = 'Hola!';  // Str
// var y = 0.16; // Float
// let m = true; // Boolean

// var a = 4;
// var b = 5;
// // Condicional simple  b > a
// if (a > b){
//     console.log('a es mayor b')
// } else {
//     console.log('b es mayor que a')
// }

/*
var : Declara una variable, opcionalmente la inicia a un valor.
let : Declara una variable local con ámbito de bloque, opcionalmente la inicia a un valor.
const : Declara un nombre de constante de solo lectura y ámbito de bloque.
*/

// let msg = '\nHello girl... go ahead learning programming languages\n'
// console.log(msg)

// const abc = 'ABC variables'
// console.log(abc)

// Funciones and operators
// function saludo(){
//     var doit = '\nThis is easy.... You can do it babe!\n'
//     console.log(doit)
// }
// saludo()

// var a = 'string'
// var b = 123
// function tipo(){
//     if (typeof(a) == String){
//        console.log('A is an string')
//     } else if (typeof(b) == String) {
//         console.log('A and B are string type of variable')
//     } else {
//         console.log('A is an String and B is an Int type of variable')
//     }
// }
// tipo()

// Calculadora
// function suma(a, b){
//     c = a + b
//     console.log('Suma ' + a + ' + ' + b + ' : ' + c)
// }

// function resta(a, b){
//     c = a - b
//     console.log('Resta ' + a + ' + ' + b + ' : ' + c)
// }

// function mult(a, b){
//     c = a * b
//     console.log('Multiplicacion ' + a + ' + ' + b + ' : ' + c)
// }

// function divs(a, b){
//     c = a / b
//     console.log('Divisicion ' + a + ' + ' + b + ' : ' + c)
// }

// function calculadora(a, b){
//     console.log('Elije una opcion\n1. suma\n2.resta\n3.multiplicacion\n4.division\n>   ');
//     opcion = 6;
//     console.log(`opcion ${opcion}`)
//     if (opcion == 1){
//         return suma(2, 2)
//     } 
//     else if (opcion == 2){
//         return resta(3, 7)
//     }
//     else if (opcion == 3){
//         return mult(8, 9)
//     }
//     else if (opcion == 4){
//         return divs(4, 2)
//     } else {
//         console.log('Esta opcion no existe!')
//     }
// }

// calculadora(a, b)

// loops

// let colors = ['red', 'green', 'blue', 'black', 'pink']

// for(let x = 1; x <= colors.length; x++){
//     console.log('\nI am falling in love with javascript!!!')
// }
// console.log('\nMa colors list ', colors)

// Buscar palabra con listas en array

// let lang = ['python', 'javascript', 'php', 'java', 'kotlin']

// for(let x = 1; x <= 1; x ++){
//     let p = 'javascript';
//     if (lang.includes(p)) {
//         console.log(`Yes, ${p} is here in the position ${lang.indexOf(p)}`)
//     } else {
//         console.log(`No, ${p} is not here!`)
//     }
// }
// console.log('Lang list has ' + lang.length + ' items ')

// Add something in an array!

// let names = new Array();
// let loops = 0
// for(let a = 1; a <= 3; a++){
//     loops = loops + 1
//     names.push('Ana', 'Emi', 'Isis', 'Olga', 'Ursula')
// }

// console.log('This loop was repeated ' + loops + ' times')
// console.log(names)

// Palabra Alreves
// function alreves(palabra){
//     let array = [];
//     for(let x = 0; x < palabra.length; x++){
//         array.push(palabra[x]);
//     }
    
//     let palabraAlreves = '';
//     while(array.length > 0){
//         palabraAlreves += array.pop();
//     }
//     return palabraAlreves;
// }
// var p = 'Money'
// console.log(`${p} : ${alreves(p)}`);

// // Arreglos 
// var miArreglo = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]

// vector1 = miArreglo[0]
// vector2 = miArreglo[1]
// vector3 = miArreglo[2]

// posicionesVector1 = miArreglo[0][1]

// console.log(`\nMi arreglo : ${miArreglo}`)
// console.log(`vector 1 : ${vector1} \nvector 2 : ${vector2} \nvector 3 : ${vector3}`)
// console.log(`Posocion 1 del vector 1 : ${posicionesVector1}`)

//  Switch

// menu = '\n1. Pizza\n2. Hamburguesa\n3. Shawarma\n'
// var producto = 'hamburguesa';
// console.log(`${menu} \nopcion :${producto}\n`);
// switch (producto) {
//     case 'pizza' :
//         console.log('Pizza : $10.55');
//         break;
//     case 'hamburguesa' :
//         console.log('Hamburguesa: $7.50');
//         break;
//     case 'shawarma' :
//         console.log('Shawarma: $8.50');
//         break;
//     default:
//         console.log('Dame una opcion correcta')
// }

// Object in js dictionary in python

// var miMascota = {
//     'nombre' : 'Mariano',
//     'edad' : 20,
//     'peso' : 200.0,
//     'especie' : 'Ave',
//     'Raza' : 'Cara sucia',
//     'color' : ['verde', 'amarillo', 'marron', 'blanco']
// };
// Normalmente esto miMascota.nombre se usa si estoy llamando a una variable que no tiene espacios
// Si tiene espacios debo usar miMascota['nombre'] para que no aparezca como no definido. que normalmente no hago.
// console.log('\nEl nombre de mi mascota es ' + miMascota.nombre + ' y tiene ' + miMascota.edad + ' años\ny tiene colores ' + miMascota.color)
// Verificar propiedades
// console.log(miMascota.hasOwnProperty('nombre'));

// Objetos Completos
// var ordenesDePizzas = [ {
//     'tipo' : 'margarita',
//     'tamano' : 'individual',
//     'precio' : 5.67,
//     'toppings' : [
//         'extra queso', 
//         'champinones',
//         'pina'
//     ],
//     'paraLlevar' : true
// } ];

// console.log('\nToppings extra : ', ordenesDePizzas[0].toppings);

// Objetos Anidados
// var miReceta = {
//     'descripcion' : 'Mi postre favorito',
//     'costo' : 15.6,
//     'ingredientes' : {
//         'masa' : {
//             'harina' : '100 grs',
//             'sal' : '1 cdta',
//             'agua' : '1 taza'
//         },
//         'cobertura' : {
//             'azucar' : '120 grs',
//             'chocolate' : '4 cdas',
//             'mantequilla' : '200 grs'
//         }
//     }
// };

// console.log('\nLlamar a ingredientes : ', miReceta.ingredientes)
// console.log('Llamar a cobertura dentro de ingredientes : ', miReceta.ingredientes.cobertura)
// console.log('Llamar a chocolate dentro de ingredientes dentro de cobertura : ', miReceta.ingredientes.cobertura.chocolate)

// Arreglos anidados

// let misPlantas = [
//     {
//         tipo : 'flores',
//         lista : ['rosas', 'tulipanes', 'dientes de leon']
//     },
//     {
//         tipo : 'arboles',
//         lista : ['abeto', 'pino', 'abedul']
//     }
// ];
// Solo puedo acceder mediante sus indices
// Desde mi punto de vista es mucho mejor usar los objetos anidados que los arreglos anidados
// console.log(`\nArray : ${misPlantas}\nTipo : ${misPlantas[0].tipo}\nLista indice [1] : ${misPlantas[0].lista[1]}`)

// Ciclo While
// let i = 1;

// while (i <= 3) {
//     console.log('Contanto desde while ', i);
//     i++;
// }

// Ciclo For
// console.log('\n')
// for(let x = 1; x <= 3; x++) {
//     console.log('Contanto desde For ', x);
// }

// Ciclo for anidado
// let miArreglo = [[1,2,3],[4,5,6],[7,8,9]];

// for(let i = 0; i < miArreglo.length; i++){
//     console.log('>>  Iteracion ', i+1);
//     let arregloAnidado = miArreglo[i]; // Arreglo
//     console.log('Arreglo : ' + arregloAnidado);

//     for(let j = 0; j < arregloAnidado.length; j++){
//         console.log('>>> Ciclo anidado');
//         console.log('Elemento : ' + arregloAnidado[j]);
//         console.log(arregloAnidado[j]); // Elemento
//     }
// }

// // Arrow Functions es la version mejorada de lambda
// console.log('\nArrow Functions')
// const concatenarArreglos = (arr1, arr2) => arr1.concat(arr2);
// console.log(concatenarArreglos([1,2],[3,4,5]));

// console.log('\nsuma de a + b + num');
// const sumar = (a, b) => {
//     let num = 6;
//     return a + b + num;
// };
// console.log(sumar(2, 3))

// console.log('\n');

// const numeros = (x, y, z) => {
//     return x + y * z;
// };
// console.log(2, 4, 6);

// // Operadores REST
// console.log('\nOperador rest');
// const suma = (...args) => {
//     return args.reduce((a, b) => a + b, 0);
// };
// console.log(suma(1,2,3, 4))

// // Operador Spread
// console.log('\nOperador Spread');
// const nume = [1, 2, 3];
// function sum(x, y, z) {
//     return x + y + z;
// }
// console.log(sum(...nume));

// // Multiplicar todo un array
// const arr = [1, 2, 3, 4];
// const reducer = (accumulator, curr) => accumulator + curr;
// console.log(arr.reduce(reducer));

// function mes() {
//     let mesNumero = [31];
//     let a = '1' ;
//     let b = mesNumero[0];
//     if(a == '1') {
//         for (let x = 1; x <= b; x++){
//             console.log(x);
//         }
//     }

// }

// mes();

console.log('hola')