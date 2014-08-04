package tests;
//click register option

import static org.junit.Assert.*;
import org.junit.Test;
import org.openqa.selenium.By;

public class test3 extends helper.CommonCode {

@Test
  public void testregisterlink() throws Exception {
    driver.get(baseUrl + "/");
    driver.findElement(By.linkText("Register")).click();
    
    String str1 = baseUrl + "/accounts/signup/";
    String str2 = driver.getCurrentUrl();
    assertEquals (str1, str2);
    
  }

}