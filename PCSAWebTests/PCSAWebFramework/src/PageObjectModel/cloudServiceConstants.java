/*
 * @author Anjali
 * @since 2016-07-11
 * This class maintains constants to be used with BrowserStack for running tests on the cloud service.
 */
package PageObjectModel;

public class cloudServiceConstants 
{
	/*
	 * Create an account with BrowserStack to get the username and accessKey.
	 * Edit these fields after creation
	 */
	public static final String USERNAME = "anjali65";
	public static final String AUTOMATE_KEY = "yo9vPJpaaGZTfhUjH9AQ";
	public static final String URL = "https://" + USERNAME + ":" + AUTOMATE_KEY + "@hub-cloud.browserstack.com/wd/hub";
}
