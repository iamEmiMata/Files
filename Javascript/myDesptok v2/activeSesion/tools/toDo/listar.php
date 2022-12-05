<?php

$config = include 'conexion.php';

try {
  $dsn = 'mysql:host=' . $config['db']['host'] . ';dbname=' . $config['db']['name'];
  $conexion = new PDO($dsn, $config['db']['user'], $config['db']['pass'], $config['db']['options']);

  $consultaSQL = "SELECT * FROM lista";

  $sentencia = $conexion->prepare($consultaSQL);
  $sentencia->execute();

  $listar = $sentencia->fetchAll();

} catch(PDOException $error) {
  $error= $error->getMessage();
}

?>