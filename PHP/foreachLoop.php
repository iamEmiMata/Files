<!-- https://programadorwebvalencia.com/cursos/php/arrays/ -->

/*

Dentro de PHP existen 4 tipos de bucles:
foreach, for, while and do-while

*/


<html>
    <body>
    	<h2>Loops</h2>
    	<h2>Foreach > Es la forma más sencilla de iterar un array.</h2>
        <h3>¿Cuantos años tienes?</h3>
        <select>
            <?php foreach (range(1, 10) as $num): ?>
            <option value="<?php echo $num; ?>"><?php echo $num . ' años'; ?></option>
            <?php endforeach; ?>
        </select>

        <?php 

        	echo '<h4>Array Animales Fantasticos : </h4>';

        	$animalesFantasticos = ['fénix', 'dragón', 'grifo', 'pegaso', 'cerbero'];
			foreach ($animalesFantasticos as $animal) {
			    echo '> ' . $animal . ' ';
			} 
			// fénix dragón grifo pegaso cerbero


			echo '<h4>Array Animales Fantasticos con index : </h4>';
			// En caso de que necesitemos la key, existe otra forma para utilizarlo.
			$animalesFantasticos = ['fénix', 'dragón', 'grifo', 'pegaso', 'cerbero'];
			foreach ($animalesFantasticos as $posicion => $animal) {
			    echo '<br>' . "El animal $animal ocupa la posición $posicion \n";
			}
			// El animal fénix ocupa la posición 0 
			// El animal dragón ocupa la posición 1 
			// El animal grifo ocupa la posición 2 
			// El animal pegaso ocupa la posición 3 
			// El animal cerbero ocupa la posición 4 

        ?>

        <?php 
        echo '<h4>Array 2 dimensiones : </h4>';
        $zara = [
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


			echo '<h4>Recorriendo Array Simple: </h4>';
			foreach ($zara as $producto) {
				    var_dump($producto);
				}

			echo '<h4>Recorriendo Array 2D: </h4>';
			foreach ($zara as $producto) {
			    foreach ($producto as $elemento) {
			        echo "$elemento \n";
			    }
			}
			


			?>


    </body>
</html>


