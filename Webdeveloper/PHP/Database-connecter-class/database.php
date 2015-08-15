<?php
class Database {
	private static
		$_username = 'root',
		$_password = '',
		$_hostname = 'localhost',
		$_database = '',
		$_dbLink = 'default',
		$_dbObj = null;
	
	private static
		$_count_fetch = 0,
		$_count_fetch_all = 0,
		$_count_exec = 0,
		$_count_sql_query = 0;
	
	public static function setUsername($value) {
		self::$_username = $value;
	}
	
	public static function setPassword($value) {
		self::$_password = $value;
	}
	
	public static function setHostname($value) {
		self::$_hostname = $value;
	}
	
	public static function setDatabase($value) {
		self::$_database = $value;
	}
	
	public static function setDBLink($value) {
		self::$_dbLink = $value;
	}
	
	public static function connect() {
		try {
			
			if(!isset(self::$_dbObj[self::$_dbLink]) || self::$_dbObj[self::$_dbLink] == null) {
				self::$_dbObj[self::$_dbLink] = new \PDO('mysql:host='. self::$_hostname .';dbname='. self::$_database,self::$_username,self::$_password);
				self::$_dbObj[self::$_dbLink]->setAttribute(\PDO::ATTR_ERRMODE, \PDO::ERRMODE_WARNING);
				self::$_dbObj[self::$_dbLink]->setAttribute(\PDO::MYSQL_ATTR_USE_BUFFERED_QUERY, true);
			}
			
			return self::$_dbObj[self::$_dbLink];
			
		} catch (\PDOExpception $e) {
			print "Database connection error sorry\n";
			exit();
		}
	}
	
	private static function _bindparam($value) {
		switch(strtolower($value)) {
			case 'int':
				return \PDO::PARAM_INT;
				break;
				
			case 'str':
				return \PDO::PARAM_STR;
				break;
				
			case 'bool':
				return \PDO::PARAM_BOOL;
				break;
				
			case 'null':
				return \PDO::PARAM_NULL;
				break;
		}
	}
	
	private static function _prepare($sqlQuery) {
		if(($query = self::$_dbObj[self::$_dbLink]->prepare($sqlQuery)) != false) {
			return $query;
		} else {
			return false;
		}
	}
	
	private static function _executeQuery($sqlQuery, array $bindparams = [], $method = '') {
		$query = self::_prepare($sqlQuery);
		if ($query !== false) {
			if(count($bindparams) > 0) {
				foreach($bindparams AS $v) {
					$query->bindParam(":{$v[0]}", $v[1], self::_bindparam($v[2]));
				}
			}
			
			$query->execute();
			switch($method) {
				case 'fetch':
					$row = $query->fetch(\PDO::FETCH_OBJ);
					return $row;
					break;
					
				case 'fetchAll':
					$row = $query->fetchAll(\PDO::FETCH_OBJ);
					return $row;
					break;
					
				case 'exec':
					return true;
					break;
					
				default:
					return false;
					break;
			}
			
		} else {
			return false;
		}
	}
	
	public static function fetch($sqlQuery, array $bindparams = []) {
		self::$_count_fetch++;
		self::$_count_sql_query++;
		return self::_executeQuery($sqlQuery, $bindparams, 'fetch');
	}
	
	public static function fetchAll($sqlQuery, array $bindparams = []) {
		self::$_count_fetch_all++;
		self::$_count_sql_query++;
		return self::_executeQuery($sqlQuery, $bindparams, 'fetchAll');
	}
	
	public static function exec($sqlQuery, array $bindparams = []) {
		self::$_count_exec++;
		self::$_count_sql_query++;
		return self::_executeQuery($sqlQuery, $bindparams, 'exec');
	}
	
	public static function getStatistics() {
		return [
			'fetch' => self::$_count_fetch,
			'fetch_all' => self::$_count_fetch_all,
			'exec' => self::$_count_exec,
			'sql_query' => self::$_count_sql_query
		];
	}
}
?>