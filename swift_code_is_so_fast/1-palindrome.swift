func is_palindrome(s: String) -> (Bool) {
	var rev_str = ""

	for character in s.characters {
	    let char = "\(character)"
	    rev_str = char + rev_str
	}
	return(s == rev_str)    
}
