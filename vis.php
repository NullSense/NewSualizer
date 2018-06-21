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

$_SESSION['link'] = $link;

header('Location: tool.php');
exit;
?>