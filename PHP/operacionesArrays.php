<!-- operaciones array -->
<?php 
echo "<br><br><h3>Array sin modificar<br></h3>";
//  Add new item in to array
$planetas[] = 'Marte';
$planetas[] = 'Tierra';
$planetas[] = 'Venus';
var_dump($planetas);
echo "<br><br><h3> >> Add new <br></h3>";
// Array de partida
$planetas = ['Marte', 'Tierra', 'Venus'];

// Añadimos 'Mercurio'
$nuevosPlanetas = array_merge($planetas, ['Mercurio']);

// Vemos el resultado
var_dump($nuevosPlanetas);


echo "<br><br><h3> >> Modify : Cambio la posicion [2] de Venus a Saturno <br></h3>";

$nuevosPlanetas[2] = 'Saturno';
var_dump($nuevosPlanetas);

echo "<br><br><h3> >> Delete : Elimino la posicion [1] : Tierra <br></h3>";

unset($nuevosPlanetas[1]);
var_dump($nuevosPlanetas);

echo "<br><br><h3> >> Add new : Tierra <br></h3>";
// Añado a la tierra otra vez
$nuevosPlanetas[] = 'Tierra';
// Muestro todo
var_dump($nuevosPlanetas);

 ?>