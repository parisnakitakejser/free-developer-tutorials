<?php
require('database.php');
Database::setUsername('root');
Database::setPassword('');
Database::setHostname('localhost');
Database::setDatabase('test');
Database::setDBLink('default');
Database::connect();

$rowSingleAccount1 = Database::fetch("SELECT * FROM account WHERE id = :id", [
	['id', 1, 'int']
]);
$rowSingleAccount2 = Database::fetch("SELECT * FROM account WHERE id = :id", [
	['id', 1, 'int']
]);

echo '<pre>';
print_r($rowSingleAccount1);
print_r($rowSingleAccount2);
echo '</pre>';

$rowMultiAccount = Database::fetchAll("SELECT * FROM account");
	
echo '<pre>';
print_r($rowMultiAccount);
echo '</pre>';


// $fullname = 'Peter';
// Database::exec("INSERT INTO account(fullname)
// VALUES(:fullname)", [
// 	['fullname', $fullname, 'str']
// ]);
	
	echo '<hr />';
	echo '<pre>';
	print_r(Database::getStatistics());
	echo '</pre>';
?>