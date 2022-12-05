<?php

include 'funciones.php';
csrf();
if (isset($_POST['submit']) && !hash_equals($_SESSION['csrf'], $_POST['csrf'])) {
  die();
}

if (isset($_POST['submit'])) {
  $resultado = [
    'error' => false,
    'mensaje' => ' Successfully Added!'
  ];

  $config = include 'tools/toDo/conexion.php';

  try {
    $dsn = 'mysql:host=' . $config['db']['host'] . ';dbname=' . $config['db']['name'];
    $conexion = new PDO($dsn, $config['db']['user'], $config['db']['pass'], $config['db']['options']);

    $table = [
      "tasks"   => $_POST['tasks'],
    ];

    $consultaSQL = "INSERT INTO lista (tasks)";
    $consultaSQL .= "values (:" . implode(", :", array_keys($table)) . ")";

    $sentencia = $conexion->prepare($consultaSQL);
    $sentencia->execute($table);

  } catch(PDOException $error) {
    $resultado['error'] = true;
    $resultado['mensaje'] = $error->getMessage();
  }
}
?>
