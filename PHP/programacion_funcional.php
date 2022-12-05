<?php 

/*

Paradigma funcional 
Las funciones esenciales para iterar y gestionar un array son: array_walk, array_filter, array_map y array_reduce.

*/


// Diccionario
$apartamentos = [
    [
        'precio/noche' => 40,
        'ciudad' => 'Valencia',
        'wifi' => True,
        'pagina web' => 'https://hotel.com'
    ],
    [
        'precio/noche' => 87,
        'ciudad' => 'Calpe',
        'wifi' => True,
        'pagina web' => 'https://calpe.com'
    ],
    [
        'precio/noche' => 67,
        'ciudad' => 'Valencia',
        'wifi' => False,
        'pagina web' => 'https://denia.com'
    ],
    [
        'precio/noche' => 105,
        'ciudad' => 'Benidorm',
        'wifi' => False,
        'pagina web' => 'https://benidorm.com'
    ]
];

array_walk($apartamentos, function ($apartamento, $posicion) {
    echo $apartamento['ciudad'] . PHP_EOL;
});

/*
Valencia
Calpe
Valencia
Benidorm
*/


?>