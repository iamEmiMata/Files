<?php 

// Variables
$hostDB = 'library.sqlite';
// Conecta con base de datos
$hostPDO = "sqlite:$hostDB";
$miPDO = new PDO($hostPDO);

// Prepara SELECT
$miConsulta = $miPDO->prepare('SELECT * FROM stock;');
// Ejecuta
$miConsulta->execute();

// Volvemos a la tabla
// Imprimo
$resultados = $miConsulta->fetchAll();
foreach ($resultados as $posicion => $columna) {
    echo $columna['name'];
}

?>