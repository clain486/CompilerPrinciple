from Compiler import Compiler


compiler = Compiler("Parser/grammar.txt", load_from_file="table_new.cfg", )
#print(compiler.recognize("prog/accepted/test-if1.c"))
print(compiler.recognize_file("prog/accepted"))
