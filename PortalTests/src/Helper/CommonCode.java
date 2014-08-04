package helper;

import java.io.File;
import java.util.concurrent.TimeUnit;
import org.apache.commons.io.FileUtils;
import org.junit.After;
import org.junit.Before;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;

public abstract class CommonCode {
	
	protected WebDriver driver;
	protected String baseUrl;
	
	@Before
	  public void setUp() throws Exception {
	    driver = new FirefoxDriver();
	    baseUrl = "http://systersportal-demo.herokuapp.com";
	    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
	  }
	
	@After
	  public void tearDown() throws Exception {
		 File scrFile = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
	     FileUtils.copyFile(scrFile, new File("/home/shwetambara/ScreenshotOnFail/screenshot.png"));   
		 driver.quit();
	   
	    }
	  }
	
	
