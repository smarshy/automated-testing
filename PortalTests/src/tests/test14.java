package tests;
//change password for admin

import static org.junit.Assert.*;

import org.junit.Test;
import org.openqa.selenium.By;

public class test14 extends helper.CommonCode {

  @Test
  public void testchangepassword() throws Exception {
	  
	  driver.get(baseUrl + "/admin/");
	  driver.findElement(By.id("id_username")).clear();
	  driver.findElement(By.id("id_username")).sendKeys("portal");
	  driver.findElement(By.id("id_password")).clear();
	  driver.findElement(By.id("id_password")).sendKeys("portal");
	  driver.findElement(By.cssSelector("input[type=\"submit\"]")).click();
	
    driver.findElement(By.linkText("Change password")).click();
    driver.findElement(By.id("id_old_password")).clear();
    driver.findElement(By.id("id_old_password")).sendKeys("portal");
    driver.findElement(By.id("id_new_password1")).clear();
    driver.findElement(By.id("id_new_password1")).sendKeys("portal");
    driver.findElement(By.id("id_new_password2")).clear();
    driver.findElement(By.id("id_new_password2")).sendKeys("portal");
    driver.findElement(By.cssSelector("input.default")).click();
    
    assertTrue(driver.getPageSource().contains("Password change successful"));
  }

}
