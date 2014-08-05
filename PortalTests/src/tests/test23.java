package tests;
//portal admin feature dashboard


import static org.junit.Assert.*;

import org.junit.Test;
import org.openqa.selenium.By;

public class test23 extends helper.CommonCode {


  @Test
  public void testDashboard() throws Exception {
	  driver.get(baseUrl + "/admin/");
	  driver.findElement(By.id("id_username")).clear();
	  driver.findElement(By.id("id_username")).sendKeys("portal");
	  driver.findElement(By.id("id_password")).clear();
	  driver.findElement(By.id("id_password")).sendKeys("portal");
	  driver.findElement(By.cssSelector("input[type=\"submit\"]")).click();
    driver.findElement(By.linkText("Dashboard")).click();
    
    assertTrue(driver.getPageSource().contains("Dashboard administration"));
   
  }

}
