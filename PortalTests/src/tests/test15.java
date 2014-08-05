package tests;
//Admin logout


import static org.junit.Assert.*;

import org.junit.Test;
import org.openqa.selenium.By;

public class test15 extends helper.CommonCode {


  @Test
  public void testAdminlogout() throws Exception {
	  driver.get(baseUrl + "/admin/");
	  driver.findElement(By.id("id_username")).clear();
	  driver.findElement(By.id("id_username")).sendKeys("portal");
	  driver.findElement(By.id("id_password")).clear();
	  driver.findElement(By.id("id_password")).sendKeys("portal");
	  driver.findElement(By.cssSelector("input[type=\"submit\"]")).click();
      driver.findElement(By.linkText("Log out")).click();
      
      assertTrue(driver.getPageSource().contains("Logged out"));
      assertTrue(driver.getPageSource().contains("Thanks for spending some quality time with the Web site today."));
      
  }

}
