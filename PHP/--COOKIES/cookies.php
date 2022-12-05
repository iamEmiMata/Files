<!-- https://programadorwebvalencia.com/cursos/php/cookies/ -->
<?php 

// Crear

// setcookie('nombre', 'valor', 'caducidad');
setcookie('idioma', 'es', time() - 1);
// Caducara en 60 segundos
$caducidad = time() + 60;
setcookie('idioma', 'es', $caducidad);


// Obtener
echo $_COOKIE['idioma'];
//espanol = es


// Actualizar
setcookie('idioma', 'fr');
echo $_COOKIE['idioma'];
// frances = fr

// Borrar
unset($_COOKIE['idioma']);
setcookie('idioma', 'es', time() - 1);

?>