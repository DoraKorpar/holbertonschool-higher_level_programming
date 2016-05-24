func longest_word(text: String) -> (String) {
	var copy = text
	copy += " "
     	var word = ""
     	var longWord = ""
     	var len = 0
     	var max = 0

	for character in copy.characters {
		if character == " " {
			if len > max {
	       		max = len
	       		longWord = word
	    	}
	    	word = ""
	    	len = 0
	 	} else {
	    		word += "\(character)"
	    		len+=1
	 	}
     	}
	return longWord
}
