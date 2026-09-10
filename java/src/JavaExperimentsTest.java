import static org.junit.Assert.*;

import org.junit.Test;


public class JavaExperimentsTest {
	
	@Test
	public void testCreate() {
		//fail("Not yet implemented");
		//JavaExperiments je = new JavaExperiments();
		assertEquals("je2", JavaExperiments.name());
	}
	
	@Test
	public void testAge() {
		JavaExperiments je = new JavaExperiments();
		assertEquals((Integer)5, (Integer)je.age());
		assertEquals("Age test", 5, je.age());
	}
	
	


}


