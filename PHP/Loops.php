<?php 

	// for 
	echo '<h4>Bucle for </h4>';

	for ($i = 0; $i < 10; $i++) {
	    echo "$i \n";
	}


	echo "<br><br>";
	echo '<h4>Bucle while </h4>';

	// while

	$i = 1;
	while ($i < 10) {
	    echo $i++ . ' ';
	}

	echo "<br><br>";
	echo '<h4>Bucle do - while </h4>';
	$i = 1;
	do {
	    echo $i++ . ' ';
	} while ($i < 10);
	// 123456789


?>