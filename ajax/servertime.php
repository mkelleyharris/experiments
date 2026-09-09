<?
header('Content-Type: application/xml');
$msg = htmlentities(trim(stripslashes($_REQUEST['msg'])));
$ts = time();
$ipClient = $_SERVER['REMOTE_ADDR'];
$ipServer = gethostbyname($_SERVER['SERVER_NAME']); 
$nameServer = $_SERVER['SERVER_NAME'];
print ("<?xml version=\"1.0\"?>");
print ("<test timestamp=\"$ts\">");
print ("<ipClient>$ipClient</ipClient>");
print ("<ipServer>$ipServer</ipServer>");
print ("<nameServer>$nameServer</nameServer>");
print ("<message>$msg</message>");
print ("</test>");
?>