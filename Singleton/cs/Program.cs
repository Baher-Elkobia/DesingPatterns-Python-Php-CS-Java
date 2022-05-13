using System;

namespace DesignPatterns.Singleton
{
    // Singleton class
    public class DataBaseInstance {
        // private varibales to store the single instance of DataBaseInstance
        private static DataBaseInstance instance;
        
        // constructor must be private to prevent creating new instance of the class since it is a Singleton
        private DataBaseInstance () {
            try {
                // some database driver initialization	
            } catch (Exception e) {
                Console.WriteLine(e);
            }
        }
        
        // Static method to get current a Singleton instance or create one if no instance was created
        public static DataBaseInstance getInstance() {
            if(instance == null) {
                    instance = new DataBaseInstance();
                }	
            return instance;
        }
    }

    // ---------- Client Code --------------
    class Program
    {
        static void Main(string[] args)
        {
            try{
                // create two DB instances
                DataBaseInstance DbInstance01 = DataBaseInstance.getInstance();
                DataBaseInstance DbInstance02 = DataBaseInstance.getInstance();

                // it shouldn't be possible to create a new instance of a singleton class, the following line will raise error during compilaton
                // DataBaseInstance DbInstance03 = new DataBaseInstance();

                // Check that both instances are the same object
                Console.WriteLine("Are both DB instances the same object?: " + Object.ReferenceEquals(DbInstance01, DbInstance02));

                // perform some SQL queries
            }
            catch(Exception){
                Console.WriteLine("Error ocurred");
            }
        }
    }
}



