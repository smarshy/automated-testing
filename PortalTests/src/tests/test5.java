package tests;
//click login option

import static org.junit.Assert.*;
import org.junit.Test;
import org.openqa.selenium.By;

public class test5 extends helper.CommonCode {

  @Test
  public void testloginlink() throws Exception {
    driver.get(baseUrl + "/");
    driver.findElement(By.linkText("Login")).click();
    
    assertEquals(baseUrl+"/accounts/login/", driver.getCurrentUrl());
  }

}
