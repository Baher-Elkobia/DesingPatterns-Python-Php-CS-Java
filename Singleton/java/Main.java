package Singleton.java;


class Main
{
	public static void main(String[] args)
	{	
        try{
        // create two DB instances
        DataBaseInstance DbInstance01 = DataBaseInstance.getInstance();
        DataBaseInstance DbInstance02 = DataBaseInstance.getInstance();

        // it shouldn't be possible to create a new instance of a singleton class, the following line will raise error during compilaton
        // DataBaseInstance DbInstance03 = new DataBaseInstance();

        // Check that both instances are the same object
        System.out.println(String.format("Are both DB instances the same object?: %s", DbInstance01.equals(DbInstance02)));

        // perform some SQL queries
        }
        catch(Exception e){
            System.out.println("Error ocurred");
            e.printStackTrace();
        }
	}
}