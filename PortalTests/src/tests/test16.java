package tests;
//user login on the portal


import static org.junit.Assert.*;

import java.io.*;

import org.junit.Test;
import org.openqa.selenium.By;

public class test16 extends helper.CommonCode {

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

}
