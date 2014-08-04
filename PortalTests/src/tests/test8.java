package tests;
//Check Github login option

import static org.junit.Assert.*;
import org.junit.Test;
import org.openqa.selenium.By;

public class test8 extends helper.CommonCode {

  @Test
  public void testloginwithgithub() throws Exception {
    driver.get(baseUrl + "/accounts/login/");
    driver.findElement(By.linkText("GitHub")).click();  
    assertTrue(driver.getCurrentUrl().contains("https://github.com/login"));
  }

}
