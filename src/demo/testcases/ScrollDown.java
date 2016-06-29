package demo.testcases;



import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.testng.annotations.Test;

public class ScrollDown {
	@Test
public void test() throws Exception{
WebDriver driver=new FirefoxDriver();
driver.get("http://www.javatpoint.com/");
Thread.sleep(6000);
((JavascriptExecutor)driver).executeScript("scroll(0,500)");




}
}
