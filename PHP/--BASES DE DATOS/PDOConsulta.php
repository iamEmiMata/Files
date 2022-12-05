<?php 


// Variables
$hostDB = '127.0.0.1';
$nombreDB = 'library';
$usuarioDB = 'root';
$contrasenyaDB = '';

// Conecta con base de datos
$hostPDO = "mysql:host=$hostDB;dbname=$nombreDB;";
$miPDO = new PDO($hostPDO, $usuarioDB, $contrasenyaDB);

// Prepara SELECT
$miConsulta = $miPDO->prepare('SELECT * FROM stock;');

// Ejecuta consulta
$miConsulta->execute();

// Imprimo
echo '<b>Columna Name</b> - <b>Columna Author</b> - <b>Columna Year</b> <br>';
$resultados = $miConsulta->fetchAll();
foreach ($resultados as $posicion => $columna) {
    echo $columna['name'] . ' - ' . $columna['author'] . ' - ' . $columna['year'] . '<br>';
}


?>