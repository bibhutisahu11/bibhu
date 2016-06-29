package demo.testcases;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.Test;



public class ScrollTest {
	@Test
public void gettingTextInScroll(){
	WebDriver driver=new FirefoxDriver();
	driver.manage().timeouts().implicitlyWait(5, TimeUnit.SECONDS);
	driver.get("http://manos.malihu.gr/repository/custom-scrollbar/demo/examples/complete_examples.html");
     JavascriptExecutor js=(JavascriptExecutor)driver;
     WebElement element = driver.findElement(By.xpath(".//*[@id='mCSB_3_container']/p[3]"));
     js.executeScript("arguments[0].scrollIntoView(true);",element);
     System.out.println(element.getText());

}
}