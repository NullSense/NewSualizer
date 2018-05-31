<?php
/**
 * Created by PhpStorm.
 * User: viablesoft
 * Date: 03.05.2018
 * Time: 11:27
 */


session_start();


$name = $_POST['dataset'];
$root = "";

foreach ($name as $dataset){
    $link = $dataset;
    break;
}

$root = $root.$link;
$dk = '/?'.$root;
$_SESSION['link'] = $root;
$_SESSION['k'] = 2;

//header('Location: HTML/'.$root);
header('Location: tool.php'.$dk);
exit;
/*
 *
 * $command = escapeshellcmd('python HDTrees.py Trees/ancestor.tre');
$output = shell_exec($command);
echo $output;


*/




?>