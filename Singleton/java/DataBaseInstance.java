package Singleton.java;

// Singleton class
public class DataBaseInstance {

	// private varibales to store the single instance of DataBaseInstance
	private static DataBaseInstance instance = null;
	
	// constructor must be private to prevent creating new instance of the class since it is a Singleton
	private DataBaseInstance () {
		try {
			// some database driver initialization	
		} catch (Exception e) {
			e.printStackTrace();
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