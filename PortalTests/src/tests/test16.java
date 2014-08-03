package tests;
//user login on the portal

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.concurrent.TimeUnit;
import org.junit.*;
import static org.junit.Assert.*;
import org.openqa.selenium.*;
import org.openqa.selenium.firefox.FirefoxDriver;

public class test16 {
  private WebDriver driver;
  private String baseUrl;
  private boolean acceptNextAlert = true;
  private StringBuffer verificationErrors = new StringBuffer();

  @Before
  public void setUp() throws Exception {
    driver = new FirefoxDriver();
    baseUrl = "http://systersportal-demo.herokuapp.com";
    driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);
  }

  @Test
  public void testUserLogin() throws Exception {
	  
	  InputStreamReader in = new InputStreamReader(System.in);
	  BufferedReader br = new BufferedReader(in);
	  System.out.println("Enter Username and Password");
	  String Username = br.readLine();
	  String Password = br.readLine();
	  
    driver.get(baseUrl + "/accounts/login/");
    driver.findElement(By.id("id_login")).clear();
    driver.findElement(By.id("id_login")).sendKeys(Username);
    driver.findElement(By.id("id_password")).clear();
    driver.findElement(By.id("id_password")).sendKeys(Password);
    driver.findElement(By.cssSelector("button.primaryAction")).click();
    
    assertTrue(driver.getPageSource().contains(Username));
  }

  @After
  public void tearDown() throws Exception {
    driver.quit();
    String verificationErrorString = verificationErrors.toString();
    if (!"".equals(verificationErrorString)) {
      fail(verificationErrorString);
    }
  }

  private boolean isElementPresent(By by) {
    try {
      driver.findElement(by);
      return true;
    } catch (NoSuchElementException e) {
      return false;
    }
  }

  private boolean isAlertPresent() {
    try {
      driver.switchTo().alert();
      return true;
    } catch (NoAlertPresentException e) {
      return false;
    }
  }

  private String closeAlertAndGetItsText() {
    try {
      Alert alert = driver.switchTo().alert();
      String alertText = alert.getText();
      if (acceptNextAlert) {
        alert.accept();
      } else {
        alert.dismiss();
      }
      return alertText;
    } finally {
      acceptNextAlert = true;
    }
  }
}
