//  Implement a (Java) Iterable object that iterates lines one by one from a text file
// A reference to a file.
public class TextFile implements Iterable<String>
{
  Scanner scanner;
  String fileName;
  public TextFile(String fileName) { // please implement this
  	try{
  		this.fileName = fileName;
		Scanner scanner = new Scanner(new FileReader(fileName));
  	}
  	catch(IOException ex){

  	}
  }
  String next(){
  	return scanner.nextLine();
  }
  boolean hasNext(){
  	return scanner.hasNext();
  }
  /** Begin reading the file, line by line. The returned Iterator.next() will return a line. */
  @Override
  public Iterator<String> iterator() { // please implement this
  	return new TextFile(fileName);
  }
}