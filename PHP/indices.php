<?php 

echo '<br>Indices <br> abcdef > Posicion [2]   >    ';
$palabra = 'abcdef';
echo $palabra[2];
// c
echo '<br>abcdef > Modifica Posicion [2]   >    ';
$palabra = 'abcdef';
$palabra[2] = 'Z';
echo $palabra;
// abZdef


echo '<br>Usando metodo split, Palabra : En un lugar de la mancha >   ';

$frase = 'En un lugar de la mancha';
$arrayDeFrase = preg_split('/[\s,]+/', $frase);
echo $arrayDeFrase[2] . "  <br>  ";
// "lugar"
var_dump($arrayDeFrase);


?>