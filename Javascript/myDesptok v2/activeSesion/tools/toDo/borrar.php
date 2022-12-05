<?php

$config = include 'conexion.php';

try {
  $dsn = 'mysql:host=' . $config['db']['host'] .';dbname=' . $config['db']['name'];
  $conexion = new PDO($dsn, $config['db']['user'], $config['db']['pass'], $config['db']['options']);
    
  $id = $_GET['id'];
  $consultaSQL = " DELETE FROM lista WHERE id = " . $id;

  $sentencia = $conexion->prepare($consultaSQL);
  $sentencia->execute();

  header('Location: ../../index.php');

} catch(PDOException $error) {
  $resultado['error'] = true;
  $resultado['mensaje'] = $error->getMessage();
}

$resultado = [
  'error' => false,
  'mensaje' => 'Successfully Deleted!'
];
?>