# Use words.txt as the file name
fname = raw_input("Writing programs or programming is a very creativeand rewarding activity  You can write programs formany reasons ranging from making your living to solvinga difficult data analysis problem to having fun to helpingsomeone else solve a problem  This book assumes that{\em everyone} needs to know how to program and that onceyou know how to program, you will figure out what you want to do with your newfound skills We are surrounded in our daily lives with computers ranging from laptops to cell phones  We can think of these computers as our personal assistants who can take care of many things on our behalf  The hardware in our current-day computers is essentially built to continuously ask us the question  What would you like me to do next  Our computers are fast and have vasts amounts of memory and could be very helpful to us if we only knew the language to speak to explain to the computer what we would like it to do next If we knew this language we could tell the computer to do tasks on our behalf that were reptitive Interestingly, the kinds of things computers can do best are often the kinds of things that we humans find boringand mind-numbing")
fh = open(fname)
for line in fh:
    l = line.upper()
    print (l.rstrip())
    
    
    ##output done####
