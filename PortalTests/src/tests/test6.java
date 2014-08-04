package tests;
//check Facebook login option

import static org.junit.Assert.*;
import org.junit.Test;
import org.openqa.selenium.By;

public class test6 extends helper.CommonCode {

  @Test
  public void testloginwithfb() throws Exception {
    driver.get(baseUrl + "/accounts/login/");
    driver.findElement(By.linkText("Facebook")).click();
    assertTrue(driver.getCurrentUrl().contains("https://www.facebook.com/login.php"));
  }

}
