<?php 

echo '<h4>Condicionales</h4>';

echo "Inicio \n";
if (2 > 0) {
    echo "Entro en el condicional \n";
}
echo 'Fin <br>';
// Inicio
// Entro en el condicional
// Fin

if (10 > 2 && True && 'HBO' != 'Netflix') {
    echo 'a cambiado <br>';
}


if ('Ghibli' == 'Ghibli') {
    echo 'Bienvenido';
} else {
    echo 'No eres bien recibido';
}

?>

<html>
    <body>
    <?php if (1 > 2): ?>
    <br>// Código que sea cierto
    <?php elseif (2 > 3): ?>
    <br>// Código que se ejecutará si no es cierto.
    <?php else: ?>
    <br>// Código que se ejecutará si no es cierto.
    <?php endif; ?>
    </body>
</html>

<?php echo (5 > 10) ? '<br>Es verdad' : '<br>Es mentira'; ?>
