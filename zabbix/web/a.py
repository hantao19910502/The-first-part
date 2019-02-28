import 	commands
tok = "MTU1MDg5NTc1Mi45NTg2NzU5Ojk0Yjg0NzUzOWZlOTBmYmYyYmRlMmI2YjBkYWFjYThkOWRkNjA5MDA="
a,b = commands.getstatusoutput('sh Verification.sh "%s"'%(tok))

print a,b
