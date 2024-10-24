import config
import os

# Class definition for SourceFile and HeaderFile
class SourceFile:
    def generateContent(self, f, db, user_code_content):
        pass

    def generate(self, db):
        file_path = os.path.join(config.SOURCE_OUT_DIR, f"{self.filename}.c")
        user_code_content = {}
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                for usercode in self.usercodes:
                    user_code_content[usercode] = re.findall(fr'/\* USER CODE BEGIN {usercode} \*/(.*?)\s*/\* USER CODE END {usercode} \*/', content, re.DOTALL)
        with open(file_path, 'w') as f:
            self.generateContent(f, db, user_code_content)
            print(f"Generated {self.filename}.c")

class HeaderFile:
    def generateContent(self, f, db, user_code_content):
        pass

    def generate(self, db):
        file_path = os.path.join(config.HEADER_OUT_DIR, f"{self.filename}.h")
        user_code_content = {}
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                for usercode in self.usercodes:
                    user_code_content[usercode] = re.findall(fr'/\* USER CODE BEGIN {usercode} \*/(.*?)\s*/\* USER CODE END {usercode} \*/', content, re.DOTALL)
        with open(file_path, 'w') as f:
            f.write(f"#ifndef {self.filename.upper()}_H\n#define {self.filename.upper()}_H\n\n")
            self.generateContent(f, db, user_code_content)
            f.write("\n\n#endif\n")
            print(f"Generated {self.filename}.h")