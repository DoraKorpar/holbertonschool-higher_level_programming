class Person {
	// declaring public attributes
	var first_name: String
	var last_name: String
	var age: Int

	// initializing public attributes
	init(first_name: String, last_name: String, age: Int) {
        	self.first_name = first_name
      	    	self.last_name = last_name
      	    	self.age = age
      	}

	// defining fullName method
      	func fullName() -> String {
      	   	return "\(self.first_name) \(self.last_name)"
      	}
}

protocol Classify {
	func isStudent() -> Bool
}

enum Subject {
	case Math, English, French, History
}

// subclass of Person with Classify protocol
class Mentor: Person, Classify {
	// defining isStudent method
	func isStudent() -> Bool {
      	   	return false
      	}

	// defining constant subject
      	var subject: Subject

	// overloading constructor to include subject
      	init(first_name: String, last_name: String, age: Int, subject: Subject = Subject.Math) {
		self.subject = subject
		super.init(first_name: first_name, last_name: last_name, age: age)
      	}

	// defining function stringSubject
	func stringSubject() -> String {
		if self.subject == Subject.Math {
			return "Math"
		}
		if self.subject == Subject.English {
			return "English"
		}
		if self.subject == Subject.French {
			return "French"
		}
		if self.subject == Subject.History {
			return "History"
		}
	return "String"
	}
}

// subclass of Person with Classify protocol
class Student: Person, Classify {
      	func isStudent() -> Bool {
      	   	return true
      	}
}
