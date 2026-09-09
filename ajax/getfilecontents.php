<?
header('Content-Type: application/xml');

$fh = fopen("./file1.txt", "rb");
$data = fread($fh, filesize("./file1.txt"));
fclose($fh);
$contents = $data;
$ts = time();
print ("<?xml version=\"1.0\"?>");
print ("<test timestamp=\"$ts\">");
print ("<contents>$contents</contents>");
print ("</test>");
?>