<?php 

function saludar_ahora(): string
{
    return 'Hola, soy una función';
}
echo saludar_ahora();



// function saludar(string $nombre = 'Anónimo'): string
// {
//     return '<br>Hola, ' . $nombre .'. Por lo que veo tu nombre mide ' . strlen($nombre) . ' carácteres.';
// }
// echo saludar('Emilia');


function incrementar(int $num): int
{
    return $num + 1;
}

echo '<br>' . incrementar(4.5);


function saludar(string $nombre = 'Anónimo', string $profesion = 'ninguna'): string
{
    return '<br>Hola, ' . $nombre .'. Por lo que veo tu nombre mide ' . strlen($nombre) . ' carácteres. De profesión ' . $profesion . '.';
}

echo saludar('Picasso', 'pintor');



?>