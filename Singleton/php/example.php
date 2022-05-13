<?php

namespace DesignPattern\Singleton\php;

class Singleton
{
    // private varibale to store the single instance of the singleton class
    private static ?Singleton $instance = null;

    // constructor must not be public to prevent creating new instance of the class since it is a Singleton
    protected function __construct() { }

    // Cloning is not allowed for singletons, therefore, __clone is protected
    protected function __clone() { }

    // Static method to get current a Singleton instance or create one if no instance was created
    public static function getInstance()
    {
        if (self::$instance == null) {
            self::$instance = new static();
        }
        return self::$instance;
    }
}

/**
 * The logging class is a good use case of Singleton pattern since you just need a single logging object, moreover,
 * You also need a way to access that logger instance from any context of your app (global access)
 */
class Logger extends Singleton
{

    // A file pointer to a log file.
    private $fileHandle;

    // initialization which is carried out once since the Singleton's constructor is called only once
    protected function __construct()
    {
        
        $this->fileHandle = fopen('php://stdout', 'w');
    }


    //  Write a log entry
    public function writeLog(string $message): void
    {
        $date = date('Y-m-d');
        fwrite($this->fileHandle, "$date: $message\n");
    }

  
    // Return a logger object
    public static function getLogger(): Logger
    {
        $logger = static::getInstance();
        return $logger;
    }
}


// ------ client code -------
// --------------------------

 $logger = Logger::getLogger();
 $logger->writeLog("Started!");

// Check that both objects are the same.

$logger01 = Logger::getLogger();
$logger02 = Logger::getLogger();

// It shouldn't be possible to create a new instance of a singleton class, 
// the following line will raise error while running the code
// $logger03 = new Logger();

if ($logger01 === $logger02) {
    $logger->writeLog("Logger has a single instance.");
} else {
    $logger->writeLog("Loggers are different.");
}

$logger->writeLog("Finished!");