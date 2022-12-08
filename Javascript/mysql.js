// crea el punto de conexion mediante node
const mysql = require('mysql')
// objeto para la conexion
const conexion = mysql.createConnection({
    host : 'localhost',
    user : 'root',
    password : '',
    database : 'library'
})

//  Valida que la conexion este activa y si no muestrame el error
conexion.connect((err) => {
    if(err) throw err
    console.log('DB Connection Activated')
})

// insert
// const insertar = "INSERT INTO stock (id, name, author, year) VALUES (1, 'Viaje al fin de la noche', 'Louis-Ferdinand Céline', 1932)"
// conexion.query(insertar, (err, rows) => {
//     if(err) throw err
// })

// consulta
const seleccion = 'select * from stock'
conexion.query(seleccion, (err, rows) => {
    if(err) throw err
    console.log('Datos : \n')
    console.log(rows) // muestra todas las labras
    console.log('cantidad de datos en la tabla : ',rows.length) //muestra la cantidad de datos
    console.log(rows[0]) // muestra tabla especifica
    console.log(rows[0].name) //muestra dato especifico
})


// Si no hay errores, cierra la conexion
conexion.end()
//  para correr el archivo ir a la carpeta en donde se ubica y consola node .\archivo.js



// Conexion con base de datos
const mysql = require('mysql')
const connection = mysql.createConnection({
    host : 'localhost',
    user : 'root',
    password : '',
    database : 'library'
})

// validamos si esta activa la connexion
connection.connect( (err) => {
    if(err) throw err
    console.log('Conexion activa!')
})

// Insert into Row
// const insert = "INSERT INTO stock(name, author, year) VALUES ('Orgullo y prejuicio', 'Jane Austen', 1813)"
// connection.query(insert, (err, rows) => {
//     if(err) throw err
// })

// Edit Row
// const edit = "UPDATE stock SET name = 'Viaje al fin de la noche', author = 'Louis-Ferdinand Céline', year = '1932' WHERE id = '1' "
// connection.query(edit, (err, rows) => {
//     if(err) throw err
// })

// Delete Row
// const deleted = "DELETE FROM stock WHERE id = '3'"
// connection.query(deleted, (err, rows) => {
//     if(err) throw err
// })

// Show Table
const select = 'select * from stock'
connection.query(select, (err, rows) => {
    if(err) throw err
    console.log('Datos : \n')
    console.log(rows)
})

connection.end()