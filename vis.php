<?php
/**
 * Created by PhpStorm.
 * User: viablesoft
 * Date: 03.05.2018
 * Time: 11:27
 */

/*if (isset($_POST['dataset[1]'])) {

   echo 2;
}
else
echo 1;
*/

$command = escapeshellcmd('python HDTrees.py Trees/ancestor.tre');
$output = shell_exec($command);
echo $output;


/* $x = rand(1, 10);
if($x %2 == 0)
header("Location: type1.html");
else
header("Location: type2.html");
*/




?>