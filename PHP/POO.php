<!-- https://programadorwebvalencia.com/cursos/php/objetos/ -->


<?php 


/*Visibilidad
Una de las características más importantes de los objetos es la visibilidad, o los permisos que puede tener las variables o funciones. Similar a dar privilegios de acceso.

Las posibilidades son:

public: cualquier puede usarlo.
private: solo es accesible desde el propio objeto.
protected: solo es accesible desde el propio objeto o herederos.*/


class Gato {
	// Variable publica
	public $nombre = 'kitty';

	public function saluda(): void {
		echo 'Miauu!';
	}
	public function comidafavorita(): void {
		echo 'el atun';
	}
	public function hobbie(): void {
		echo 'trepar las cortinas';
	}

}

// se instancia el objeto Gato
$miGato = new Gato('Kitty');
echo "Mi gato se llama " . $miGato->nombre;
echo "<br>(='-'=) "; echo $miGato->saluda();

echo '<br>A '; echo $miGato->nombre; 
echo ' le gusta '; echo $miGato->comidafavorita();
echo " y "; echo $miGato->hobbie();
?>