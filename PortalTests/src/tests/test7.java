package tests;
//check Google login option

import static org.junit.Assert.*;
import org.junit.Test;
import org.openqa.selenium.By;

public class test7 extends helper.CommonCode {

  @Test
  public void testloginwithgoogle() throws Exception {
	  driver.get(baseUrl + "/accounts/login/");
	  driver.findElement(By.linkText("Google")).click();
	  boolean b = driver.getCurrentUrl().contains("https://accounts.google.com/ServiceLogin");
	  assertTrue(b);

  }

 }