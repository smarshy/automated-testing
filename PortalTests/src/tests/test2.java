package tests;
//click About option

import static org.junit.Assert.*;
import org.junit.Test;
import org.openqa.selenium.By;

public class test2 extends helper.CommonCode {

	@Test
	public void testABIlink() throws Exception {
	    driver.get(baseUrl + "/");
	    driver.findElement(By.linkText("About")).click();
	    String str = driver.getCurrentUrl();
	    assertEquals(str, "http://anitaborg.org/");
	  }

}

