package com.example.tests;

import org.junit.*;
import org.openqa.selenium.*;

public class Users extends commons.CommonCode{
  private WebDriver driver;
  private String baseUrl;
 
  @Test
  public void testLogout() throws Exception {
    driver.get(baseUrl + "/");
    driver.findElement(By.linkText("Members")).click();
  }
}