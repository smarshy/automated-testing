package tests;
//Admin login and view features


import static org.junit.Assert.*;

import org.junit.Test;
import org.openqa.selenium.By;

public class test18 extends helper.CommonCode {

  @Test
  public void testloginasAdmin() throws Exception {
	  driver.get(baseUrl + "/admin/");
	  driver.findElement(By.id("id_username")).clear();
	  driver.findElement(By.id("id_username")).sendKeys("portal");
	  driver.findElement(By.id("id_password")).clear();
	  driver.findElement(By.id("id_password")).sendKeys("portal");
	  driver.findElement(By.cssSelector("input[type=\"submit\"]")).click();
	  
	 assertTrue(driver.getPageSource().contains("Site administration"));
    
  }

}
