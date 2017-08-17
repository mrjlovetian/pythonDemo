from sya import exit

def gold_room():
	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("man, learn to type a number")
		