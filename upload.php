<?php
/**
 * Created by PhpStorm.
 * User: viablesoft
 * Date: 29.04.2018
 * Time: 23:09
 */

if($_SERVER["REQUEST_METHOD"] == "POST"){
    // Check if file was uploaded without errors
    if(isset($_FILES["fileToUpload"]) && $_FILES["fileToUpload"]["error"] == 0){
        $filename = $_FILES["fileToUpload"]["name"];
        $filetype = $_FILES["fileToUpload"]["type"];
        $filesize = $_FILES["fileToUpload"]["size"];
        move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], "uploads/" . $_FILES["fileToUpload"]["name"]);
    }

    header('Location: tool.php');
    exit;
}
?>
