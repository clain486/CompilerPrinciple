from LexicalAnalysis.Lexer import Lexer
from Parser.LR1Parser import LR1Parser
from FileReader import FileReader
from Parser.Grammer import Grammer
import os
import sys


class Compiler:
    def __init__(self, grammer_filename, start_symbol="program", load_from_file=None):
        self.grammer = Grammer(grammer_filename)
        self.lr1parser = LR1Parser(self.grammer.rules, self.grammer.non_terminal, self.grammer.terminal, start_symbol,
                                   load_from_file=load_from_file)

    def recognize(self, filename):
        filereader = FileReader(filename)
        source_code = filereader.content()
        lexer = Lexer(source_code)
        lexer.tokenize()
        return self.lr1parser.recognize(lexer.tokens)

    def recognize_files(self, folder_path, output_file):
        original_stdout = sys.stdout  # 保存原始的stdout以便之后恢复
        with open(output_file, "w", encoding="utf-8") as file:
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                sys.stdout = file  # 将stdout重定向到文件
                try:
                    result = self.recognize(file_path)
                    file.write(f"{filename}: {'正确' if result else '错误'}\n")
                except Exception as e:
                    file.write(f"{filename}: 编译过程中出现错误 - {e}\n")
                finally:
                    sys.stdout = original_stdout
