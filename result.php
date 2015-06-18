<?php

ini_set('display_errors',1);
error_reporting(E_ALL);

    if (isset($_FILES["fileToUpload"]) && ($_FILES["fileToUpload"]["error"] == UPLOAD_ERR_OK)) {

        $file = basename($_FILES["fileToUpload"]["name"]);

        $timestamp = date('Y-m-d-H-i-s');

        $newPath = './uploads/' . $timestamp . ".xlsx";
        
        if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $newPath)){
            #print "File saved in $newPath";

            $host  = $_SERVER['HTTP_HOST'];
            $path = "./uploads/" . $timestamp . ".amp";
        }
        
        else{
            print "Couldn't move file to $newPath";
        }
    }

    else{
        print "No valid file uploaded";
    }

    # Call the python script with the timestamp as an argument
	shell_exec('python translate.py ' . escapeshellarg($timestamp));

    header("Content-disposition: attachment; filename=$path");
    header("Content-type: text/plain");
    readfile("$path");
    exit;
?>