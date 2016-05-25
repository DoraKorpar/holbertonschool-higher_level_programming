class Person {
	// declaring public attributes
	var first_name: String
	var last_name: String
	var age: Int

	// Constructor
	init(first_name: String, last_name: String, age: Int) {
        	self.first_name = first_name
      	    	self.last_name = last_name
      	    	self.age = age
      	}

	// defining fullName method
      	func fullName() -> String {
      	   	return "\(self.first_name) \(self.last_name)"
      	}

	// defining className method for subclasses
	func className() -> String {
		return "Person"
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
	// method to determine class
	override func className () -> String {
		return "Mentor"
	}

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

	// defining function stringSubject, which returns string based on Subject
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
	// method to determine class
	override func className () -> String {
		return "Student"
	}

      	func isStudent() -> Bool {
      	   	return true
      	}
}

// new class
class School {
	// public attributes
	var name: String
	var list_persons: [Person]

	// Constructor
	init(name: String) {
		self.name = name
		self.list_persons = []
	}

	// public methods
	func addStudent(p: Person) -> Bool {
		if p.className() == "Student" {
			self.list_persons.append(p)
			return true
		}
		return false
	}

	func addMentor(p: Person) -> Bool {
		if p.className() == "Mentor" {
			self.list_persons.append(p)
			return true
		}
		return false
	}
}
