<?php 

echo "<h4>Diccionario</h4>";

$empleados = [
    'Juan' => 34,
    'Luisa' => 56
];

var_dump($empleados);
echo '<br> Luisa > ', $empleados['Luisa'];


// anadir nuevo item al diccionario
echo "<h4> Add nuevo </h4>";
$empleados['Manolo'] = 99;
var_dump($empleados);


echo "<h4> Modificar </h4>";
$empleados['Manolo'] = 11;
var_dump($empleados);


echo "<h4> Eliminar </h4>";
unset($empleados['Manolo']);
var_dump($empleados);
 ?>