package tests;
//navigate to the portal site

import static org.junit.Assert.*;
import org.junit.Test;
import org.openqa.selenium.By;

public class test1 extends helper.CommonCode {


	@Test
	public void testSysterslink() {
		driver.get(baseUrl + "/");
	    driver.findElement(By.linkText("Systers")).click();
	    String str = driver.getCurrentUrl();
	    boolean content = driver.getPageSource().contains("We envision a future");
	    assertEquals(baseUrl+"/",str);
	    assertTrue(content);
	}

}
