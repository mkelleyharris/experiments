
import java.lang.RuntimeException;

public class JavaExperiments {
	
	public class MyException extends RuntimeException {
		public MyException() {
			super();
		}
	}
	
	static public String name() {
		//throw MyException();
		//throw new RuntimeException("Junk");
		return "je2";
	}
	
	public int age() {
		return 5;
	}

}
