<?php 

	echo '<h4>Arrays 2D</h4>';

	$array = [
    	[]
	];

	echo '<h5>Array vacio </h5>';
	var_dump($array);


	// 

	echo '<h5>Array Tienda </h5>';
	$tienda = [
	    123 => [
	      'nombre' => 'Camisa a cuadros',
	      'precio' => 29.95,
	      'sexo' => 'Hombre'
	    ],
	    234 => [
	      'nombre' => 'Falda manga',
	      'precio' => 19.95,
	      'sexo' => 'Mujer'
	    ],
	    345 => [
	      'nombre' => 'Bolso minúsculo',
	      'precio' => 50,
	      'sexo' => 'Mujer'
	    ]
	];

	var_dump($tienda);

	echo '<h5>Imprimiendo el nombre en el nodo 234</h5>';
	echo $tienda[234]['nombre'];

 ?>