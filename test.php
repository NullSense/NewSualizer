<?php

			
			
		/*$arg2 = "uploads/test.txt";
			$command = 'python HDTrees.py '.$arg2;
			$output = passthru($command);
			//var_dump($output);
			*/
			
			
			
			$path = "HTI/t.py";
			$arg = "uploads/test.txt";
			$command = escapeshellcmd($path);
			$message = shell_exec($command);
			echo $message;
			
			
			
			//shell_exec("/path/to/python-script.py");
			


?>